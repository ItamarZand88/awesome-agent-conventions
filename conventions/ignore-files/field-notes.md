### Composition
- **gitignore syntax, verbatim.** The bbgo `.aiignore` says so outright and links the gitignore docs; holochain's `.cursorignore` is three lines (`target/`, `**/target/**`, `.git/`). Short, pattern-based, build-output- and VCS-focused.

### Anti-patterns
- **Treating it as a security boundary.** It reduces what's sent as context; it is *not* a hard secret control. Don't rely on `.cursorignore` to keep credentials out of the model - keep secrets out of the tree.
- Over-broad globs that also hide the context the agent legitimately needs.
- Forgetting generated/vendored output, so the agent wastes its window indexing `dist/`.

### Edge cases
- Tools split the job: Cursor's `.cursorignore` blocks both **access and indexing**, while `.cursorindexingignore` excludes from indexing *only* (the file stays readable) - the names are easy to get backwards. An Agent's terminal and MCP-server tools can't enforce `.cursorignore` at all, a second reason it isn't a hard boundary.
- Negation (`!pattern`) and precedence interact with `.gitignore`; an agent may union both.
