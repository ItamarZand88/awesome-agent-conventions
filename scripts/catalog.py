#!/usr/bin/env python3
"""Catalog metadata helpers for convention-led pages."""
import json
import os

import jsonschema
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONVENTIONS_DIR = os.path.join(ROOT, "conventions")
CONVENTION_SCHEMA_PATH = os.path.join(ROOT, "scripts", "convention.schema.json")
SOURCES_SCHEMA_PATH = os.path.join(ROOT, "scripts", "sources.schema.json")


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_yaml(path):
    with open(path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    return data or {}


def local_metadata_paths(slug):
    slug_dir = os.path.join(CONVENTIONS_DIR, slug)
    return (
        os.path.join(slug_dir, "convention.yml"),
        os.path.join(slug_dir, "sources.yml"),
    )


def has_local_metadata(slug):
    convention_path, sources_path = local_metadata_paths(slug)
    return os.path.exists(convention_path) or os.path.exists(sources_path)


def load_local_metadata(slug):
    convention_path, sources_path = local_metadata_paths(slug)
    return load_yaml(convention_path), load_yaml(sources_path)


def local_targets(sources):
    targets = []
    for example in sources.get("examples", []):
        targets.append(
            {
                "type": "web",
                "url": example["url"],
                "as": example["filename"],
                "source_label": example["label"],
            }
        )
    return targets


def _schema_errors(schema_path, data):
    schema = load_json(schema_path)
    validator = jsonschema.Draft202012Validator(
        schema,
        format_checker=jsonschema.FormatChecker(),
    )
    return sorted(validator.iter_errors(data), key=lambda err: list(err.path))


def validate_local_metadata(slug, categories):
    errors = []
    convention_path, sources_path = local_metadata_paths(slug)

    if not os.path.exists(convention_path):
        errors.append(f"{slug}: missing convention.yml")
        return errors
    if not os.path.exists(sources_path):
        errors.append(f"{slug}: missing sources.yml")
        return errors

    convention, sources = load_local_metadata(slug)

    for err in _schema_errors(CONVENTION_SCHEMA_PATH, convention):
        path = ".".join(str(p) for p in err.path) or "<root>"
        errors.append(f"{slug}/convention.yml:{path}: {err.message}")

    for err in _schema_errors(SOURCES_SCHEMA_PATH, sources):
        path = ".".join(str(p) for p in err.path) or "<root>"
        errors.append(f"{slug}/sources.yml:{path}: {err.message}")

    if convention.get("slug") != slug:
        errors.append(f"{slug}/convention.yml: slug must equal directory name")
    if sources.get("slug") != slug:
        errors.append(f"{slug}/sources.yml: slug must equal directory name")
    if convention.get("category") not in categories:
        errors.append(f"{slug}/convention.yml: unknown category {convention.get('category')!r}")

    example_labels = [item.get("label") for item in sources.get("examples", [])]
    if len(example_labels) != len(set(example_labels)):
        errors.append(f"{slug}/sources.yml: duplicate example labels")

    return errors
