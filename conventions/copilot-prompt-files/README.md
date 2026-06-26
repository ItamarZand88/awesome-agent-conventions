# Copilot prompt & instruction files 🟢 Adopted

> Modular, path-scoped Copilot context: *.instructions.md auto-attach to matching files via an applyTo glob, while *.prompt.md are reusable prompts you invoke by name - the granular cousins of a single .github/copilot-instructions.md.

- **Read by:** GitHub Copilot in VS Code / Copilot CLI
- **Location:** .github/prompts/*.prompt.md and .github/instructions/*.instructions.md
- **Spec:** [https://code.visualstudio.com/docs/agent-customization/prompt-files](https://code.visualstudio.com/docs/agent-customization/prompt-files)
- **Evidence:** VS Code Copilot docs define .github/prompts/*.prompt.md and .github/instructions/*.instructions.md, with public examples in GitHub repos.
- **Last verified:** 2026-06-26
- **Files:** `.prompt.md`, `.instructions.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `.prompt.md`

Invokable saved prompts under .github/prompts/, run as a slash-command.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `azure-search-openai-review-pr-comments` | [`Azure-Samples/azure-search-openai-demo`](https://github.com/Azure-Samples/azure-search-openai-demo) | [`examples/azure-search-openai-review-pr-comments/review_pr_comments.prompt.md`](examples/azure-search-openai-review-pr-comments/review_pr_comments.prompt.md) | [source](https://raw.githubusercontent.com/Azure-Samples/azure-search-openai-demo/main/.github/prompts/review_pr_comments.prompt.md) |
| `dotnet-docs-editing-fullpass` | [`dotnet/docs`](https://github.com/dotnet/docs) | [`examples/dotnet-docs-editing-fullpass/Editing.FullPass.prompt.md`](examples/dotnet-docs-editing-fullpass/Editing.FullPass.prompt.md) | [source](https://raw.githubusercontent.com/dotnet/docs/main/.github/prompts/Editing.FullPass.prompt.md) |
| `dotnet-docs-merge-article` | [`dotnet/docs`](https://github.com/dotnet/docs) | [`examples/dotnet-docs-merge-article/Merge.Article.prompt.md`](examples/dotnet-docs-merge-article/Merge.Article.prompt.md) | [source](https://raw.githubusercontent.com/dotnet/docs/main/.github/prompts/Merge.Article.prompt.md) |
| `dotnet-docs-refresh-links` | [`dotnet/docs`](https://github.com/dotnet/docs) | [`examples/dotnet-docs-refresh-links/RefreshLinks.prompt.md`](examples/dotnet-docs-refresh-links/RefreshLinks.prompt.md) | [source](https://raw.githubusercontent.com/dotnet/docs/main/.github/prompts/RefreshLinks.prompt.md) |
| `dotnet-docs-snippets-migrate` | [`dotnet/docs`](https://github.com/dotnet/docs) | [`examples/dotnet-docs-snippets-migrate/Snippets.Migrate.prompt.md`](examples/dotnet-docs-snippets-migrate/Snippets.Migrate.prompt.md) | [source](https://raw.githubusercontent.com/dotnet/docs/main/.github/prompts/Snippets.Migrate.prompt.md) |
| `edge-ai-deploy` | [`microsoft/edge-ai`](https://github.com/microsoft/edge-ai) | [`examples/edge-ai-deploy/deploy.prompt.md`](examples/edge-ai-deploy/deploy.prompt.md) | [source](https://raw.githubusercontent.com/microsoft/edge-ai/main/.github/prompts/deploy.prompt.md) |
| `edge-ai-getting-started` | [`microsoft/edge-ai`](https://github.com/microsoft/edge-ai) | [`examples/edge-ai-getting-started/getting-started.prompt.md`](examples/edge-ai-getting-started/getting-started.prompt.md) | [source](https://raw.githubusercontent.com/microsoft/edge-ai/main/.github/prompts/getting-started.prompt.md) |
| `edge-ai-project-planning` | [`microsoft/edge-ai`](https://github.com/microsoft/edge-ai) | [`examples/edge-ai-project-planning/edge-ai-project-planning.prompt.md`](examples/edge-ai-project-planning/edge-ai-project-planning.prompt.md) | [source](https://raw.githubusercontent.com/microsoft/edge-ai/main/.github/prompts/edge-ai-project-planning.prompt.md) |
| `edge-ai-terraform-from-blueprint` | [`microsoft/edge-ai`](https://github.com/microsoft/edge-ai) | [`examples/edge-ai-terraform-from-blueprint/terraform-from-blueprint.prompt.md`](examples/edge-ai-terraform-from-blueprint/terraform-from-blueprint.prompt.md) | [source](https://raw.githubusercontent.com/microsoft/edge-ai/main/.github/prompts/terraform-from-blueprint.prompt.md) |
| `playwright-movies-fix` | [`debs-obrien/playwright-movies-app`](https://github.com/debs-obrien/playwright-movies-app) | [`examples/playwright-movies-fix/fix.prompt.md`](examples/playwright-movies-fix/fix.prompt.md) | [source](https://raw.githubusercontent.com/debs-obrien/playwright-movies-app/main/.github/prompts/fix.prompt.md) |
| `playwright-movies-plan` | [`debs-obrien/playwright-movies-app`](https://github.com/debs-obrien/playwright-movies-app) | [`examples/playwright-movies-plan/plan.prompt.md`](examples/playwright-movies-plan/plan.prompt.md) | [source](https://raw.githubusercontent.com/debs-obrien/playwright-movies-app/main/.github/prompts/plan.prompt.md) |
| `playwright-movies` | [`debs-obrien/playwright-movies-app`](https://github.com/debs-obrien/playwright-movies-app) | [`examples/playwright-movies/generate.prompt.md`](examples/playwright-movies/generate.prompt.md) | [source](https://raw.githubusercontent.com/debs-obrien/playwright-movies-app/main/.github/prompts/generate.prompt.md) |

### `.instructions.md`

Auto-attached instructions under .github/instructions/, scoped by an applyTo glob in frontmatter.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `awesome-copilot-ansible` | [`github/awesome-copilot`](https://github.com/github/awesome-copilot) | [`examples/awesome-copilot-ansible/ansible.instructions.md`](examples/awesome-copilot-ansible/ansible.instructions.md) | [source](https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/ansible.instructions.md) |
| `awesome-copilot-bicep-best-practices` | [`github/awesome-copilot`](https://github.com/github/awesome-copilot) | [`examples/awesome-copilot-bicep-best-practices/bicep-code-best-practices.instructions.md`](examples/awesome-copilot-bicep-best-practices/bicep-code-best-practices.instructions.md) | [source](https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/bicep-code-best-practices.instructions.md) |
| `awesome-copilot-csharp` | [`github/awesome-copilot`](https://github.com/github/awesome-copilot) | [`examples/awesome-copilot-csharp/csharp.instructions.md`](examples/awesome-copilot-csharp/csharp.instructions.md) | [source](https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/csharp.instructions.md) |
| `awesome-copilot-docker-best-practices` | [`github/awesome-copilot`](https://github.com/github/awesome-copilot) | [`examples/awesome-copilot-docker-best-practices/containerization-docker-best-practices.instructions.md`](examples/awesome-copilot-docker-best-practices/containerization-docker-best-practices.instructions.md) | [source](https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/containerization-docker-best-practices.instructions.md) |
| `awesome-copilot-github-actions-cicd` | [`github/awesome-copilot`](https://github.com/github/awesome-copilot) | [`examples/awesome-copilot-github-actions-cicd/github-actions-ci-cd-best-practices.instructions.md`](examples/awesome-copilot-github-actions-cicd/github-actions-ci-cd-best-practices.instructions.md) | [source](https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/github-actions-ci-cd-best-practices.instructions.md) |
| `awesome-copilot-go` | [`github/awesome-copilot`](https://github.com/github/awesome-copilot) | [`examples/awesome-copilot-go/go.instructions.md`](examples/awesome-copilot-go/go.instructions.md) | [source](https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/go.instructions.md) |
| `awesome-copilot-kubernetes-deployment` | [`github/awesome-copilot`](https://github.com/github/awesome-copilot) | [`examples/awesome-copilot-kubernetes-deployment/kubernetes-deployment-best-practices.instructions.md`](examples/awesome-copilot-kubernetes-deployment/kubernetes-deployment-best-practices.instructions.md) | [source](https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/kubernetes-deployment-best-practices.instructions.md) |
| `awesome-copilot-markdown` | [`github/awesome-copilot`](https://github.com/github/awesome-copilot) | [`examples/awesome-copilot-markdown/markdown.instructions.md`](examples/awesome-copilot-markdown/markdown.instructions.md) | [source](https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/markdown.instructions.md) |
| `awesome-copilot-ms-sql-dba` | [`github/awesome-copilot`](https://github.com/github/awesome-copilot) | [`examples/awesome-copilot-ms-sql-dba/ms-sql-dba.instructions.md`](examples/awesome-copilot-ms-sql-dba/ms-sql-dba.instructions.md) | [source](https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/ms-sql-dba.instructions.md) |
| `awesome-copilot-nestjs` | [`github/awesome-copilot`](https://github.com/github/awesome-copilot) | [`examples/awesome-copilot-nestjs/nestjs.instructions.md`](examples/awesome-copilot-nestjs/nestjs.instructions.md) | [source](https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/nestjs.instructions.md) |
| `awesome-copilot-nextjs` | [`github/awesome-copilot`](https://github.com/github/awesome-copilot) | [`examples/awesome-copilot-nextjs/nextjs.instructions.md`](examples/awesome-copilot-nextjs/nextjs.instructions.md) | [source](https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/nextjs.instructions.md) |
| `awesome-copilot-object-calisthenics` | [`github/awesome-copilot`](https://github.com/github/awesome-copilot) | [`examples/awesome-copilot-object-calisthenics/object-calisthenics.instructions.md`](examples/awesome-copilot-object-calisthenics/object-calisthenics.instructions.md) | [source](https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/object-calisthenics.instructions.md) |
| `awesome-copilot` | [`github/awesome-copilot`](https://github.com/github/awesome-copilot) | [`examples/awesome-copilot/a11y.instructions.md`](examples/awesome-copilot/a11y.instructions.md) | [source](https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/a11y.instructions.md) |

## Field notes

### Fields (frontmatter)
**`*.prompt.md`** (invokable saved prompts; all optional):

| Field | Notes |
| --- | --- |
| `description` | short description of the prompt |
| `name` | name shown after typing `/` (defaults to the filename) |
| `argument-hint` | hint text in the chat input |
| `agent` | `ask` / `agent` / `plan` or a custom agent (this is the current name; `mode` is the legacy alias) |
| `model` | model identifier (defaults to the selected model) |
| `tools` | tool/toolset names, MCP tools, or `<server>/*` |

**`*.instructions.md`** (auto-attached instructions; all optional):

| Field | Notes |
| --- | --- |
| `applyTo` | glob(s) deciding which files auto-attach the instructions; `**` = all files |
| `description` | hover text in the Chat view |
| `name` | display name in the UI (defaults to the filename) |

**Prompt-body variables:** `${input:name}` / `${input:name:placeholder}`, `${selection}`, `${selectedText}`, `${file}`, `${fileBasename}`, `${workspaceFolder}`, `${workspaceFolderBasename}`; `#tool:<name>` tool references; Markdown relative-path links for file references.

### Composition
- **`*.instructions.md` lead with an `applyTo` glob** (e.g. `applyTo: "**/*.ts"`) plus a `description`. Every file matching the glob silently stacks its instructions into context when Copilot edits a match - path-scoped, automatic.
- **`*.prompt.md` are invoked by name** (slash-command style) and read like a saved task.

