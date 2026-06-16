### Composition
A four-stage funnel, narrowing from principles to actions:
- **`constitution.md`** — durable principles. The template ships as `[PLACEHOLDER]` tokens with `<!-- example -->` comments (e.g. *"III. Test-First (NON-NEGOTIABLE)"*), so the agent fills structure rather than inventing it.
- **`spec.md`** — the *what and why* of one feature: requirements and user stories, explicitly **no implementation detail**.
- **`plan.md`** — the *how*: stack, architecture, approach.
- **`tasks.md`** — an ordered, reviewable task list derived from the plan.

### Anti-patterns
- Leaking implementation choices into `spec.md` — the template fights this on purpose.
- Skipping the constitution, so the agent has no non-negotiables to honor.
- Treating `tasks.md` as throwaway instead of the reviewable contract it's meant to be.

### Edge cases
- Layout splits by role: `constitution.md` lives in `.specify/memory/`; `spec/plan/tasks` are per-feature under `specs/<feature>/`.
- The templates are tool-agnostic — the same files drive Copilot, Claude, Gemini, and Cursor via their slash commands.
