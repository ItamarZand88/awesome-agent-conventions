#!/usr/bin/env python3
"""Fetch real agent-convention files and rebuild per-convention READMEs.

Source of truth: scripts/targets.json. For every convention (except those
marked `manual_readme`) this fetches each declared target, saves it under
conventions/<slug>/examples/ with a line-1 provenance comment, then rebuilds
conventions/<slug>/README.md from what was actually captured.

Never crashes on a bad target — a non-200 or network error prints a `miss`
and moves on. The only hard exit is a GitHub API rate-limit (403/429), which
is unrecoverable without waiting or a token.

Usage:
    python scripts/extract.py                 # fetch everything + rebuild READMEs
    python scripts/extract.py --only spec-kit  # one convention
    python scripts/extract.py --index-only     # rebuild READMEs, fetch nothing
"""
import argparse
import json
import os
import re
import sys
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    sys.exit("requests not installed — run: pip install -r scripts/requirements.txt")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGETS_PATH = os.path.join(ROOT, "scripts", "targets.json")
CONVENTIONS_DIR = os.path.join(ROOT, "conventions")

USER_AGENT = (
    "awesome-agent-conventions-extractor/1.0 "
    "(+https://github.com/ItamarZand88/awesome-agent-conventions)"
)
TIMEOUT = 30

# Examples are representative samples, not archives. Some real files (notably
# llms-full.txt — the entire docs concatenated) run to tens of MB, which has no
# place in a forkable catalog. Cap each saved example and mark any truncation.
MAX_EXAMPLE_BYTES = 256 * 1024

BADGES = {
    "🟢": "🟢 Adopted",
    "🟡": "🟡 Emerging",
    "🔵": "🔵 Proposed",
}

PROVENANCE_RE = re.compile(r"<!-- source: (?P<label>.+?) — (?P<url>.+?) -->")


# --- target helpers --------------------------------------------------------

def source_label(target, url):
    """Domain for plain web URLs, owner-repo for GitHub sources."""
    if target.get("type") == "github":
        return f"{target['owner']}-{target['repo']}"
    host = urlparse(url).netloc
    if host == "raw.githubusercontent.com":
        parts = [p for p in urlparse(url).path.split("/") if p]
        if len(parts) >= 2:
            return f"{parts[0]}-{parts[1]}"
    return host or "source"


def target_filename(target, url):
    """`as` override, else the URL/path basename."""
    if target.get("as"):
        return target["as"]
    if target.get("type") == "github":
        return os.path.basename(target["path"]) or "index"
    return os.path.basename(urlparse(url).path) or "index"


# --- fetching --------------------------------------------------------------

def fetch_web(url):
    resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=TIMEOUT)
    resp.raise_for_status()
    return resp.text


