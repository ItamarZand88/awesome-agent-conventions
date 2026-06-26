# Memory Bank 🟢 Adopted

> Cline's structured memory system - a set of Markdown files an agent reads at the start of every task to reconstruct full project context after its session memory resets. The six files shown are Cline's set; tools like Roo Code use an overlapping but different variant.

- **Read by:** Cline, Roo Code, and Cursor (via the Memory Bank custom-instructions pattern)
- **Location:** A memory-bank/ directory at the repository root
- **Spec:** [https://docs.cline.bot/best-practices/memory-bank](https://docs.cline.bot/best-practices/memory-bank)
- **Evidence:** Cline documents Memory Bank as a structured multi-file context system, and public repositories commit the full file set.
- **Last verified:** 2026-06-26
- **Files:** `projectbrief.md`, `productContext.md`, `activeContext.md`, `systemPatterns.md`, `techContext.md`, `progress.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `projectbrief.md`

Foundation doc - why the project exists, core requirements and goals.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `app-med-ai-gen` | [`ModusCreateOrg/app-med-ai-gen`](https://github.com/ModusCreateOrg/app-med-ai-gen) | [`examples/app-med-ai-gen/projectbrief.md`](examples/app-med-ai-gen/projectbrief.md) | [source](https://raw.githubusercontent.com/ModusCreateOrg/app-med-ai-gen/main/memory-bank/projectbrief.md) |
| `aws-sso-manager` | [`cfircoo/aws-sso-manager`](https://github.com/cfircoo/aws-sso-manager) | [`examples/aws-sso-manager/projectbrief.md`](examples/aws-sso-manager/projectbrief.md) | [source](https://raw.githubusercontent.com/cfircoo/aws-sso-manager/main/memory-bank/projectbrief.md) |
| `eloc-control-panel` | [`EDsteve/ELOC-Control-Panel`](https://github.com/EDsteve/ELOC-Control-Panel) | [`examples/eloc-control-panel/projectbrief.md`](examples/eloc-control-panel/projectbrief.md) | [source](https://raw.githubusercontent.com/EDsteve/ELOC-Control-Panel/main/memory-bank/projectbrief.md) |
| `filesystem-mcp` | [`SylphxAI/filesystem-mcp`](https://github.com/SylphxAI/filesystem-mcp) | [`examples/filesystem-mcp/projectbrief.md`](examples/filesystem-mcp/projectbrief.md) | [source](https://raw.githubusercontent.com/SylphxAI/filesystem-mcp/main/memory-bank/projectbrief.md) |
| `gitpod` | [`gitpod-io/gitpod`](https://github.com/gitpod-io/gitpod) | [`examples/gitpod/projectbrief.md`](examples/gitpod/projectbrief.md) | [source](https://raw.githubusercontent.com/gitpod-io/gitpod/main/memory-bank/projectbrief.md) |
| `goose-loadtest` | [`tag1consulting/goose`](https://github.com/tag1consulting/goose) | [`examples/goose-loadtest/projectbrief.md`](examples/goose-loadtest/projectbrief.md) | [source](https://raw.githubusercontent.com/tag1consulting/goose/main/memory-bank/projectbrief.md) |
| `klox` | [`dkopko/klox`](https://github.com/dkopko/klox) | [`examples/klox/projectbrief.md`](examples/klox/projectbrief.md) | [source](https://raw.githubusercontent.com/dkopko/klox/master/memory-bank/projectbrief.md) |
| `parse-efd-fiscal` | [`chapzin/parse-efd-fiscal`](https://github.com/chapzin/parse-efd-fiscal) | [`examples/parse-efd-fiscal/projectbrief.md`](examples/parse-efd-fiscal/projectbrief.md) | [source](https://raw.githubusercontent.com/chapzin/parse-efd-fiscal/master/memory-bank/projectbrief.md) |
| `pure3270` | [`dtg01100/pure3270`](https://github.com/dtg01100/pure3270) | [`examples/pure3270/projectbrief.md`](examples/pure3270/projectbrief.md) | [source](https://raw.githubusercontent.com/dtg01100/pure3270/main/memory-bank/projectbrief.md) |
| `repo-sprint-digest` | [`sasamuku/repo-sprint-digest`](https://github.com/sasamuku/repo-sprint-digest) | [`examples/repo-sprint-digest/projectbrief.md`](examples/repo-sprint-digest/projectbrief.md) | [source](https://raw.githubusercontent.com/sasamuku/repo-sprint-digest/main/memory-bank/projectbrief.md) |
| `stream-closed-captioner` | [`talk2MeGooseman/stream-closed-captioner-extension`](https://github.com/talk2MeGooseman/stream-closed-captioner-extension) | [`examples/stream-closed-captioner/projectbrief.md`](examples/stream-closed-captioner/projectbrief.md) | [source](https://raw.githubusercontent.com/talk2MeGooseman/stream-closed-captioner-extension/main/memory-bank/projectbrief.md) |

### `productContext.md`

Problem space and the intended user experience.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `app-med-ai-gen` | [`ModusCreateOrg/app-med-ai-gen`](https://github.com/ModusCreateOrg/app-med-ai-gen) | [`examples/app-med-ai-gen/productContext.md`](examples/app-med-ai-gen/productContext.md) | [source](https://raw.githubusercontent.com/ModusCreateOrg/app-med-ai-gen/main/memory-bank/productContext.md) |
| `aws-sso-manager` | [`cfircoo/aws-sso-manager`](https://github.com/cfircoo/aws-sso-manager) | [`examples/aws-sso-manager/productContext.md`](examples/aws-sso-manager/productContext.md) | [source](https://raw.githubusercontent.com/cfircoo/aws-sso-manager/main/memory-bank/productContext.md) |
| `eloc-control-panel` | [`EDsteve/ELOC-Control-Panel`](https://github.com/EDsteve/ELOC-Control-Panel) | [`examples/eloc-control-panel/productContext.md`](examples/eloc-control-panel/productContext.md) | [source](https://raw.githubusercontent.com/EDsteve/ELOC-Control-Panel/main/memory-bank/productContext.md) |
| `filesystem-mcp` | [`SylphxAI/filesystem-mcp`](https://github.com/SylphxAI/filesystem-mcp) | [`examples/filesystem-mcp/productContext.md`](examples/filesystem-mcp/productContext.md) | [source](https://raw.githubusercontent.com/SylphxAI/filesystem-mcp/main/memory-bank/productContext.md) |
| `gitpod` | [`gitpod-io/gitpod`](https://github.com/gitpod-io/gitpod) | [`examples/gitpod/productContext.md`](examples/gitpod/productContext.md) | [source](https://raw.githubusercontent.com/gitpod-io/gitpod/main/memory-bank/productContext.md) |
| `goose-loadtest` | [`tag1consulting/goose`](https://github.com/tag1consulting/goose) | [`examples/goose-loadtest/productContext.md`](examples/goose-loadtest/productContext.md) | [source](https://raw.githubusercontent.com/tag1consulting/goose/main/memory-bank/productContext.md) |
| `klox` | [`dkopko/klox`](https://github.com/dkopko/klox) | [`examples/klox/productContext.md`](examples/klox/productContext.md) | [source](https://raw.githubusercontent.com/dkopko/klox/master/memory-bank/productContext.md) |
| `parse-efd-fiscal` | [`chapzin/parse-efd-fiscal`](https://github.com/chapzin/parse-efd-fiscal) | [`examples/parse-efd-fiscal/productContext.md`](examples/parse-efd-fiscal/productContext.md) | [source](https://raw.githubusercontent.com/chapzin/parse-efd-fiscal/master/memory-bank/productContext.md) |
| `pure3270` | [`dtg01100/pure3270`](https://github.com/dtg01100/pure3270) | [`examples/pure3270/productContext.md`](examples/pure3270/productContext.md) | [source](https://raw.githubusercontent.com/dtg01100/pure3270/main/memory-bank/productContext.md) |
| `repo-sprint-digest` | [`sasamuku/repo-sprint-digest`](https://github.com/sasamuku/repo-sprint-digest) | [`examples/repo-sprint-digest/productContext.md`](examples/repo-sprint-digest/productContext.md) | [source](https://raw.githubusercontent.com/sasamuku/repo-sprint-digest/main/memory-bank/productContext.md) |
| `stream-closed-captioner` | [`talk2MeGooseman/stream-closed-captioner-extension`](https://github.com/talk2MeGooseman/stream-closed-captioner-extension) | [`examples/stream-closed-captioner/productContext.md`](examples/stream-closed-captioner/productContext.md) | [source](https://raw.githubusercontent.com/talk2MeGooseman/stream-closed-captioner-extension/main/memory-bank/productContext.md) |

### `activeContext.md`

Current focus, recent changes, next steps - the most frequently updated file.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `app-med-ai-gen` | [`ModusCreateOrg/app-med-ai-gen`](https://github.com/ModusCreateOrg/app-med-ai-gen) | [`examples/app-med-ai-gen/activeContext.md`](examples/app-med-ai-gen/activeContext.md) | [source](https://raw.githubusercontent.com/ModusCreateOrg/app-med-ai-gen/main/memory-bank/activeContext.md) |
| `aws-sso-manager` | [`cfircoo/aws-sso-manager`](https://github.com/cfircoo/aws-sso-manager) | [`examples/aws-sso-manager/activeContext.md`](examples/aws-sso-manager/activeContext.md) | [source](https://raw.githubusercontent.com/cfircoo/aws-sso-manager/main/memory-bank/activeContext.md) |
| `eloc-control-panel` | [`EDsteve/ELOC-Control-Panel`](https://github.com/EDsteve/ELOC-Control-Panel) | [`examples/eloc-control-panel/activeContext.md`](examples/eloc-control-panel/activeContext.md) | [source](https://raw.githubusercontent.com/EDsteve/ELOC-Control-Panel/main/memory-bank/activeContext.md) |
| `filesystem-mcp` | [`SylphxAI/filesystem-mcp`](https://github.com/SylphxAI/filesystem-mcp) | [`examples/filesystem-mcp/activeContext.md`](examples/filesystem-mcp/activeContext.md) | [source](https://raw.githubusercontent.com/SylphxAI/filesystem-mcp/main/memory-bank/activeContext.md) |
| `gitpod` | [`gitpod-io/gitpod`](https://github.com/gitpod-io/gitpod) | [`examples/gitpod/activeContext.md`](examples/gitpod/activeContext.md) | [source](https://raw.githubusercontent.com/gitpod-io/gitpod/main/memory-bank/activeContext.md) |
| `goose-loadtest` | [`tag1consulting/goose`](https://github.com/tag1consulting/goose) | [`examples/goose-loadtest/activeContext.md`](examples/goose-loadtest/activeContext.md) | [source](https://raw.githubusercontent.com/tag1consulting/goose/main/memory-bank/activeContext.md) |
| `klox` | [`dkopko/klox`](https://github.com/dkopko/klox) | [`examples/klox/activeContext.md`](examples/klox/activeContext.md) | [source](https://raw.githubusercontent.com/dkopko/klox/master/memory-bank/activeContext.md) |
| `parse-efd-fiscal` | [`chapzin/parse-efd-fiscal`](https://github.com/chapzin/parse-efd-fiscal) | [`examples/parse-efd-fiscal/activeContext.md`](examples/parse-efd-fiscal/activeContext.md) | [source](https://raw.githubusercontent.com/chapzin/parse-efd-fiscal/master/memory-bank/activeContext.md) |
| `pure3270` | [`dtg01100/pure3270`](https://github.com/dtg01100/pure3270) | [`examples/pure3270/activeContext.md`](examples/pure3270/activeContext.md) | [source](https://raw.githubusercontent.com/dtg01100/pure3270/main/memory-bank/activeContext.md) |
| `repo-sprint-digest` | [`sasamuku/repo-sprint-digest`](https://github.com/sasamuku/repo-sprint-digest) | [`examples/repo-sprint-digest/activeContext.md`](examples/repo-sprint-digest/activeContext.md) | [source](https://raw.githubusercontent.com/sasamuku/repo-sprint-digest/main/memory-bank/activeContext.md) |
| `stream-closed-captioner` | [`talk2MeGooseman/stream-closed-captioner-extension`](https://github.com/talk2MeGooseman/stream-closed-captioner-extension) | [`examples/stream-closed-captioner/activeContext.md`](examples/stream-closed-captioner/activeContext.md) | [source](https://raw.githubusercontent.com/talk2MeGooseman/stream-closed-captioner-extension/main/memory-bank/activeContext.md) |

### `systemPatterns.md`

Architecture, key technical decisions, and design patterns.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `app-med-ai-gen` | [`ModusCreateOrg/app-med-ai-gen`](https://github.com/ModusCreateOrg/app-med-ai-gen) | [`examples/app-med-ai-gen/systemPatterns.md`](examples/app-med-ai-gen/systemPatterns.md) | [source](https://raw.githubusercontent.com/ModusCreateOrg/app-med-ai-gen/main/memory-bank/systemPatterns.md) |
| `aws-sso-manager` | [`cfircoo/aws-sso-manager`](https://github.com/cfircoo/aws-sso-manager) | [`examples/aws-sso-manager/systemPatterns.md`](examples/aws-sso-manager/systemPatterns.md) | [source](https://raw.githubusercontent.com/cfircoo/aws-sso-manager/main/memory-bank/systemPatterns.md) |
| `eloc-control-panel` | [`EDsteve/ELOC-Control-Panel`](https://github.com/EDsteve/ELOC-Control-Panel) | [`examples/eloc-control-panel/systemPatterns.md`](examples/eloc-control-panel/systemPatterns.md) | [source](https://raw.githubusercontent.com/EDsteve/ELOC-Control-Panel/main/memory-bank/systemPatterns.md) |
| `filesystem-mcp` | [`SylphxAI/filesystem-mcp`](https://github.com/SylphxAI/filesystem-mcp) | [`examples/filesystem-mcp/systemPatterns.md`](examples/filesystem-mcp/systemPatterns.md) | [source](https://raw.githubusercontent.com/SylphxAI/filesystem-mcp/main/memory-bank/systemPatterns.md) |
| `gitpod` | [`gitpod-io/gitpod`](https://github.com/gitpod-io/gitpod) | [`examples/gitpod/systemPatterns.md`](examples/gitpod/systemPatterns.md) | [source](https://raw.githubusercontent.com/gitpod-io/gitpod/main/memory-bank/systemPatterns.md) |
| `goose-loadtest` | [`tag1consulting/goose`](https://github.com/tag1consulting/goose) | [`examples/goose-loadtest/systemPatterns.md`](examples/goose-loadtest/systemPatterns.md) | [source](https://raw.githubusercontent.com/tag1consulting/goose/main/memory-bank/systemPatterns.md) |
| `klox` | [`dkopko/klox`](https://github.com/dkopko/klox) | [`examples/klox/systemPatterns.md`](examples/klox/systemPatterns.md) | [source](https://raw.githubusercontent.com/dkopko/klox/master/memory-bank/systemPatterns.md) |
| `parse-efd-fiscal` | [`chapzin/parse-efd-fiscal`](https://github.com/chapzin/parse-efd-fiscal) | [`examples/parse-efd-fiscal/systemPatterns.md`](examples/parse-efd-fiscal/systemPatterns.md) | [source](https://raw.githubusercontent.com/chapzin/parse-efd-fiscal/master/memory-bank/systemPatterns.md) |
| `pure3270` | [`dtg01100/pure3270`](https://github.com/dtg01100/pure3270) | [`examples/pure3270/systemPatterns.md`](examples/pure3270/systemPatterns.md) | [source](https://raw.githubusercontent.com/dtg01100/pure3270/main/memory-bank/systemPatterns.md) |
| `repo-sprint-digest` | [`sasamuku/repo-sprint-digest`](https://github.com/sasamuku/repo-sprint-digest) | [`examples/repo-sprint-digest/systemPatterns.md`](examples/repo-sprint-digest/systemPatterns.md) | [source](https://raw.githubusercontent.com/sasamuku/repo-sprint-digest/main/memory-bank/systemPatterns.md) |
| `stream-closed-captioner` | [`talk2MeGooseman/stream-closed-captioner-extension`](https://github.com/talk2MeGooseman/stream-closed-captioner-extension) | [`examples/stream-closed-captioner/systemPatterns.md`](examples/stream-closed-captioner/systemPatterns.md) | [source](https://raw.githubusercontent.com/talk2MeGooseman/stream-closed-captioner-extension/main/memory-bank/systemPatterns.md) |

### `techContext.md`

Technologies, setup, constraints, and dependencies.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `app-med-ai-gen` | [`ModusCreateOrg/app-med-ai-gen`](https://github.com/ModusCreateOrg/app-med-ai-gen) | [`examples/app-med-ai-gen/techContext.md`](examples/app-med-ai-gen/techContext.md) | [source](https://raw.githubusercontent.com/ModusCreateOrg/app-med-ai-gen/main/memory-bank/techContext.md) |
| `aws-sso-manager` | [`cfircoo/aws-sso-manager`](https://github.com/cfircoo/aws-sso-manager) | [`examples/aws-sso-manager/techContext.md`](examples/aws-sso-manager/techContext.md) | [source](https://raw.githubusercontent.com/cfircoo/aws-sso-manager/main/memory-bank/techContext.md) |
| `eloc-control-panel` | [`EDsteve/ELOC-Control-Panel`](https://github.com/EDsteve/ELOC-Control-Panel) | [`examples/eloc-control-panel/techContext.md`](examples/eloc-control-panel/techContext.md) | [source](https://raw.githubusercontent.com/EDsteve/ELOC-Control-Panel/main/memory-bank/techContext.md) |
| `filesystem-mcp` | [`SylphxAI/filesystem-mcp`](https://github.com/SylphxAI/filesystem-mcp) | [`examples/filesystem-mcp/techContext.md`](examples/filesystem-mcp/techContext.md) | [source](https://raw.githubusercontent.com/SylphxAI/filesystem-mcp/main/memory-bank/techContext.md) |
| `gitpod` | [`gitpod-io/gitpod`](https://github.com/gitpod-io/gitpod) | [`examples/gitpod/techContext.md`](examples/gitpod/techContext.md) | [source](https://raw.githubusercontent.com/gitpod-io/gitpod/main/memory-bank/techContext.md) |
| `goose-loadtest` | [`tag1consulting/goose`](https://github.com/tag1consulting/goose) | [`examples/goose-loadtest/techContext.md`](examples/goose-loadtest/techContext.md) | [source](https://raw.githubusercontent.com/tag1consulting/goose/main/memory-bank/techContext.md) |
| `klox` | [`dkopko/klox`](https://github.com/dkopko/klox) | [`examples/klox/techContext.md`](examples/klox/techContext.md) | [source](https://raw.githubusercontent.com/dkopko/klox/master/memory-bank/techContext.md) |
| `parse-efd-fiscal` | [`chapzin/parse-efd-fiscal`](https://github.com/chapzin/parse-efd-fiscal) | [`examples/parse-efd-fiscal/techContext.md`](examples/parse-efd-fiscal/techContext.md) | [source](https://raw.githubusercontent.com/chapzin/parse-efd-fiscal/master/memory-bank/techContext.md) |
| `pure3270` | [`dtg01100/pure3270`](https://github.com/dtg01100/pure3270) | [`examples/pure3270/techContext.md`](examples/pure3270/techContext.md) | [source](https://raw.githubusercontent.com/dtg01100/pure3270/main/memory-bank/techContext.md) |
| `repo-sprint-digest` | [`sasamuku/repo-sprint-digest`](https://github.com/sasamuku/repo-sprint-digest) | [`examples/repo-sprint-digest/techContext.md`](examples/repo-sprint-digest/techContext.md) | [source](https://raw.githubusercontent.com/sasamuku/repo-sprint-digest/main/memory-bank/techContext.md) |
| `stream-closed-captioner` | [`talk2MeGooseman/stream-closed-captioner-extension`](https://github.com/talk2MeGooseman/stream-closed-captioner-extension) | [`examples/stream-closed-captioner/techContext.md`](examples/stream-closed-captioner/techContext.md) | [source](https://raw.githubusercontent.com/talk2MeGooseman/stream-closed-captioner-extension/main/memory-bank/techContext.md) |

### `progress.md`

What works, what's left to build, and known issues.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `app-med-ai-gen` | [`ModusCreateOrg/app-med-ai-gen`](https://github.com/ModusCreateOrg/app-med-ai-gen) | [`examples/app-med-ai-gen/progress.md`](examples/app-med-ai-gen/progress.md) | [source](https://raw.githubusercontent.com/ModusCreateOrg/app-med-ai-gen/main/memory-bank/progress.md) |
| `aws-sso-manager` | [`cfircoo/aws-sso-manager`](https://github.com/cfircoo/aws-sso-manager) | [`examples/aws-sso-manager/progress.md`](examples/aws-sso-manager/progress.md) | [source](https://raw.githubusercontent.com/cfircoo/aws-sso-manager/main/memory-bank/progress.md) |
| `eloc-control-panel` | [`EDsteve/ELOC-Control-Panel`](https://github.com/EDsteve/ELOC-Control-Panel) | [`examples/eloc-control-panel/progress.md`](examples/eloc-control-panel/progress.md) | [source](https://raw.githubusercontent.com/EDsteve/ELOC-Control-Panel/main/memory-bank/progress.md) |
| `filesystem-mcp` | [`SylphxAI/filesystem-mcp`](https://github.com/SylphxAI/filesystem-mcp) | [`examples/filesystem-mcp/progress.md`](examples/filesystem-mcp/progress.md) | [source](https://raw.githubusercontent.com/SylphxAI/filesystem-mcp/main/memory-bank/progress.md) |
| `gitpod` | [`gitpod-io/gitpod`](https://github.com/gitpod-io/gitpod) | [`examples/gitpod/progress.md`](examples/gitpod/progress.md) | [source](https://raw.githubusercontent.com/gitpod-io/gitpod/main/memory-bank/progress.md) |
| `goose-loadtest` | [`tag1consulting/goose`](https://github.com/tag1consulting/goose) | [`examples/goose-loadtest/progress.md`](examples/goose-loadtest/progress.md) | [source](https://raw.githubusercontent.com/tag1consulting/goose/main/memory-bank/progress.md) |
| `klox` | [`dkopko/klox`](https://github.com/dkopko/klox) | [`examples/klox/progress.md`](examples/klox/progress.md) | [source](https://raw.githubusercontent.com/dkopko/klox/master/memory-bank/progress.md) |
| `parse-efd-fiscal` | [`chapzin/parse-efd-fiscal`](https://github.com/chapzin/parse-efd-fiscal) | [`examples/parse-efd-fiscal/progress.md`](examples/parse-efd-fiscal/progress.md) | [source](https://raw.githubusercontent.com/chapzin/parse-efd-fiscal/master/memory-bank/progress.md) |
| `pure3270` | [`dtg01100/pure3270`](https://github.com/dtg01100/pure3270) | [`examples/pure3270/progress.md`](examples/pure3270/progress.md) | [source](https://raw.githubusercontent.com/dtg01100/pure3270/main/memory-bank/progress.md) |
| `repo-sprint-digest` | [`sasamuku/repo-sprint-digest`](https://github.com/sasamuku/repo-sprint-digest) | [`examples/repo-sprint-digest/progress.md`](examples/repo-sprint-digest/progress.md) | [source](https://raw.githubusercontent.com/sasamuku/repo-sprint-digest/main/memory-bank/progress.md) |
| `stream-closed-captioner` | [`talk2MeGooseman/stream-closed-captioner-extension`](https://github.com/talk2MeGooseman/stream-closed-captioner-extension) | [`examples/stream-closed-captioner/progress.md`](examples/stream-closed-captioner/progress.md) | [source](https://raw.githubusercontent.com/talk2MeGooseman/stream-closed-captioner-extension/main/memory-bank/progress.md) |

## Field notes

### Files & flow
Six core files, plus optional extras, in a strict dependency graph:

```
projectbrief  ->  productContext, systemPatterns, techContext  ->  activeContext  ->  progress
```

- **`projectbrief.md`** - foundation / source of truth; core requirements + goals. Should rarely change.
- **`productContext.md`** - why it exists, problems solved, UX goals.
- **`systemPatterns.md`** - architecture, key decisions, component relationships.
- **`techContext.md`** - stack, setup, constraints, dependencies.
- **`activeContext.md`** - current focus, recent changes, next steps; the **most-updated** file.
- **`progress.md`** - what works, what's left, known issues, status.
- **Optional extras** inside `memory-bank/` are explicitly allowed: extra files/folders for complex features, integrations, API docs, testing strategy, deployment.

**Workflow:** the phrases `initialize memory bank`, `update memory bank` (triggers a full review of *all* files), and `follow your custom instructions` (resume); plus **Plan Mode** (reads the bank, proposes a strategy, can't edit) vs **Act Mode** (executes and documents).

### Composition
- The files run stable -> volatile: `projectbrief` is the root; the three middle files build on it; `activeContext` carries Current Work Focus -> Recent Changes -> Next Steps; `progress` tracks what works and what's left.

### Anti-patterns
- Letting `activeContext.md` decay into a human changelog - current *state* is more useful to an agent than release-note prose.
- Files that contradict each other after an update (the brief says X, techContext says Y).
- Not running `update memory bank` at the end of a task - the next session then reconstructs stale context.

### Edge cases
- The whole premise is **memory reset**: each file must stand on its own because the agent re-reads the bank cold every task.
- `projectbrief.md` should rarely change; `activeContext.md` / `progress.md` are the churn files. Mixing those cadences in one file defeats the structure.

### Adoption / maturity
- Memory Bank is a Cline-documented pattern, not a generic Markdown folder convention. Roo Code and Cursor users commonly reuse it through custom instructions, but the canonical shape and commands come from Cline.
- Because the files are version-controlled, the bank is more auditable than local auto-memory, but also easier to pollute with transient notes unless `update memory bank` is treated like a review step.

### Related conventions
- Use `MEMORY.md` for local agent recall that should not be committed.
- Use AGENTS.md or tool-specific instruction files for rules that must always steer implementation, rather than for historical state.

### Sources checked
- [Cline Memory Bank docs](https://docs.cline.bot/best-practices/memory-bank)
- [Gitpod Memory Bank examples](https://github.com/gitpod-io/gitpod/tree/main/memory-bank)
