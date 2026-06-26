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

### Documents & Office

| Example | Represents | Upstream | File | Exact source |
| --- | --- | --- | --- | --- |
| `pdf` | A skill that relies on bundled tooling and domain-specific operational guidance. | [`anthropics/skills`](https://github.com/anthropics/skills) | [`examples/pdf/SKILL.md`](examples/pdf/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/pdf/SKILL.md) |
| `docx` | Create, read, and edit Word .docx files | [`anthropics/skills`](https://github.com/anthropics/skills) | [`examples/docx/SKILL.md`](examples/docx/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/docx/SKILL.md) |
| `pptx` | Create, read, and edit PowerPoint .pptx files | [`anthropics/skills`](https://github.com/anthropics/skills) | [`examples/pptx/SKILL.md`](examples/pptx/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/pptx/SKILL.md) |
| `xlsx` | Create, read, and edit Excel .xlsx spreadsheets | [`anthropics/skills`](https://github.com/anthropics/skills) | [`examples/xlsx/SKILL.md`](examples/xlsx/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/xlsx/SKILL.md) |
| `docx-tracked-changes` | Produces Word tracked changes (insertions, deletions, margin comments); activates on requests to redline/markup a document for review | [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills) | [`examples/docx-tracked-changes/SKILL.md`](examples/docx-tracked-changes/SKILL.md) | [source](https://raw.githubusercontent.com/mohitagw15856/pm-claude-skills/main/skills/docx-tracked-changes/SKILL.md) |
| `pptx-slide-auditor` | Slide-by-slide PowerPoint audit for layout, overflow, hierarchy and inconsistency before a meeting | [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills) | [`examples/pptx-slide-auditor/SKILL.md`](examples/pptx-slide-auditor/SKILL.md) | [source](https://raw.githubusercontent.com/mohitagw15856/pm-claude-skills/main/skills/pptx-slide-auditor/SKILL.md) |
| `md-document-html` | Converts long-form markdown (specs/RFCs/reports) into a single-file interactive HTML document with TOC and search | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) | [`examples/md-document-html/SKILL.md`](examples/md-document-html/SKILL.md) | [source](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/markdown-html/skills/md-document/SKILL.md) |
| `md-slides-html` | Converts a markdown deck into a single-file HTML presentation with keyboard nav, presenter mode and print-to-PDF | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) | [`examples/md-slides-html/SKILL.md`](examples/md-slides-html/SKILL.md) | [source](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/markdown-html/skills/md-slides/SKILL.md) |
| `quarto-authoring` | Authoring guidance for Quarto (.qmd) documents, books, sites, presentations incl. callouts, cross-refs and citations | [`posit-dev/skills`](https://github.com/posit-dev/skills) | [`examples/quarto-authoring/SKILL.md`](examples/quarto-authoring/SKILL.md) | [source](https://raw.githubusercontent.com/posit-dev/skills/main/quarto/quarto-authoring/SKILL.md) |
| `google-apps-script-sheets` | Builds Google Sheets/Workspace automation (menus, triggers, sidebars, email batches, PDF export) | [`jezweb/claude-skills`](https://github.com/jezweb/claude-skills) | [`examples/google-apps-script-sheets/SKILL.md`](examples/google-apps-script-sheets/SKILL.md) | [source](https://raw.githubusercontent.com/jezweb/claude-skills/main/plugins/integrations/skills/google-apps-script/SKILL.md) |
| `excel-automation-composio` | Create/format workbooks and read/write cells across Microsoft Excel (OneDrive) and Google Sheets | [`ComposioHQ/awesome-claude-skills`](https://github.com/ComposioHQ/awesome-claude-skills) | [`examples/excel-automation-composio/SKILL.md`](examples/excel-automation-composio/SKILL.md) | [source](https://raw.githubusercontent.com/ComposioHQ/awesome-claude-skills/master/composio-skills/excel-automation/SKILL.md) |
| `googleslides-automation-composio` | Build and batch-edit Google Slides decks from Markdown/templates and pull thumbnails | [`ComposioHQ/awesome-claude-skills`](https://github.com/ComposioHQ/awesome-claude-skills) | [`examples/googleslides-automation-composio/SKILL.md`](examples/googleslides-automation-composio/SKILL.md) | [source](https://raw.githubusercontent.com/ComposioHQ/awesome-claude-skills/master/composio-skills/googleslides-automation/SKILL.md) |
| `ocrspace-automation-composio` | Run OCR over images/PDFs to extract text via the OCR.space toolkit | [`ComposioHQ/awesome-claude-skills`](https://github.com/ComposioHQ/awesome-claude-skills) | [`examples/ocrspace-automation-composio/SKILL.md`](examples/ocrspace-automation-composio/SKILL.md) | [source](https://raw.githubusercontent.com/ComposioHQ/awesome-claude-skills/master/composio-skills/ocrspace-automation/SKILL.md) |
| `file-conversion-changethisfile` | Convert files across ~999 routes (PDF to Word, HEIC to JPG, MP4 to MP3, CSV to JSON) via ChangeThisFile | [`wshobson/agents`](https://github.com/wshobson/agents) | [`examples/file-conversion-changethisfile/SKILL.md`](examples/file-conversion-changethisfile/SKILL.md) | [source](https://raw.githubusercontent.com/wshobson/agents/main/plugins/file-conversion/skills/file-conversion/SKILL.md) |
| `opendataloader-pdf` | Parse PDFs into Markdown/JSON/HTML (tables, scans, formulas) for RAG/LLM pipelines | [`chujianyun/skills`](https://github.com/chujianyun/skills) | [`examples/opendataloader-pdf/SKILL.md`](examples/opendataloader-pdf/SKILL.md) | [source](https://raw.githubusercontent.com/chujianyun/skills/main/skills/opendataloader-pdf/SKILL.md) |
| `alt-text-figures` | Generate and audit accessible alt text for figures in R packages and Quarto documents | [`posit-dev/skills`](https://github.com/posit-dev/skills) | [`examples/alt-text-figures/SKILL.md`](examples/alt-text-figures/SKILL.md) | [source](https://raw.githubusercontent.com/posit-dev/skills/main/alt-text/SKILL.md) |

### Design & Creative

| Example | Represents | Upstream | File | Exact source |
| --- | --- | --- | --- | --- |
| `algorithmic-art` | Generative art with p5.js using seeded randomness and interactive parameter exploration | [`anthropics/skills`](https://github.com/anthropics/skills) | [`examples/algorithmic-art/SKILL.md`](examples/algorithmic-art/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/algorithmic-art/SKILL.md) |
| `brand-guidelines` | Applies Anthropic brand colors and typography to artifacts | [`anthropics/skills`](https://github.com/anthropics/skills) | [`examples/brand-guidelines/SKILL.md`](examples/brand-guidelines/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/brand-guidelines/SKILL.md) |
| `canvas-design` | Create visual art as .png/.pdf using design philosophy | [`anthropics/skills`](https://github.com/anthropics/skills) | [`examples/canvas-design/SKILL.md`](examples/canvas-design/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/canvas-design/SKILL.md) |
| `frontend-design` | Guidance for distinctive, intentional frontend UI design | [`anthropics/skills`](https://github.com/anthropics/skills) | [`examples/frontend-design/SKILL.md`](examples/frontend-design/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md) |
| `slack-gif-creator` | Create animated GIFs optimized for Slack | [`anthropics/skills`](https://github.com/anthropics/skills) | [`examples/slack-gif-creator/SKILL.md`](examples/slack-gif-creator/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/slack-gif-creator/SKILL.md) |
| `theme-factory` | Toolkit for styling artifacts with a consistent theme | [`anthropics/skills`](https://github.com/anthropics/skills) | [`examples/theme-factory/SKILL.md`](examples/theme-factory/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/theme-factory/SKILL.md) |
| `web-artifacts-builder` | Build elaborate multi-component claude.ai HTML artifacts | [`anthropics/skills`](https://github.com/anthropics/skills) | [`examples/web-artifacts-builder/SKILL.md`](examples/web-artifacts-builder/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/web-artifacts-builder/SKILL.md) |
| `swiftui-design-skill` | Designs distinctive iOS/macOS SwiftUI interfaces with anti-AI-slop rules and a 5-dimension review | [`Wholiver/swiftui-design-skill`](https://github.com/Wholiver/swiftui-design-skill) | [`examples/swiftui-design-skill/SKILL.md`](examples/swiftui-design-skill/SKILL.md) | [source](https://raw.githubusercontent.com/Wholiver/swiftui-design-skill/main/SKILL.md) |
| `spine-2d-animation` | Rigs and keyframes 2D characters into Spine skeletal animations (.json/.atlas/.png) with HTML5 preview | [`GenielabsOpenSource/spine-animation-ai`](https://github.com/GenielabsOpenSource/spine-animation-ai) | [`examples/spine-2d-animation/SKILL.md`](examples/spine-2d-animation/SKILL.md) | [source](https://raw.githubusercontent.com/GenielabsOpenSource/spine-animation-ai/main/SKILL.md) |
| `nano-image-generator` | Generates icons, logos, banners and illustrations via Nano Banana Pro with reference-image style transfer | [`lxfater/nano-image-generator-skill`](https://github.com/lxfater/nano-image-generator-skill) | [`examples/nano-image-generator/SKILL.md`](examples/nano-image-generator/SKILL.md) | [source](https://raw.githubusercontent.com/lxfater/nano-image-generator-skill/main/SKILL.md) |
| `claw3d-print-workflow` | Unified 3D workflow: AI model creation, Thingiverse search, slicing and 3D printing as opt-in modules | [`makermate/claw3d-skill`](https://github.com/makermate/claw3d-skill) | [`examples/claw3d-print-workflow/SKILL.md`](examples/claw3d-print-workflow/SKILL.md) | [source](https://raw.githubusercontent.com/makermate/claw3d-skill/main/SKILL.md) |
| `qwen3-tts-voice` | Local Qwen3-TTS voice workflow for single-line synthesis, audiobook batch dubbing, and voice cloning | [`mu-zi-lee/qwen3-tts-skill`](https://github.com/mu-zi-lee/qwen3-tts-skill) | [`examples/qwen3-tts-voice/SKILL.md`](examples/qwen3-tts-voice/SKILL.md) | [source](https://raw.githubusercontent.com/mu-zi-lee/qwen3-tts-skill/main/SKILL.md) |
| `game-character-sprites` | Creates fixed-cell pixel-art character spritesheets (idle/walk/attack, 4/8-way) with transparent previews | [`tachikomared/character-animation-creator-skill`](https://github.com/tachikomared/character-animation-creator-skill) | [`examples/game-character-sprites/SKILL.md`](examples/game-character-sprites/SKILL.md) | [source](https://raw.githubusercontent.com/tachikomared/character-animation-creator-skill/main/SKILL.md) |
| `premium-ui-builder` | Premium UI design advisor that turns generic/AI-looking interfaces into polished, implementation-ready directions | [`ziguishian/premium-ui-builder-skill`](https://github.com/ziguishian/premium-ui-builder-skill) | [`examples/premium-ui-builder/SKILL.md`](examples/premium-ui-builder/SKILL.md) | [source](https://raw.githubusercontent.com/ziguishian/premium-ui-builder-skill/main/SKILL.md) |
| `wshobson-visual-design-foundations` | Core visual-design principles (hierarchy, color, type, spacing) for establishing or auditing a UI | [`wshobson/agents`](https://github.com/wshobson/agents) | [`examples/wshobson-visual-design-foundations/SKILL.md`](examples/wshobson-visual-design-foundations/SKILL.md) | [source](https://raw.githubusercontent.com/wshobson/agents/main/plugins/ui-design/skills/visual-design-foundations/SKILL.md) |
| `wshobson-interaction-design` | Patterns for micro-interactions, states, and motion when designing interactive UI behavior | [`wshobson/agents`](https://github.com/wshobson/agents) | [`examples/wshobson-interaction-design/SKILL.md`](examples/wshobson-interaction-design/SKILL.md) | [source](https://raw.githubusercontent.com/wshobson/agents/main/plugins/ui-design/skills/interaction-design/SKILL.md) |
| `wshobson-tailwind-design-system` | Build a token-driven Tailwind design system: themes, tokens, reusable component styles | [`wshobson/agents`](https://github.com/wshobson/agents) | [`examples/wshobson-tailwind-design-system/SKILL.md`](examples/wshobson-tailwind-design-system/SKILL.md) | [source](https://raw.githubusercontent.com/wshobson/agents/main/plugins/frontend-mobile-development/skills/tailwind-design-system/SKILL.md) |
| `alireza-apple-hig-expert` | Audit/design Apple-platform UI against the Human Interface Guidelines incl. Liquid Glass | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) | [`examples/alireza-apple-hig-expert/SKILL.md`](examples/alireza-apple-hig-expert/SKILL.md) | [source](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/product-team/apple-hig-expert/skills/apple-hig-expert/SKILL.md) |
| `claudekit-aesthetic-ui` | Make interfaces beautiful via proven design principles and inspiration analysis | [`mrgoonie/claudekit-skills`](https://github.com/mrgoonie/claudekit-skills) | [`examples/claudekit-aesthetic-ui/SKILL.md`](examples/claudekit-aesthetic-ui/SKILL.md) | [source](https://raw.githubusercontent.com/mrgoonie/claudekit-skills/main/.claude/skills/aesthetic/SKILL.md) |
| `aso-appstore-screenshots` | Generate high-converting ASO-optimized App Store screenshot images from an app's codebase | [`adamlyttleapps/claude-skill-aso-appstore-screenshots`](https://github.com/adamlyttleapps/claude-skill-aso-appstore-screenshots) | [`examples/aso-appstore-screenshots/SKILL.md`](examples/aso-appstore-screenshots/SKILL.md) | [source](https://raw.githubusercontent.com/adamlyttleapps/claude-skill-aso-appstore-screenshots/main/SKILL.md) |
| `webgpu-threejs-tsl` | WebGPU + Three.js TSL shaders, node materials, compute and post-processing for creative-coding scenes | [`dgreenheck/webgpu-claude-skill`](https://github.com/dgreenheck/webgpu-claude-skill) | [`examples/webgpu-threejs-tsl/SKILL.md`](examples/webgpu-threejs-tsl/SKILL.md) | [source](https://raw.githubusercontent.com/dgreenheck/webgpu-claude-skill/main/skills/webgpu-threejs-tsl/SKILL.md) |

### Dev & Tooling

| Example | Represents | Upstream | File | Exact source |
| --- | --- | --- | --- | --- |
| `mcp-builder` | A procedure-heavy skill with a precise activation description and implementation workflow. | [`anthropics/skills`](https://github.com/anthropics/skills) | [`examples/mcp-builder/SKILL.md`](examples/mcp-builder/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/mcp-builder/SKILL.md) |
| `claude-api` | Building applications with the Claude API | [`anthropics/skills`](https://github.com/anthropics/skills) | [`examples/claude-api/SKILL.md`](examples/claude-api/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/claude-api/SKILL.md) |
| `skill-creator` | Create, modify, and measure Agent Skills | [`anthropics/skills`](https://github.com/anthropics/skills) | [`examples/skill-creator/SKILL.md`](examples/skill-creator/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md) |
| `webapp-testing` | Test local web apps with Playwright | [`anthropics/skills`](https://github.com/anthropics/skills) | [`examples/webapp-testing/SKILL.md`](examples/webapp-testing/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/webapp-testing/SKILL.md) |
| `repo-task-proof-loop` | Community: repo-local spec-freeze build-evidence-verify loop for large coding tasks | [`DenisSergeevitch/repo-task-proof-loop`](https://github.com/DenisSergeevitch/repo-task-proof-loop) | [`examples/repo-task-proof-loop/SKILL.md`](examples/repo-task-proof-loop/SKILL.md) | [source](https://raw.githubusercontent.com/DenisSergeevitch/repo-task-proof-loop/main/SKILL.md) |
| `guardian-cli` | Community: AI-powered penetration-testing automation CLI orchestrating multiple agents | [`zakirkun/guardian-cli`](https://github.com/zakirkun/guardian-cli) | [`examples/guardian-cli/SKILL.md`](examples/guardian-cli/SKILL.md) | [source](https://raw.githubusercontent.com/zakirkun/guardian-cli/main/SKILL.md) |
| `web-access` | Community: route all networking via a real browser CDP skill | [`eze-is/web-access`](https://github.com/eze-is/web-access) | [`examples/web-access/SKILL.md`](examples/web-access/SKILL.md) | [source](https://raw.githubusercontent.com/eze-is/web-access/main/SKILL.md) |
| `superpowers-systematic-debugging` | Four-phase root-cause debugging discipline; activates on any bug, test failure, or unexpected behavior before proposing fixes | [`obra/superpowers`](https://github.com/obra/superpowers) | [`examples/superpowers-systematic-debugging/SKILL.md`](examples/superpowers-systematic-debugging/SKILL.md) | [source](https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/SKILL.md) |
| `superpowers-git-worktrees` | Sets up isolated git worktrees for parallel feature work | [`obra/superpowers`](https://github.com/obra/superpowers) | [`examples/superpowers-git-worktrees/SKILL.md`](examples/superpowers-git-worktrees/SKILL.md) | [source](https://raw.githubusercontent.com/obra/superpowers/main/skills/using-git-worktrees/SKILL.md) |
| `superpowers-test-driven-development` | Red-green-refactor TDD loop with failing-test-first enforcement | [`obra/superpowers`](https://github.com/obra/superpowers) | [`examples/superpowers-test-driven-development/SKILL.md`](examples/superpowers-test-driven-development/SKILL.md) | [source](https://raw.githubusercontent.com/obra/superpowers/main/skills/test-driven-development/SKILL.md) |
| `wshobson-terraform-module-library` | Builds reusable IaC modules for AWS/Azure/GCP/OCI | [`wshobson/agents`](https://github.com/wshobson/agents) | [`examples/wshobson-terraform-module-library/SKILL.md`](examples/wshobson-terraform-module-library/SKILL.md) | [source](https://raw.githubusercontent.com/wshobson/agents/main/plugins/cloud-infrastructure/skills/terraform-module-library/SKILL.md) |
| `wshobson-git-advanced-workflows` | Advanced git: rebase, cherry-pick, bisect, worktrees, reflog recovery | [`wshobson/agents`](https://github.com/wshobson/agents) | [`examples/wshobson-git-advanced-workflows/SKILL.md`](examples/wshobson-git-advanced-workflows/SKILL.md) | [source](https://raw.githubusercontent.com/wshobson/agents/main/plugins/developer-essentials/skills/git-advanced-workflows/SKILL.md) |
| `browserbase-browser` | Drives a web browser via natural-language CLI (local Chrome or remote Browserbase) | [`browserbase/skills`](https://github.com/browserbase/skills) | [`examples/browserbase-browser/SKILL.md`](examples/browserbase-browser/SKILL.md) | [source](https://raw.githubusercontent.com/browserbase/skills/main/skills/browser/SKILL.md) |
| `prowler-pytest` | Pytest patterns (fixtures, mocking, parametrize, markers) for Python | [`prowler-cloud/prowler`](https://github.com/prowler-cloud/prowler) | [`examples/prowler-pytest/SKILL.md`](examples/prowler-pytest/SKILL.md) | [source](https://raw.githubusercontent.com/prowler-cloud/prowler/master/skills/pytest/SKILL.md) |
| `superpowers-requesting-code-review` | Dispatches a fresh-context reviewer subagent to catch issues before merge; activates when completing features or before merging | [`obra/superpowers`](https://github.com/obra/superpowers) | [`examples/superpowers-requesting-code-review/SKILL.md`](examples/superpowers-requesting-code-review/SKILL.md) | [source](https://raw.githubusercontent.com/obra/superpowers/main/skills/requesting-code-review/SKILL.md) |
| `wshobson-debugging-strategies` | Systematic debugging, profiling and root-cause analysis across any stack | [`wshobson/agents`](https://github.com/wshobson/agents) | [`examples/wshobson-debugging-strategies/SKILL.md`](examples/wshobson-debugging-strategies/SKILL.md) | [source](https://raw.githubusercontent.com/wshobson/agents/main/plugins/developer-essentials/skills/debugging-strategies/SKILL.md) |
| `wshobson-github-actions-templates` | Production-ready GitHub Actions CI/CD workflows for test/build/deploy | [`wshobson/agents`](https://github.com/wshobson/agents) | [`examples/wshobson-github-actions-templates/SKILL.md`](examples/wshobson-github-actions-templates/SKILL.md) | [source](https://raw.githubusercontent.com/wshobson/agents/main/plugins/cicd-automation/skills/github-actions-templates/SKILL.md) |
| `trailofbits-semgrep` | Runs Semgrep SAST with parallel subagents (full or high-confidence modes, Pro taint analysis) | [`trailofbits/skills`](https://github.com/trailofbits/skills) | [`examples/trailofbits-semgrep/SKILL.md`](examples/trailofbits-semgrep/SKILL.md) | [source](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/static-analysis/skills/semgrep/SKILL.md) |
| `trailofbits-codeql` | Scans codebases with CodeQL interprocedural data-flow/taint tracking | [`trailofbits/skills`](https://github.com/trailofbits/skills) | [`examples/trailofbits-codeql/SKILL.md`](examples/trailofbits-codeql/SKILL.md) | [source](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/static-analysis/skills/codeql/SKILL.md) |
| `browserbase-ui-test` | AI-powered adversarial UI testing via the browse CLI, diff-aware; QAs UI changes and accessibility | [`browserbase/skills`](https://github.com/browserbase/skills) | [`examples/browserbase-ui-test/SKILL.md`](examples/browserbase-ui-test/SKILL.md) | [source](https://raw.githubusercontent.com/browserbase/skills/main/skills/ui-test/SKILL.md) |
| `playwright-browser-testing` | Playwright browser automation that auto-detects dev servers and writes clean test scripts | [`lackeyjb/playwright-skill`](https://github.com/lackeyjb/playwright-skill) | [`examples/playwright-browser-testing/SKILL.md`](examples/playwright-browser-testing/SKILL.md) | [source](https://raw.githubusercontent.com/lackeyjb/playwright-skill/main/skills/playwright-skill/SKILL.md) |
| `dotnet-csharp-coding-standards` | Modern high-performance C# patterns (records, pattern matching, Span<T>, async, C#12+) | [`Aaronontheweb/dotnet-skills`](https://github.com/Aaronontheweb/dotnet-skills) | [`examples/dotnet-csharp-coding-standards/SKILL.md`](examples/dotnet-csharp-coding-standards/SKILL.md) | [source](https://raw.githubusercontent.com/Aaronontheweb/dotnet-skills/master/skills/csharp-coding-standards/SKILL.md) |

### Content & Comms

| Example | Represents | Upstream | File | Exact source |
| --- | --- | --- | --- | --- |
| `doc-coauthoring` | Structured workflow for co-authoring documentation | [`anthropics/skills`](https://github.com/anthropics/skills) | [`examples/doc-coauthoring/SKILL.md`](examples/doc-coauthoring/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/doc-coauthoring/SKILL.md) |
| `internal-comms` | Write internal communications in company formats | [`anthropics/skills`](https://github.com/anthropics/skills) | [`examples/internal-comms/SKILL.md`](examples/internal-comms/SKILL.md) | [source](https://raw.githubusercontent.com/anthropics/skills/main/skills/internal-comms/SKILL.md) |
| `xhs-note-creator` | Community: Xiaohongshu (RedBook) note creator with themed image cards | [`comeonzhj/Auto-Redbook-Skills`](https://github.com/comeonzhj/Auto-Redbook-Skills) | [`examples/xhs-note-creator/SKILL.md`](examples/xhs-note-creator/SKILL.md) | [source](https://raw.githubusercontent.com/comeonzhj/Auto-Redbook-Skills/main/SKILL.md) |
| `newsletter-writer` | Writes a full creator newsletter issue (subject lines, hook, body, CTA) for Substack/beehiiv/ConvertKit | [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills) | [`examples/newsletter-writer/SKILL.md`](examples/newsletter-writer/SKILL.md) | [source](https://raw.githubusercontent.com/mohitagw15856/pm-claude-skills/main/skills/newsletter-writer/SKILL.md) |
| `press-release-writer` | Writes a structured press release (headline, dateline, body, boilerplate, contact) around the news angle | [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills) | [`examples/press-release-writer/SKILL.md`](examples/press-release-writer/SKILL.md) | [source](https://raw.githubusercontent.com/mohitagw15856/pm-claude-skills/main/skills/press-release/SKILL.md) |
| `seo-keyword-research` | SEO keyword research prioritizing volume, difficulty, intent and topic clusters (English + Chinese) | [`aaron-he-zhu/seo-geo-claude-skills`](https://github.com/aaron-he-zhu/seo-geo-claude-skills) | [`examples/seo-keyword-research/SKILL.md`](examples/seo-keyword-research/SKILL.md) | [source](https://raw.githubusercontent.com/aaron-he-zhu/seo-geo-claude-skills/main/research/keyword-research/SKILL.md) |
| `seo-content-writer` | Drafts SEO-optimized posts, articles and landing pages with target keywords and snippet structure | [`aaron-he-zhu/seo-geo-claude-skills`](https://github.com/aaron-he-zhu/seo-geo-claude-skills) | [`examples/seo-content-writer/SKILL.md`](examples/seo-content-writer/SKILL.md) | [source](https://raw.githubusercontent.com/aaron-he-zhu/seo-geo-claude-skills/main/build/seo-content-writer/SKILL.md) |
| `geo-content-optimizer` | Improves content citation-readiness for AI engines (ChatGPT, Perplexity, AI Overviews, Gemini) | [`aaron-he-zhu/seo-geo-claude-skills`](https://github.com/aaron-he-zhu/seo-geo-claude-skills) | [`examples/geo-content-optimizer/SKILL.md`](examples/geo-content-optimizer/SKILL.md) | [source](https://raw.githubusercontent.com/aaron-he-zhu/seo-geo-claude-skills/main/build/geo-content-optimizer/SKILL.md) |
| `character-voice-writing` | Writes dialogue and explores a character's voice from a full profile or bare sketch (model-invocable) | [`haowjy/creative-writing-skills`](https://github.com/haowjy/creative-writing-skills) | [`examples/character-voice-writing/SKILL.md`](examples/character-voice-writing/SKILL.md) | [source](https://raw.githubusercontent.com/haowjy/creative-writing-skills/main/skills/character-voice/SKILL.md) |
| `brand-copywriter` | Generates marketing copy via proven frameworks for ads, landing/sales pages, email sequences and LinkedIn | [`ognjengt/founder-skills`](https://github.com/ognjengt/founder-skills) | [`examples/brand-copywriter/SKILL.md`](examples/brand-copywriter/SKILL.md) | [source](https://raw.githubusercontent.com/ognjengt/founder-skills/main/skills/brand-copywriter/SKILL.md) |
| `social-publishing-socialclaw` | Schedules/publishes social posts across 13 platforms via the SocialClaw API (needs SOCIALCLAW_API_KEY) | [`wshobson/agents`](https://github.com/wshobson/agents) | [`examples/social-publishing-socialclaw/SKILL.md`](examples/social-publishing-socialclaw/SKILL.md) | [source](https://raw.githubusercontent.com/wshobson/agents/main/plugins/social-publishing/skills/social-publishing/SKILL.md) |
| `resume-cover-letter` | Writes role-tailored resumes/CVs and cover letters with ATS-friendly formatting and regional formats | [`jezweb/claude-skills`](https://github.com/jezweb/claude-skills) | [`examples/resume-cover-letter/SKILL.md`](examples/resume-cover-letter/SKILL.md) | [source](https://raw.githubusercontent.com/jezweb/claude-skills/main/plugins/writing/skills/resume-cover-letter/SKILL.md) |
| `competitive-ads-extractor` | Scrape and analyze competitor ads from Facebook/LinkedIn ad libraries for messaging insight | [`ComposioHQ/awesome-claude-skills`](https://github.com/ComposioHQ/awesome-claude-skills) | [`examples/competitive-ads-extractor/SKILL.md`](examples/competitive-ads-extractor/SKILL.md) | [source](https://raw.githubusercontent.com/ComposioHQ/awesome-claude-skills/master/competitive-ads-extractor/SKILL.md) |
| `ad-creative-paid-ads` | Generate and iterate paid-ad copy and headlines (RSA, Meta, LinkedIn) at scale | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) | [`examples/ad-creative-paid-ads/SKILL.md`](examples/ad-creative-paid-ads/SKILL.md) | [source](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/ad-creative/SKILL.md) |
| `cold-email-outreach` | Write and sequence B2B cold-outreach emails and humanize sales-y drafts | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) | [`examples/cold-email-outreach/SKILL.md`](examples/cold-email-outreach/SKILL.md) | [source](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/cold-email/SKILL.md) |
| `content-gap-analysis` | Map missing topics and keyword gaps versus competitors for editorial planning | [`aaron-he-zhu/seo-geo-claude-skills`](https://github.com/aaron-he-zhu/seo-geo-claude-skills) | [`examples/content-gap-analysis/SKILL.md`](examples/content-gap-analysis/SKILL.md) | [source](https://raw.githubusercontent.com/aaron-he-zhu/seo-geo-claude-skills/main/research/content-gap-analysis/SKILL.md) |
| `content-repurposer` | Atomize one source into X thread, LinkedIn post, newsletter section, IG carousel, and short-form script | [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills) | [`examples/content-repurposer/SKILL.md`](examples/content-repurposer/SKILL.md) | [source](https://raw.githubusercontent.com/mohitagw15856/pm-claude-skills/main/plugins/pm-creator/skills/content-repurposer/SKILL.md) |
| `social-media-posts` | Produce platform-specific posts for LinkedIn/Facebook/Instagram/Reddit with limits, hashtags, hooks | [`jezweb/claude-skills`](https://github.com/jezweb/claude-skills) | [`examples/social-media-posts/SKILL.md`](examples/social-media-posts/SKILL.md) | [source](https://raw.githubusercontent.com/jezweb/claude-skills/main/plugins/social-media/skills/social-media-posts/SKILL.md) |
| `remove-ai-flavor` | Rewrite drafts to strip AI-tells and template tone for a natural human voice | [`chujianyun/skills`](https://github.com/chujianyun/skills) | [`examples/remove-ai-flavor/SKILL.md`](examples/remove-ai-flavor/SKILL.md) | [source](https://raw.githubusercontent.com/chujianyun/skills/main/skills/remove-ai-flavor/SKILL.md) |

### Data & Analysis

| Example | Represents | Upstream | File | Exact source |
| --- | --- | --- | --- | --- |
| `wshobson-backtesting-frameworks` | Builds robust trading backtests handling look-ahead/survivorship bias and transaction costs | [`wshobson/agents`](https://github.com/wshobson/agents) | [`examples/wshobson-backtesting-frameworks/SKILL.md`](examples/wshobson-backtesting-frameworks/SKILL.md) | [source](https://raw.githubusercontent.com/wshobson/agents/main/plugins/quantitative-trading/skills/backtesting-frameworks/SKILL.md) |
| `chdb-datastore` | pandas API over a ClickHouse engine for fast filter/group/join across parquet/csv/S3/Postgres | [`chdb-io/chdb`](https://github.com/chdb-io/chdb) | [`examples/chdb-datastore/SKILL.md`](examples/chdb-datastore/SKILL.md) | [source](https://raw.githubusercontent.com/chdb-io/chdb/main/agent/skills/chdb-datastore/SKILL.md) |
| `pycse` | Scientific computing toolkit: nonlinear regression, uncertainty quantification, design of experiments | [`jkitchin/pycse`](https://github.com/jkitchin/pycse) | [`examples/pycse/SKILL.md`](examples/pycse/SKILL.md) | [source](https://raw.githubusercontent.com/jkitchin/pycse/master/src/pycse/SKILL.md) |
| `research-time-series-econometrics` | Time-series econometrics: ARIMA, VAR, cointegration, stationarity, forecasting | [`wentorai/research-plugins`](https://github.com/wentorai/research-plugins) | [`examples/research-time-series-econometrics/SKILL.md`](examples/research-time-series-econometrics/SKILL.md) | [source](https://raw.githubusercontent.com/wentorai/research-plugins/main/skills/analysis/econometrics/time-series-guide/SKILL.md) |
| `research-hypothesis-testing` | Statistical hypothesis testing, power analysis, and significance reporting | [`wentorai/research-plugins`](https://github.com/wentorai/research-plugins) | [`examples/research-hypothesis-testing/SKILL.md`](examples/research-hypothesis-testing/SKILL.md) | [source](https://raw.githubusercontent.com/wentorai/research-plugins/main/skills/analysis/statistics/hypothesis-testing-guide/SKILL.md) |
| `omicverse-single-cell-clustering` | Single-cell clustering (Leiden, Louvain, GMM, cNMF) and batch correction for scRNA-seq | [`omicverse/omicverse`](https://github.com/omicverse/omicverse) | [`examples/omicverse-single-cell-clustering/SKILL.md`](examples/omicverse-single-cell-clustering/SKILL.md) | [source](https://raw.githubusercontent.com/omicverse/omicverse/master/.claude/skills/single-clustering/SKILL.md) |
| `zorai-yfinance` | Downloads Yahoo Finance market data (prices, options, fundamentals) into pandas | [`mkurman/zorai`](https://github.com/mkurman/zorai) | [`examples/zorai-yfinance/SKILL.md`](examples/zorai-yfinance/SKILL.md) | [source](https://raw.githubusercontent.com/mkurman/zorai/main/skills/scientific-skills/yfinance/SKILL.md) |
| `wshobson-rag-implementation` | Builds Retrieval-Augmented Generation systems with vector DBs and semantic search for knowledge-grounded AI | [`wshobson/agents`](https://github.com/wshobson/agents) | [`examples/wshobson-rag-implementation/SKILL.md`](examples/wshobson-rag-implementation/SKILL.md) | [source](https://raw.githubusercontent.com/wshobson/agents/main/plugins/llm-application-dev/skills/rag-implementation/SKILL.md) |
| `wshobson-spark-optimization` | Optimizes Apache Spark jobs via partitioning, caching, shuffle and memory tuning | [`wshobson/agents`](https://github.com/wshobson/agents) | [`examples/wshobson-spark-optimization/SKILL.md`](examples/wshobson-spark-optimization/SKILL.md) | [source](https://raw.githubusercontent.com/wshobson/agents/main/plugins/data-engineering/skills/spark-optimization/SKILL.md) |
| `wshobson-ml-pipeline-workflow` | End-to-end MLOps pipelines from data prep through training, validation and deployment | [`wshobson/agents`](https://github.com/wshobson/agents) | [`examples/wshobson-ml-pipeline-workflow/SKILL.md`](examples/wshobson-ml-pipeline-workflow/SKILL.md) | [source](https://raw.githubusercontent.com/wshobson/agents/main/plugins/machine-learning-ops/skills/ml-pipeline-workflow/SKILL.md) |
| `browserbase-company-research` | Discovers and deep-researches target companies via Browserbase Search, scores ICP fit into a report/CSV | [`browserbase/skills`](https://github.com/browserbase/skills) | [`examples/browserbase-company-research/SKILL.md`](examples/browserbase-company-research/SKILL.md) | [source](https://raw.githubusercontent.com/browserbase/skills/main/skills/company-research/SKILL.md) |
| `tradermonty-technical-analyst` | Technical analysis of weekly price charts (trends, support/resistance, scenarios) for stocks/crypto/forex | [`tradermonty/claude-trading-skills`](https://github.com/tradermonty/claude-trading-skills) | [`examples/tradermonty-technical-analyst/SKILL.md`](examples/tradermonty-technical-analyst/SKILL.md) | [source](https://raw.githubusercontent.com/tradermonty/claude-trading-skills/main/skills/technical-analyst/SKILL.md) |
| `tradermonty-backtest-expert` | Systematic backtesting of trading strategies (robustness, slippage, bias prevention) | [`tradermonty/claude-trading-skills`](https://github.com/tradermonty/claude-trading-skills) | [`examples/tradermonty-backtest-expert/SKILL.md`](examples/tradermonty-backtest-expert/SKILL.md) | [source](https://raw.githubusercontent.com/tradermonty/claude-trading-skills/main/skills/backtest-expert/SKILL.md) |
| `posit-ggsql` | Writes ggsql queries (a grammar-of-graphics for SQL) for data visualization | [`posit-dev/skills`](https://github.com/posit-dev/skills) | [`examples/posit-ggsql/SKILL.md`](examples/posit-ggsql/SKILL.md) | [source](https://raw.githubusercontent.com/posit-dev/skills/main/ggsql/ggsql/SKILL.md) |

### Domain-specific & Niche

| Example | Represents | Upstream | File | Exact source |
| --- | --- | --- | --- | --- |
| `bazi` | Community: Chinese four-pillars (Bazi) birth-chart analysis | [`jinchenma94/bazi-skill`](https://github.com/jinchenma94/bazi-skill) | [`examples/bazi/SKILL.md`](examples/bazi/SKILL.md) | [source](https://raw.githubusercontent.com/jinchenma94/bazi-skill/main/SKILL.md) |
| `market-sages-investors` | Convenes a council of 13 legendary investors to analyze a stock ticker and synthesize a recommendation | [`hyhmrright/market-sages`](https://github.com/hyhmrright/market-sages) | [`examples/market-sages-investors/SKILL.md`](examples/market-sages-investors/SKILL.md) | [source](https://raw.githubusercontent.com/hyhmrright/market-sages/main/skill.md) |
| `milo-solana-portfolio` | Autonomous Solana portfolio management API: non-custodial wallets, transfers, orders, auto-trading | [`and-milo/agent-to-agent-portfolio-manager`](https://github.com/and-milo/agent-to-agent-portfolio-manager) | [`examples/milo-solana-portfolio/SKILL.md`](examples/milo-solana-portfolio/SKILL.md) | [source](https://raw.githubusercontent.com/and-milo/agent-to-agent-portfolio-manager/main/skill.md) |
| `weixin-minigame-dev` | WeChat Mini Game development guide: platform API limits, Canvas constraints, best practices | [`wukaikailive/weixin-game-skill`](https://github.com/wukaikailive/weixin-game-skill) | [`examples/weixin-minigame-dev/SKILL.md`](examples/weixin-minigame-dev/SKILL.md) | [source](https://raw.githubusercontent.com/wukaikailive/weixin-game-skill/main/skill.md) |
| `mlai-textbooks` | Expert tutor for ML/AI algorithms from Bishop's PRML and Norvig's AIMA via the mlai-textbooks package | [`dhruv-anand-aintech/mlai-textbooks-skill`](https://github.com/dhruv-anand-aintech/mlai-textbooks-skill) | [`examples/mlai-textbooks/SKILL.md`](examples/mlai-textbooks/SKILL.md) | [source](https://raw.githubusercontent.com/dhruv-anand-aintech/mlai-textbooks-skill/main/skill.md) |
| `taleb-perspective` | Applies Nassim Taleb's mental models (antifragility, black swan, barbell, skin-in-the-game) to decisions | [`alchaincyf/taleb-skill`](https://github.com/alchaincyf/taleb-skill) | [`examples/taleb-perspective/SKILL.md`](examples/taleb-perspective/SKILL.md) | [source](https://raw.githubusercontent.com/alchaincyf/taleb-skill/main/SKILL.md) |
| `employment-contract-templates` | Drafts employment contracts, offer letters, and HR policy documents following legal best practices | [`wshobson/agents`](https://github.com/wshobson/agents) | [`examples/employment-contract-templates/SKILL.md`](examples/employment-contract-templates/SKILL.md) | [source](https://raw.githubusercontent.com/wshobson/agents/main/plugins/hr-legal-compliance/skills/employment-contract-templates/SKILL.md) |
| `wshobson-godot-gdscript-patterns` | Godot 4 GDScript patterns (signals, scenes, state machines, optimization) for building games | [`wshobson/agents`](https://github.com/wshobson/agents) | [`examples/wshobson-godot-gdscript-patterns/SKILL.md`](examples/wshobson-godot-gdscript-patterns/SKILL.md) | [source](https://raw.githubusercontent.com/wshobson/agents/main/plugins/game-development/skills/godot-gdscript-patterns/SKILL.md) |
| `wshobson-unity-ecs-patterns` | Unity DOTS/ECS architecture and performance patterns for data-oriented game systems | [`wshobson/agents`](https://github.com/wshobson/agents) | [`examples/wshobson-unity-ecs-patterns/SKILL.md`](examples/wshobson-unity-ecs-patterns/SKILL.md) | [source](https://raw.githubusercontent.com/wshobson/agents/main/plugins/game-development/skills/unity-ecs-patterns/SKILL.md) |
| `wshobson-risk-metrics-calculation` | Compute trading/portfolio risk metrics (VaR, drawdown, Sharpe, volatility) | [`wshobson/agents`](https://github.com/wshobson/agents) | [`examples/wshobson-risk-metrics-calculation/SKILL.md`](examples/wshobson-risk-metrics-calculation/SKILL.md) | [source](https://raw.githubusercontent.com/wshobson/agents/main/plugins/quantitative-trading/skills/risk-metrics-calculation/SKILL.md) |
| `wshobson-gdpr-data-handling` | GDPR-compliant data handling, consent, and data-subject rights for systems processing EU personal data | [`wshobson/agents`](https://github.com/wshobson/agents) | [`examples/wshobson-gdpr-data-handling/SKILL.md`](examples/wshobson-gdpr-data-handling/SKILL.md) | [source](https://raw.githubusercontent.com/wshobson/agents/main/plugins/hr-legal-compliance/skills/gdpr-data-handling/SKILL.md) |
| `alireza-clinical-research` | Design prospective clinical studies (endpoints, power/sample-size, GO/NO-GO phase-gate) | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) | [`examples/alireza-clinical-research/SKILL.md`](examples/alireza-clinical-research/SKILL.md) | [source](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/research-ops/skills/clinical-research/SKILL.md) |
| `jeffallan-shopify-expert` | Build/debug Shopify themes, apps, and Storefront/Hydrogen integrations | [`Jeffallan/claude-skills`](https://github.com/Jeffallan/claude-skills) | [`examples/jeffallan-shopify-expert/SKILL.md`](examples/jeffallan-shopify-expert/SKILL.md) | [source](https://raw.githubusercontent.com/Jeffallan/claude-skills/main/skills/shopify-expert/SKILL.md) |
| `pm-retention-analysis` | Structure a product retention/churn deep-dive with root-cause hypotheses and interventions | [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills) | [`examples/pm-retention-analysis/SKILL.md`](examples/pm-retention-analysis/SKILL.md) | [source](https://raw.githubusercontent.com/mohitagw15856/pm-claude-skills/main/plugins/pm-analytics/skills/retention-analysis/SKILL.md) |
| `china-finance-dcf` | DCF valuation for A-share equities using Chinese financial data and China-specific WACC inputs | [`jwangkun/claude-for-financial-services-cn`](https://github.com/jwangkun/claude-for-financial-services-cn) | [`examples/china-finance-dcf/SKILL.md`](examples/china-finance-dcf/SKILL.md) | [source](https://raw.githubusercontent.com/jwangkun/claude-for-financial-services-cn/main/vertical-plugins/china-finance/skills/china-dcf/SKILL.md) |
