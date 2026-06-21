### Composition
- **gitignore syntax, verbatim.** Short, pattern-based files focused on build output, secrets, and VCS dirs - holochain's `.cursorignore` is three lines (`target/`, `**/target/**`, `.git/`); ag-grid's `.aiignore` fences off `credentials/` and `.env.local`.
- **Different files control different surfaces.** Cursor splits `.cursorignore` (best-effort block for access and indexing) from `.cursorindexingignore` (indexing only). Devin Desktop / Windsurf uses `.codeiumignore` at the workspace root, plus a global `~/.codeium/.codeiumignore`. JetBrains Junie respects `.aiignore`.

### Anti-patterns
- **Treating it as a security boundary.** It reduces what's sent as context; it is *not* a hard secret control. Don't rely on `.cursorignore` to keep credentials out of the model - keep secrets out of the tree.
- Over-broad globs that also hide the context the agent legitimately needs.
- Forgetting generated/vendored output, so the agent wastes its window indexing `dist/`.

### Edge cases
- Tools split the job: Cursor's `.cursorignore` blocks both **access and indexing**, while `.cursorindexingignore` excludes from indexing *only* (the file stays readable) - the names are easy to get backwards. An Agent's terminal and MCP-server tools can't enforce `.cursorignore` at all, a second reason it isn't a hard boundary.
- Negation (`!pattern`) and precedence interact with `.gitignore`; an agent may union both.

### Adoption / maturity
- Ignore files are adopted because they solve a practical context-window and privacy problem, but they are tool-enforced hints, not repository security controls.
- Treat them like `.gitignore`: useful, reviewed, and version-controlled, but not sufficient for secrets. Secrets should not be committed, and sensitive generated files should be blocked by the tool's own permissions or environment policy too.

### Sources checked
- [Cursor ignore file docs](https://cursor.com/docs/reference/ignore-file)
- [JetBrains Junie .aiignore docs](https://www.jetbrains.com/help/ai-assistant/junie-agent.html)
- [Devin Desktop / Windsurf .codeiumignore docs](https://docs.devin.ai/desktop/context-awareness/windsurf-ignore)
