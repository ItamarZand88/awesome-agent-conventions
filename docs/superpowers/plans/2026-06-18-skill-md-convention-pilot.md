# Skill-md Convention Pilot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first convention-led catalog page for `skill-md`, backed by local `convention.yml` and `sources.yml` metadata while preserving deterministic fetching and verification.

**Architecture:** Add a small catalog metadata layer that can read per-convention YAML files and fall back to `scripts/targets.json` for conventions not yet migrated. Update the extractor/generator only enough for the `skill-md` pilot, then validate the new local files and generated README through existing verification commands.

**Tech Stack:** Python 3, `jsonschema`, `requests`, new dependency `PyYAML`, Markdown, YAML, existing Makefile verification targets.

## Global Constraints

- Pilot only `conventions/skill-md` before migrating other conventions.
- Keep fetched examples with line-1 provenance comments.
- Render convention explanation before examples.
- Keep `scripts/targets.json` working for all non-pilot conventions.
- Do not remove extracted examples.
- Do not hand-edit generated README output after generator support exists.
- Existing checks must pass: schema, generated docs, example provenance, and links.

---

## File Structure

- Create `conventions/skill-md/convention.yml`: hand-curated convention metadata for the pilot.
- Create `conventions/skill-md/sources.yml`: hand-curated research sources and example fetch targets for the pilot.
- Create `scripts/convention.schema.json`: schema for local convention metadata.
- Create `scripts/sources.schema.json`: schema for local research and example metadata.
- Create `scripts/catalog.py`: shared loader/normalizer for `convention.yml`, `sources.yml`, and legacy `targets.json` data.
- Modify `scripts/requirements.txt`: add `PyYAML`.
- Modify `scripts/validate_targets.py`: validate pilot local metadata and keep legacy checks.
- Modify `scripts/extract.py`: render migrated conventions from local metadata; keep legacy rendering for the rest.
- Modify `scripts/check_links.py` if local source URLs are not already discovered from generated README output.
- Modify `conventions/skill-md/README.md`: generated output changes from example-led to convention-led.
- Modify `CONTRIBUTING.md`: document the pilot metadata model and when to use local files.

---

### Task 1: Add YAML Dependency And Local Metadata Schemas

**Files:**
- Modify: `scripts/requirements.txt`
- Create: `scripts/convention.schema.json`
- Create: `scripts/sources.schema.json`

**Interfaces:**
- Consumes: Existing `jsonschema` validation pattern in `scripts/validate_targets.py`.
- Produces: JSON Schemas consumed by `scripts/catalog.py` / `scripts/validate_targets.py`.

- [ ] **Step 1: Add the YAML dependency**

Modify `scripts/requirements.txt` to:

```text
jsonschema>=4.23
requests>=2.31
PyYAML>=6.0
```

- [ ] **Step 2: Create `scripts/convention.schema.json`**

