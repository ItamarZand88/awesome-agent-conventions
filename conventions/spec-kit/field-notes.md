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
