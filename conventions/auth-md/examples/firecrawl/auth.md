<!-- source: firecrawl — https://firecrawl.dev/auth.md -->
# Firecrawl auth.md

You are an agent. Firecrawl supports agentic registration for WorkOS ID-JAG identity assertions: discover -> register -> call API. Follow the steps in order; do not skip ahead.

Firecrawl currently supports one registration method:

- `identity_assertion` with `assertion_type: "urn:ietf:params:oauth:token-type:id-jag"`
- `requested_credential_type: "api_key"`
- Credentials are Firecrawl API keys used as bearer tokens.

Firecrawl does not currently support anonymous registration, verified-email registration, claim flows, or `access_token` issuance through `/agent/auth`. Credential revocation is supported but provider-driven (initiated by WorkOS); agents never call it — see [Revocation](#revocation) below.

This is the direct WorkOS ID-JAG registration flow for identity-aware agents. If you need a human to sign in through the browser, install Firecrawl tooling, or save `FIRECRAWL_API_KEY` into a project, use `https://www.firecrawl.dev/agent-onboarding/SKILL.md` instead.

## Step 1 - Discover

Discovery is two hops. On cloud Firecrawl, an unauthenticated call to `https://api.firecrawl.dev` returns `401` with `WWW-Authenticate: Bearer resource_metadata="https://www.firecrawl.dev/.well-known/oauth-protected-resource"`. Fetch that URL when the header is present. If you do not have the header in hand, use the conventional metadata URL below.

### 1a. Fetch the Protected Resource Metadata

```http
GET https://www.firecrawl.dev/.well-known/oauth-protected-resource
```

Expected response shape:

```json
{
  "resource": "https://api.firecrawl.dev/",
  "resource_name": "Firecrawl API",
  "resource_logo_uri": "https://www.firecrawl.dev/brand/firecrawl-logo.png",
  "authorization_servers": ["https://www.firecrawl.dev"],
  "scopes_supported": ["firecrawl:global"],
  "bearer_methods_supported": ["header"],
  "agent_auth_uri": "https://www.firecrawl.dev/.well-known/oauth-authorization-server"
}
```

Use `resource` as the `aud` when minting an ID-JAG for Firecrawl. Send issued credentials with `Authorization: Bearer <credential>`.

### 1b. Fetch the Authorization Server Metadata

```http
GET https://www.firecrawl.dev/.well-known/oauth-authorization-server
```

The response includes this `agent_auth` block:

```json
{
  "agent_auth": {
    "skill": "https://www.firecrawl.dev/auth.md",
    "register_uri": "https://www.firecrawl.dev/agent/auth",
    "revocation_uri": "https://www.firecrawl.dev/agent/auth/revoke",
    "identity_types_supported": ["identity_assertion"],
    "identity_assertion": {
      "assertion_types_supported": ["urn:ietf:params:oauth:token-type:id-jag"],
      "credential_types_supported": ["api_key"]
    },
    "events_supported": [
      "https://schemas.workos.com/events/agent/auth/identity/assertion/revoked"
    ]
  }
}
```

Only use methods and credential types listed in `agent_auth`.

## Step 2 - Pick a Method

Use `identity_assertion + id-jag` only if you have a session tied to a user identity and can exchange it for an ID-JAG audience-bound to Firecrawl.

Do not use these methods for Firecrawl today:

- `anonymous`
- `identity_assertion + verified_email`
- claim ceremony endpoints

Revocation is **provider-driven** (initiated by WorkOS); agents never call the revocation endpoint directly — see [Revocation](#revocation).

## Step 3 - Register With ID-JAG

Before minting the ID-JAG, confirm the user consents to assert their identity to Firecrawl using the `resource_name`, `resource_logo_uri`, and scope set from Step 1.

Mint the assertion with:

- `aud` = the `resource` from Protected Resource Metadata, normally `https://api.firecrawl.dev/`
- `iss` = `https://auth.workos.bot`
- `typ` = `oauth-id-jag+jwt`
- `alg` = `RS256`
- `sub` = stable WorkOS subject for the user
- `client_id` = a WorkOS client ID trusted by Firecrawl
- `email` = the user's email address
- `email_verified: true`
- Fresh `jti`
- `iat` = issued-at epoch seconds
- Near-term `exp`, around 5 minutes

Firecrawl currently expects verified email in ID-JAG payloads. `phone_number_verified` alone is not supported today.
Firecrawl rate limits this endpoint at 60 identity-assertion registrations per hour per IP and about 1,000 per hour globally. If the caller IP is unavailable, Firecrawl skips the per-IP limit and still applies the global limit.

```http
POST https://www.firecrawl.dev/agent/auth
Content-Type: application/json

{
  "type": "identity_assertion",
  "assertion_type": "urn:ietf:params:oauth:token-type:id-jag",
  "assertion": "<your ID-JAG JWT>",
  "requested_credential_type": "api_key"
}
```

Response:

```json
{
  "user_id": "<uuid>",
  "api_key": "fc-...",
  "registration_id": "reg_...",
  "registration_type": "agent-provider",
  "credential_type": "api_key",
  "credential": "fc-...",
  "credential_expires": null,
  "scopes": ["firecrawl:global"]
}
```

Use `api_key` or `credential` as the bearer token in Step 4. Both contain the same Firecrawl API key value.

Credits are scoped to the Firecrawl team/org, not to an individual API key. A newly-created Firecrawl account receives the Free plan allowance, currently 1,000 monthly credits. If the assertion maps to an existing Firecrawl user, this flow mints another API key for that user's existing team and does not grant separate credits.

## Step 4 - Use the Credential

Present the Firecrawl API key as a bearer token:

```http
POST https://api.firecrawl.dev/v2/scrape
Authorization: Bearer <fc-...>
Content-Type: application/json
```

Full API reference: `https://docs.firecrawl.dev/`.

If you get a 401 on a previously-working credential, drop the credential and restart discovery. Do not stash the credential and retry indefinitely.

## Errors

Firecrawl returns OAuth-style JSON errors:

```json
{
  "error": "invalid_request",
  "error_description": "..."
}
```

### Error codes

| Code                          | HTTP | Retryable | What to do                                                                                                                                                        |
| ----------------------------- | ---- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `invalid_request`             | 400  | No        | Fix the JSON body or required registration fields.                                                                                                                |
| `unsupported_credential_type` | 400  | No        | Use `requested_credential_type: "api_key"`. Firecrawl does not issue other credential types through `/agent/auth` today.                                          |
| `invalid_signature`           | 401  | No\*      | Mint a fresh WorkOS ID-JAG with `alg: RS256` and a valid signature.                                                                                               |
| `audience_mismatch`           | 401  | No\*      | Set `aud` to the Protected Resource Metadata `resource` (`https://api.firecrawl.dev/`).                                                                           |
| `credential_expired`          | 401  | Yes\*     | Mint a fresh WorkOS ID-JAG with a near-term `exp` (about 5 minutes).                                                                                              |
| `issuer_not_enabled`          | 401  | No        | Use `iss: https://auth.workos.bot` from WorkOS.                                                                                                                   |
| `invalid_client_id`           | 401  | No        | Use a WorkOS ID-JAG with a Firecrawl-trusted `client_id`.                                                                                                         |
| `missing_verified_email`      | 401  | No        | Include `email_verified: true` in the ID-JAG payload.                                                                                                             |
| `replay_detected`             | 401  | No        | Mint a fresh WorkOS ID-JAG with a new `jti`. Do not retry the same assertion.                                                                                     |
| `rate_limited`                | 429  | Yes       | Wait before retrying with a fresh WorkOS ID-JAG.                                                                                                                  |
| `invalid_assertion`           | 401  | No\*      | Mint a fresh WorkOS ID-JAG with correct issuer, audience, type, signature, expiry, and verified email. Used when the failure does not match a more specific code. |
| `server_error`                | 500  | Yes       | Retry with backoff. Indicates a Firecrawl-side failure after the JWT was accepted (provisioning or replay-store outage)—not an assertion fault.                   |

\*Retryable only after fixing the underlying assertion (mint a fresh ID-JAG). Do not retry the same assertion indefinitely.

### WorkOS naming reference

Firecrawl uses canonical error names in responses. When integrating against [WorkOS auth.md](https://workos.com/auth-md/docs/apps), map as follows:

| Firecrawl code                | WorkOS equivalent             |
| ----------------------------- | ----------------------------- |
| `audience_mismatch`           | `invalid_audience`            |
| `credential_expired`          | `expired`                     |
| `issuer_not_enabled`          | `invalid_issuer`              |
| `invalid_signature`           | `invalid_signature`           |
| `invalid_client_id`           | `invalid_client_id`           |
| `missing_verified_email`      | `missing_verified_email`      |
| `unsupported_credential_type` | `unsupported_credential_type` |
| `replay_detected`             | `replay_detected`             |

Firecrawl uses `error_description` in JSON responses; WorkOS examples use `message`. HTTP status codes for assertion failures are Firecrawl choices unless noted elsewhere (for example OTP flows in the full WorkOS guide).

## Revocation

Your Firecrawl API key can be revoked by the agent provider (WorkOS) — for example when the user signs out or unlinks the agent at the provider. Revocation is **provider-driven**: the provider notifies Firecrawl directly, so there is nothing for you to call.

You detect a revocation the same way as any dead credential: a previously-working key starts returning `401`. When that happens, drop the key and start over at Step 1 — mint a fresh ID-JAG and register again.
