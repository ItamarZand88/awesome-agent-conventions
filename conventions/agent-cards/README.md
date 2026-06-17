# Agent Cards (A2A) 🟠 Emerging

> The Agent2Agent (A2A) capability card — a JSON document at a well-known path advertising an agent's skills, endpoints, and auth so other agents can discover and call it. Backed by a real spec; adoption is growing but early.

- **Read by:** A2A-compatible agents discovering another agent's capabilities
- **Location:** /.well-known/agent.json (a.k.a. /.well-known/agent-card.json)
- **Spec:** [https://a2a-protocol.org/latest/specification/](https://a2a-protocol.org/latest/specification/)
- **Files:** `agent.json`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) — none are hand-written._

### `agent.json`

| Source | File | Provenance |
| --- | --- | --- |
| `air-ticketing` | [`air-ticketing.agent.json`](examples/air-ticketing.agent.json) | [source](https://raw.githubusercontent.com/a2aproject/a2a-samples/main/samples/python/agents/a2a_mcp/agent_cards/air_ticketing_agent.json) |
| `currency` | [`currency.agent.json`](examples/currency.agent.json) | [source](https://raw.githubusercontent.com/a2aproject/a2a-samples/main/samples/python/agents/adk_currency_agent/src/currency_agent/agent_card.json) |

## Field notes

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
