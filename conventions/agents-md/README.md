# AGENTS.md 🟢 Adopted

> A plain-Markdown "README for agents" - build/test commands, conventions, and gotchas an agent needs before touching the code. The most widely adopted cross-tool instruction file.

- **Read by:** Most coding agents - OpenAI Codex, Cursor, Jules, Aider, Gemini CLI, Zed, and others
- **Location:** Repository root; the nearest AGENTS.md up the tree wins, and nested files override parents
- **Spec:** [https://agents.md](https://agents.md)
- **Files:** `AGENTS.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `AGENTS.md`

| Source | File | Provenance |
| --- | --- | --- |
| `airflow` | [`airflow.AGENTS.md`](examples/airflow.AGENTS.md) | [source](https://raw.githubusercontent.com/apache/airflow/main/AGENTS.md) |
| `codex` | [`codex.AGENTS.md`](examples/codex.AGENTS.md) | [source](https://raw.githubusercontent.com/openai/codex/main/AGENTS.md) |

## Field notes

### Composition
Strong AGENTS.md files are **imperative and executable**, not descriptive:
- **Exact commands first** - how to build, test, and run a *single* test. An agent can't guess `just argument-comment-lint`; spell it out.
- **Code-style rules as a checklist** - the Codex example is almost entirely rules (honor specific clippy lints, exhaustive `match`, the `/*param_name*/` argument-comment lint), each with a link to the rule it enforces.
- **A sandbox/environment contract** - Codex documents `CODEX_SANDBOX_NETWORK_DISABLED=1` and *why* certain tests early-exit, so the agent doesn't "fix" tests that were written around its sandbox.

### Anti-patterns
- Restating the human `README.md` instead of telling the agent what to *do*.
- Vague guidance ("write clean code") that doesn't change a single decision.
- Omitting the precise command or naming a tool without saying how to install it.

### Edge cases
- **Precedence:** the nearest AGENTS.md up the tree wins; nested files override parents. The Codex file scopes itself to the `codex-rs/` subtree.
- **Monorepos:** prefer a per-package AGENTS.md over one giant root file.
- **Convergence:** many tools now read AGENTS.md as the canonical file, with `CLAUDE.md`/`GEMINI.md` symlinking or pointing to it.
