# AI ignore files 🟢 Adopted

> gitignore-syntax files that fence an AI agent out of paths - secrets, vendored code, generated output - so they're never sent to the model as context.

- **Read by:** JetBrains Junie (.aiignore), Cursor (.cursorignore), Codeium/Windsurf (.codeiumignore)
- **Location:** Repository root (gitignore-style glob syntax)
- **Spec:** [https://cursor.com/docs/reference/ignore-file](https://cursor.com/docs/reference/ignore-file)
- **Evidence:** Cursor, JetBrains Junie, and Codeium/Windsurf-style tools use gitignore-like files to exclude paths from AI context.
- **Last verified:** 2026-06-18
- **Files:** `.aiignore`, `.cursorignore`, `.codeiumignore`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `.aiignore`

JetBrains Junie / AI Assistant.

| Source | File | Provenance |
| --- | --- | --- |
| `ag-grid` | [`ag-grid.aiignore`](examples/ag-grid.aiignore) | [source](https://raw.githubusercontent.com/ag-grid/ag-grid/latest/.rulesync/.aiignore) |

### `.cursorignore`

Cursor.

| Source | File | Provenance |
| --- | --- | --- |
| `api-console` | [`api-console.cursorignore`](examples/api-console.cursorignore) | [source](https://raw.githubusercontent.com/mulesoft/api-console/master/.cursorignore) |
| `holochain` | [`holochain.cursorignore`](examples/holochain.cursorignore) | [source](https://raw.githubusercontent.com/holochain/holochain/develop/.cursorignore) |

### `.codeiumignore`

Codeium (now Windsurf).

| Source | File | Provenance |
| --- | --- | --- |
| `wikimedia` | [`wikimedia.codeiumignore`](examples/wikimedia.codeiumignore) | [source](https://raw.githubusercontent.com/wikimedia/wikimedia-fundraising-dev/master/.codeiumignore) |

## Field notes

### Composition
- **gitignore syntax, verbatim.** Short, pattern-based files focused on build output, secrets, and VCS dirs - holochain's `.cursorignore` is three lines (`target/`, `**/target/**`, `.git/`); ag-grid's `.aiignore` fences off `credentials/` and `.env.local`.

### Anti-patterns
- **Treating it as a security boundary.** It reduces what's sent as context; it is *not* a hard secret control. Don't rely on `.cursorignore` to keep credentials out of the model - keep secrets out of the tree.
- Over-broad globs that also hide the context the agent legitimately needs.
- Forgetting generated/vendored output, so the agent wastes its window indexing `dist/`.

### Edge cases
- Tools split the job: Cursor's `.cursorignore` blocks both **access and indexing**, while `.cursorindexingignore` excludes from indexing *only* (the file stays readable) - the names are easy to get backwards. An Agent's terminal and MCP-server tools can't enforce `.cursorignore` at all, a second reason it isn't a hard boundary.
- Negation (`!pattern`) and precedence interact with `.gitignore`; an agent may union both.
