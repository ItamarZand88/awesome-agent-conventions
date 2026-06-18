#!/usr/bin/env python3
"""Validate scripts/targets.json and the generated convention tree.

This goes beyond JSON syntax: it checks the JSON Schema, category references,
slug names, target-to-file matching, generated directories, and orphan
convention pages. The goal is to catch catalog drift before it reaches CI.
"""
import json
import os
import re
import sys
from urllib.parse import urlparse

import jsonschema

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGETS_PATH = os.path.join(ROOT, "scripts", "targets.json")
SCHEMA_PATH = os.path.join(ROOT, "scripts", "targets.schema.json")
CONVENTIONS_DIR = os.path.join(ROOT, "conventions")

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MATURITIES = {"🟢", "🟠", "🔵"}


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def target_filename(target):
    if target.get("as"):
        return target["as"]
    if target.get("type") == "github":
        return os.path.basename(target["path"]) or "index"
    return os.path.basename(urlparse(target["url"]).path) or "index"


def file_matches_declared(filename, declared):
    for item in declared:
        name = item["name"]
        if item.get("kind") == "pattern":
            continue
        if name.startswith("."):
            if filename.endswith(name):
                return True
        elif filename == name:
            return True
    return False


def fail(errors):
    for err in errors:
        print(f"ERROR: {err}", file=sys.stderr)
    sys.exit(1)


def main():
    errors = []
    data = load_json(TARGETS_PATH)
    schema = load_json(SCHEMA_PATH)

    validator = jsonschema.Draft202012Validator(
        schema,
        format_checker=jsonschema.FormatChecker(),
    )
    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        path = ".".join(str(p) for p in err.path) or "<root>"
        errors.append(f"{path}: {err.message}")

    categories = data.get("categories", [])
    category_set = set(categories)
    conventions = data.get("conventions", {})

    for slug, conv in conventions.items():
        if not SLUG_RE.match(slug):
            errors.append(f"{slug}: slug must be lowercase kebab-case")
        if conv.get("category") not in category_set:
            errors.append(f"{slug}: unknown category {conv.get('category')!r}")
        if conv.get("maturity") not in MATURITIES:
            errors.append(f"{slug}: unknown maturity {conv.get('maturity')!r}")

        files = conv.get("files", [])
        names = [f.get("name") for f in files]
        if len(names) != len(set(names)):
            errors.append(f"{slug}: duplicate file names in files[]")
        for item in files:
            if item.get("kind") == "pattern":
                if not item.get("pattern"):
                    errors.append(f"{slug}: pattern file {item['name']!r} needs a pattern description")
                for inst in item.get("instances", []):
                    if not inst.get("label") or not inst.get("url"):
                        errors.append(f"{slug}: pattern instance needs label and url")

        for target in conv.get("targets", []):
            filename = target_filename(target)
            if not file_matches_declared(filename, files):
                errors.append(
                    f"{slug}: target saves as {filename!r}, which does not match any non-pattern file"
                )

        slug_dir = os.path.join(CONVENTIONS_DIR, slug)
        if not os.path.isdir(slug_dir):
            errors.append(f"{slug}: missing conventions/{slug}/ directory")
        elif conv.get("manual_readme"):
            if not os.path.exists(os.path.join(slug_dir, "README.md")):
                errors.append(f"{slug}: manual_readme convention needs README.md")

    actual_dirs = {
        name
        for name in os.listdir(CONVENTIONS_DIR)
        if os.path.isdir(os.path.join(CONVENTIONS_DIR, name))
    }
    expected_dirs = set(conventions)
    for orphan in sorted(actual_dirs - expected_dirs):
        errors.append(f"orphan convention directory: conventions/{orphan}")

    if errors:
        fail(errors)

    used_categories = {conv["category"] for conv in conventions.values()}
    unused = [cat for cat in categories if cat not in used_categories]
    if unused:
        print("warn: unused categories: " + ", ".join(unused))
    print(f"targets.json valid - {len(conventions)} conventions across {len(categories)} categories")


if __name__ == "__main__":
    main()
