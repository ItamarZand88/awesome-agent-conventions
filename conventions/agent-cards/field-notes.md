### Composition
A flat JSON capability descriptor. The A2A currency-agent card carries:
- **Identity & versioning** — `name`, `description`, `protocolVersion` (`0.3.0`), `provider`.
- **Transport & modalities** — `preferredTransport` (`JSONRPC`), `defaultInputModes` / `defaultOutputModes` (text, `application/json`).
- **`capabilities`** (e.g. `streaming: true`) and a **`skills`** array describing what the agent can actually do.

### Anti-patterns
- Hand-rolling JSON that drifts from the spec's required fields — `protocolVersion` and `skills` are not optional decoration.
- Advertising skills the agent doesn't implement (the card is a contract other agents call against).
- Pinning a stale `protocolVersion` after upgrading the runtime.

### Edge cases
- **🟠 Emerging:** the spec defines a well-known path (`/.well-known/agent.json`, a.k.a. `agent-card.json`), but in practice cards are often **served at runtime** rather than committed — both examples here come from the A2A samples repo, not a live `.well-known/` path.
- Naming is still settling (`agent.json` vs `agent-card.json`); fetchers should tolerate both.
