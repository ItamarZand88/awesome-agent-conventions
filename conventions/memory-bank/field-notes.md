### Composition
The six files form a deliberate dependency order, from stable to volatile:
- **`projectbrief.md`** is the root - Gitpod's is a feature table plus a short goals list.
- **`productContext.md` / `systemPatterns.md` / `techContext.md`** build on it (problem space, architecture, stack).
- **`activeContext.md`** carries *Current Work Focus → Recent Changes → Next Steps* and is the **most frequently updated** file.
- **`progress.md`** tracks what works and what's left.

### Anti-patterns
- Letting `activeContext.md` decay into a human changelog - Gitpod's "Recent Changes" already drifts toward release-note prose, which is less useful to an agent than current *state*.
- Files that contradict each other after an update (the brief says X, techContext says Y).
- Not updating the bank at the end of a task - the next session then reconstructs stale context.

### Edge cases
- The whole premise is **memory reset**: each file must stand on its own because the agent re-reads the bank cold every task.
- `projectbrief.md` should rarely change; `activeContext.md`/`progress.md` are the churn files. Mixing those cadences in one file defeats the structure.