Create the file with this schema:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/ItamarZand88/awesome-agent-conventions/blob/main/scripts/convention.schema.json",
  "title": "awesome-agent-conventions local convention metadata",
  "type": "object",
  "required": [
    "slug",
    "name",
    "category",
    "maturity",
    "summary",
    "purpose",
    "readers",
    "locations",
    "files",
    "principles",
    "related"
  ],
  "additionalProperties": false,
  "properties": {
    "slug": { "type": "string", "pattern": "^[a-z0-9]+(?:-[a-z0-9]+)*$" },
    "name": { "type": "string", "minLength": 1 },
    "category": { "type": "string", "minLength": 1 },
    "maturity": { "enum": ["🟢", "🟠", "🔵"] },
    "summary": { "type": "string", "minLength": 1 },
    "purpose": { "type": "string", "minLength": 1 },
    "readers": {
      "type": "array",
      "minItems": 1,
      "items": { "type": "string", "minLength": 1 }
    },
    "writers": {
      "type": "array",
      "items": { "type": "string", "minLength": 1 }
    },
    "locations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["path", "description"],
        "additionalProperties": false,
        "properties": {
          "path": { "type": "string", "minLength": 1 },
          "description": { "type": "string", "minLength": 1 }
        }
      }
    },
    "loading": {
      "type": "array",
      "items": { "type": "string", "minLength": 1 }
    },
    "files": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["name", "description"],
        "additionalProperties": false,
        "properties": {
          "name": { "type": "string", "minLength": 1 },
          "description": { "type": "string", "minLength": 1 },
          "required": { "type": "boolean" }
        }
      }
    },
    "shape": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "description"],
        "additionalProperties": false,
        "properties": {
          "name": { "type": "string", "minLength": 1 },
          "description": { "type": "string", "minLength": 1 },
          "required": { "type": "boolean" }
        }
      }
    },
    "principles": {
      "type": "array",
      "minItems": 1,
      "items": { "type": "string", "minLength": 1 }
    },
    "related": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["slug", "relationship"],
        "additionalProperties": false,
        "properties": {
          "slug": { "type": "string", "minLength": 1 },
          "relationship": { "type": "string", "minLength": 1 }
        }
      }
    }
  }
}
```

- [ ] **Step 3: Create `scripts/sources.schema.json`**

Create the file with this schema:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/ItamarZand88/awesome-agent-conventions/blob/main/scripts/sources.schema.json",
  "title": "awesome-agent-conventions local sources metadata",
  "type": "object",
  "required": ["slug", "research", "examples"],
  "additionalProperties": false,
  "properties": {
    "slug": { "type": "string", "pattern": "^[a-z0-9]+(?:-[a-z0-9]+)*$" },
    "research": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["label", "url", "type", "why"],
        "additionalProperties": false,
        "properties": {
          "label": { "type": "string", "minLength": 1 },
          "url": { "type": "string", "format": "uri" },
          "type": { "enum": ["spec", "docs", "repo", "example", "article"] },
          "why": { "type": "string", "minLength": 1 }
        }
      }
    },
    "examples": {
      "type": "array",
      "items": {
        "type": "object",
        "required": [
          "label",
          "represents",
          "upstream",
          "url",
          "filename"
        ],
        "additionalProperties": false,
        "properties": {
          "label": { "type": "string", "minLength": 1 },
          "represents": { "type": "string", "minLength": 1 },
          "upstream": {
            "type": "object",
            "required": ["label", "url"],
            "additionalProperties": false,
            "properties": {
              "label": { "type": "string", "minLength": 1 },
              "url": { "type": "string", "format": "uri" }
            }
          },
          "url": { "type": "string", "format": "uri" },
          "filename": { "type": "string", "minLength": 1 }
        }
      }
    }
  }
}
```

- [ ] **Step 4: Run schema syntax checks**

Run:

```bash
.venv/bin/python -m json.tool scripts/convention.schema.json >/dev/null
.venv/bin/python -m json.tool scripts/sources.schema.json >/dev/null
```

Expected: both commands exit `0`.

- [ ] **Step 5: Commit**

```bash
git add scripts/requirements.txt scripts/convention.schema.json scripts/sources.schema.json
git commit -m "Add local convention metadata schemas"
```

---

### Task 2: Add Local Metadata Loader

**Files:**
- Create: `scripts/catalog.py`
- Modify: `scripts/validate_targets.py`

**Interfaces:**
- Consumes: `conventions/<slug>/convention.yml`, `conventions/<slug>/sources.yml`, `scripts/targets.json`.
- Produces:
  - `load_yaml(path: str) -> dict`
  - `local_metadata_paths(slug: str) -> tuple[str, str]`
  - `has_local_metadata(slug: str) -> bool`
  - `load_local_metadata(slug: str) -> tuple[dict, dict]`
  - `validate_local_metadata(slug: str, categories: set[str]) -> list[str]`

- [ ] **Step 1: Write the loader**

Create `scripts/catalog.py`:

```python
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
```

- [ ] **Step 2: Validate import fails before dependency install when PyYAML is missing**

Run:

```bash
.venv/bin/python - <<'PY'
import scripts.catalog
print("catalog import ok")
PY
```

Expected after installing `PyYAML`: prints `catalog import ok`. If it fails with `ModuleNotFoundError: No module named 'yaml'`, run `.venv/bin/pip install -r scripts/requirements.txt`.

- [ ] **Step 3: Wire local validation into `validate_targets.py`**

Add this import near the top:

