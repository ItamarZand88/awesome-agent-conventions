# SKILL.md 🟢 Adopted

> A self-contained, model-invoked capability: YAML frontmatter (name + description) tells the agent when to load it; the body teaches it how. Progressive disclosure keeps it cheap until needed.

- **Read by:** Claude (Agent Skills), Claude Code, and the open Agent Skills ecosystem
- **Location:** A skill directory: <skill-name>/SKILL.md (plus bundled scripts and resources)
- **Spec:** [https://agentskills.io](https://agentskills.io)
- **Evidence:** Agent Skills documentation and public skill repositories define SKILL.md as the load-on-demand capability manifest.
- **Last verified:** 2026-06-18
- **Files:** `SKILL.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `SKILL.md`

| Source | File | Provenance |
| --- | --- | --- |
| `mcp-builder` | [`examples/mcp-builder/SKILL.md`](examples/mcp-builder/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/mcp-builder/SKILL.md) |
| `pdf` | [`examples/pdf/SKILL.md`](examples/pdf/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/pdf/SKILL.md) |

## Field notes

### Fields (frontmatter)
**Open standard ([agentskills.io](https://agentskills.io/specification))** - `name` and `description` are required, the rest optional:

| Field | Req | Notes |
| --- | --- | --- |
| `name` | yes | 1-64 chars, lowercase `a-z0-9` + hyphens; no leading/trailing or consecutive hyphens; **must match the parent directory name** |
| `description` | yes | 1-1024 chars; says *what* it does and *when* to use it - this is the trigger signal |
| `license` | no | license name, or a reference to a bundled license file |
| `compatibility` | no | 1-500 chars; environment requirements (product, system packages, network) |
| `metadata` | no | map of string->string; arbitrary client-defined keys (there is **no** top-level `version` - put it here) |
| `allowed-tools` | no | **space-separated** tool list, e.g. `Bash(git:*) Read`; **experimental**, support varies |

**Claude Code superset** (all optional; `name` defaults to the directory name) adds: `when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `disallowed-tools`, `model` (or `inherit`), `effort` (`low`/`medium`/`high`/`xhigh`/`max`), `context: fork`, `agent`, `hooks`, `paths` (activation globs), `shell` (`bash`/`powershell`). Body substitutions: `$ARGUMENTS`, `$ARGUMENTS[N]`, `$N`, `$name`, `${CLAUDE_SESSION_ID}`, `${CLAUDE_EFFORT}`, `${CLAUDE_SKILL_DIR}`, and `` !`cmd` `` dynamic injection.

### Composition
- **Frontmatter is the contract.** `name` + `description` are always in context; the body loads only when the skill triggers. The mcp-builder example's description spells out *when* to use it and *in which languages* (*"Use when building MCP servers... whether in Python (FastMCP) or Node/TypeScript"*) - that sentence is what makes the trigger fire.
- **Body = procedure.** A phased workflow ("Phase 1: Deep Research and Planning..."), not reference prose.
- Optional `license` and bundled scripts/resources sit beside `SKILL.md` and load on demand.

### Anti-patterns
- A vague description ("helps with MCP") - the single biggest cause of a skill that never triggers.
- Cramming reference material into the body that should be a bundled file pulled in only when needed.
- A description that describes the topic but never says *when to use it*.

### Edge cases
- **Progressive disclosure** is the whole economy: `name` + `description` (~100 tokens) are always loaded; the body is recommended **under 5000 tokens / 500 lines**, with bundled files referenced one level deep.
- Two description caps to know: the open spec limits `description` to **1024 chars**; Claude Code truncates the *listed* description at ~**1536 chars** (configurable via `maxSkillDescriptionChars`).
- The same `SKILL.md` format spans Claude.ai, Claude Code, and the open Agent Skills ecosystem - write the description tool-agnostically. `.claude/skills/` is loaded from `--add-dir` (commands are not).

### Adoption / maturity
- `SKILL.md` has both an open specification and Anthropic product support. The open spec defines the portable minimum; Claude Code and Amp add richer invocation, tool, and subagent behavior.
- The main operational risk is trigger quality. A skill with a precise "use when..." description can stay out of context until needed; a vague one either never triggers or triggers too broadly.

### Related conventions
- Claude commands have merged into skills in Claude Code. Keep a workflow in `.claude/commands/*.md` only when you need legacy single-file compatibility; use `SKILL.md` when the capability needs resources, scripts, references, or model-invoked activation.
- AGENTS.md / CLAUDE.md should hold standing facts; SKILL.md should hold procedures.

### Sources checked
- [Agent Skills specification](https://agentskills.io/specification)
- [Anthropic Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Claude Code skills docs](https://code.claude.com/docs/en/slash-commands)
- [Amp skill format docs](https://ampcode.com/manual)
