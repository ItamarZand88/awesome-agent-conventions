# Copilot prompt & instruction files 🟢 Adopted

> Modular, path-scoped Copilot context: *.instructions.md auto-attach to matching files via an applyTo glob, while *.prompt.md are reusable prompts you invoke by name - the granular cousins of a single .github/copilot-instructions.md.

- **Read by:** GitHub Copilot in VS Code / Copilot CLI
- **Location:** .github/prompts/*.prompt.md and .github/instructions/*.instructions.md
- **Spec:** [https://code.visualstudio.com/docs/agent-customization/prompt-files](https://code.visualstudio.com/docs/agent-customization/prompt-files)
- **Files:** `.prompt.md`, `.instructions.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `.prompt.md`

Invokable saved prompts under .github/prompts/, run as a slash-command.

| Source | File | Provenance |
| --- | --- | --- |
| `playwright-movies` | [`playwright-movies.generate.prompt.md`](examples/playwright-movies.generate.prompt.md) | [source](https://raw.githubusercontent.com/debs-obrien/playwright-movies-app/main/.github/prompts/generate.prompt.md) |

### `.instructions.md`

Auto-attached instructions under .github/instructions/, scoped by an applyTo glob in frontmatter.

| Source | File | Provenance |
| --- | --- | --- |
| `awesome-copilot` | [`awesome-copilot.a11y.instructions.md`](examples/awesome-copilot.a11y.instructions.md) | [source](https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/a11y.instructions.md) |

## Field notes

### Fields (frontmatter)
**`*.prompt.md`** (invokable saved prompts; all optional):

| Field | Notes |
| --- | --- |
| `description` | short description of the prompt |
| `name` | name shown after typing `/` (defaults to the filename) |
| `argument-hint` | hint text in the chat input |
| `agent` | `ask` / `agent` / `plan` or a custom agent (this is the current name; `mode` is the legacy alias) |
| `model` | model identifier (defaults to the selected model) |
| `tools` | tool/toolset names, MCP tools, or `<server>/*` |

**`*.instructions.md`** (auto-attached instructions; all optional):

| Field | Notes |
| --- | --- |
| `applyTo` | glob(s) deciding which files auto-attach the instructions; `**` = all files |
| `description` | hover text in the Chat view |
| `name` | display name in the UI (defaults to the filename) |

**Prompt-body variables:** `${input:name}` / `${input:name:placeholder}`, `${selection}`, `${selectedText}`, `${file}`, `${fileBasename}`, `${workspaceFolder}`, `${workspaceFolderBasename}`; `#tool:<name>` tool references; Markdown relative-path links for file references.

### Composition
- **`*.instructions.md` lead with an `applyTo` glob** (e.g. `applyTo: "**/*.ts"`) plus a `description`. Every file matching the glob silently stacks its instructions into context when Copilot edits a match - path-scoped, automatic.
- **`*.prompt.md` are invoked by name** (slash-command style) and read like a saved task.

### Anti-patterns
- A broad `applyTo: "**"` instruction file that attaches everywhere - that re-creates the always-on token cost the granular format was meant to avoid.
- Copying the monolithic `.github/copilot-instructions.md` into many files without actually scoping them. Scoping is the whole point.

### Edge cases
- **Default locations are settled:** `.github/prompts/` and `.github/instructions/` (searched recursively), configurable via the `chat.promptFilesLocations` / `chat.instructionsFilesLocations` settings. VS Code can also read Claude-format `.claude/rules/`.
- `mode` was renamed to `agent` (values `ask`/`agent`/`plan`); older files still use `mode: agent`/`edit`.
- Largely VS Code / Copilot territory: other tools read the single `.github/copilot-instructions.md` but don't all honor the modular `.prompt.md` / `.instructions.md` split.