```python
from scripts.catalog import has_local_metadata, validate_local_metadata
```

Inside the `for slug, conv in conventions.items():` loop, after category/maturity checks, add:

```python
        if has_local_metadata(slug):
            errors.extend(validate_local_metadata(slug, category_set))
```

- [ ] **Step 4: Run validation**

Run:

```bash
.venv/bin/python scripts/validate_targets.py
```

Expected before adding pilot files: still passes, because no convention has local metadata yet.

- [ ] **Step 5: Commit**

```bash
git add scripts/catalog.py scripts/validate_targets.py
git commit -m "Load local convention metadata"
```

---

### Task 3: Create `skill-md` Convention-Led Metadata

**Files:**
- Create: `conventions/skill-md/convention.yml`
- Create: `conventions/skill-md/sources.yml`

**Interfaces:**
- Consumes: schemas from Task 1.
- Produces: local metadata consumed by `scripts/catalog.py`, `scripts/validate_targets.py`, and later `scripts/extract.py`.

- [ ] **Step 1: Create `conventions/skill-md/convention.yml`**

```yaml
slug: skill-md
name: SKILL.md
category: Skills & prompt assets
maturity: 🟢
summary: A self-contained, model-invoked capability file that tells an agent when to load a reusable procedure and how to execute it.
purpose: SKILL.md lets an agent keep specialized workflows, scripts, references, and resources out of the main context until the model or user needs that capability.
readers:
  - Claude Agent Skills
  - Claude Code
  - Amp
  - Agent Skills-compatible tools
writers:
  - Tool authors
  - Product teams packaging agent capabilities
  - Developers turning repeated agent workflows into reusable capabilities
locations:
  - path: <skill-name>/SKILL.md
    description: Portable Agent Skills directory format; bundled scripts and resources live beside the manifest.
  - path: .claude/skills/<skill-name>/SKILL.md
    description: Claude Code project skill location.
  - path: ~/.claude/skills/<skill-name>/SKILL.md
    description: Claude Code user skill location.
loading:
  - The skill name and description are listed up front; the body and bundled files are loaded only when the skill is relevant.
  - The open specification requires name and description frontmatter; product-specific runtimes may add optional fields.
  - Keep the description precise because it is the activation signal.
files:
  - name: SKILL.md
    required: true
    description: Markdown manifest with YAML frontmatter followed by task instructions.
shape:
  - name: name
    required: true
    description: Lowercase skill identifier; in the open spec it must match the parent directory.
  - name: description
    required: true
    description: Activation text that states what the skill does and when to use it.
  - name: body
    required: true
    description: Procedural instructions, references to bundled resources, and workflow steps.
  - name: bundled files
    required: false
    description: Optional scripts, references, templates, and assets loaded only after the skill is activated.
principles:
  - Use SKILL.md for repeatable capabilities, not standing project context.
  - Put activation criteria in the description, not buried in the body.
  - Keep the body procedural and move bulky reference material into bundled files.
  - Prefer portable open-spec fields unless a runtime-specific extension is necessary.
  - Treat examples as capability packages, not as the definition of the convention.
related:
  - slug: claude-commands
    relationship: Claude commands are legacy or direct-invocation workflows; SKILL.md is better when a capability needs resources, scripts, or model-invoked activation.
  - slug: agents-md
    relationship: AGENTS.md carries standing project instructions; SKILL.md carries reusable procedures.
  - slug: claude-md
    relationship: CLAUDE.md is project memory loaded into context; SKILL.md is loaded on demand.
  - slug: prompt-assets
    relationship: Prompt assets externalize prompts; SKILL.md packages a broader operational capability around instructions and resources.
```

- [ ] **Step 2: Create `conventions/skill-md/sources.yml`**

