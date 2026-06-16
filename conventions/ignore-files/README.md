# AI ignore files 🟢 Adopted

> gitignore-syntax files that fence an AI agent out of paths — secrets, vendored code, generated output — so they're never sent to the model as context.

- **Read by:** JetBrains Junie (.aiignore), Cursor (.cursorignore), Codeium/Windsurf (.codeiumignore)
- **Location:** Repository root (gitignore-style glob syntax)
- **Spec:** [https://www.jetbrains.com/help/junie/aiignore.html](https://www.jetbrains.com/help/junie/aiignore.html)
- **Files:** `.aiignore`, `.cursorignore`, `.codeiumignore`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) — none are hand-written._

### `.aiignore`

JetBrains Junie / AI Assistant.

| Source | File | Provenance |
| --- | --- | --- |
| `c9s-bbgo` | [`c9s-bbgo..aiignore`](examples/c9s-bbgo..aiignore) | [source](https://raw.githubusercontent.com/c9s/bbgo/main/.aiignore) |

### `.cursorignore`

Cursor.

| Source | File | Provenance |
| --- | --- | --- |
| `holochain-holochain` | [`holochain-holochain..cursorignore`](examples/holochain-holochain..cursorignore) | [source](https://raw.githubusercontent.com/holochain/holochain/develop/.cursorignore) |
| `mulesoft-api-console` | [`mulesoft-api-console..cursorignore`](examples/mulesoft-api-console..cursorignore) | [source](https://raw.githubusercontent.com/mulesoft/api-console/master/.cursorignore) |

### `.codeiumignore`

Codeium / Windsurf.

| Source | File | Provenance |
| --- | --- | --- |
| `seontechnologies-playwright-utils` | [`seontechnologies-playwright-utils..codeiumignore`](examples/seontechnologies-playwright-utils..codeiumignore) | [source](https://raw.githubusercontent.com/seontechnologies/playwright-utils/main/.codeiumignore) |

## Field notes

### Composition
- **gitignore syntax, verbatim.** The bbgo `.aiignore` says so outright and links the gitignore docs; holochain's `.cursorignore` is three lines (`target/`, `**/target/**`, `.git/`). Short, pattern-based, build-output- and VCS-focused.

### Anti-patterns
- **Treating it as a security boundary.** It reduces what's sent as context; it is *not* a hard secret control. Don't rely on `.cursorignore` to keep credentials out of the model — keep secrets out of the tree.
- Over-broad globs that also hide the context the agent legitimately needs.
- Forgetting generated/vendored output, so the agent wastes its window indexing `dist/`.

### Edge cases
- Tools split the job: Cursor distinguishes **index-ignore** (`.cursorignore`) from indexing-only variants, and behavior around *access* vs *indexing* differs per tool — read the specific tool's semantics.
- Negation (`!pattern`) and precedence interact with `.gitignore`; an agent may union both.
