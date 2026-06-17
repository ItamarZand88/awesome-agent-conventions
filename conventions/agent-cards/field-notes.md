### Composition
A flat JSON capability descriptor. The A2A currency-agent card carries:
- **Identity & versioning** - `name`, `description`, `provider`, and `protocolVersion`. The current A2A spec is **v1.0** (`protocolVersion: "1.0"`, plus a top-level `protocolVersions: ["1.0"]` and `supportedInterfaces`); the vendored samples here are older snapshots still pinned at `0.3.0`.
- **Transport & modalities** - `preferredTransport` (`JSONRPC`), `defaultInputModes` / `defaultOutputModes` (text, `application/json`).
- **`capabilities`** (e.g. `streaming: true`) and a **`skills`** array describing what the agent can actually do.

### Anti-patterns
- Hand-rolling JSON that drifts from the spec's required fields - `protocolVersion` and `skills` are not optional decoration.
- Advertising skills the agent doesn't implement (the card is a contract other agents call against).
- Pinning a stale `protocolVersion` after upgrading the runtime.

### Edge cases
- **Governance:** A2A was donated to the **Linux Foundation** (June 2025) and has since reached **v1.0** - the 🟠 here reflects real-world adoption, not an unfinished spec.
- **Well-known path:** the current standard is `/.well-known/agent-card.json`; the older `/.well-known/agent.json` is a legacy alias, so fetchers should tolerate both. In practice cards are often **served at runtime** rather than committed - both examples here come from the A2A samples repo, not a live `.well-known/` path.