```yaml
slug: skill-md
research:
  - label: Agent Skills specification
    type: spec
    url: https://agentskills.io/specification
    why: Defines the portable SKILL.md contract, required frontmatter, and packaging model.
  - label: Anthropic Agent Skills overview
    type: docs
    url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
    why: Documents Anthropic product support and how skills are used by Claude.
  - label: Claude Code skills and commands docs
    type: docs
    url: https://code.claude.com/docs/en/slash-commands
    why: Captures Claude Code's command-to-skill convergence and runtime extensions.
  - label: Amp manual
    type: docs
    url: https://ampcode.com/manual
    why: Shows another implementation using skills and runtime-specific skill metadata.
  - label: anthropics/skills
    type: repo
    url: https://github.com/anthropics/skills
    why: Provides maintained public examples of complete skill packages.
examples:
  - label: mcp-builder
    represents: A procedure-heavy skill with a precise activation description and implementation workflow.
    upstream:
      label: anthropics/skills
      url: https://github.com/anthropics/skills
    url: https://raw.githubusercontent.com/anthropics/skills/main/skills/mcp-builder/SKILL.md
    filename: SKILL.md
  - label: pdf
    represents: A skill that relies on bundled tooling and domain-specific operational guidance.
    upstream:
      label: anthropics/skills
      url: https://github.com/anthropics/skills
    url: https://raw.githubusercontent.com/anthropics/skills/main/skills/pdf/SKILL.md
    filename: SKILL.md
```

- [ ] **Step 3: Run validation**

Run:

```bash
.venv/bin/python scripts/validate_targets.py
```

Expected: `targets.json valid - 21 conventions across 11 categories`.

- [ ] **Step 4: Commit**

```bash
git add conventions/skill-md/convention.yml conventions/skill-md/sources.yml
git commit -m "Add skill-md local catalog metadata"
```

---

### Task 4: Render `skill-md` From Local Metadata

**Files:**
- Modify: `scripts/catalog.py`
- Modify: `scripts/extract.py`
- Modify: `conventions/skill-md/README.md`

**Interfaces:**
- Consumes:
  - `load_local_metadata(slug) -> tuple[dict, dict]`
  - existing `examples_for(examples_dir, filename)`
  - existing `read_provenance(path) -> tuple[str, str | None]`
- Produces:
  - `local_targets(sources: dict) -> list[dict]`
  - migrated README renderer for `skill-md`.

- [ ] **Step 1: Add target normalization to `scripts/catalog.py`**

Append:

```python
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
```

- [ ] **Step 2: Import helpers in `scripts/extract.py`**

Add near imports:

```python
from scripts.catalog import has_local_metadata, load_local_metadata, local_targets
```

- [ ] **Step 3: Use local targets for fetching migrated conventions**

At the start of `process_convention`, add:

```python
    local_convention = None
    local_sources = None
    if has_local_metadata(slug):
        local_convention, local_sources = load_local_metadata(slug)
        conv = {
            **conv,
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
```

- [ ] **Step 4: Add a local README renderer**

In `scripts/extract.py`, create `rebuild_local_convention_readme(slug, convention, sources)` beside `rebuild_convention_readme`:

