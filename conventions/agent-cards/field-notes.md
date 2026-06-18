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
