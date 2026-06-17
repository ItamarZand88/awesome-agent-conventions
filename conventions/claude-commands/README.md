# Claude Code commands 🟢 Adopted

> A Markdown file Claude Code exposes as a /slash-command - a reusable, version-controlled prompt workflow, with optional frontmatter (allowed-tools, model, argument-hint) and $ARGUMENTS / shell / @file placeholders. Now converging with Agent Skills, but still widely committed in its own right.

- **Read by:** Claude Code - project .claude/commands/ and user ~/.claude/commands/
- **Location:** .claude/commands/*.md (project) and ~/.claude/commands/*.md (user)
- **Spec:** [https://code.claude.com/docs/en/slash-commands](https://code.claude.com/docs/en/slash-commands)
- **Files:** `.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `.md`

Any Markdown file under .claude/commands/; the filename is the command name (pr.md -> /pr). Optional YAML frontmatter: description, argument-hint, allowed-tools, model.

| Source | File | Provenance |
| --- | --- | --- |
| `marigold` | [`marigold.vrt.md`](examples/marigold.vrt.md) | [source](https://raw.githubusercontent.com/marigold-ui/marigold/main/.claude/commands/vrt.md) |
| `tunarr` | [`tunarr.pr.md`](examples/tunarr.pr.md) | [source](https://raw.githubusercontent.com/chrisbenincasa/tunarr/main/.claude/commands/pr.md) |

## Field notes

### Composition
- **Frontmatter pins the tools.** Real files lock `allowed-tools` to a narrow shell allowlist (e.g. `Bash(git add *)`, `Bash(git commit *)`) so the workflow runs without a per-call approval prompt - the main reason teams commit these into the repo.
- **Dynamic context injection is the killer feature.** `` !`git diff` `` runs the shell command and inlines its *output* before Claude reads the prompt, grounding the workflow in live repo state rather than guesses. `$ARGUMENTS` / `$1` substitute user input; `@path` pulls files in.

### Anti-patterns
- Side-effectful commands (`/deploy`, `/commit`) without `disable-model-invocation: true` - Claude may auto-trigger them when the code "looks ready."
- Re-stating what a skill already does. Since commands now merge into skills, keep one home per capability.

### Edge cases
- **Commands merged into skills.** `.claude/commands/deploy.md` and `.claude/skills/deploy/SKILL.md` both create `/deploy`; if both exist, the skill wins. Treat `commands/*.md` as the legacy single-file form and `SKILL.md` as the successor (it adds a supporting-file directory plus auto-invocation).
- **Discovery is bounded.** Commands load only from the starting directory up to the repo root, plus `~/.claude/commands/` - not from `--add-dir` paths.
- `!` is recognized only at line start or after whitespace, so `KEY=!`cmd`` is left as literal text.
