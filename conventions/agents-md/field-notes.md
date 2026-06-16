### Composition
Strong AGENTS.md files are **imperative and executable**, not descriptive:
- **Exact commands first** — how to build, test, and run a *single* test. An agent can't guess `just argument-comment-lint`; spell it out.
- **Code-style rules as a checklist** — the Codex example is almost entirely rules (honor specific clippy lints, exhaustive `match`, the `/*param_name*/` argument-comment lint), each with a link to the rule it enforces.
- **A sandbox/environment contract** — Codex documents `CODEX_SANDBOX_NETWORK_DISABLED=1` and *why* certain tests early-exit, so the agent doesn't "fix" tests that were written around its sandbox.

### Anti-patterns
- Restating the human `README.md` instead of telling the agent what to *do*.
- Vague guidance ("write clean code") that doesn't change a single decision.
- Omitting the precise command or naming a tool without saying how to install it.

### Edge cases
- **Precedence:** the nearest AGENTS.md up the tree wins; nested files override parents. The Codex file scopes itself to the `codex-rs/` subtree.
- **Monorepos:** prefer a per-package AGENTS.md over one giant root file.
- **Convergence:** many tools now read AGENTS.md as the canonical file, with `CLAUDE.md`/`GEMINI.md` symlinking or pointing to it.
