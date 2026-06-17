### Composition
- **`*.instructions.md` lead with an `applyTo` glob** (e.g. `applyTo: "**/*.ts"`) plus a `description`. Every file matching the glob silently stacks its instructions into context when Copilot edits a match - path-scoped, automatic.
- **`*.prompt.md` are invoked by name** (slash-command style) and read like a saved task, often with `mode`, `tools`, and `description` frontmatter.

### Anti-patterns
- A broad `applyTo: "**"` instruction file that attaches everywhere - that re-creates the always-on token cost the granular format was meant to avoid.
- Copying the monolithic `.github/copilot-instructions.md` into many files without actually scoping them. Scoping is the whole point.

### Edge cases
- **Paths are converging, not fixed.** Instructions are documented under `.github/instructions/`, but collections (e.g. github/awesome-copilot) ship them under a top-level `/instructions/`. The `applyTo` frontmatter is what binds the rule, not the exact directory.
- Largely VS Code / Copilot territory today: other tools read the single `.github/copilot-instructions.md` but don't all honor the modular `.prompt.md` / `.instructions.md` split.
