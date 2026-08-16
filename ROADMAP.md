# Roadmap

This is intentionally small. The catalog should stay sharp: real files, real
examples, honest maturity labels.

## v0.1 - Public launch

- Open-source readiness files and templates.
- Generated root README and category pages.
- Schema validation for `scripts/targets.json`.
- Link checking and generated-output drift checks in CI.
- Third-party example notice and license-report tooling.
- Per-convention maturity evidence and `last_verified` metadata.

## v0.2 - Evidence quality

- Expand evidence fields from one-line rationale to structured source links.
- Add stricter provenance checks that connect every example to its declared
  target, saved filename, and upstream source.
- Publish a periodic license report in release notes.

## v0.3 - Discovery and navigation

- Add search-friendly category pages to GitHub Pages or a static site if the
  README grows too dense.
- Add a machine-readable index export for downstream tools.
- Add convention aliases so renamed slugs and legacy paths can be discovered.

## v0.4 - Adoption tracking

- Track documented readers separately from public examples.
- Add "adoption evidence" links for each maturity tier.
- Move watchlist items into full entries only when they meet the promotion bar.

## v0.5 - Effective context semantics

- Track how a convention becomes active at runtime: always-on, path-scoped,
  glob-scoped, explicit invocation, model-selected, or tool-configured.
- Track precedence when several files can apply at once: global vs repo vs
  folder rules, legacy vs modern rule files, and user prompt overrides.
- Track boundaries that affect what actually reaches the agent: ignore files,
  indexing-only excludes, generated outputs, MCP/tool exposure, and prompt assets.
- Add portability notes for same-looking Markdown files whose runtime behavior
  differs across Cursor, Claude Code, Codex, Cline, Devin/Cascade, Windsurf, and
  Copilot.

## Non-goals

- Becoming a glossary of AI terms.
- Listing every prompt-engineering pattern.
- Relicensing upstream examples.
- Treating proposed namespaces as adopted standards.
