### Files & flow
Six core files, plus optional extras, in a strict dependency graph:

```
projectbrief  ->  productContext, systemPatterns, techContext  ->  activeContext  ->  progress
```

- **`projectbrief.md`** - foundation / source of truth; core requirements + goals. Should rarely change.
- **`productContext.md`** - why it exists, problems solved, UX goals.
- **`systemPatterns.md`** - architecture, key decisions, component relationships.
- **`techContext.md`** - stack, setup, constraints, dependencies.
- **`activeContext.md`** - current focus, recent changes, next steps; the **most-updated** file.
- **`progress.md`** - what works, what's left, known issues, status.
- **Optional extras** inside `memory-bank/` are explicitly allowed: extra files/folders for complex features, integrations, API docs, testing strategy, deployment.

**Workflow:** the phrases `initialize memory bank`, `update memory bank` (triggers a full review of *all* files), and `follow your custom instructions` (resume); plus **Plan Mode** (reads the bank, proposes a strategy, can't edit) vs **Act Mode** (executes and documents).

### Composition
- The files run stable -> volatile: `projectbrief` is the root; the three middle files build on it; `activeContext` carries Current Work Focus -> Recent Changes -> Next Steps; `progress` tracks what works and what's left.

### Anti-patterns
- Letting `activeContext.md` decay into a human changelog - current *state* is more useful to an agent than release-note prose.
- Files that contradict each other after an update (the brief says X, techContext says Y).
- Not running `update memory bank` at the end of a task - the next session then reconstructs stale context.

### Edge cases
- The whole premise is **memory reset**: each file must stand on its own because the agent re-reads the bank cold every task.
- `projectbrief.md` should rarely change; `activeContext.md` / `progress.md` are the churn files. Mixing those cadences in one file defeats the structure.

### Adoption / maturity
- Memory Bank is a Cline-documented pattern, not a generic Markdown folder convention. Roo Code and Cursor users commonly reuse it through custom instructions, but the canonical shape and commands come from Cline.
- Because the files are version-controlled, the bank is more auditable than local auto-memory, but also easier to pollute with transient notes unless `update memory bank` is treated like a review step.

### Related conventions
- Use `MEMORY.md` for local agent recall that should not be committed.
- Use AGENTS.md or tool-specific instruction files for rules that must always steer implementation, rather than for historical state.

### Sources checked
- [Cline Memory Bank docs](https://docs.cline.bot/best-practices/memory-bank)
- [Gitpod Memory Bank examples](https://github.com/gitpod-io/gitpod/tree/main/memory-bank)
