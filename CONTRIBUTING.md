# Contributing

This is a collection of the **real files** AI agents read, write, and act on — not
a glossary. Two rules keep it credible: a strict inclusion filter, and an honest
maturity tier on every entry. Please read both before opening a PR.

## The inclusion filter

A file qualifies only if it is an **agent convention file**: it exists for an AI
agent to **read, write, or act on**.

- ✅ **In:** any file an agent consumes or maintains, regardless of extension —
  `AGENTS.md`, `CLAUDE.md`, `SKILL.md`, `.cursorrules`, `.aiignore`, `.prompty`,
  `llms.txt`, `agent.json`, `pricing.md`, …
- ❌ **Out:** files written for humans — `README.md`, `CONTRIBUTING.md`,
  `SECURITY.md`, `CHANGELOG.md`, `CODE_OF_CONDUCT.md`. A doc a person reads is
  not an agent convention, even if an agent happens to glance at it.

If you can't say *which agent reads or writes the file and what it does with it*,
it probably doesn't belong.

## The maturity requirement

Every entry **must** carry exactly one tier, and you must be able to evidence it.
This is the credibility firewall — a proposed idea is never listed beside an
adopted standard as if they were equal.

| Badge | Tier | Bar to clear |
| --- | --- | --- |
| 🟢 | **Adopted** | Demonstrably in production across multiple tools or teams. |
| 🟠 | **Emerging** | A real published spec from a real org, but early / limited adoption. |
| 🔵 | **Proposed** | A published concept with no demonstrated adoption — often one author staking a namespace. |

If you can't evidence the tier you want, drop the entry or mark it 🔵. When in
doubt, label down, not up.

## How to add or update an entry

`scripts/targets.json` is the single source of truth. Everything else is generated.

1. **Add the convention** to `conventions` in `scripts/targets.json` with its
   `name`, `category` (one of the declared `categories`), `maturity`, `files`,
   `read_by`, `location`, `spec`, and `summary`.
2. **Add real sources** under `targets` — prefer `raw.githubusercontent.com`
   (`{"type": "web", "url": "…"}`), optionally with an `"as"` rename so the saved
   filename matches a declared file. A `{"type": "github", "owner", "repo",
   "path"}` form is also supported via the Contents API (`GITHUB_TOKEN` optional).
   Add `"source_label": "…"` to override the auto-computed label (which defaults
   to the domain or `owner-repo`) — useful when several examples come from one
   repo and should surface by what they are: the design.md entries pull from
   `VoltAgent/awesome-design-md` but label as `apple`, `claude`, `cursor`, `figma`.
3. **Regenerate:**

   ```bash
   pip install -r scripts/requirements.txt
   python scripts/extract.py --only <your-slug>   # fetch + rebuild that page
   python scripts/build_readme.py                 # rebuild the root index
   ```

4. **Write Field notes** in a `conventions/<slug>/field-notes.md` sidecar if you
   have real observations (composition, anti-patterns, edge cases). The extractor
   inlines that sidecar under the generated `## Field notes` heading, so your prose
   survives every regeneration. The sidecar holds the section *body* only (lead
   prose plus `### Composition` / `### Anti-patterns` / `### Edge cases`); the H2 is
   added by the generator. This is where the collection earns its depth.

## Examples vs. patterns

Most files are **artifacts**: the extractor vendors the real file into `examples/`
because its specific content is what teaches. A few files are better shown as a
**pattern** — when the real file is a multi-megabyte dump or pure boilerplate
where any instance just restates the schema (the canonical case is
`llms-full.txt`). For those, set `"kind": "pattern"` on the file in
`scripts/targets.json`, give it a short `pattern` description and a list of
`instances` (`{ "label", "url" }`), and add **no** `targets` for it. The generator
then renders a "Pattern — not an extracted file" block linking the live instances
instead of an examples table, and clears any stale vendored copy.

Default to `artifact`. Reach for `pattern` only when a vendored file would be
noise rather than something worth copying — real files are the whole point of
this collection.

## Rules of the road

- **Don't hand-write example files.** Only the extractor creates them, each with
  a line-1 provenance comment. Hand-typed examples will be rejected.
- **Don't hand-edit generated files** — the root `README.md` and most convention
  `README.md`s are rebuilt by the scripts. The human-editable surfaces are
  `scripts/targets.json` and the per-convention `field-notes.md` sidecars. A
  convention flagged `"manual_readme": true` is the exception: its whole page is
  hand-written and the extractor leaves it alone.
- **Re-run `build_readme.py` after any `targets.json` edit**, or the index goes
  stale.
- **Be honest in summaries about adoption.** Overstating a tier is the one thing
  that breaks this list.
