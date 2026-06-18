# Spec Kit 🟢 Adopted

> GitHub's spec-driven workflow - a constitution plus per-feature spec → plan → tasks files that drive an agent through structured, reviewable implementation.

- **Read by:** GitHub Spec Kit's slash-command agents (Copilot, Claude, Gemini, Cursor, and more)
- **Location:** .specify/memory/constitution.md and specs/<feature>/{spec,plan,tasks}.md
- **Spec:** [https://github.com/github/spec-kit](https://github.com/github/spec-kit)
- **Evidence:** GitHub Spec Kit publishes templates and slash-command workflows that consume constitution, spec, plan, and tasks files.
- **Last verified:** 2026-06-18
- **Files:** `constitution.md`, `spec.md`, `plan.md`, `tasks.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `constitution.md`

Project principles and non-negotiable rules the agent honors across every feature.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `spec-kit` | [`github/spec-kit`](https://github.com/github/spec-kit) | [`examples/spec-kit/constitution.md`](examples/spec-kit/constitution.md) | [source](https://raw.githubusercontent.com/github/spec-kit/main/templates/constitution-template.md) |

### `spec.md`

The what and why of one feature - requirements and user stories, no implementation detail.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `spec-kit` | [`github/spec-kit`](https://github.com/github/spec-kit) | [`examples/spec-kit/spec.md`](examples/spec-kit/spec.md) | [source](https://raw.githubusercontent.com/github/spec-kit/main/templates/spec-template.md) |

### `plan.md`

The technical approach, stack, and architecture for the spec.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `spec-kit` | [`github/spec-kit`](https://github.com/github/spec-kit) | [`examples/spec-kit/plan.md`](examples/spec-kit/plan.md) | [source](https://raw.githubusercontent.com/github/spec-kit/main/templates/plan-template.md) |

### `tasks.md`

An ordered, reviewable task list generated from the plan.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `spec-kit` | [`github/spec-kit`](https://github.com/github/spec-kit) | [`examples/spec-kit/tasks.md`](examples/spec-kit/tasks.md) | [source](https://raw.githubusercontent.com/github/spec-kit/main/templates/tasks-template.md) |

## Field notes

### Artifacts & commands
**Files:** `constitution.md` (in `.specify/memory/`); per feature under `specs/NNN-feature/`: `spec.md`, `plan.md`, `tasks.md`, plus plan-phase byproducts `research.md`, `data-model.md`, `quickstart.md`, and `contracts/`. Planning also generates an agent file (e.g. `CLAUDE.md`). Templates live under `.specify/templates/` (+ `overrides/`, `presets/`, `extensions/`).

**Namespaced slash commands** (run in order as needed):

| Command | Does |
| --- | --- |
| `/speckit.constitution` | create/update governing principles |
| `/speckit.specify` | requirements & user stories (what/why) |
| `/speckit.clarify` | ask ~5 targeted questions; adds a `## Clarifications` section |
| `/speckit.plan` | technical plan + byproduct artifacts |
| `/speckit.tasks` | dependency-ordered task list |
| `/speckit.analyze` | cross-artifact consistency/coverage check |
| `/speckit.checklist` | quality-validation checklists |
| `/speckit.implement` | execute tasks, build the feature |
| `/speckit.taskstoissues` | convert tasks into GitHub issues |

### Composition
A funnel narrowing from principles to actions:
- **`constitution.md`** - durable principles; the template ships as `[PLACEHOLDER]` tokens with `<!-- example -->` comments so the agent fills structure rather than inventing it.
- **`spec.md`** - the *what and why* of one feature, explicitly **no implementation detail**.
- **`plan.md`** - the *how*: stack, architecture, approach.
- **`tasks.md`** - an ordered, reviewable task list derived from the plan.

### Anti-patterns
- Leaking implementation choices into `spec.md` - the template fights this on purpose.
- Skipping the constitution, so the agent has no non-negotiables to honor.
- Treating `tasks.md` as throwaway instead of the reviewable contract it's meant to be.

### Edge cases
- Layout splits by role: `constitution.md` in `.specify/memory/`; `spec/plan/tasks` per-feature under `specs/<feature>/`.
- Tool-agnostic: the same files drive Copilot, Claude, Gemini, Cursor (30+ agents). In skills mode the commands map to `speckit-<name>`.

### Adoption / maturity
- Spec Kit is adopted as a GitHub-published workflow and template set, not merely a naming idea. The repository provides both the files and the slash-command flow that consumes them.
- The important boundary is role separation: `spec.md` is requirements, `plan.md` is implementation approach, and `tasks.md` is execution order. Mixing those roles makes consistency checks less useful.

### Related conventions
- Use Kiro steering or AGENTS.md for persistent project context that applies across many specs.
- Use Claude/GitHub/Cursor command files for the command surface; the durable artifacts are the Spec Kit Markdown files themselves.

### Sources checked
- [GitHub Spec Kit repository](https://github.com/github/spec-kit)
- [Spec Kit templates](https://github.com/github/spec-kit/tree/main/templates)