def fetch_github(owner, repo, path):
    """Optional GitHub Contents-API path; uses GITHUB_TOKEN if present."""
    api = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    headers = {
        "Accept": "application/vnd.github.raw+json",
        "User-Agent": USER_AGENT,
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    resp = requests.get(api, headers=headers, timeout=TIMEOUT)
    if resp.status_code in (403, 429):
        remaining = resp.headers.get("X-RateLimit-Remaining", "?")
        reset = resp.headers.get("X-RateLimit-Reset", "?")
        sys.exit(
            f"GitHub API rate limit hit (remaining={remaining}, reset epoch={reset}). "
            "Set GITHUB_TOKEN or wait, then re-run. Tip: prefer raw.githubusercontent.com "
            "`web` targets, which are not rate-limited."
        )
    resp.raise_for_status()
    return resp.text


def fetch_target(target):
    """Return (text, canonical_url). Raises on failure (caller catches)."""
    kind = target.get("type", "web")
    if kind == "web":
        return fetch_web(target["url"]), target["url"]
    if kind == "github":
        text = fetch_github(target["owner"], target["repo"], target["path"])
        url = (
            f"https://github.com/{target['owner']}/{target['repo']}"
            f"/blob/HEAD/{target['path']}"
        )
        return text, url
    raise ValueError(f"unknown target type: {kind!r}")


# --- README rebuild --------------------------------------------------------

def spec_link(spec):
    if not spec:
        return "—"
    href = spec if spec.startswith("http") else f"https://{spec}"
    return f"[{spec}]({href})"

def read_provenance(path):
    with open(path, encoding="utf-8") as fh:
        first = fh.readline()
    m = PROVENANCE_RE.search(first)
    if m:
        return m.group("label"), m.group("url")
    return os.path.basename(path), None


def examples_for(examples_dir, filename):
    """Match saved examples to a declared file by filename suffix.

    Saved files are named `<label>.<saved-filename>`, so a declared file like
    `AGENTS.md` matches anything ending in `.AGENTS.md`, and a dot-extension
    declared file like `.prompty` matches anything ending in `.prompty`
    (e.g. a saved `microsoft-prompty.chat-basic.prompty`). Suffix-matching —
    rather than `*.AGENTS.md` globbing — is what lets one declared file collect
    examples whose own basenames differ.
    """
    if not os.path.isdir(examples_dir):
        return []
    suffix = filename if filename.startswith(".") else f".{filename}"
    return sorted(
        os.path.join(examples_dir, name)
        for name in os.listdir(examples_dir)
        if name.endswith(suffix)
    )


def rebuild_convention_readme(slug, conv):
    slug_dir = os.path.join(CONVENTIONS_DIR, slug)
    examples_dir = os.path.join(slug_dir, "examples")
    os.makedirs(slug_dir, exist_ok=True)

    # Pattern files vendor nothing — clear any stale extracted examples so the
    # repo never carries a dump that the page no longer references.
    for f in conv["files"]:
        if f.get("kind") == "pattern":
            for stale in examples_for(examples_dir, f["name"]):
                os.remove(stale)

    badge = BADGES.get(conv["maturity"], conv["maturity"])
    out = []
    out.append(f"# {conv['name']} {badge}")
    out.append("")
    out.append(f"> {conv['summary']}")
    out.append("")
    out.append(f"- **Read by:** {conv['read_by']}")
    out.append(f"- **Location:** {conv['location']}")
    out.append(f"- **Spec:** {spec_link(conv['spec'])}")
    file_list = ", ".join(f"`{f['name']}`" for f in conv["files"])
    out.append(f"- **Files:** {file_list}")
    out.append("")
    out.append("## Examples")
    out.append("")
    out.append(
        "_Every file below was fetched from a public source by "
        "[`scripts/extract.py`](../../scripts/extract.py) — none are hand-written._"
    )
    out.append("")

    for f in conv["files"]:
        fname = f["name"]
        out.append(f"### `{fname}`")
        out.append("")
        if f.get("note"):
            out.append(f["note"])
            out.append("")
        if f.get("kind") == "pattern":
            out.append("**Pattern — not an extracted file.**")
            out.append("")
            if f.get("pattern"):
                out.append(f["pattern"])
                out.append("")
            instances = f.get("instances", [])
            if instances:
                out.append("Live instances (fetch directly — too large or instance-specific to vendor):")
                out.append("")
                for inst in instances:
                    out.append(f"- [{inst['label']}]({inst['url']})")
                out.append("")
            continue
        matches = examples_for(examples_dir, fname)
        if matches:
            out.append("| Source | File | Provenance |")
            out.append("| --- | --- | --- |")
            for m in matches:
                base = os.path.basename(m)
                label, url = read_provenance(m)
                prov = f"[source]({url})" if url else "—"
                out.append(f"| `{label}` | [`{base}`](examples/{base}) | {prov} |")
        else:
            out.append(
                "_No example captured yet — add a target in "
                "[`scripts/targets.json`](../../scripts/targets.json) and run "
                "`python scripts/extract.py --only " + slug + "`._"
            )
        out.append("")

    out.append("## Field notes")
    out.append("")
    notes_path = os.path.join(slug_dir, "field-notes.md")
    if os.path.exists(notes_path):
        # Human-written observations live in a sidecar so regenerating the
        # README never clobbers them. The sidecar holds the section body
        # (prose + ### subsections); the H2 above is owned by the generator.
        with open(notes_path, encoding="utf-8") as fh:
            out.append(fh.read().strip("\n"))
        out.append("")
    else:
        out.append(
            "_Written by humans, kept in a `field-notes.md` sidecar in this folder so "
            "regenerating the README never clobbers them. Drop one in to replace this stub._"
        )
        out.append("")
        out.append("### Composition")
        out.append("- What sections do strong examples share? What order?")
        out.append("")
        out.append("### Anti-patterns")
        out.append("- What do weak examples do that you should avoid?")
        out.append("")
        out.append("### Edge cases")
        out.append("- Nesting, precedence, size limits, tool-specific quirks.")
        out.append("")

    readme_path = os.path.join(slug_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    print(f"  readme: {os.path.relpath(readme_path, ROOT)}")


# --- per-convention pipeline -----------------------------------------------

def process_convention(slug, conv, index_only):
    slug_dir = os.path.join(CONVENTIONS_DIR, slug)
    examples_dir = os.path.join(slug_dir, "examples")

    if not index_only:
        os.makedirs(examples_dir, exist_ok=True)
        for target in conv.get("targets", []):
            try:
                text, url = fetch_target(target)
            except SystemExit:
                raise  # rate-limit: propagate the hard exit
            except Exception as exc:  # noqa: BLE001 — never crash on one target
                ref = target.get("url") or target
                print(f"  miss: {ref} — {exc}")
                continue
            label = source_label(target, url)
            fname = target_filename(target, url)
            dest = os.path.join(examples_dir, f"{label}.{fname}")
            provenance = f"<!-- source: {label} — {url} -->\n"
            full_len = len(text.encode("utf-8"))
            truncated = full_len > MAX_EXAMPLE_BYTES
            body = (
                text.encode("utf-8")[:MAX_EXAMPLE_BYTES].decode("utf-8", "ignore")
                if truncated
                else text
            )
            with open(dest, "w", encoding="utf-8") as fh:
                fh.write(provenance)
                fh.write(body)
                if truncated:
                    fh.write(
                        f"\n\n<!-- TRUNCATED by extract.py: kept the first {MAX_EXAMPLE_BYTES} "
                        f"of {full_len} bytes. This is a representative sample; fetch the full "
                        f"file from the source URL above. -->\n"
                    )
            msg = f"  ok:   {os.path.relpath(dest, ROOT)}"
            if truncated:
                msg += f"  (truncated {full_len} → {MAX_EXAMPLE_BYTES} bytes)"
            print(msg)

    rebuild_convention_readme(slug, conv)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--only", metavar="SLUG", help="process a single convention")
    ap.add_argument(
        "--index-only",
        action="store_true",
        help="rebuild READMEs from existing examples without fetching",
    )
    args = ap.parse_args()

    with open(TARGETS_PATH, encoding="utf-8") as fh:
        data = json.load(fh)
    conventions = data["conventions"]

    if args.only:
        if args.only not in conventions:
            sys.exit(f"unknown slug: {args.only}")
        slugs = [args.only]
    else:
        slugs = list(conventions.keys())

    for slug in slugs:
        conv = conventions[slug]
        if conv.get("manual_readme"):
            print(f"== {slug} == (manual README — skipped)")
            continue
        print(f"== {slug} ==")
        process_convention(slug, conv, args.index_only)

    print("done.")


if __name__ == "__main__":
    main()
