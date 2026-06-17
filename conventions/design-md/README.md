# DESIGN.md 🟢 Adopted

> A structured, machine-readable design specification - tokens, components, and layout intent - that an agent reads to generate or keep UI consistent with an established system.

- **Read by:** Google Stitch and design-aware agents that consume a design spec
- **Location:** Repository root or a design/ directory
- **Spec:** [https://stitch.withgoogle.com/docs/design-md/specification](https://stitch.withgoogle.com/docs/design-md/specification)
- **Files:** `DESIGN.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `DESIGN.md`

| Source | File | Provenance |
| --- | --- | --- |
| `apple` | [`apple.DESIGN.md`](examples/apple.DESIGN.md) | [source](https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/design-md/apple/DESIGN.md) |
| `claude` | [`claude.DESIGN.md`](examples/claude.DESIGN.md) | [source](https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/design-md/claude/DESIGN.md) |
| `cursor` | [`cursor.DESIGN.md`](examples/cursor.DESIGN.md) | [source](https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/design-md/cursor/DESIGN.md) |
| `figma` | [`figma.DESIGN.md`](examples/figma.DESIGN.md) | [source](https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/design-md/figma/DESIGN.md) |

## Field notes

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
- **`version: alpha`** across these files is a tell: the format itself is still settling, so treat token names as per-file, not a shared vocabulary.
- A `DESIGN.md` is a *mirror* of a design system, not its source of truth - when the site changes, the file goes stale unless regenerated.
