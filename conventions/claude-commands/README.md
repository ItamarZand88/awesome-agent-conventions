# Claude Code commands 🟢 Adopted

> A Markdown file Claude Code exposes as a /slash-command - a reusable, version-controlled prompt workflow, with optional frontmatter (allowed-tools, model, argument-hint) and $ARGUMENTS and shell placeholders (@file references are a general Claude Code prompt feature, not command-specific). Now converging with Agent Skills, but still widely committed in its own right.

- **Read by:** Claude Code - project .claude/commands/ and user ~/.claude/commands/
- **Location:** .claude/commands/*.md (project) and ~/.claude/commands/*.md (user)
- **Spec:** [https://code.claude.com/docs/en/slash-commands](https://code.claude.com/docs/en/slash-commands)
- **Evidence:** Claude Code slash-command docs define .claude/commands/*.md, and active repos commit reusable command files.
- **Last verified:** 2026-06-26
- **Files:** `.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `.md`

Any Markdown file under .claude/commands/; the filename is the command name (pr.md -> /pr). Optional YAML frontmatter: description, argument-hint, allowed-tools, model.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `ai-config-commit` | [`aspiers/ai-config`](https://github.com/aspiers/ai-config) | [`examples/ai-config-commit/commit.md`](examples/ai-config-commit/commit.md) | [source](https://raw.githubusercontent.com/aspiers/ai-config/main/.claude/commands/commit.md) |
| `ai-config-pr-desc` | [`aspiers/ai-config`](https://github.com/aspiers/ai-config) | [`examples/ai-config-pr-desc/pr-desc.md`](examples/ai-config-pr-desc/pr-desc.md) | [source](https://raw.githubusercontent.com/aspiers/ai-config/main/.claude/commands/pr-desc.md) |
| `ai-config-review` | [`aspiers/ai-config`](https://github.com/aspiers/ai-config) | [`examples/ai-config-review/review.md`](examples/ai-config-review/review.md) | [source](https://raw.githubusercontent.com/aspiers/ai-config/main/.claude/commands/review.md) |
| `anthropics-triage-issue` | [`anthropics/claude-code`](https://github.com/anthropics/claude-code) | [`examples/anthropics-triage-issue/triage-issue.md`](examples/anthropics-triage-issue/triage-issue.md) | [source](https://raw.githubusercontent.com/anthropics/claude-code/main/.claude/commands/triage-issue.md) |
| `bikeindex-pr` | [`bikeindex/bike_index`](https://github.com/bikeindex/bike_index) | [`examples/bikeindex-pr/pr.md`](examples/bikeindex-pr/pr.md) | [source](https://raw.githubusercontent.com/bikeindex/bike_index/main/.claude/commands/pr.md) |
| `claude-code` | [`anthropics/claude-code`](https://github.com/anthropics/claude-code) | [`examples/claude-code/commit-push-pr.md`](examples/claude-code/commit-push-pr.md) | [source](https://raw.githubusercontent.com/anthropics/claude-code/main/.claude/commands/commit-push-pr.md) |
| `claude-code` | [`anthropics/claude-code`](https://github.com/anthropics/claude-code) | [`examples/claude-code/dedupe.md`](examples/claude-code/dedupe.md) | [source](https://raw.githubusercontent.com/anthropics/claude-code/main/.claude/commands/dedupe.md) |
| `eventsourcing-commit-beads` | [`CodeForBreakfast/eventsourcing`](https://github.com/CodeForBreakfast/eventsourcing) | [`examples/eventsourcing-commit-beads/commit-beads.md`](examples/eventsourcing-commit-beads/commit-beads.md) | [source](https://raw.githubusercontent.com/CodeForBreakfast/eventsourcing/main/.claude/commands/commit-beads.md) |
| `fantomas-format` | [`fsprojects/fantomas`](https://github.com/fsprojects/fantomas) | [`examples/fantomas-format/format.md`](examples/fantomas-format/format.md) | [source](https://raw.githubusercontent.com/fsprojects/fantomas/main/.claude/commands/format.md) |
| `fantomas-oak` | [`fsprojects/fantomas`](https://github.com/fsprojects/fantomas) | [`examples/fantomas-oak/oak.md`](examples/fantomas-oak/oak.md) | [source](https://raw.githubusercontent.com/fsprojects/fantomas/main/.claude/commands/oak.md) |
| `hydra-bootstrap` | [`CategoricalData/hydra`](https://github.com/CategoricalData/hydra) | [`examples/hydra-bootstrap/bootstrap.md`](examples/hydra-bootstrap/bootstrap.md) | [source](https://raw.githubusercontent.com/CategoricalData/hydra/main/.claude/commands/bootstrap.md) |
| `hydra-improve-docs` | [`CategoricalData/hydra`](https://github.com/CategoricalData/hydra) | [`examples/hydra-improve-docs/improve-docs.md`](examples/hydra-improve-docs/improve-docs.md) | [source](https://raw.githubusercontent.com/CategoricalData/hydra/main/.claude/commands/improve-docs.md) |
| `hydra-lexicon` | [`CategoricalData/hydra`](https://github.com/CategoricalData/hydra) | [`examples/hydra-lexicon/lexicon.md`](examples/hydra-lexicon/lexicon.md) | [source](https://raw.githubusercontent.com/CategoricalData/hydra/main/.claude/commands/lexicon.md) |
| `marigold-create-component` | [`marigold-ui/marigold`](https://github.com/marigold-ui/marigold) | [`examples/marigold-create-component/create-component.md`](examples/marigold-create-component/create-component.md) | [source](https://raw.githubusercontent.com/marigold-ui/marigold/main/.claude/commands/create-component.md) |
| `marigold-vrt` | [`marigold-ui/marigold`](https://github.com/marigold-ui/marigold) | [`examples/marigold-vrt/vrt.md`](examples/marigold-vrt/vrt.md) | [source](https://raw.githubusercontent.com/marigold-ui/marigold/main/.claude/commands/vrt.md) |
| `modelchecker-implement` | [`benbrastmckie/ModelChecker`](https://github.com/benbrastmckie/ModelChecker) | [`examples/modelchecker-implement/implement.md`](examples/modelchecker-implement/implement.md) | [source](https://raw.githubusercontent.com/benbrastmckie/ModelChecker/master/.claude/commands/implement.md) |
| `sentry-gh-review` | [`getsentry/sentry`](https://github.com/getsentry/sentry) | [`examples/sentry-gh-review/gh-review.md`](examples/sentry-gh-review/gh-review.md) | [source](https://raw.githubusercontent.com/getsentry/sentry/master/.claude/commands/gh-review.md) |
| `sentry-setup-dev` | [`getsentry/sentry`](https://github.com/getsentry/sentry) | [`examples/sentry-setup-dev/setup-dev.md`](examples/sentry-setup-dev/setup-dev.md) | [source](https://raw.githubusercontent.com/getsentry/sentry/master/.claude/commands/setup-dev.md) |
| `sentry` | [`getsentry/sentry`](https://github.com/getsentry/sentry) | [`examples/sentry/gh-pr.md`](examples/sentry/gh-pr.md) | [source](https://raw.githubusercontent.com/getsentry/sentry/master/.claude/commands/gh-pr.md) |
| `sidekiq-unique-jobs-review-pr` | [`mhenrixon/sidekiq-unique-jobs`](https://github.com/mhenrixon/sidekiq-unique-jobs) | [`examples/sidekiq-unique-jobs-review-pr/review-pr.md`](examples/sidekiq-unique-jobs-review-pr/review-pr.md) | [source](https://raw.githubusercontent.com/mhenrixon/sidekiq-unique-jobs/main/.claude/commands/review-pr.md) |
| `sidekiq-unique-jobs-security` | [`mhenrixon/sidekiq-unique-jobs`](https://github.com/mhenrixon/sidekiq-unique-jobs) | [`examples/sidekiq-unique-jobs-security/security.md`](examples/sidekiq-unique-jobs-security/security.md) | [source](https://raw.githubusercontent.com/mhenrixon/sidekiq-unique-jobs/main/.claude/commands/security.md) |
| `sidekiq-unique-jobs-tdd` | [`mhenrixon/sidekiq-unique-jobs`](https://github.com/mhenrixon/sidekiq-unique-jobs) | [`examples/sidekiq-unique-jobs-tdd/tdd.md`](examples/sidekiq-unique-jobs-tdd/tdd.md) | [source](https://raw.githubusercontent.com/mhenrixon/sidekiq-unique-jobs/main/.claude/commands/tdd.md) |

## Field notes

### Fields (frontmatter)
Commands now share the full Skills frontmatter (all optional):

| Field | Notes |
| --- | --- |
| `description` | shown in the `/` menu; defaults to the first body paragraph |
| `argument-hint` | autocomplete hint, e.g. `[issue-number]` |
| `arguments` | named positional args (space-separated or YAML list) for `$name` substitution |
| `allowed-tools` / `disallowed-tools` | tool allow/deny list; `disallowed-tools` clears on the next message |
| `model` | a `/model` value or `inherit` |
| `effort` | `low` / `medium` / `high` / `xhigh` / `max` |
| `disable-model-invocation` | `true` = only the user can run it (default `false`) |
| `user-invocable` | `false` hides it from the `/` menu (default `true`) |
| `context: fork` + `agent` | run the command in a forked subagent (`Explore`/`Plan`/`general-purpose`/custom) |
| `hooks` | lifecycle hooks |
| `paths` | restrict auto-activation to matching file globs |
| `shell` | `bash` / `powershell` for `` !`cmd` `` injection |

**Body placeholders:** `$ARGUMENTS`; `$N` (**0-based** - `$0` is the first arg) and `$ARGUMENTS[N]`; `$name` (declared via `arguments`); `${CLAUDE_SESSION_ID}`, `${CLAUDE_EFFORT}`, `${CLAUDE_SKILL_DIR}`; `` !`cmd` `` (and ` ```! ` fenced blocks) to inline shell output before the model reads the prompt; `@file` references; `\$` to escape.

### Composition
- **Frontmatter pins the tools.** Real files lock `allowed-tools` to a narrow shell allowlist (e.g. `Bash(git add *)`, `Bash(git commit *)`) so the workflow runs without a per-call approval prompt - the main reason teams commit these into the repo.
- **Dynamic context injection is the killer feature.** `` !`git diff` `` runs the shell command and inlines its *output* before Claude reads the prompt, grounding the workflow in live repo state rather than guesses.

### Anti-patterns
- Side-effectful commands (`/deploy`, `/commit`) without `disable-model-invocation: true` - Claude may auto-trigger them when the code "looks ready."
- Re-stating what a skill already does. Since commands now merge into skills, keep one home per capability.

### Edge cases
- **Commands merged into skills.** `.claude/commands/deploy.md` and `.claude/skills/deploy/SKILL.md` both create `/deploy`; if both exist, the skill wins. Treat `commands/*.md` as the legacy single-file form and `SKILL.md` as the successor (it adds a supporting-file directory plus auto-invocation).
- **Discovery is bounded.** Commands load only from the starting directory up to the repo root, plus `~/.claude/commands/` - not from `--add-dir` paths (skills are the exception). The `disableSkillShellExecution` setting neutralizes `` !`cmd` ``.
- `!` is recognized only at line start or after whitespace, so `KEY=!`cmd`` is left as literal text.

### Adoption / maturity
- Claude command files are adopted because many repos already committed them, but Claude Code now describes custom commands as part of the Skills surface. That makes `.claude/commands/*.md` a legacy-compatible single-file form rather than the preferred home for complex workflows.
- Dynamic shell injection is powerful but high-risk: it should be paired with narrow `allowed-tools`, explicit arguments, and `disable-model-invocation` for side-effectful flows.

### Related conventions
- Prefer `SKILL.md` when a command needs support files, scripts, references, or automatic model invocation.
- Prefer AGENTS.md / CLAUDE.md for standing project facts; command files are for tasks the user intentionally invokes.

### Sources checked
- [Claude Code skills and custom commands docs](https://code.claude.com/docs/en/slash-commands)
- [Claude Code command examples](https://github.com/anthropics/claude-code/tree/main/.claude/commands)