### Anti-patterns
- A broad `applyTo: "**"` instruction file that attaches everywhere - that re-creates the always-on token cost the granular format was meant to avoid.
- Copying the monolithic `.github/copilot-instructions.md` into many files without actually scoping them. Scoping is the whole point.

### Edge cases
- **Default locations are settled:** `.github/prompts/` and `.github/instructions/` (searched recursively), configurable via the `chat.promptFilesLocations` / `chat.instructionsFilesLocations` settings. VS Code can also read Claude-format `.claude/rules/`.
- `mode` was renamed to `agent` (values `ask`/`agent`/`plan`); older files still use `mode: agent`/`edit`.
- Largely VS Code / Copilot territory: other tools read the single `.github/copilot-instructions.md` but don't all honor the modular `.prompt.md` / `.instructions.md` split.

### Adoption / maturity
- Copilot prompt and instruction files are official VS Code / Copilot agent customization files. Prompt files are manual slash-command style workflows; instruction files are automatically attached based on glob scope.
- The `tools` list is resolved with priority: prompt-file tools, then tools from the referenced custom agent, then default selected-agent tools. That makes prompt files a useful way to intentionally narrow or broaden tool access for one workflow.

### Related conventions
- `.github/copilot-instructions.md` is the monolithic repo-level form; `.github/instructions/*.instructions.md` is the scoped form.
- Use `SKILL.md` rather than `*.prompt.md` when the workflow should be portable beyond VS Code and can carry supporting files.

### Sources checked
- [VS Code prompt files docs](https://code.visualstudio.com/docs/agent-customization/prompt-files)
- [VS Code custom instructions docs](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [GitHub Awesome Copilot examples](https://github.com/github/awesome-copilot)