```python
def markdown_list(items):
    return "\n".join(f"- {item}" for item in items)


def rebuild_local_convention_readme(slug, convention, sources):
    slug_dir = os.path.join(CONVENTIONS_DIR, slug)
    examples_dir = os.path.join(slug_dir, "examples")
    badge = BADGES.get(convention["maturity"], convention["maturity"])
    out = []

    out.append(f"# {convention['name']} {badge}")
    out.append("")
    out.append(f"> {convention['summary']}")
    out.append("")
    out.append("## What it is")
    out.append("")
    out.append(convention["purpose"])
    out.append("")
    out.append("## Who reads or writes it")
    out.append("")
    out.append("**Readers:**")
    out.append("")
    out.append(markdown_list(convention["readers"]))
    if convention.get("writers"):
        out.append("")
        out.append("**Writers:**")
        out.append("")
        out.append(markdown_list(convention["writers"]))
    out.append("")
    out.append("## Where it lives")
    out.append("")
    for item in convention["locations"]:
        out.append(f"- `{item['path']}` - {item['description']}")
    if convention.get("loading"):
        out.append("")
        out.append("## Loading rules")
        out.append("")
        out.append(markdown_list(convention["loading"]))
    out.append("")
    out.append("## File shape")
    out.append("")
    out.append("| Part | Required | Meaning |")
    out.append("| --- | --- | --- |")
    for item in convention.get("shape", []):
        req = "yes" if item.get("required") else "no"
        out.append(f"| `{item['name']}` | {req} | {item['description']} |")
    out.append("")
    out.append("## Operational principles")
    out.append("")
    out.append(markdown_list(convention["principles"]))
    if convention.get("related"):
        out.append("")
        out.append("## Interoperability")
        out.append("")
        for item in convention["related"]:
            out.append(f"- [`{item['slug']}`](../{item['slug']}/) - {item['relationship']}")
    out.append("")
    out.append("## Field notes")
    out.append("")
    notes_path = os.path.join(slug_dir, "field-notes.md")
    with open(notes_path, encoding="utf-8") as fh:
        out.append(fh.read().strip("\n"))
    out.append("")
    out.append("## Evidence and sources")
    out.append("")
    out.append("| Source | Type | Why it matters |")
    out.append("| --- | --- | --- |")
    for item in sources["research"]:
        out.append(f"| [{item['label']}]({item['url']}) | `{item['type']}` | {item['why']} |")
    out.append("")
    out.append("## Examples")
    out.append("")
    out.append(
        "_Examples are curated evidence for the convention. They are fetched by "
        "[`scripts/extract.py`](../../scripts/extract.py) and keep line-1 provenance._"
    )
    out.append("")
    if sources.get("examples"):
        out.append("| Example | Represents | Upstream | File | Exact source |")
        out.append("| --- | --- | --- | --- | --- |")
        for example in sources["examples"]:
            local_path = os.path.join(
                "examples",
                source_dirname(example["label"]),
                example["filename"],
            )
            out.append(
                f"| `{example['label']}` | {example['represents']} | "
                f"[`{example['upstream']['label']}`]({example['upstream']['url']}) | "
                f"[`{local_path}`]({local_path}) | [source]({example['url']}) |"
            )
    else:
        out.append("_No examples are currently vendored for this convention._")
    out.append("")

    readme_path = os.path.join(slug_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    print(f"  readme: {os.path.relpath(readme_path, ROOT)}")
```

- [ ] **Step 5: Dispatch local renderer from `process_convention`**

Replace the final `rebuild_convention_readme(slug, conv)` call with:

```python
    if local_convention and local_sources:
        rebuild_local_convention_readme(slug, local_convention, local_sources)
    else:
        rebuild_convention_readme(slug, conv)
```

- [ ] **Step 6: Regenerate the pilot page**

Run:

```bash
.venv/bin/python scripts/extract.py --only skill-md --index-only
```

Expected: `conventions/skill-md/README.md` starts with `## What it is` before `## Examples`.

- [ ] **Step 7: Commit**

```bash
git add scripts/catalog.py scripts/extract.py conventions/skill-md/README.md
git commit -m "Render skill-md from local metadata"
```

---

### Task 5: Keep Generated Checks Stable

**Files:**
- Modify: `scripts/check_generated.py` if needed
- Modify: `scripts/check_links.py` if needed
- Modify: generated docs if the generators change them

**Interfaces:**
- Consumes: existing `make verify` pipeline.
- Produces: stable generated-output check with local metadata support.

- [ ] **Step 1: Run generated check**

Run:

```bash
.venv/bin/python scripts/check_generated.py
```

Expected: `generated outputs stable`.

- [ ] **Step 2: If generated check fails, inspect stat**

Run:

```bash
git --no-pager diff --stat -- README.md conventions categories
```

Expected: only `conventions/skill-md/README.md` should differ from the previous generator model. If root/category pages differ, keep them only when they reflect intentional `skill-md` metadata.

- [ ] **Step 3: Run link check**

Run:

```bash
.venv/bin/python scripts/check_links.py
```

Expected: all URLs resolve. If links from `sources.yml` are not discovered because they only appear in generated `skill-md/README.md` after generation, no code change is needed. If they are missed, update `scripts/check_links.py` to include links from generated convention READMEs, matching its existing Markdown URL extraction style.

- [ ] **Step 4: Run full verification**

Run:

```bash
make verify PYTHON=.venv/bin/python
```

Expected:

```text
targets.json valid - 21 conventions across 11 categories
generated outputs stable
checked 60 vendored examples
checked 85 urls - 85 ok, 0 degraded, 0 warn, 0 FAIL
```

