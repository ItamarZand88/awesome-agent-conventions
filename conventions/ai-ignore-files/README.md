# AI ignore files 🟢 Adopted

> gitignore-syntax files that fence an AI agent out of paths - secrets, vendored code, generated output - so they're never sent to the model as context.

- **Read by:** JetBrains Junie (.aiignore), Cursor (.cursorignore), Codeium/Windsurf (.codeiumignore)
- **Location:** Repository root (gitignore-style glob syntax)
- **Spec:** [https://cursor.com/docs/reference/ignore-file](https://cursor.com/docs/reference/ignore-file)
- **Evidence:** Cursor, JetBrains Junie, and Codeium/Windsurf-style tools use gitignore-like files to exclude paths from AI context.
- **Last verified:** 2026-06-26
- **Files:** `.aiignore`, `.cursorignore`, `.codeiumignore`, `.aiexclude`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `.aiignore`

JetBrains Junie / AI Assistant.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `ag-grid` | [`ag-grid/ag-grid`](https://github.com/ag-grid/ag-grid) | [`examples/ag-grid/.aiignore`](examples/ag-grid/.aiignore) | [source](https://raw.githubusercontent.com/ag-grid/ag-grid/latest/.rulesync/.aiignore) |
| `agentstack-aiignore` | [`i-am-bee/agentstack`](https://github.com/i-am-bee/agentstack) | [`examples/agentstack-aiignore/.aiignore`](examples/agentstack-aiignore/.aiignore) | [source](https://raw.githubusercontent.com/i-am-bee/agentstack/main/.aiignore) |
| `flutter-genui-aiignore` | [`flutter/genui`](https://github.com/flutter/genui) | [`examples/flutter-genui-aiignore/.aiignore`](examples/flutter-genui-aiignore/.aiignore) | [source](https://raw.githubusercontent.com/flutter/genui/main/packages/json_schema_builder/.aiignore) |
| `lifi-contracts-aiignore` | [`lifinance/contracts`](https://github.com/lifinance/contracts) | [`examples/lifi-contracts-aiignore/.aiignore`](examples/lifi-contracts-aiignore/.aiignore) | [source](https://raw.githubusercontent.com/lifinance/contracts/main/.aiignore) |
| `lizmap-aiignore` | [`3liz/lizmap-web-client`](https://github.com/3liz/lizmap-web-client) | [`examples/lizmap-aiignore/.aiignore`](examples/lizmap-aiignore/.aiignore) | [source](https://raw.githubusercontent.com/3liz/lizmap-web-client/master/.aiignore) |
| `rusefi-aiignore` | [`rusefi/rusefi`](https://github.com/rusefi/rusefi) | [`examples/rusefi-aiignore/.aiignore`](examples/rusefi-aiignore/.aiignore) | [source](https://raw.githubusercontent.com/rusefi/rusefi/master/.aiignore) |
| `wprig-aiignore` | [`wprig/wprig`](https://github.com/wprig/wprig) | [`examples/wprig-aiignore/.aiignore`](examples/wprig-aiignore/.aiignore) | [source](https://raw.githubusercontent.com/wprig/wprig/master/.aiignore) |

### `.cursorignore`

Cursor.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `api-console` | [`mulesoft/api-console`](https://github.com/mulesoft/api-console) | [`examples/api-console/.cursorignore`](examples/api-console/.cursorignore) | [source](https://raw.githubusercontent.com/mulesoft/api-console/master/.cursorignore) |
| `async-memcached-cursorignore` | [`Shopify/async-memcached`](https://github.com/Shopify/async-memcached) | [`examples/async-memcached-cursorignore/.cursorignore`](examples/async-memcached-cursorignore/.cursorignore) | [source](https://raw.githubusercontent.com/Shopify/async-memcached/main/.cursorignore) |
| `atlantes-cursorignore` | [`allenai/atlantes`](https://github.com/allenai/atlantes) | [`examples/atlantes-cursorignore/.cursorignore`](examples/atlantes-cursorignore/.cursorignore) | [source](https://raw.githubusercontent.com/allenai/atlantes/main/.cursorignore) |
| `dbdemos-cursorignore` | [`databricks-demos/dbdemos`](https://github.com/databricks-demos/dbdemos) | [`examples/dbdemos-cursorignore/.cursorignore`](examples/dbdemos-cursorignore/.cursorignore) | [source](https://raw.githubusercontent.com/databricks-demos/dbdemos/main/.cursorignore) |
| `elastiflow-pipelines-cursorignore` | [`elastiflow/pipelines`](https://github.com/elastiflow/pipelines) | [`examples/elastiflow-pipelines-cursorignore/.cursorignore`](examples/elastiflow-pipelines-cursorignore/.cursorignore) | [source](https://raw.githubusercontent.com/elastiflow/pipelines/main/.cursorignore) |
| `flatcitybuf-cursorignore` | [`cityjson/flatcitybuf`](https://github.com/cityjson/flatcitybuf) | [`examples/flatcitybuf-cursorignore/.cursorignore`](examples/flatcitybuf-cursorignore/.cursorignore) | [source](https://raw.githubusercontent.com/cityjson/flatcitybuf/main/.cursorignore) |
| `holochain` | [`holochain/holochain`](https://github.com/holochain/holochain) | [`examples/holochain/.cursorignore`](examples/holochain/.cursorignore) | [source](https://raw.githubusercontent.com/holochain/holochain/develop/.cursorignore) |
| `plutus-cursorignore` | [`IntersectMBO/plutus`](https://github.com/IntersectMBO/plutus) | [`examples/plutus-cursorignore/.cursorignore`](examples/plutus-cursorignore/.cursorignore) | [source](https://raw.githubusercontent.com/IntersectMBO/plutus/master/.cursorignore) |

### `.codeiumignore`

Codeium (now Windsurf).

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `wikimedia` | [`wikimedia/wikimedia-fundraising-dev`](https://github.com/wikimedia/wikimedia-fundraising-dev) | [`examples/wikimedia/.codeiumignore`](examples/wikimedia/.codeiumignore) | [source](https://raw.githubusercontent.com/wikimedia/wikimedia-fundraising-dev/master/.codeiumignore) |

### `.aiexclude`

Android Studio Gemini / JetBrains AI exclusion file.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `adyen-android-aiexclude` | [`Adyen/adyen-android`](https://github.com/Adyen/adyen-android) | [`examples/adyen-android-aiexclude/.aiexclude`](examples/adyen-android-aiexclude/.aiexclude) | [source](https://raw.githubusercontent.com/Adyen/adyen-android/main/.aiexclude) |
| `guardian-source-apps-aiexclude` | [`guardian/source-apps`](https://github.com/guardian/source-apps) | [`examples/guardian-source-apps-aiexclude/.aiexclude`](examples/guardian-source-apps-aiexclude/.aiexclude) | [source](https://raw.githubusercontent.com/guardian/source-apps/main/.aiexclude) |
| `meshtastic-android-aiexclude` | [`meshtastic/Meshtastic-Android`](https://github.com/meshtastic/Meshtastic-Android) | [`examples/meshtastic-android-aiexclude/.aiexclude`](examples/meshtastic-android-aiexclude/.aiexclude) | [source](https://raw.githubusercontent.com/meshtastic/Meshtastic-Android/main/.aiexclude) |
| `rxdb-aiexclude` | [`pubkey/rxdb`](https://github.com/pubkey/rxdb) | [`examples/rxdb-aiexclude/.aiexclude`](examples/rxdb-aiexclude/.aiexclude) | [source](https://raw.githubusercontent.com/pubkey/rxdb/master/.aiexclude) |
| `stabilitymatrix-aiexclude` | [`LykosAI/StabilityMatrix`](https://github.com/LykosAI/StabilityMatrix) | [`examples/stabilitymatrix-aiexclude/.aiexclude`](examples/stabilitymatrix-aiexclude/.aiexclude) | [source](https://raw.githubusercontent.com/LykosAI/StabilityMatrix/main/.aiexclude) |
| `wordpress-android-aiexclude` | [`wordpress-mobile/WordPress-Android`](https://github.com/wordpress-mobile/WordPress-Android) | [`examples/wordpress-android-aiexclude/.aiexclude`](examples/wordpress-android-aiexclude/.aiexclude) | [source](https://raw.githubusercontent.com/wordpress-mobile/WordPress-Android/trunk/.aiexclude) |

## Field notes

### Composition
- **gitignore syntax, verbatim.** Short, pattern-based files focused on build output, secrets, and VCS dirs - holochain's `.cursorignore` is three lines (`target/`, `**/target/**`, `.git/`); ag-grid's `.aiignore` fences off `credentials/` and `.env.local`.
- **Different files control different surfaces.** Cursor splits `.cursorignore` (best-effort block for access and indexing) from `.cursorindexingignore` (indexing only). Devin Desktop / Windsurf uses `.codeiumignore` at the workspace root, plus a global `~/.codeium/.codeiumignore`. JetBrains Junie respects `.aiignore`.

### Anti-patterns
- **Treating it as a security boundary.** It reduces what's sent as context; it is *not* a hard secret control. Don't rely on `.cursorignore` to keep credentials out of the model - keep secrets out of the tree.
- Over-broad globs that also hide the context the agent legitimately needs.
- Forgetting generated/vendored output, so the agent wastes its window indexing `dist/`.

### Edge cases
- Tools split the job: Cursor's `.cursorignore` blocks both **access and indexing**, while `.cursorindexingignore` excludes from indexing *only* (the file stays readable) - the names are easy to get backwards. An Agent's terminal and MCP-server tools can't enforce `.cursorignore` at all, a second reason it isn't a hard boundary.
- Negation (`!pattern`) and precedence interact with `.gitignore`; an agent may union both.

### Adoption / maturity
- Ignore files are adopted because they solve a practical context-window and privacy problem, but they are tool-enforced hints, not repository security controls.
- Treat them like `.gitignore`: useful, reviewed, and version-controlled, but not sufficient for secrets. Secrets should not be committed, and sensitive generated files should be blocked by the tool's own permissions or environment policy too.

### Sources checked
- [Cursor ignore file docs](https://cursor.com/docs/reference/ignore-file)
- [JetBrains Junie .aiignore docs](https://www.jetbrains.com/help/ai-assistant/junie-agent.html)
- [Devin Desktop / Windsurf .codeiumignore docs](https://docs.devin.ai/desktop/context-awareness/windsurf-ignore)
