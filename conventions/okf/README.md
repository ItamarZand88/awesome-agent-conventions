# OKF (Open Knowledge Format) 🟠 Emerging

> A machine-first organizational knowledge base: a version-controlled folder of typed Markdown files (one concept per file) that any agent reads as ground-truth context. Open-sourced by Google Cloud in 2026 as the content layer to MCP's transport.

- **Read by:** Agents over MCP (okfy, openknowledge, superops okf CLIs); Google's knowledge-catalog ingests bundles
- **Location:** A bundle directory in a Git repo; each concept is one .md file, nested index.md per directory
- **Spec:** [https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)
- **Evidence:** Google Cloud published the OKF spec and sample bundles (GA4, Bitcoin, Stack Overflow) under Apache-2.0 in 2026; a community ecosystem of CLIs, conformance checkers, and agent skills already builds on it.
- **Last verified:** 2026-06-27
- **Files:** `.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `.md`

One concept per Markdown file with YAML frontmatter (required `type`, plus title/description/resource/tags); a bundle is a directory of these.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `bitcoin-bundle` | [`GoogleCloudPlatform/knowledge-catalog`](https://github.com/GoogleCloudPlatform/knowledge-catalog) | [`examples/bitcoin-bundle/index.md`](examples/bitcoin-bundle/index.md) | [source](https://raw.githubusercontent.com/GoogleCloudPlatform/knowledge-catalog/main/okf/bundles/crypto_bitcoin/index.md) |
| `bitcoin-dataset` | [`GoogleCloudPlatform/knowledge-catalog`](https://github.com/GoogleCloudPlatform/knowledge-catalog) | [`examples/bitcoin-dataset/crypto_bitcoin.md`](examples/bitcoin-dataset/crypto_bitcoin.md) | [source](https://raw.githubusercontent.com/GoogleCloudPlatform/knowledge-catalog/main/okf/bundles/crypto_bitcoin/datasets/crypto_bitcoin.md) |
| `bitcoin-table-blocks` | [`GoogleCloudPlatform/knowledge-catalog`](https://github.com/GoogleCloudPlatform/knowledge-catalog) | [`examples/bitcoin-table-blocks/blocks.md`](examples/bitcoin-table-blocks/blocks.md) | [source](https://raw.githubusercontent.com/GoogleCloudPlatform/knowledge-catalog/main/okf/bundles/crypto_bitcoin/tables/blocks.md) |
| `bitcoin-table-transactions` | [`GoogleCloudPlatform/knowledge-catalog`](https://github.com/GoogleCloudPlatform/knowledge-catalog) | [`examples/bitcoin-table-transactions/transactions.md`](examples/bitcoin-table-transactions/transactions.md) | [source](https://raw.githubusercontent.com/GoogleCloudPlatform/knowledge-catalog/main/okf/bundles/crypto_bitcoin/tables/transactions.md) |
| `ga4-bundle` | [`GoogleCloudPlatform/knowledge-catalog`](https://github.com/GoogleCloudPlatform/knowledge-catalog) | [`examples/ga4-bundle/index.md`](examples/ga4-bundle/index.md) | [source](https://raw.githubusercontent.com/GoogleCloudPlatform/knowledge-catalog/main/okf/bundles/ga4/index.md) |
| `ga4-dataset` | [`GoogleCloudPlatform/knowledge-catalog`](https://github.com/GoogleCloudPlatform/knowledge-catalog) | [`examples/ga4-dataset/ga4_obfuscated_sample_ecommerce.md`](examples/ga4-dataset/ga4_obfuscated_sample_ecommerce.md) | [source](https://raw.githubusercontent.com/GoogleCloudPlatform/knowledge-catalog/main/okf/bundles/ga4/datasets/ga4_obfuscated_sample_ecommerce.md) |
| `ga4-join-clickstats` | [`GoogleCloudPlatform/knowledge-catalog`](https://github.com/GoogleCloudPlatform/knowledge-catalog) | [`examples/ga4-join-clickstats/events___ads_clickstats.md`](examples/ga4-join-clickstats/events___ads_clickstats.md) | [source](https://raw.githubusercontent.com/GoogleCloudPlatform/knowledge-catalog/main/okf/bundles/ga4/references/joins/events___ads_clickstats.md) |
| `ga4-metric-event-count` | [`GoogleCloudPlatform/knowledge-catalog`](https://github.com/GoogleCloudPlatform/knowledge-catalog) | [`examples/ga4-metric-event-count/event_count.md`](examples/ga4-metric-event-count/event_count.md) | [source](https://raw.githubusercontent.com/GoogleCloudPlatform/knowledge-catalog/main/okf/bundles/ga4/references/metrics/event_count.md) |
| `ga4-metric-pageviews` | [`GoogleCloudPlatform/knowledge-catalog`](https://github.com/GoogleCloudPlatform/knowledge-catalog) | [`examples/ga4-metric-pageviews/avg_pageviews.md`](examples/ga4-metric-pageviews/avg_pageviews.md) | [source](https://raw.githubusercontent.com/GoogleCloudPlatform/knowledge-catalog/main/okf/bundles/ga4/references/metrics/avg_pageviews.md) |

## Field notes

### The format
OKF (Open Knowledge Format) is an open spec from Google Cloud, released in 2026 under Apache-2.0 and versioned at v0.1. A *bundle* is a plain directory of Markdown files in a Git repository, where each file describes exactly one thing - one table, one metric, one runbook, one dataset. The framing the spec authors use: if MCP is the socket that connects an agent to your tools, OKF is the knowledge that flows through it.

- **Frontmatter is the contract.** Each concept file opens with YAML frontmatter. `type` is the one load-bearing field (e.g. `BigQuery Dataset`, `Table`, `Metric`); `title`, `description`, `resource`, `tags`, and `timestamp` are the common generated fields. The body is human-readable Markdown.
- **One concept per file, linked by relative paths.** Directories carry an `index.md`, and concepts cross-reference each other with ordinary Markdown links - so a bundle renders on GitHub, zips up, and diffs in a pull request like any other repo content.
- **Served over MCP, read progressively.** An agent starts from small previews (the index + frontmatter) and only loads a full concept when it needs it. Google's knowledge-catalog can ingest a bundle and serve it straight to agents.

### Composition
- The vendored examples are Google's canonical `ga4` and `crypto_bitcoin` bundles: a bundle `index.md`, dataset files, table files, metric definitions, and a join reference - the same shape across both, which is the point.
- Managed exactly like code: version-controlled, reviewed in PRs, with a full history. The knowledge stops living in a Confluence page, a Slack thread, or one tenured employee's head and becomes a file every agent can read.

### Anti-patterns
- A human-prose wiki page mislabeled as OKF - OKF is written machine-first for agents, not as narrative documentation.
- One file that documents many things. The unit is one concept per file; that is what keeps previews cheap and references precise.
- Reaching for a vector database or RAG pipeline to hold context that is really a small set of stable, specific facts. OKF's bet is that plain typed files beat fuzzy chunk search for institutional knowledge.

### Edge cases
- **The spec is deliberately forgiving.** A consumer must tolerate a broken link, an unknown field, or a `type` it has never seen - real knowledge is always half-finished, so a bundle is built to keep working while it grows.
- **🟠 Emerging:** a published Google spec with real sample bundles and a fast-growing tool ecosystem, but still v0.1 and only weeks old. Treat the shape as indicative.

### Adoption and maturity
- Spec, sample bundles (GA4, Stack Overflow, Bitcoin), an HTML bundle viewer, and knowledge-catalog ingestion are all public from Google Cloud.
- A community layer already exists: CLIs (`okfy-ai`, `openknowledge-sh`, `superops okf`), a conformance checker, a frontmatter-maintenance skill, and `/okf` Claude Code / Codex skills.

### Related conventions
- **Pairs with [`mcp-config`](../mcp-config/README.md):** MCP is the transport, OKF is the content that travels over it.
- **Distinct from [`llms-txt`](../llms-txt/README.md):** llms.txt is a single web-served index of docs; OKF is a multi-file, typed, repo-resident knowledge base of domain facts.
- **Distinct from [`agents-md`](../agents-md/README.md) / [`claude-md`](../claude-md/README.md):** those carry standing project *instructions*; OKF carries factual domain *knowledge* the agent looks things up in.
