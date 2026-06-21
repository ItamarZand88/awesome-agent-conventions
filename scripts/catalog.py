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


def has_complete_local_metadata(slug):
    convention_path, sources_path = local_metadata_paths(slug)
    return os.path.exists(convention_path) and os.path.exists(sources_path)


def load_local_metadata(slug):
    convention_path, sources_path = local_metadata_paths(slug)
    return load_yaml(convention_path), load_yaml(sources_path)


def iter_complete_local_metadata():
    for slug in sorted(os.listdir(CONVENTIONS_DIR)):
        if has_complete_local_metadata(slug):
            yield slug, *load_local_metadata(slug)


def complete_local_metadata_slugs():
    return [slug for slug, _, _ in iter_complete_local_metadata()]


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


def local_example_urls(slug_or_sources):
    if isinstance(slug_or_sources, str):
        _, sources = load_local_metadata(slug_or_sources)
    else:
        sources = slug_or_sources
    return [example["url"] for example in sources.get("examples", []) if example.get("url")]


def local_source_urls(slug_or_sources):
    if isinstance(slug_or_sources, str):
        _, sources = load_local_metadata(slug_or_sources)
    else:
        sources = slug_or_sources

    urls = []
    for item in sources.get("research", []):
        if item.get("url"):
            urls.append(item["url"])
    for example in sources.get("examples", []):
        if example.get("url"):
            urls.append(example["url"])
        upstream = example.get("upstream", {})
        if upstream.get("url"):
            urls.append(upstream["url"])
    return urls


def local_link_entries(slug_or_sources):
    if isinstance(slug_or_sources, str):
        _, sources = load_local_metadata(slug_or_sources)
    else:
        sources = slug_or_sources

    entries = []
    for item in sources.get("research", []):
        if item.get("url"):
            entries.append(("research", item["url"]))
    for example in sources.get("examples", []):
        if example.get("url"):
            entries.append(("example", example["url"]))
        upstream = example.get("upstream", {})
        if upstream.get("url"):
            entries.append(("upstream", upstream["url"]))
    return entries


def legacy_example_urls(convention):
    urls = []
    for target in convention.get("targets", []):
        if target.get("url"):
            urls.append(target["url"])
        elif target.get("type") == "github":
            urls.append(
                f"https://github.com/{target['owner']}/{target['repo']}"
                f"/blob/HEAD/{target['path']}"
            )
    return urls


def effective_example_urls(slug, convention):
    if has_complete_local_metadata(slug):
        return local_example_urls(slug)
    return legacy_example_urls(convention)


def effective_link_entries(slug, convention):
    if has_complete_local_metadata(slug):
        return local_link_entries(slug)

    entries = []
    if convention.get("spec"):
        entries.append(("spec", convention["spec"]))
    for target in convention.get("targets", []):
        if target.get("url"):
            entries.append(("target", target["url"]))
    for file_entry in convention.get("files", []):
        for instance in file_entry.get("instances", []):
            if instance.get("url"):
                entries.append(("instance", instance["url"]))
    return entries


def local_spec_url(sources):
    for item in sources.get("research", []):
        if item.get("type") == "spec" and item.get("url"):
            return item["url"]
    return None


def overlay_local_convention(conv, local_convention, local_sources):
    overlaid = dict(conv)
    overlaid.update(
        {
            "name": local_convention["name"],
            "category": local_convention["category"],
            "maturity": local_convention["maturity"],
            "summary": local_convention["summary"],
            "read_by": ", ".join(local_convention["readers"]),
            "location": "; ".join(
                f"{item['path']} - {item['description']}"
                for item in local_convention["locations"]
            ),
            "files": [
                {"name": item["name"], "note": item["description"]}
                for item in local_convention["files"]
            ],
            "targets": local_targets(local_sources),
        }
    )
    spec = local_spec_url(local_sources)
    if spec:
        overlaid["spec"] = spec
    return overlaid


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
