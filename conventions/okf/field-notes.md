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
