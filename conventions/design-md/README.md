# DESIGN.md 🟢 Adopted

> A structured, machine-readable design specification — tokens, components, and layout intent — that an agent reads to generate or keep UI consistent with an established system.

- **Read by:** Google Stitch and design-aware agents that consume a design spec
- **Location:** Repository root or a design/ directory
- **Spec:** [https://stitch.withgoogle.com/docs/design-md/specification](https://stitch.withgoogle.com/docs/design-md/specification)
- **Files:** `DESIGN.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) — none are hand-written._

### `DESIGN.md`

| Source | File | Provenance |
| --- | --- | --- |
| `vinta-awesome-python` | [`vinta-awesome-python.DESIGN.md`](examples/vinta-awesome-python.DESIGN.md) | [source](https://raw.githubusercontent.com/vinta/awesome-python/master/DESIGN.md) |

## Field notes

### Composition
The vinta/awesome-python example is a textbook machine-readable spec:
- **Frontmatter** (`version`, `name`, `description`) + an **Overview** that states audience and *jobs-to-be-done* before any pixels.
- **Token sections** — Colors / Typography / Layout / Elevation & Depth / Shapes / Components — and it explicitly *"follows the Google Stitch DESIGN.md format."*
- A **source-of-truth pointer**: *"token values live in `website/static/style.css`"* — the `.md` mirrors the system, it doesn't own it.

### Anti-patterns
- A human architecture/design doc mislabeled `DESIGN.md` — that's a doc for people and fails this collection's filter.
- Tokens that drift from the real stylesheet; once they disagree, the agent generates against fiction.
- Marketing copy where the spec wants terse, structured values.

### Edge cases
- **Principled divergence is allowed if declared:** the spec calls for hex tokens, but this file uses **OKLCH** and *says so*, naming the divergence rather than hiding it.
- "Source of truth lives in CSS" means the `.md` can go stale — date it or generate it from the stylesheet.
