# Rules files 🟢 Adopted

> Per-tool rule files that scope agent behavior - older single-file forms (.cursorrules, .clinerules, .windsurfrules) and newer directory-based, glob-scoped forms (.cursor/rules/*.mdc, .clinerules/, .windsurf/rules/*.md).

- **Read by:** Cursor (.cursorrules / .mdc), Cline (.clinerules/ and legacy .clinerules), Windsurf (.windsurfrules)
- **Location:** Repo root, or a rules directory (.cursor/rules/*.mdc, .clinerules/, .windsurf/rules/*.md)
- **Spec:** [https://docs.cline.bot/customization/cline-rules](https://docs.cline.bot/customization/cline-rules)
- **Evidence:** Cursor, Cline, and Windsurf document and/or detect project rule files, including both legacy single files and directory-based rules.
- **Last verified:** 2026-06-26
- **Files:** `.cursorrules`, `.mdc`, `.clinerules`, `.clinerules/`, `.windsurfrules`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `.cursorrules`

Cursor - legacy single-file form (superseded by .cursor/rules/*.mdc).

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `devin` | [`grapeot/devin.cursorrules`](https://github.com/grapeot/devin.cursorrules) | [`examples/devin/.cursorrules`](examples/devin/.cursorrules) | [source](https://raw.githubusercontent.com/grapeot/devin.cursorrules/master/.cursorrules) |

### `.mdc`

Cursor - modern rule file with frontmatter and glob scoping, under .cursor/rules/.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `awesome-cursorrules-android-compose` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-android-compose/android-jetpack-compose-cursorrules-prompt-file.mdc`](examples/awesome-cursorrules-android-compose/android-jetpack-compose-cursorrules-prompt-file.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/android-jetpack-compose-cursorrules-prompt-file.mdc) |
| `awesome-cursorrules-blender-python` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-blender-python/blender-python-addon.mdc`](examples/awesome-cursorrules-blender-python/blender-python-addon.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/blender-python-addon.mdc) |
| `awesome-cursorrules-clean-code` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-clean-code/clean-code.mdc`](examples/awesome-cursorrules-clean-code/clean-code.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/clean-code.mdc) |
| `awesome-cursorrules-cpp` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-cpp/cpp.mdc`](examples/awesome-cursorrules-cpp/cpp.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/cpp.mdc) |
| `awesome-cursorrules-database` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-database/database.mdc`](examples/awesome-cursorrules-database/database.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/database.mdc) |
| `awesome-cursorrules-docker` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-docker/docker.mdc`](examples/awesome-cursorrules-docker/docker.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/docker.mdc) |
| `awesome-cursorrules-fastapi` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-fastapi/fastapi.mdc`](examples/awesome-cursorrules-fastapi/fastapi.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/fastapi.mdc) |
| `awesome-cursorrules-flutter` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-flutter/flutter-app-expert-cursorrules-prompt-file.mdc`](examples/awesome-cursorrules-flutter/flutter-app-expert-cursorrules-prompt-file.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/flutter-app-expert-cursorrules-prompt-file.mdc) |
| `awesome-cursorrules-fortran` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-fortran/fortran.mdc`](examples/awesome-cursorrules-fortran/fortran.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/fortran.mdc) |
| `awesome-cursorrules-gitflow` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-gitflow/gitflow.mdc`](examples/awesome-cursorrules-gitflow/gitflow.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/gitflow.mdc) |
| `awesome-cursorrules-go-backend-scalability` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-go-backend-scalability/go-backend-scalability-cursorrules-prompt-file.mdc`](examples/awesome-cursorrules-go-backend-scalability/go-backend-scalability-cursorrules-prompt-file.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/go-backend-scalability-cursorrules-prompt-file.mdc) |
| `awesome-cursorrules-go` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-go/go.mdc`](examples/awesome-cursorrules-go/go.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/go.mdc) |
| `awesome-cursorrules-java-springboot` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-java-springboot/java-springboot-jpa-cursorrules-prompt-file.mdc`](examples/awesome-cursorrules-java-springboot/java-springboot-jpa-cursorrules-prompt-file.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/java-springboot-jpa-cursorrules-prompt-file.mdc) |
| `awesome-cursorrules-kotlin-ktor` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-kotlin-ktor/kotlin-ktor-development-cursorrules-prompt-file.mdc`](examples/awesome-cursorrules-kotlin-ktor/kotlin-ktor-development-cursorrules-prompt-file.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/kotlin-ktor-development-cursorrules-prompt-file.mdc) |
| `awesome-cursorrules-laravel-php` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-laravel-php/laravel-php-83-cursorrules-prompt-file.mdc`](examples/awesome-cursorrules-laravel-php/laravel-php-83-cursorrules-prompt-file.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/laravel-php-83-cursorrules-prompt-file.mdc) |
| `awesome-cursorrules-nextjs` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-nextjs/nextjs.mdc`](examples/awesome-cursorrules-nextjs/nextjs.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/nextjs.mdc) |
| `awesome-cursorrules-node-express` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-node-express/node-express.mdc`](examples/awesome-cursorrules-node-express/node-express.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/node-express.mdc) |
| `awesome-cursorrules-postgresql` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-postgresql/postgresql.mdc`](examples/awesome-cursorrules-postgresql/postgresql.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/postgresql.mdc) |
| `awesome-cursorrules-python` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-python/python.mdc`](examples/awesome-cursorrules-python/python.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/python.mdc) |
| `awesome-cursorrules-rails` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-rails/rails-cursorrules-prompt-file.mdc`](examples/awesome-cursorrules-rails/rails-cursorrules-prompt-file.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/rails-cursorrules-prompt-file.mdc) |
| `awesome-cursorrules-react` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-react/react.mdc`](examples/awesome-cursorrules-react/react.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/react.mdc) |
| `awesome-cursorrules-rust` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-rust/rust.mdc`](examples/awesome-cursorrules-rust/rust.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/rust.mdc) |
| `awesome-cursorrules-solidity-foundry` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-solidity-foundry/solidity-foundry-cursorrules-prompt-file.mdc`](examples/awesome-cursorrules-solidity-foundry/solidity-foundry-cursorrules-prompt-file.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/solidity-foundry-cursorrules-prompt-file.mdc) |
| `awesome-cursorrules-svelte` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-svelte/svelte.mdc`](examples/awesome-cursorrules-svelte/svelte.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/svelte.mdc) |
| `awesome-cursorrules-swiftui` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules-swiftui/swiftui-guidelines-cursorrules-prompt-file.mdc`](examples/awesome-cursorrules-swiftui/swiftui-guidelines-cursorrules-prompt-file.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/swiftui-guidelines-cursorrules-prompt-file.mdc) |
| `awesome-cursorrules` | [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) | [`examples/awesome-cursorrules/angular-typescript-cursorrules-prompt-file.mdc`](examples/awesome-cursorrules/angular-typescript-cursorrules-prompt-file.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/angular-typescript-cursorrules-prompt-file.mdc) |

### `.clinerules`

Cline - legacy single-file form, still detected.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `atlas-mcp-server-clinerules` | [`cyanheads/atlas-mcp-server`](https://github.com/cyanheads/atlas-mcp-server) | [`examples/atlas-mcp-server-clinerules/.clinerules`](examples/atlas-mcp-server-clinerules/.clinerules) | [source](https://raw.githubusercontent.com/cyanheads/atlas-mcp-server/main/.clinerules) |
| `mizchi-ailab-clinerules` | [`mizchi/ailab`](https://github.com/mizchi/ailab) | [`examples/mizchi-ailab-clinerules/.clinerules`](examples/mizchi-ailab-clinerules/.clinerules) | [source](https://raw.githubusercontent.com/mizchi/ailab/main/.clinerules) |
| `potatovn-clinerules` | [`GoldenPotato137/PotatoVN`](https://github.com/GoldenPotato137/PotatoVN) | [`examples/potatovn-clinerules/.clinerules`](examples/potatovn-clinerules/.clinerules) | [source](https://raw.githubusercontent.com/GoldenPotato137/PotatoVN/dev/.clinerules) |
| `raycast` | [`raycast/extensions`](https://github.com/raycast/extensions) | [`examples/raycast/.clinerules`](examples/raycast/.clinerules) | [source](https://raw.githubusercontent.com/raycast/extensions/main/extensions/1bookmark/.clinerules) |

### `.clinerules/`

Cline - primary workspace rules directory; Markdown/text files are combined and can be toggled.

**Pattern - not an extracted file.**

A project-root directory containing focused Markdown or text rule files such as `coding.md`, `testing.md`, and `architecture.md`. Cline combines the files into one workspace rule set, while the UI can toggle individual rules.

Live instances (fetch directly - too large or instance-specific to vendor):

- [Cline docs example](https://docs.cline.bot/customization/cline-rules)
- [wjmuse/mcp_daily_life .clinerules directory](https://github.com/wjmuse/mcp_daily_life/tree/main/.clinerules)

### `.windsurfrules`

Windsurf - legacy single-file form (superseded by .windsurf/rules/*.md).

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `chadnext-windsurfrules` | [`moinulmoin/chadnext`](https://github.com/moinulmoin/chadnext) | [`examples/chadnext-windsurfrules/.windsurfrules`](examples/chadnext-windsurfrules/.windsurfrules) | [source](https://raw.githubusercontent.com/moinulmoin/chadnext/main/.windsurfrules) |
| `enferno-windsurfrules` | [`level09/enferno`](https://github.com/level09/enferno) | [`examples/enferno-windsurfrules/.windsurfrules`](examples/enferno-windsurfrules/.windsurfrules) | [source](https://raw.githubusercontent.com/level09/enferno/master/.windsurfrules) |
| `snyk` | [`snyk/vscode-extension`](https://github.com/snyk/vscode-extension) | [`examples/snyk/.windsurfrules`](examples/snyk/.windsurfrules) | [source](https://raw.githubusercontent.com/snyk/vscode-extension/main/.windsurfrules) |
| `tmuxp-windsurfrules` | [`tmux-python/tmuxp`](https://github.com/tmux-python/tmuxp) | [`examples/tmuxp-windsurfrules/.windsurfrules`](examples/tmuxp-windsurfrules/.windsurfrules) | [source](https://raw.githubusercontent.com/tmux-python/tmuxp/master/.windsurfrules) |
| `vectra-windsurfrules` | [`Stevenic/vectra`](https://github.com/Stevenic/vectra) | [`examples/vectra-windsurfrules/.windsurfrules`](examples/vectra-windsurfrules/.windsurfrules) | [source](https://raw.githubusercontent.com/Stevenic/vectra/main/.windsurfrules) |

## Field notes

### Fields (frontmatter)
**Cursor `.mdc`** (in `.cursor/rules/`; a plain `.md` there is ignored): `description`, `globs` (**comma-separated string, not a YAML array**), `alwaysApply` (bool). The combination selects one of **four rule types**:

| Type | `alwaysApply` | `description` | `globs` |
| --- | --- | --- | --- |
| Always | `true` | - | - |
| Auto Attached | `false` | - | set |
| Agent Requested | `false` | **required** | - |
| Manual (`@rule`) | `false` | - | - |

**Devin Desktop / legacy Windsurf rules**: preferred workspace path is now `.devin/rules/*.md`; `.windsurf/rules/*.md` remains a fallback. Frontmatter uses `trigger` (`always_on` / `model_decision` / `glob` / `manual`), `description` (for `model_decision`), and `globs` (for `glob`). Limits: **12,000 chars** per workspace rule file, **6,000** for the global rules file.

**Cline `.clinerules/`**: primary workspace rules directory at the project root. Cline processes all `.md` and `.txt` files inside it, combines workspace and global rules, and gives workspace rules precedence when they conflict. Legacy `.clinerules` single-file rules are still detected.

**Legacy single-file forms** - `.cursorrules`, `.clinerules`, `.windsurfrules` - are plain prose, always injected, no frontmatter.

### Composition
- **Modern (`.mdc`)** carries frontmatter that *scopes* the rule by glob or description instead of being on for everything.
- **Legacy** is a flat prose file; the well-known devin.cursorrules is structured as *Instructions / Lessons / Scratchpad*.

### Anti-patterns
- Large `alwaysApply: true` / `always_on` rule files - prepended to every request, quietly inflating token cost.
- Affirmation prose that doesn't change behavior ("you are a genius... double-check your work") - concrete rules ("do not nest code more than 2 levels deep") earn their place.
- Keeping a flat `.cursorrules` when a glob-scoped `.cursor/rules/*.mdc` would target the rule precisely.

### Edge cases
- **Four activation modes**, not three: Always, Auto-Attached (glob), Agent-Requested (by description), and **Manual** (`@rule` mention) - pick the narrowest that works. Windsurf mirrors these via its `trigger` field.
- `.cursorrules` is superseded by `.cursor/rules/*.mdc`, `.clinerules` by `.clinerules/`, and `.windsurfrules` by `.devin/rules/*.md` / `.windsurf/rules/*.md`; these tools increasingly also accept a plain `AGENTS.md`. `.cursor/rules/` can be **nested** per subdirectory, and rules reference files with `@filename`.
- Root-level AGENTS.md in Devin/Cascade is processed by the same rules engine as always-on context, while subdirectory AGENTS.md files act like location-scoped glob rules. Do not duplicate the same guidance in both a rule and AGENTS.md.

### Adoption / maturity
- Rules files are adopted, but fragmented. Cursor, Cline, Devin/Cascade/Windsurf, and legacy tools all have slightly different names and activation semantics.
- The safest repo policy is "narrow by default": keep global/always-on rules short, move language-specific or workflow-specific instructions into glob/model/manual rules, and keep one canonical source for cross-tool instructions.

### Sources checked
- [Cursor Rules docs](https://cursor.com/docs/rules)
- [Devin/Cascade Memories & Rules docs](https://docs.devin.ai/desktop/cascade/memories)
- [Cline Rules docs](https://docs.cline.bot/customization/cline-rules)
- [Warp rules docs](https://docs.warp.dev/agent-platform/capabilities/rules/)
