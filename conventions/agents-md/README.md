# AGENTS.md 🟢 Adopted

> A plain-Markdown "README for agents" - build/test commands, conventions, and gotchas an agent needs before touching the code. The most widely adopted cross-tool instruction file.

- **Read by:** Most coding agents - OpenAI Codex, Cursor, Jules, Aider, Gemini CLI, Zed, and others
- **Location:** Repository root; the nearest AGENTS.md up the tree wins, and nested files override parents
- **Spec:** [https://agents.md](https://agents.md)
- **Evidence:** Cross-tool convention documented at agents.md and read by multiple coding agents, with public examples from OpenAI Codex and Apache Airflow.
- **Last verified:** 2026-06-18
- **Files:** `AGENTS.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `AGENTS.md`

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `airflow` | [`apache/airflow`](https://github.com/apache/airflow) | [`examples/airflow/AGENTS.md`](examples/airflow/AGENTS.md) | [source](https://raw.githubusercontent.com/apache/airflow/main/AGENTS.md) |
| `codex` | [`openai/codex`](https://github.com/openai/codex) | [`examples/codex/AGENTS.md`](examples/codex/AGENTS.md) | [source](https://raw.githubusercontent.com/openai/codex/main/AGENTS.md) |

## Field notes

### Structure
**No frontmatter, no schema** - the spec is explicit: *"AGENTS.md is just standard Markdown. Use any headings you like."* The conventional (not required) sections it suggests: Project overview, Build & test commands, Code style, Testing instructions, Security considerations; the sample file also shows "Dev environment tips" and "PR instructions." Adoption is broad - 60k+ projects and 24+ compatible tools.

### Composition
Strong AGENTS.md files are **imperative and executable**, not descriptive:
- **Exact commands first** - how to build, test, and run a *single* test. An agent can't guess `just argument-comment-lint`; spell it out.
- **Code-style rules as a checklist** - the Codex example is almost entirely rules (honor specific clippy lints, exhaustive `match`, the `/*param_name*/` argument-comment lint), each linking the rule it enforces.
- **A sandbox/environment contract** - Codex documents `CODEX_SANDBOX_NETWORK_DISABLED=1` and *why* certain tests early-exit, so the agent doesn't "fix" tests written around its sandbox.

### Anti-patterns
- Restating the human `README.md` instead of telling the agent what to *do*.
- Vague guidance ("write clean code") that doesn't change a single decision.
- Omitting the precise command or naming a tool without saying how to install it.

### Edge cases
- **Precedence:** the nearest AGENTS.md up the tree wins and nested files override parents - but an **explicit user chat prompt overrides everything**. The Codex file scopes itself to the `codex-rs/` subtree.
- **Monorepos:** prefer a per-package AGENTS.md over one giant root file (OpenAI's monorepo ships 88 of them).
- **Convergence:** many tools now read AGENTS.md as the canonical file, with `CLAUDE.md`/`GEMINI.md` symlinking or `@`-importing it.

### Adoption / maturity
- The public spec positions AGENTS.md as a cross-tool, plain-Markdown convention rather than a vendor-specific config file. It reports broad open-source adoption and lists compatible tools across OpenAI Codex, Google Jules, Aider, Zed, Warp, Cursor, Amp, GitHub Copilot, Devin/Cascade, and others.
- The format is intentionally low ceremony: no required fields beyond the filename, no frontmatter, and no parser contract beyond Markdown. That is why it has become the migration target for older `CLAUDE.md`, `GEMINI.md`, `.cursorrules`, `.windsurfrules`, and singular `AGENT.md` files.

### Related conventions
- Use `CLAUDE.md`, `GEMINI.md`, `QWEN.md`, `WARP.md`, or `.github/copilot-instructions.md` only when a specific tool needs behavior AGENTS.md cannot express or has not yet adopted.
- Use rules directories (`.cursor/rules/`, `.devin/rules/`, `.clinerules/`) for narrow file-glob or model-decision activation; use AGENTS.md for durable directory-scoped project guidance.

### Sources checked
- [AGENTS.md spec](https://agents.md/)
- [OpenAI Codex AGENTS.md example](https://raw.githubusercontent.com/openai/codex/main/AGENTS.md)
- [Apache Airflow AGENTS.md example](https://raw.githubusercontent.com/apache/airflow/main/AGENTS.md)
