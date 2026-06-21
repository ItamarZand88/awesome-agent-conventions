### Fields
The frontmatter is the **machine-readable token store**, not just metadata. `name` is the only required field (plus a `primary` color as the practical minimum):

| Field | Req | Notes |
| --- | --- | --- |
| `name` | yes | design-system name |
| `version` | no | spec/format version (current value `alpha`) |
| `description` | no | one-line thesis of the visual identity |
| `colors` | ~ | map tokenName -> CSS color (e.g. `primary`, `canvas`, `accent`) |
| `typography` | no | map -> object (`fontFamily`, `fontWeight`, `fontSize`, `lineHeight`, `letterSpacing`) |
| `spacing` | no | scale of dimensions |
| `rounded` | no | border-radius scale |
| `components` | no | per-component token bindings (may use composite refs like `{typography.label-md}`) |

**Markdown body sections** (canonical core, in order; omit if irrelevant): Overview -> Colors -> Typography -> Layout -> Elevation & Depth -> Shapes -> Components -> Do's and Don'ts. Examples commonly add Responsive Behavior, Iteration Guide, Known Gaps. **Token references** use `{path.to.token}` (e.g. `{colors.primary}`), binding prose to the frontmatter so they don't drift.

### Composition
- A consistent spine: a frontmatter token store + a body that orders Overview -> Colors -> Typography -> Layout -> ... -> Components, plus the parts that make it *operable*: Do's and Don'ts and Known Gaps.
- Token-keyed values keep prose and tokens bound: `{colors.canvas}` (#f7f7f4), `{colors.primary}` (#f54e00).

### Anti-patterns
- A human architecture/design doc mislabeled `DESIGN.md` - that's a doc for people and fails this collection's filter.
- Prose that describes vibes without emitting tokens an agent can apply ("clean and modern" generates nothing).
- Dropping Do's and Don'ts / Known Gaps - without them the file documents a look but can't *steer* generation.

### Edge cases
- **Open-sourced by Google Labs in 2026** (Apache-2.0 draft spec at `github.com/google-labs-code/design.md`) and repositioned as cross-tool - meant for Claude Code and other coding agents, not just Stitch. Still a draft (`version: alpha`), so the `components` token vocabulary is per-file, not yet a shared standard.
- **Scarcity is encoded, not assumed:** Cursor's spec reserves its one brand color "used scarcely" and pins display weight at 400 - constraints an agent must be told.
- A `DESIGN.md` is a *mirror* of a design system, not its source of truth - it goes stale unless regenerated when the system changes.

### Adoption / maturity
- DESIGN.md is adopted enough to matter because the spec, CLI, examples, and Google Labs repository are public, and example libraries already collect real brand files. The format itself is still marked `alpha`, so lint against the current spec before treating a file as authoritative.
- The CLI makes the format more than prose: `lint` catches broken token references and contrast issues, `diff` surfaces regressions, and `export` can emit Tailwind v3, Tailwind v4 CSS tokens, or W3C DTCG-compatible tokens.

### Related conventions
- Use DESIGN.md for visual identity and reusable UI system constraints. Do not use it for product requirements, architecture notes, or generic app documentation.
- Pair with AGENTS.md when the agent also needs build/test commands or implementation workflow; keep those out of the design spec.

### Sources checked
- [Google Labs DESIGN.md repository](https://github.com/google-labs-code/design.md)
- [DESIGN.md examples collection](https://github.com/VoltAgent/awesome-design-md)
