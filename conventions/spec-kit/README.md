# Spec Kit 🟢 Adopted

> GitHub's spec-driven workflow - a constitution plus per-feature spec → plan → tasks files that drive an agent through structured, reviewable implementation.

- **Read by:** GitHub Spec Kit's slash-command agents (Copilot, Claude, Gemini, Cursor, and more)
- **Location:** .specify/memory/constitution.md and specs/<feature>/{spec,plan,tasks}.md
- **Spec:** [https://github.com/github/spec-kit](https://github.com/github/spec-kit)
- **Files:** `constitution.md`, `spec.md`, `plan.md`, `tasks.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `constitution.md`

Project principles and non-negotiable rules the agent honors across every feature.

| Source | File | Provenance |
| --- | --- | --- |
| `spec-kit` | [`spec-kit.constitution.md`](examples/spec-kit.constitution.md) | [source](https://raw.githubusercontent.com/github/spec-kit/main/templates/constitution-template.md) |

### `spec.md`

The what and why of one feature - requirements and user stories, no implementation detail.

| Source | File | Provenance |
| --- | --- | --- |
| `spec-kit` | [`spec-kit.spec.md`](examples/spec-kit.spec.md) | [source](https://raw.githubusercontent.com/github/spec-kit/main/templates/spec-template.md) |

### `plan.md`

The technical approach, stack, and architecture for the spec.

| Source | File | Provenance |
| --- | --- | --- |
| `spec-kit` | [`spec-kit.plan.md`](examples/spec-kit.plan.md) | [source](https://raw.githubusercontent.com/github/spec-kit/main/templates/plan-template.md) |

### `tasks.md`

An ordered, reviewable task list generated from the plan.

| Source | File | Provenance |
| --- | --- | --- |
| `spec-kit` | [`spec-kit.tasks.md`](examples/spec-kit.tasks.md) | [source](https://raw.githubusercontent.com/github/spec-kit/main/templates/tasks-template.md) |

## Field notes

### Composition
A four-stage funnel, narrowing from principles to actions:
- **`constitution.md`** - durable principles. The template ships as `[PLACEHOLDER]` tokens with `<!-- example -->` comments (e.g. *"III. Test-First (NON-NEGOTIABLE)"*), so the agent fills structure rather than inventing it.
- **`spec.md`** - the *what and why* of one feature: requirements and user stories, explicitly **no implementation detail**.
- **`plan.md`** - the *how*: stack, architecture, approach.
- **`tasks.md`** - an ordered, reviewable task list derived from the plan.

### Anti-patterns
- Leaking implementation choices into `spec.md` - the template fights this on purpose.
- Skipping the constitution, so the agent has no non-negotiables to honor.
- Treating `tasks.md` as throwaway instead of the reviewable contract it's meant to be.

### Edge cases
- Layout splits by role: `constitution.md` lives in `.specify/memory/`; `spec/plan/tasks` are per-feature under `specs/<feature>/`.
- The templates are tool-agnostic - the same files drive Copilot, Claude, Gemini, and Cursor (30+ agents) via namespaced slash commands (`/speckit.constitution`, `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.implement`).
