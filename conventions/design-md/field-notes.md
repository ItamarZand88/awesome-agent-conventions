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
