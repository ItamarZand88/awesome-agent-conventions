# Memory Bank 🟢 Adopted

> Cline's structured memory system - a set of Markdown files an agent reads at the start of every task to reconstruct full project context after its session memory resets.

- **Read by:** Cline, Roo Code, and Cursor (via the Memory Bank custom-instructions pattern)
- **Location:** A memory-bank/ directory at the repository root
- **Spec:** [https://docs.cline.bot/best-practices/memory-bank](https://docs.cline.bot/best-practices/memory-bank)
- **Evidence:** Cline documents Memory Bank as a structured multi-file context system, and public repositories commit the full file set.
- **Last verified:** 2026-06-18
- **Files:** `projectbrief.md`, `productContext.md`, `activeContext.md`, `systemPatterns.md`, `techContext.md`, `progress.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `projectbrief.md`

Foundation doc - why the project exists, core requirements and goals.

| Source | File | Provenance |
| --- | --- | --- |
| `gitpod` | [`gitpod.projectbrief.md`](examples/gitpod.projectbrief.md) | [source](https://raw.githubusercontent.com/gitpod-io/gitpod/main/memory-bank/projectbrief.md) |

### `productContext.md`

Problem space and the intended user experience.

| Source | File | Provenance |
| --- | --- | --- |
| `gitpod` | [`gitpod.productContext.md`](examples/gitpod.productContext.md) | [source](https://raw.githubusercontent.com/gitpod-io/gitpod/main/memory-bank/productContext.md) |

### `activeContext.md`

Current focus, recent changes, next steps - the most frequently updated file.

| Source | File | Provenance |
| --- | --- | --- |
| `gitpod` | [`gitpod.activeContext.md`](examples/gitpod.activeContext.md) | [source](https://raw.githubusercontent.com/gitpod-io/gitpod/main/memory-bank/activeContext.md) |

### `systemPatterns.md`

Architecture, key technical decisions, and design patterns.

| Source | File | Provenance |
| --- | --- | --- |
| `gitpod` | [`gitpod.systemPatterns.md`](examples/gitpod.systemPatterns.md) | [source](https://raw.githubusercontent.com/gitpod-io/gitpod/main/memory-bank/systemPatterns.md) |

### `techContext.md`

Technologies, setup, constraints, and dependencies.

| Source | File | Provenance |
| --- | --- | --- |
| `gitpod` | [`gitpod.techContext.md`](examples/gitpod.techContext.md) | [source](https://raw.githubusercontent.com/gitpod-io/gitpod/main/memory-bank/techContext.md) |

### `progress.md`

What works, what's left to build, and known issues.

| Source | File | Provenance |
| --- | --- | --- |
| `gitpod` | [`gitpod.progress.md`](examples/gitpod.progress.md) | [source](https://raw.githubusercontent.com/gitpod-io/gitpod/main/memory-bank/progress.md) |

## Field notes

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
