### Composition
The VoltAgent brand examples (Apple, Claude, Cursor, Figma) share a consistent, machine-readable spine:
- **Frontmatter** - `version`, `name`, and a dense `description` that captures the brand's whole visual thesis in a sentence (Apple: *"a photography-first interface… a single Action Blue (#0066cc)… UI chrome recedes"*).
- **A fixed section order** - `Overview → Colors → Typography → Layout → Elevation & Depth → Shapes → Components`, then the parts that make it *operable* by an agent: `Do's and Don'ts`, `Responsive Behavior`, an `Iteration Guide`, and an honest `Known Gaps`.
- **Token-keyed values** - colors/sizes are referenced as `{colors.canvas}` (#f7f7f4), `{colors.primary}` (#f54e00), so prose and tokens stay bound together rather than drifting.

### Anti-patterns
- A human architecture/design doc mislabeled `DESIGN.md` - that's a doc for people and fails this collection's filter.
- Prose that describes vibes without emitting tokens an agent can apply ("clean and modern" generates nothing).
- Dropping the `Do's and Don'ts` / `Known Gaps` sections - without them the file documents a look but can't *steer* generation.

### Edge cases
- **Scarcity is encoded, not assumed:** Cursor's spec reserves its one brand color (`{colors.primary}`, Cursor Orange) "used scarcely" and pins display weight at 400 - constraints an agent must be told, because it will otherwise reach for bold and accent everything.
- **The format was open-sourced by Google Labs in 2026** (draft spec at `github.com/google-labs-code/design.md`) and repositioned as cross-tool - meant for Claude Code and other coding agents, not just Stitch. It's still a draft (`version: alpha` in these files), so treat token names as per-file, not yet a shared vocabulary.
- A `DESIGN.md` is a *mirror* of a design system, not its source of truth - when the site changes, the file goes stale unless regenerated.
