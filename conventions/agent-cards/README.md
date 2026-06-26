# Agent Cards (A2A) 🟠 Emerging

> The Agent2Agent (A2A) capability card - a JSON document at a well-known path advertising an agent's skills, endpoints, and auth so other agents can discover and call it. Now a Linux Foundation project at v1.0; adoption is growing but early.

- **Read by:** A2A-compatible agents discovering another agent's capabilities
- **Location:** /.well-known/agent-card.json (the older /.well-known/agent.json is a legacy alias)
- **Spec:** [https://a2a-protocol.org/latest/specification/](https://a2a-protocol.org/latest/specification/)
- **Evidence:** A2A v1.0 specifies Agent Cards and the well-known agent-card.json path, with public sample cards but still-early ecosystem adoption.
- **Last verified:** 2026-06-26
- **Files:** `agent-card.json`, `agent.json`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `agent-card.json`

Current A2A well-known Agent Card filename.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `a2a-adk-skills` | [`a2aproject/a2a-samples`](https://github.com/a2aproject/a2a-samples) | [`examples/a2a-adk-skills/agent-card.json`](examples/a2a-adk-skills/agent-card.json) | [source](https://raw.githubusercontent.com/a2aproject/a2a-samples/main/samples/python/agents/adk_skills_agent/src/skills_agent/agent_card.json) |
| `a2a-car-rental` | [`a2aproject/a2a-samples`](https://github.com/a2aproject/a2a-samples) | [`examples/a2a-car-rental/agent-card.json`](examples/a2a-car-rental/agent-card.json) | [source](https://raw.githubusercontent.com/a2aproject/a2a-samples/main/samples/python/agents/a2a_mcp/agent_cards/car_rental_agent.json) |
| `a2a-hotel-booking` | [`a2aproject/a2a-samples`](https://github.com/a2aproject/a2a-samples) | [`examples/a2a-hotel-booking/agent-card.json`](examples/a2a-hotel-booking/agent-card.json) | [source](https://raw.githubusercontent.com/a2aproject/a2a-samples/main/samples/python/agents/a2a_mcp/agent_cards/hotel_booking_agent.json) |
| `a2a-orchestrator` | [`a2aproject/a2a-samples`](https://github.com/a2aproject/a2a-samples) | [`examples/a2a-orchestrator/agent-card.json`](examples/a2a-orchestrator/agent-card.json) | [source](https://raw.githubusercontent.com/a2aproject/a2a-samples/main/samples/python/agents/a2a_mcp/agent_cards/orchestrator_agent.json) |
| `a2a-planner` | [`a2aproject/a2a-samples`](https://github.com/a2aproject/a2a-samples) | [`examples/a2a-planner/agent-card.json`](examples/a2a-planner/agent-card.json) | [source](https://raw.githubusercontent.com/a2aproject/a2a-samples/main/samples/python/agents/a2a_mcp/agent_cards/planner_agent.json) |
| `air-ticketing` | [`a2aproject/a2a-samples`](https://github.com/a2aproject/a2a-samples) | [`examples/air-ticketing/agent-card.json`](examples/air-ticketing/agent-card.json) | [source](https://raw.githubusercontent.com/a2aproject/a2a-samples/main/samples/python/agents/a2a_mcp/agent_cards/air_ticketing_agent.json) |
| `currency` | [`a2aproject/a2a-samples`](https://github.com/a2aproject/a2a-samples) | [`examples/currency/agent-card.json`](examples/currency/agent-card.json) | [source](https://raw.githubusercontent.com/a2aproject/a2a-samples/main/samples/python/agents/adk_currency_agent/src/currency_agent/agent_card.json) |
| `kagent-adk-basic` | [`kagent-dev/kagent`](https://github.com/kagent-dev/kagent) | [`examples/kagent-adk-basic/agent-card.json`](examples/kagent-adk-basic/agent-card.json) | [source](https://raw.githubusercontent.com/kagent-dev/kagent/main/python/samples/adk/basic/basic/agent-card.json) |
| `kagent-go-e2e-kebab` | [`kagent-dev/kagent`](https://github.com/kagent-dev/kagent) | [`examples/kagent-go-e2e-kebab/agent-card.json`](examples/kagent-go-e2e-kebab/agent-card.json) | [source](https://raw.githubusercontent.com/kagent-dev/kagent/main/go/core/test/e2e/agents/kebab/kebab/agent-card.json) |
| `kagent-langgraph-currency` | [`kagent-dev/kagent`](https://github.com/kagent-dev/kagent) | [`examples/kagent-langgraph-currency/agent-card.json`](examples/kagent-langgraph-currency/agent-card.json) | [source](https://raw.githubusercontent.com/kagent-dev/kagent/main/python/samples/langgraph/currency/currency/agent-card.json) |
| `kagent-langgraph-hitl-tools` | [`kagent-dev/kagent`](https://github.com/kagent-dev/kagent) | [`examples/kagent-langgraph-hitl-tools/agent-card.json`](examples/kagent-langgraph-hitl-tools/agent-card.json) | [source](https://raw.githubusercontent.com/kagent-dev/kagent/main/python/samples/langgraph/hitl-tools/hitl_tools/agent-card.json) |
| `kagent-langgraph-kebab` | [`kagent-dev/kagent`](https://github.com/kagent-dev/kagent) | [`examples/kagent-langgraph-kebab/agent-card.json`](examples/kagent-langgraph-kebab/agent-card.json) | [source](https://raw.githubusercontent.com/kagent-dev/kagent/main/python/samples/langgraph/kebab/kebab/agent-card.json) |
| `kagent-openai-basic` | [`kagent-dev/kagent`](https://github.com/kagent-dev/kagent) | [`examples/kagent-openai-basic/agent-card.json`](examples/kagent-openai-basic/agent-card.json) | [source](https://raw.githubusercontent.com/kagent-dev/kagent/main/python/samples/openai/basic_agent/basic_agent/agent-card.json) |
| `kagent-poem-flow` | [`kagent-dev/kagent`](https://github.com/kagent-dev/kagent) | [`examples/kagent-poem-flow/agent-card.json`](examples/kagent-poem-flow/agent-card.json) | [source](https://raw.githubusercontent.com/kagent-dev/kagent/main/python/samples/crewai/poem_flow/src/poem_flow/agent-card.json) |
| `kagent-research-crew` | [`kagent-dev/kagent`](https://github.com/kagent-dev/kagent) | [`examples/kagent-research-crew/agent-card.json`](examples/kagent-research-crew/agent-card.json) | [source](https://raw.githubusercontent.com/kagent-dev/kagent/main/python/samples/crewai/research-crew/src/research_crew/agent-card.json) |

### `agent.json`

Legacy alias seen in earlier A2A material and deployments.

**Pattern - not an extracted file.**

A legacy well-known alias for an A2A Agent Card. New agents should publish `/.well-known/agent-card.json`; clients may still tolerate `/.well-known/agent.json` while interoperating with older deployments.

## Field notes

### Fields (A2A v1.0 `AgentCard`)
Top-level (required unless noted):

| Field | Notes |
| --- | --- |
| `name` | human-readable agent name |
| `description` | what the agent does |
| `version` | the agent's own version, e.g. `"1.0.0"` |
| `supportedInterfaces` | array of `AgentInterface`; **first entry is preferred**. Replaces 0.x `url` + `preferredTransport` + `additionalInterfaces` |
| `capabilities` | `AgentCapabilities` object |
| `defaultInputModes` / `defaultOutputModes` | media types across all skills |
| `skills` | array of `AgentSkill` |
| `provider` | optional `AgentProvider` |
| `securitySchemes` / `security` | optional auth scheme defs + requirements |
| `documentationUrl`, `iconUrl`, `signatures` | optional |

Nested objects: **`AgentInterface`** {`url`, `protocolBinding` (open string: `JSONRPC`/`GRPC`/`HTTP+JSON`), `protocolVersion`, `tenant?`}; **`AgentCapabilities`** {`streaming?`, `pushNotifications?`, `extensions?`, `extendedAgentCard?`}; **`AgentSkill`** {`id`, `name`, `description`, `tags`, `examples?`, `inputModes?`, `outputModes?`, `security?`}; **`AgentProvider`** {`url`, `organization`}; **`AgentCardSignature`** {`protected`, `signature`, `header?`} (JWS, RFC 7515).

### Composition
- A JSON capability descriptor: identity (`name`/`description`/`version`/`provider`), the transport endpoints (`supportedInterfaces`), `capabilities`, and a `skills` array describing what the agent can actually do.
- The vendored samples still show **pre-v1 card shapes** in the wild: top-level `url`, and in one case top-level `protocolVersion: "0.3.0"` plus `preferredTransport` - fields that v1.0 restructured.

### Anti-patterns
- Hand-rolling JSON that drifts from the spec's required fields - `skills`, `capabilities`, and `supportedInterfaces` are not optional decoration.
- Advertising skills the agent doesn't implement (the card is a contract other agents call against).
- Pinning a stale protocol version after upgrading the runtime.

### Edge cases
- **v1.0 restructured the card.** There is **no top-level `protocolVersion`** anymore - it moved to `AgentInterface.protocolVersion` (per endpoint). `preferredTransport` and `additionalInterfaces` were consolidated into `supportedInterfaces[]` (preference = first entry), the per-interface field is `protocolBinding` (an open string, not the old `transport` enum), and `supportsAuthenticatedExtendedCard` moved to `capabilities.extendedAgentCard`. (There is no `protocolVersions` array - that spelling was a rejected proposal.)
- **Governance:** A2A was donated to the **Linux Foundation** (June 2025) and reached **v1.0** - the 🟠 reflects real-world adoption, not an unfinished spec. The proto at `a2aproject/A2A` is the authoritative source.
- **Well-known path:** the current standard is `/.well-known/agent-card.json`; `/.well-known/agent.json` is a legacy alias, so tolerate both but publish the current name for new agents. In practice cards are often **served at runtime** rather than committed - both examples here come from the A2A samples repo.

### Adoption / maturity
- A2A Agent Cards are real protocol objects in a public v1.0 spec. They remain 🟠 rather than 🟢 here because broad independent production discovery is still early, and many public samples still show pre-v1 fields.
- A card is a discovery contract. If the card advertises a skill, transport, media type, auth scheme, or extension, clients may select behavior from that declaration before ever talking to the agent.

### Related conventions
- Agent Cards are for agent-to-agent discovery and invocation. MCP config is for connecting an agent host to tools. They can coexist, but one does not substitute for the other.
- `auth.md` can describe how an agent obtains credentials; Agent Card `securitySchemes` and `security` describe what the A2A endpoint requires.

### Sources checked
- [A2A protocol specification](https://a2a-protocol.org/latest/specification/)
- [a2aproject/A2A repository](https://github.com/a2aproject/A2A)
- [A2A sample Agent Cards](https://github.com/a2aproject/a2a-samples)
