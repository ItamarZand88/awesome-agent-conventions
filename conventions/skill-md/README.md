# SKILL.md 🟢 Adopted

> A self-contained, model-invoked capability file that tells an agent when to load a reusable procedure and how to execute it.

## What it is

SKILL.md lets an agent keep specialized workflows, scripts, references, and resources out of the main context until the model or user needs that capability. The open specification began at Anthropic and is now community-maintained at agentskills.io.

## Who reads or writes it

**Readers:**

- Claude Agent Skills
- Claude Code
- Amp
- Agent Skills-compatible tools

**Writers:**

- Tool authors
- Product teams packaging agent capabilities
- Developers turning repeated agent workflows into reusable capabilities

## Where it lives

- `<skill-name>/SKILL.md` - Portable Agent Skills directory format; bundled scripts and resources live beside the manifest.
- `.claude/skills/<skill-name>/SKILL.md` - Claude Code project skill location.
- `~/.claude/skills/<skill-name>/SKILL.md` - Claude Code user skill location.

## Loading rules

- The skill name and description are listed up front; the body and bundled files are loaded only when the skill is relevant.
- The open specification requires name and description frontmatter; product-specific runtimes may add optional fields.
- Keep the description precise because it is the activation signal.

## File shape

| Part | Required | Meaning |
| --- | --- | --- |
| `name` | yes | Lowercase skill identifier; in the open spec it must match the parent directory. |
| `description` | yes | Activation text that states what the skill does and when to use it. |
| `body` | yes | Procedural instructions, references to bundled resources, and workflow steps. |
| `bundled files` | no | Optional scripts, references, templates, and assets loaded only after the skill is activated. |

## Operational principles

- Use SKILL.md for repeatable capabilities, not standing project context.
- Put activation criteria in the description, not buried in the body.
- Keep the body procedural and move bulky reference material into bundled files.
- Prefer portable open-spec fields unless a runtime-specific extension is necessary.
- Treat examples as capability packages, not as the definition of the convention.

## Interoperability

- [`claude-commands`](../claude-commands/) - Claude commands are legacy or direct-invocation workflows; SKILL.md is better when a capability needs resources, scripts, references, or model-invoked activation.
- [`agents-md`](../agents-md/) - AGENTS.md carries standing project instructions; SKILL.md carries reusable procedures.
- [`claude-md`](../claude-md/) - CLAUDE.md is project memory loaded into context; SKILL.md is loaded on demand.
- [`prompt-assets`](../prompt-assets/) - Prompt assets externalize prompts; SKILL.md packages a broader operational capability around instructions and resources.

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

## Evidence and sources

| Source | Type | Why it matters |
| --- | --- | --- |
| [Agent Skills specification](https://agentskills.io/specification) | `spec` | Defines the portable SKILL.md contract, required frontmatter, and packaging model. |
| [Anthropic Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) | `docs` | Documents Anthropic product support and how skills are used by Claude. |
| [Claude Code skills and commands docs](https://code.claude.com/docs/en/slash-commands) | `docs` | Captures Claude Code's command-to-skill convergence and runtime extensions. |
| [Amp manual](https://ampcode.com/manual) | `docs` | Shows another implementation using skills and runtime-specific skill metadata. |
| [anthropics/skills](https://github.com/anthropics/skills) | `repo` | Provides maintained public examples of complete skill packages. |

## Examples

_Examples are curated evidence for the convention. They are fetched by [`scripts/extract.py`](../../scripts/extract.py) and keep line-1 provenance._

| Example | Represents | Upstream | File | Exact source |
| --- | --- | --- | --- | --- |
| `mcp-builder` | A procedure-heavy skill with a precise activation description and implementation workflow. | [`anthropics/skills`](https://github.com/anthropics/skills) | [`examples/mcp-builder/SKILL.md`](examples/mcp-builder/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/mcp-builder/SKILL.md) |
| `pdf` | A skill that relies on bundled tooling and domain-specific operational guidance. | [`anthropics/skills`](https://github.com/anthropics/skills) | [`examples/pdf/SKILL.md`](examples/pdf/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/pdf/SKILL.md) |
| `x-twitter-scraper` | A product API skill with precise activation text, safety metadata, and bundled reference links for agent use. | [`Xquik-dev/x-twitter-scraper`](https://github.com/Xquik-dev/x-twitter-scraper) | [`examples/x-twitter-scraper/SKILL.md`](examples/x-twitter-scraper/SKILL.md) | [source](https://raw.githubusercontent.com/Xquik-dev/x-twitter-scraper/master/skills/x-twitter-scraper/SKILL.md) |
