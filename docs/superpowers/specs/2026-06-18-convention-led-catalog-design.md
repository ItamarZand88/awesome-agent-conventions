# Convention-Led Catalog Design

Date: 2026-06-18

## Context

The catalog has drifted toward an example-led structure: `scripts/targets.json`
declares conventions, fetch targets, labels, and enough metadata to generate the
public README pages. That made the repo reproducible, but it also gave the
fetcher too much editorial responsibility. A deterministic script can preserve
examples and provenance, but it cannot decide which principles define a
convention, why an example is representative, or how a reader should compare
neighboring conventions.

The project should instead read as a field guide to agent conventions. Examples
remain useful evidence, but they are supporting material, not the organizing
principle.

## Goals

- Make each convention page explain the convention before showing examples.
- Keep human editorial judgment close to each convention rather than buried in a
  central generated JSON file.
- Preserve deterministic fetching, provenance, link checking, and generated
  README stability.
- Make upstream origins and research sources explicit without making examples
  the center of the page.
- Pilot the new model on one convention before migrating the whole catalog.

## Non-Goals

- Do not remove extracted examples.
- Do not replace deterministic verification with hand-maintained generated pages.
- Do not redesign every convention in one pass before validating the new shape.
- Do not turn the repo into a large scraped archive of upstream files.

## Recommended Content Model

Each convention should have local, human-curated metadata beside its README:

- `conventions/<slug>/convention.yml`: canonical convention metadata.
- `conventions/<slug>/field-notes.md`: long-form editorial analysis.
- `conventions/<slug>/sources.yml`: research sources and example targets.
- `conventions/<slug>/examples/<example>/<filename>`: fetched examples.

`scripts/targets.json` should gradually shrink from the main editorial source
of truth into an index or compatibility layer. The fetcher should read local
per-convention files, fetch declared examples, and regenerate pages.

## Convention Page Shape

Generated convention READMEs should lead with the convention itself:

1. What it is.
2. Why it exists.
3. Who reads or writes it.
4. Where it lives and how loading works.
5. File shape, schema, or expected sections.
6. Operational principles.
7. Interoperability with nearby conventions.
8. Anti-patterns and edge cases.
9. Evidence and research sources.
10. Curated examples.

Examples should be selected because they clarify the convention. A small set of
well-described examples is better than a long list of fetched files.

## Pilot Scope

The first pilot should be `skill-md`.

Reasons:

- It already exposes the weakness of an example-led page: `mcp-builder` and
  `pdf` are examples, but the real subject is the `SKILL.md` convention.
- The convention has meaningful structure: frontmatter, trigger semantics,
  progressive disclosure, bundled resources, compatibility, and tool-specific
  extensions.
- It has several adjacent conventions to distinguish from: Claude commands,
  AGENTS.md, CLAUDE.md, and prompt assets.

The pilot should add:

- `conventions/skill-md/convention.yml`
- `conventions/skill-md/sources.yml`
- an expanded `conventions/skill-md/field-notes.md` if needed
- generator support for reading the new local files
- generated README output that puts convention principles before examples

## Data Responsibilities

`convention.yml` should describe stable convention facts:

- name
- maturity
- category
- summary
- purpose
- readers
- writers, when relevant
- locations
- loading and precedence rules
- file shape or schema summary
- principles
- related conventions

`sources.yml` should describe evidence:

- official specs and docs
- relevant repositories
- example targets to fetch
- why each example is representative
- upstream repo or domain
- exact source URL or path
- local example label and filename

`field-notes.md` should remain prose:

- practical interpretation
- caveats
- anti-patterns
- edge cases
- migration guidance
- notes that benefit from explanation rather than schema

## Generator Responsibilities

The generator should:

- read local convention metadata first
- render the convention explanation before examples
- fetch only examples declared in `sources.yml`
- keep line-1 provenance comments in fetched files
- keep link and generated-output checks deterministic
- reject stale or ambiguous example metadata during verification

The generator should not infer editorial labels, upstream identity, or example
meaning from URLs when those are provided explicitly.

## Migration Strategy

1. Implement the `skill-md` pilot only.
2. Compare the generated README against the current page.
3. Adjust the schema and page order until the page reads as a reference, not an
   examples report.
4. Add validation for the new local files.
5. Migrate the rest of the conventions in batches by category.
6. Retire or reduce `scripts/targets.json` once all conventions have local
   metadata.

## Verification

The pilot is complete when:

- `conventions/skill-md/README.md` can be regenerated from local metadata.
- fetched examples still include provenance.
- the page explains `SKILL.md` before showing examples.
- upstream origin, exact source, and example purpose are all explicit.
- existing checks pass: schema, generated docs, example provenance, and links.

## Open Decision

After the pilot, decide whether `scripts/targets.json` remains as a generated
aggregate index or is replaced entirely by per-convention metadata plus a small
category index.
