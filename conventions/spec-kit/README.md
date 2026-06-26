# Spec Kit 🟢 Adopted

> GitHub's spec-driven workflow - a constitution plus per-feature spec → plan → tasks files that drive an agent through structured, reviewable implementation.

- **Read by:** GitHub Spec Kit's slash-command agents (Copilot, Claude, Gemini, Cursor, and more)
- **Location:** .specify/memory/constitution.md and specs/<feature>/{spec,plan,tasks}.md
- **Spec:** [https://github.com/github/spec-kit](https://github.com/github/spec-kit)
- **Evidence:** GitHub Spec Kit publishes templates and slash-command workflows that consume constitution, spec, plan, and tasks files.
- **Last verified:** 2026-06-26
- **Files:** `constitution.md`, `spec.md`, `plan.md`, `tasks.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `constitution.md`

Project principles and non-negotiable rules the agent honors across every feature.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `argus-constitution` | [`aarthi-ntrjn/argus`](https://github.com/aarthi-ntrjn/argus) | [`examples/argus-constitution/constitution.md`](examples/argus-constitution/constitution.md) | [source](https://raw.githubusercontent.com/aarthi-ntrjn/argus/master/.specify/memory/constitution.md) |
| `editor-constitution` | [`tui-cs/Editor`](https://github.com/tui-cs/Editor) | [`examples/editor-constitution/constitution.md`](examples/editor-constitution/constitution.md) | [source](https://raw.githubusercontent.com/tui-cs/Editor/develop/specs/constitution.md) |
| `openarg-constitution` | [`colossus-lab/openarg_backend`](https://github.com/colossus-lab/openarg_backend) | [`examples/openarg-constitution/constitution.md`](examples/openarg-constitution/constitution.md) | [source](https://raw.githubusercontent.com/colossus-lab/openarg_backend/main/specs/constitution.md) |
| `rclick-macos-app` | [`wflixu/RClick`](https://github.com/wflixu/RClick) | [`examples/rclick-macos-app/constitution.md`](examples/rclick-macos-app/constitution.md) | [source](https://raw.githubusercontent.com/wflixu/RClick/main/.specify/memory/constitution.md) |
| `spec-kit` | [`github/spec-kit`](https://github.com/github/spec-kit) | [`examples/spec-kit/constitution.md`](examples/spec-kit/constitution.md) | [source](https://raw.githubusercontent.com/github/spec-kit/main/templates/constitution-template.md) |

### `spec.md`

The what and why of one feature - requirements and user stories, no implementation detail.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `argus-security-review` | [`aarthi-ntrjn/argus`](https://github.com/aarthi-ntrjn/argus) | [`examples/argus-security-review/spec.md`](examples/argus-security-review/spec.md) | [source](https://raw.githubusercontent.com/aarthi-ntrjn/argus/master/specs/009-security-review/spec.md) |
| `argus-session-dashboard` | [`aarthi-ntrjn/argus`](https://github.com/aarthi-ntrjn/argus) | [`examples/argus-session-dashboard/spec.md`](examples/argus-session-dashboard/spec.md) | [source](https://raw.githubusercontent.com/aarthi-ntrjn/argus/master/specs/001-session-dashboard/spec.md) |
| `editor-clipboard` | [`tui-cs/Editor`](https://github.com/tui-cs/Editor) | [`examples/editor-clipboard/spec.md`](examples/editor-clipboard/spec.md) | [source](https://raw.githubusercontent.com/tui-cs/Editor/develop/specs/clipboard/spec.md) |
| `editor-multi-caret` | [`tui-cs/Editor`](https://github.com/tui-cs/Editor) | [`examples/editor-multi-caret/spec.md`](examples/editor-multi-caret/spec.md) | [source](https://raw.githubusercontent.com/tui-cs/Editor/develop/specs/multi-caret/spec.md) |
| `openarg-auth` | [`colossus-lab/openarg_backend`](https://github.com/colossus-lab/openarg_backend) | [`examples/openarg-auth/spec.md`](examples/openarg-auth/spec.md) | [source](https://raw.githubusercontent.com/colossus-lab/openarg_backend/main/specs/003-auth/spec.md) |
| `openarg-semantic-cache` | [`colossus-lab/openarg_backend`](https://github.com/colossus-lab/openarg_backend) | [`examples/openarg-semantic-cache/spec.md`](examples/openarg-semantic-cache/spec.md) | [source](https://raw.githubusercontent.com/colossus-lab/openarg_backend/main/specs/004-semantic-cache/spec.md) |
| `rclick-macos-app` | [`wflixu/RClick`](https://github.com/wflixu/RClick) | [`examples/rclick-macos-app/spec.md`](examples/rclick-macos-app/spec.md) | [source](https://raw.githubusercontent.com/wflixu/RClick/main/specs/001-macos-app-macos/spec.md) |
| `spec-kit` | [`github/spec-kit`](https://github.com/github/spec-kit) | [`examples/spec-kit/spec.md`](examples/spec-kit/spec.md) | [source](https://raw.githubusercontent.com/github/spec-kit/main/templates/spec-template.md) |

### `plan.md`

The technical approach, stack, and architecture for the spec.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `argus-security-review` | [`aarthi-ntrjn/argus`](https://github.com/aarthi-ntrjn/argus) | [`examples/argus-security-review/plan.md`](examples/argus-security-review/plan.md) | [source](https://raw.githubusercontent.com/aarthi-ntrjn/argus/master/specs/009-security-review/plan.md) |
| `argus-session-dashboard` | [`aarthi-ntrjn/argus`](https://github.com/aarthi-ntrjn/argus) | [`examples/argus-session-dashboard/plan.md`](examples/argus-session-dashboard/plan.md) | [source](https://raw.githubusercontent.com/aarthi-ntrjn/argus/master/specs/001-session-dashboard/plan.md) |
| `openarg-auth` | [`colossus-lab/openarg_backend`](https://github.com/colossus-lab/openarg_backend) | [`examples/openarg-auth/plan.md`](examples/openarg-auth/plan.md) | [source](https://raw.githubusercontent.com/colossus-lab/openarg_backend/main/specs/003-auth/plan.md) |
| `openarg-semantic-cache` | [`colossus-lab/openarg_backend`](https://github.com/colossus-lab/openarg_backend) | [`examples/openarg-semantic-cache/plan.md`](examples/openarg-semantic-cache/plan.md) | [source](https://raw.githubusercontent.com/colossus-lab/openarg_backend/main/specs/004-semantic-cache/plan.md) |
| `rclick-macos-app` | [`wflixu/RClick`](https://github.com/wflixu/RClick) | [`examples/rclick-macos-app/plan.md`](examples/rclick-macos-app/plan.md) | [source](https://raw.githubusercontent.com/wflixu/RClick/main/specs/001-macos-app-macos/plan.md) |
| `spec-kit` | [`github/spec-kit`](https://github.com/github/spec-kit) | [`examples/spec-kit/plan.md`](examples/spec-kit/plan.md) | [source](https://raw.githubusercontent.com/github/spec-kit/main/templates/plan-template.md) |

### `tasks.md`

An ordered, reviewable task list generated from the plan.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `argus-security-review` | [`aarthi-ntrjn/argus`](https://github.com/aarthi-ntrjn/argus) | [`examples/argus-security-review/tasks.md`](examples/argus-security-review/tasks.md) | [source](https://raw.githubusercontent.com/aarthi-ntrjn/argus/master/specs/009-security-review/tasks.md) |
| `argus-session-dashboard` | [`aarthi-ntrjn/argus`](https://github.com/aarthi-ntrjn/argus) | [`examples/argus-session-dashboard/tasks.md`](examples/argus-session-dashboard/tasks.md) | [source](https://raw.githubusercontent.com/aarthi-ntrjn/argus/master/specs/001-session-dashboard/tasks.md) |
| `rclick-macos-app` | [`wflixu/RClick`](https://github.com/wflixu/RClick) | [`examples/rclick-macos-app/tasks.md`](examples/rclick-macos-app/tasks.md) | [source](https://raw.githubusercontent.com/wflixu/RClick/main/specs/001-macos-app-macos/tasks.md) |
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
