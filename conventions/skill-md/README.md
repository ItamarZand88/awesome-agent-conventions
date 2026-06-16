# SKILL.md 🟢 Adopted

> A self-contained, model-invoked capability: YAML frontmatter (name + description) tells the agent when to load it; the body teaches it how. Progressive disclosure keeps it cheap until needed.

- **Read by:** Claude (Agent Skills), Claude Code, and the open Agent Skills ecosystem
- **Location:** A skill directory: <skill-name>/SKILL.md (plus bundled scripts and resources)
- **Spec:** [https://agentskills.io](https://agentskills.io)
- **Files:** `SKILL.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) — none are hand-written._

### `SKILL.md`

| Source | File | Provenance |
| --- | --- | --- |
| `anthropics-skills` | [`anthropics-skills.mcp-builder.SKILL.md`](examples/anthropics-skills.mcp-builder.SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/mcp-builder/SKILL.md) |
| `anthropics-skills` | [`anthropics-skills.pdf.SKILL.md`](examples/anthropics-skills.pdf.SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/pdf/SKILL.md) |

## Field notes

### Composition
- **Frontmatter is the contract.** `name` + `description` are always in context; the body is loaded only when the skill triggers. The mcp-builder example's description spells out *when* to use it and *in which languages* (*"Use when building MCP servers… whether in Python (FastMCP) or Node/TypeScript"*) — that sentence is what makes the trigger fire.
- **Body = procedure.** A phased workflow ("Phase 1: Deep Research and Planning…"), not reference prose.
- Optional `license` and bundled scripts/resources sit beside `SKILL.md` and load on demand.

### Anti-patterns
- A vague description ("helps with MCP") — the single biggest cause of a skill that never triggers.
- Cramming reference material into the body that should be a bundled file pulled in only when needed.
- A description that describes the topic but never says *when to use it*.

### Edge cases
- **Progressive disclosure** is the whole economy: keep the always-loaded surface (description) small and push detail into the on-demand body/resources.
- The same `SKILL.md` format spans Claude.ai, Claude Code, and the open Agent Skills ecosystem — write the description tool-agnostically.
