#!/usr/bin/env python3
"""Check example provenance and optionally report upstream licenses.

Default mode queries GitHub's license API for GitHub-backed example sources and
prints a compact report. Use --offline in CI to avoid network calls while still
checking every vendored example has line-1 provenance and maps to a declared
target URL.
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGETS_PATH = os.path.join(ROOT, "scripts", "targets.json")
CONVENTIONS_DIR = os.path.join(ROOT, "conventions")

PROVENANCE_RE = re.compile(r"<!-- source: (?P<label>.+?) — (?P<url>.+?) -->")
UA = "awesome-agent-conventions-license-audit/1.0 (+https://github.com/ItamarZand88/awesome-agent-conventions)"

COPYLEFT = {"AGPL-3.0", "GPL-2.0", "GPL-3.0", "LGPL-2.1", "LGPL-3.0"}
PERMISSIVE = {"Apache-2.0", "MIT", "MIT-0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "CC0-1.0"}


def load_targets():
    with open(TARGETS_PATH, encoding="utf-8") as fh:
        return json.load(fh)["conventions"]


def declared_urls(conventions):
    urls = set()
    for conv in conventions.values():
        for target in conv.get("targets", []):
            if target.get("url"):
                urls.add(target["url"])
            elif target.get("type") == "github":
                urls.add(
                    f"https://github.com/{target['owner']}/{target['repo']}"
                    f"/blob/HEAD/{target['path']}"
                )
    return urls


def iter_examples():
    for slug in sorted(os.listdir(CONVENTIONS_DIR)):
        examples_dir = os.path.join(CONVENTIONS_DIR, slug, "examples")
        if not os.path.isdir(examples_dir):
            continue
        for name in sorted(os.listdir(examples_dir)):
            path = os.path.join(examples_dir, name)
            if os.path.isfile(path):
                yield slug, name, path


def read_provenance(path):
    with open(path, encoding="utf-8") as fh:
        first = fh.readline().strip()
    match = PROVENANCE_RE.fullmatch(first)
    if not match:
        return None
    return match.group("label"), match.group("url")


def github_repo_from_url(url):
    parsed = urlparse(url)
    parts = [part for part in parsed.path.split("/") if part]
    if parsed.netloc == "raw.githubusercontent.com" and len(parts) >= 2:
        return f"{parts[0]}/{parts[1]}"
    if parsed.netloc == "github.com" and len(parts) >= 2:
        return f"{parts[0]}/{parts[1]}"
    return None


def classify(spdx):
    if spdx in PERMISSIVE:
        return "permissive"
    if spdx in COPYLEFT:
        return "copyleft"
    if spdx in {"NOASSERTION", "UNAVAILABLE"}:
        return "unclear"
    return "other"


def fetch_license(repo):
    url = f"https://api.github.com/repos/{repo}/license"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": UA,
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.load(resp)
            return payload.get("license", {}).get("spdx_id") or "NOASSERTION"
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return "UNAVAILABLE"
        return f"HTTP-{exc.code}"
    except Exception as exc:  # noqa: BLE001 - report, do not crash the audit
        return type(exc).__name__


def collect(offline):
    conventions = load_targets()
    allowed_urls = declared_urls(conventions)
    errors = []
    examples = []
    repos = defaultdict(set)
    websites = defaultdict(set)

    for slug, name, path in iter_examples():
        provenance = read_provenance(path)
        if not provenance:
            errors.append(f"{slug}/examples/{name}: missing line-1 provenance")
            continue
        label, url = provenance
        if url not in allowed_urls:
            errors.append(f"{slug}/examples/{name}: provenance URL is not declared in scripts/targets.json")
        examples.append((slug, name, label, url))
        repo = github_repo_from_url(url)
        if repo:
            repos[repo].add(slug)
        else:
            websites[urlparse(url).netloc or url].add(slug)

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        sys.exit(1)

    licenses = {}
    if not offline:
        for repo in sorted(repos):
            licenses[repo] = fetch_license(repo)
    return examples, repos, websites, licenses


def print_text(examples, repos, websites, licenses, offline):
    print(f"checked {len(examples)} vendored examples")
    print(f"github sources: {len(repos)}")
    print(f"website sources: {len(websites)}")
    if offline:
        print("offline mode: provenance checked; license API not queried")
        return
    buckets = defaultdict(list)
    for repo, spdx in licenses.items():
        buckets[classify(spdx)].append((repo, spdx))
    for bucket in ("permissive", "copyleft", "unclear", "other"):
        rows = buckets.get(bucket, [])
        if not rows:
            continue
        print(f"\n{bucket}:")
        for repo, spdx in rows:
            slugs = ", ".join(sorted(repos[repo]))
            print(f"  {repo}: {spdx} ({slugs})")
    if websites:
        print("\nwebsite terms / non-GitHub sources:")
        for host, slugs in sorted(websites.items()):
            print(f"  {host}: {', '.join(sorted(slugs))}")


def print_markdown(examples, repos, websites, licenses, offline):
    print("# Example License Report\n")
    print(f"- Vendored examples checked: **{len(examples)}**")
    print(f"- GitHub-backed sources: **{len(repos)}**")
    print(f"- Direct website sources: **{len(websites)}**")
    if offline:
        print("- Mode: **offline provenance check only**")
        return
    print("\n| Source | SPDX / status | Class | Conventions |")
    print("| --- | --- | --- | --- |")
    for repo in sorted(repos):
        spdx = licenses.get(repo, "UNAVAILABLE")
        slugs = ", ".join(sorted(repos[repo]))
        print(f"| `{repo}` | `{spdx}` | {classify(spdx)} | {slugs} |")
    for host, slugs in sorted(websites.items()):
        print(f"| `{host}` | website terms | website | {', '.join(sorted(slugs))} |")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true", help="check provenance only, with no network calls")
    parser.add_argument("--markdown", action="store_true", help="print a Markdown report")
    args = parser.parse_args()

    examples, repos, websites, licenses = collect(args.offline)
    if args.markdown:
        print_markdown(examples, repos, websites, licenses, args.offline)
    else:
        print_text(examples, repos, websites, licenses, args.offline)


if __name__ == "__main__":
    main()
