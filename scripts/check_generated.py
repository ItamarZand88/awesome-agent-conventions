#!/usr/bin/env python3
"""Fail if running the generators changes generated files.

Unlike a raw `git diff --exit-code`, this is friendly to local work in progress:
it snapshots the existing diff, runs the generators, and fails only if the diff
changed. In CI, the starting diff is empty, so it still catches missing generated
outputs.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENERATED_PATHS = ["README.md", "conventions", "categories"]


def run(args, **kwargs):
    return subprocess.run(args, cwd=ROOT, check=True, text=True, **kwargs)


def diff():
    result = subprocess.run(
        ["git", "diff", "--", *GENERATED_PATHS],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def main():
    before = diff()
    run([sys.executable, "scripts/build_readme.py"], stdout=subprocess.DEVNULL)
    run([sys.executable, "scripts/extract.py", "--index-only"], stdout=subprocess.DEVNULL)
    after = diff()
    if before != after:
        print("Generated files changed after running generators.", file=sys.stderr)
        print("Run `make build` and commit the result.", file=sys.stderr)
        subprocess.run(["git", "--no-pager", "diff", "--stat", "--", *GENERATED_PATHS], cwd=ROOT)
        sys.exit(1)
    print("generated outputs stable")


if __name__ == "__main__":
    main()
