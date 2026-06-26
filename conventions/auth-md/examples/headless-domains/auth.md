<!-- source: headless-domains — https://headlessdomains.com/auth.md -->
# HeadlessDomains Authentication

HeadlessDomains supports agent-native authentication for autonomous domain registration, renewal, profile updates, and DNS-linked identity operations.

## Service

- Base URL: https://headlessdomains.com
- API base URL: https://headlessdomains.com/api/v1
- Protected resource metadata: https://headlessdomains.com/.well-known/oauth-protected-resource
- Authorization server metadata: https://headlessdomains.com/.well-known/oauth-authorization-server
- OpenAPI: https://headlessdomains.com/openapi.json
- Agent skill file: https://headlessdomains.com/skill.md

## Identity Model

Human SSO is not required to start. Autonomous agents may provision themselves, receive a HeadlessDomains API key, and pay with Machine Payments Protocol (MPP).

GFAVIP and PowerLobster identity can be attached later for claiming, delegation, account recovery, provenance, reputation, and higher-trust ecosystem actions.

Current assurance levels:

- Anonymous Agent: provisioned directly by HeadlessDomains, can use MPP and receive an API key.
- Claimed Agent: originally autonomous, later bound to a human account by claim code.
- Delegated Agent: planned, created or authorized by a human in PowerLobster with explicit permissions.
- Verified Agent: planned, backed by signed PowerLobster/GFAVIP identity assertions.

## Supported Methods

- `X-API-Key: hd_agent_...`
- `Authorization: Bearer <GFAVIP token>`
- `Authorization: Payment <MPP receipt>` for MPP payment replay flows

For MPP flows, prefer `X-API-Key` for agent identity because the `Authorization` header may be used by the payment receipt:

```http
X-API-Key: hd_agent_...
Authorization: Payment <receipt>
```

This keeps payment identity and actor identity separate:

- MPP proves the request paid.
- The HeadlessDomains API key proves the same agent identity is acting.
- GFAVIP/PowerLobster identity proves the human or delegated agent is accountable.

## Anonymous Agent Registration

Agents can provision a zero-human-start identity:

```http
POST https://headlessdomains.com/agent/auth
Content-Type: application/json

{"name":"Example Agent"}
```

The response includes:

- `agent_id`
- `api_key`
- `claim_code`

The same flow is available at `POST /api/v1/agents/provision` for backward compatibility.

## Claim Flow

Autonomous agents receive a claim code that a human operator can bind to their dashboard later. This lets an agent start independently and attach to a human-controlled account when appropriate.

## Identity Assertions

PowerLobster/GFAVIP identity assertions are planned, not active yet. HeadlessDomains metadata marks `identity_assertion` as planned until PowerLobster/GFAVIP can mint audience-specific ID-JAGs, publish JWKS, support user consent, and honor revocation.

## Discovery Headers

API endpoints that require authentication may return:

```http
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Bearer resource_metadata="https://headlessdomains.com/.well-known/oauth-protected-resource"
```

MPP payment challenges remain separate and use `402 Payment Required` with their own `WWW-Authenticate: Payment ...` header.

## Security Notes

- Do not commit API keys to public repositories.
- Use `X-API-Key` for MPP flows so the payment receipt can use `Authorization`.
- Treat claim codes like one-time handoff secrets.
- Use GFAVIP/PowerLobster identity when delegation, recovery, auditability, or reputation matters.
