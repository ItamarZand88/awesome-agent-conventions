# Memory Bank 🟢 Adopted

> Cline's structured memory system — a set of Markdown files an agent reads at the start of every task to reconstruct full project context after its session memory resets.

- **Read by:** Cline, Roo Code, and Cursor (via the Memory Bank custom-instructions pattern)
- **Location:** A memory-bank/ directory at the repository root
- **Spec:** [https://docs.cline.bot/best-practices/memory-bank](https://docs.cline.bot/best-practices/memory-bank)
- **Files:** `projectbrief.md`, `productContext.md`, `activeContext.md`, `systemPatterns.md`, `techContext.md`, `progress.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) — none are hand-written._

### `projectbrief.md`

Foundation doc — why the project exists, core requirements and goals.

| Source | File | Provenance |
| --- | --- | --- |
| `gitpod` | [`gitpod.projectbrief.md`](examples/gitpod.projectbrief.md) | [source](https://raw.githubusercontent.com/gitpod-io/gitpod/main/memory-bank/projectbrief.md) |

### `productContext.md`

Problem space and the intended user experience.

| Source | File | Provenance |
| --- | --- | --- |
| `gitpod` | [`gitpod.productContext.md`](examples/gitpod.productContext.md) | [source](https://raw.githubusercontent.com/gitpod-io/gitpod/main/memory-bank/productContext.md) |

### `activeContext.md`

Current focus, recent changes, next steps — the most frequently updated file.

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

### Composition
The six files form a deliberate dependency order, from stable to volatile:
- **`projectbrief.md`** is the root — Gitpod's is a feature table plus a short goals list.
- **`productContext.md` / `systemPatterns.md` / `techContext.md`** build on it (problem space, architecture, stack).
- **`activeContext.md`** carries *Current Work Focus → Recent Changes → Next Steps* and is the **most frequently updated** file.
- **`progress.md`** tracks what works and what's left.

### Anti-patterns
- Letting `activeContext.md` decay into a human changelog — Gitpod's "Recent Changes" already drifts toward release-note prose, which is less useful to an agent than current *state*.
- Files that contradict each other after an update (the brief says X, techContext says Y).
- Not updating the bank at the end of a task — the next session then reconstructs stale context.

### Edge cases
- The whole premise is **memory reset**: each file must stand on its own because the agent re-reads the bank cold every task.
- `projectbrief.md` should rarely change; `activeContext.md`/`progress.md` are the churn files. Mixing those cadences in one file defeats the structure.