The URL count may increase if `sources.yml` adds rendered links that were not previously present. The pass condition is `0 FAIL`.

- [ ] **Step 5: Commit**

```bash
git add scripts/check_generated.py scripts/check_links.py README.md categories conventions
git commit -m "Keep generated checks stable for local metadata"
```

Only include files that actually changed.

---

### Task 6: Document The Pilot Contributor Workflow

**Files:**
- Modify: `CONTRIBUTING.md`
- Modify: `README.md` only if root generated copy needs a short mention through `scripts/build_readme.py`
- Modify: `scripts/build_readme.py` only if root generated copy changes

**Interfaces:**
- Consumes: final local metadata model from Tasks 1-5.
- Produces: contributor guidance for pilot-era metadata.

- [ ] **Step 1: Update `CONTRIBUTING.md`**

Add this section after "How to add or update an entry":

```markdown
## Convention-led metadata pilot

`skill-md` is the first convention-led page. It keeps hand-curated convention
metadata in `conventions/skill-md/convention.yml` and evidence/example metadata
in `conventions/skill-md/sources.yml`. During the pilot, other conventions still
use `scripts/targets.json`.

For migrated conventions:

- Put stable facts in `convention.yml`.
- Put specs, docs, repos, and example fetch targets in `sources.yml`.
- Keep interpretation, anti-patterns, and edge cases in `field-notes.md`.
- Let `scripts/extract.py` regenerate the README and examples.

Do not migrate another convention until the `skill-md` pilot has been reviewed.
```

- [ ] **Step 2: Run Markdown grep for stale guidance**

Run:

```bash
rg -n "targets.json is the single source of truth|single source of truth" README.md CONTRIBUTING.md scripts conventions
```

Expected: either no stale claim, or wording that explicitly says `targets.json` remains the legacy source for non-migrated conventions.

- [ ] **Step 3: Commit**

```bash
git add CONTRIBUTING.md README.md scripts/build_readme.py
git commit -m "Document convention-led metadata pilot"
```

Only include files that actually changed.

---

### Task 7: Final Pilot Verification And Review

**Files:**
- Review all changed files from Tasks 1-6.

**Interfaces:**
- Consumes: completed pilot.
- Produces: verified branch ready for push or PR.

- [ ] **Step 1: Run syntax checks**

Run:

```bash
.venv/bin/python -m py_compile scripts/catalog.py scripts/extract.py scripts/validate_targets.py scripts/check_generated.py scripts/check_links.py
```

Expected: exit `0`.

- [ ] **Step 2: Run full verification**

Run:

```bash
make verify PYTHON=.venv/bin/python
```

Expected: validation, generated output, example provenance, and link checks all pass with `0 FAIL`.

- [ ] **Step 3: Inspect the pilot README manually**

Run:

```bash
sed -n '1,260p' conventions/skill-md/README.md
```

Expected ordering:

```text
# SKILL.md
## What it is
## Who reads or writes it
## Where it lives
## Loading rules
## File shape
## Operational principles
## Interoperability
## Field notes
## Evidence and sources
## Examples
```

- [ ] **Step 4: Confirm examples still exist and have provenance**

Run:

```bash
head -n 1 conventions/skill-md/examples/mcp-builder/SKILL.md
head -n 1 conventions/skill-md/examples/pdf/SKILL.md
```

Expected: each line starts with `<!-- source:`.

- [ ] **Step 5: Check git diff**

Run:

```bash
git diff --stat
git diff --check
```

Expected: `git diff --check` exits `0`.

- [ ] **Step 6: Commit any remaining final adjustments**

```bash
git add -A
git commit -m "Pilot convention-led skill-md catalog page"
```

Skip this commit if there are no remaining changes after prior task commits.

---

## Self-Review

- Spec coverage: The plan implements the `skill-md` pilot, local `convention.yml`, local `sources.yml`, generator support, deterministic fetching, validation, documentation, and final verification.
- Red-flag scan: No vague markers or unspecified "handle later" steps remain.
- Type consistency: Local metadata functions are named consistently across tasks: `has_local_metadata`, `load_local_metadata`, `validate_local_metadata`, and `local_targets`.
- Scope check: The plan does not migrate any convention beyond `skill-md`.
