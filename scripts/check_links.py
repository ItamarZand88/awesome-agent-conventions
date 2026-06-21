#!/usr/bin/env python3
"""Verify every catalog URL still resolves.

The whole list rests on one promise: the links are real. This checks legacy
`spec`, `targets[].url`, and pattern-file `instances[].url` for conventions
that still rely on `scripts/targets.json`, plus local metadata URLs from
migrated `sources.yml` files for conventions that have complete local metadata.

Failure policy is deliberately honest-but-not-flaky:

- 2xx / 3xx                  → ok
- 404 / 410                  → FAIL (the link is genuinely gone)
- persistent connection error → FAIL (dead host / DNS)
- 401 / 403 / 429 / 5xx      → WARN, not fail (bot-blocking or transient - a
                               CI runner getting Cloudflare-challenged is not
                               the same as a dead link)
- redirect to a shallower path → DEGRADED, not fail (a deep link that now
                               bounces to a docs index - still 200, but no
                               longer lands on the page we promised; the silent
                               rot a plain status check misses)

Exit code is non-zero only when there is at least one FAIL, so CI stays green
through the noise that isn't our problem and goes red on the rot that is.
DEGRADED is surfaced loudly for review but does not break the build - vendors
restructure docs, and that shouldn't redden every contributor's PR.

Usage:
    python scripts/check_links.py            # check every URL
    python scripts/check_links.py --only spec-kit
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

from catalog import effective_link_entries

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGETS_PATH = os.path.join(ROOT, "scripts", "targets.json")

UA = "awesome-agent-conventions-linkcheck/1.0 (+https://github.com/ItamarZand88/awesome-agent-conventions)"
TIMEOUT = 30
RETRIES = 2          # retry transient/connection failures before giving up
DEAD = {404, 410}    # the only codes that mean "this link is gone"


def collect(data, only=None):
    """Yield (kind, slug, url) for every URL we promise resolves."""
    seen_urls = set()
    for slug, conv in data["conventions"].items():
        if only and slug != only:
            continue
        for kind, url in effective_link_entries(slug, conv):
            item = (kind, slug, url)
            if (slug, url) not in seen_urls:
                seen_urls.add((slug, url))
                yield item


def _depth(url):
    """Count non-empty path segments - /a/b/c → 3, / or bare host → 0."""
    return len([p for p in urlparse(url).path.split("/") if p])


def check(item):
    kind, slug, url = item
    last = None
    for attempt in range(RETRIES + 1):
        try:
            req = urllib.request.Request(url, method="GET", headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                final = resp.geturl()
                # A deep link that redirects to a shallower path lost the specific
                # page (e.g. /context/rules → /docs). A redirect that keeps depth
                # is a legit move (page relocated, locale prefix, trailing slash).
                if _depth(final) < _depth(url):
                    return (item, "degraded", final)
                return (item, "ok", resp.status)
        except urllib.error.HTTPError as e:
            if e.code in DEAD:
                return (item, "fail", e.code)
            last = ("warn", e.code)            # 401/403/429/5xx - don't fail
        except Exception as e:                 # noqa: BLE001 - connection/DNS/timeout
            last = ("conn", type(e).__name__)
        if attempt < RETRIES:
            time.sleep(1.5 * (attempt + 1))
    # Persistent connection error => treat as dead; a tolerated HTTP code => warn.
    status, detail = last
    return (item, "fail" if status == "conn" else "warn", detail)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--only", metavar="SLUG", help="check a single convention")
    args = ap.parse_args()

    with open(TARGETS_PATH, encoding="utf-8") as fh:
        data = json.load(fh)
    items = list(collect(data, args.only))
    if not items:
        sys.exit(f"no URLs to check (unknown slug: {args.only!r}?)")

    with ThreadPoolExecutor(max_workers=16) as ex:
        results = list(ex.map(check, items))

    fails = [r for r in results if r[1] == "fail"]
    degraded = [r for r in results if r[1] == "degraded"]
    warns = [r for r in results if r[1] == "warn"]

    tags = {"fail": "FAIL", "degraded": "DEGRADED", "warn": "warn"}
    order = {"fail": 0, "degraded": 1, "warn": 2, "ok": 3}
    for (kind, slug, url), verdict, detail in sorted(results, key=lambda r: order[r[1]]):
        if verdict == "ok":
            continue
        suffix = f"redirects to {detail}" if verdict == "degraded" else detail
        print(f"  {tags[verdict]}  [{slug}] {kind}: {url}  ({suffix})")

    ok = len(results) - len(fails) - len(degraded) - len(warns)
    print(
        f"\nchecked {len(results)} urls - {ok} ok, "
        f"{len(degraded)} degraded, {len(warns)} warn, {len(fails)} FAIL"
    )
    if degraded:
        print(
            "\nDegraded links still return 200 but no longer land on the promised page. "
            "Update local metadata for migrated conventions or scripts/targets.json for legacy conventions, "
            "then re-run the generators."
        )
    if fails:
        print(
            "\nDead links found. Update local metadata for migrated conventions or scripts/targets.json "
            "for legacy conventions, then re-run the generators."
        )
        sys.exit(1)
    if not degraded:
        print("All links resolve and land where promised (warnings are tolerated bot-blocks / transient codes).")


if __name__ == "__main__":
    main()
