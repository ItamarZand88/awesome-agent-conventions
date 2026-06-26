<!-- source: apify — https://apify.com/auth.md -->
# auth.md - Apify agent registration

You are an agent. Apify is a cloud platform and marketplace for web data extraction and automation tools called Actors. This file describes how agents should onboard to Apify.

**Canonical URL:** `https://apify.com/auth.md`

**Status:** Preview. Apify is publishing this document first so agents can discover the planned registration flow. The endpoint URLs and response shapes below are provisional and may change before native `auth.md` registration is generally available. Until the discovery metadata advertises supported flows, use one of the fallback paths below.

## Current fallback paths

Use these paths while native `auth.md` registration is rolling out:

1. **MCP with a user present:** connect to `https://mcp.apify.com` and complete OAuth in the browser.
2. **API token:** ask the user for an Apify API token from `https://console.apify.com/settings/integrations` and send it as `Authorization: Bearer <APIFY_TOKEN>`.
3. **No Apify account and paid Actor access:** use x402 for supported Pay Per Event Actors. See `https://docs.apify.com/platform/integrations/x402`.

For broader agent guidance, read `https://apify.com/.well-known/agents.md`.

## Step 1 - Discover

Discovery uses OAuth Protected Resource Metadata and Authorization Server Metadata.

Discovery metadata for native `auth.md` registration is not available yet. When enabled, agents should fetch the protected resource metadata from the API resource server:

```http
GET https://api.apify.com/.well-known/oauth-protected-resource
```

Planned shape:

```json
{
    "resource": "https://api.apify.com/v2/",
    "resource_name": "Apify",
    "resource_logo_uri": "https://apify.com/img/logo.svg",
    "authorization_servers": ["https://api.apify.com/"],
    "scopes_supported": ["actor.read", "actor.run", "dataset.read"],
    "bearer_methods_supported": ["header"]
}
```

Then fetch the authorization server metadata:

```http
GET https://api.apify.com/.well-known/oauth-authorization-server
```

Planned `agent_auth` block:

```json
{
    "agent_auth": {
        "skill": "https://apify.com/auth.md",
        "register_uri": "https://api.apify.com/v2/agent/auth",
        "claim_uri": "https://api.apify.com/v2/agent/auth/claim",
        "revocation_uri": "https://api.apify.com/v2/agent/auth/revoke",
        "identity_types_supported": ["anonymous", "identity_assertion"],
        "anonymous": {
            "credential_types_supported": ["api_key"]
        },
        "identity_assertion": {
            "assertion_types_supported": ["verified_email", "urn:ietf:params:oauth:token-type:id-jag"],
            "credential_types_supported": ["api_key", "access_token"]
        },
        "events_supported": ["https://schemas.workos.com/events/agent/auth/identity/assertion/revoked"]
    }
}
```

Until these metadata endpoints return supported flows, use the fallback paths above.

## Step 2 - Pick a method

Use this order:

1. If you have a provider-issued ID-JAG for this user and Apify trusts the issuer, use `identity_assertion` with `urn:ietf:params:oauth:token-type:id-jag`.
2. If you only know the user's email, use `identity_assertion` with `verified_email`.
3. If you have no user identity, use `anonymous`.

Before sending any user identity to Apify, show the user the service name (`Apify`), logo, and scope set you will receive.

## Step 3 - Register

### Anonymous

```http
POST https://api.apify.com/v2/agent/auth
Content-Type: application/json

{
    "type": "anonymous",
    "requested_credential_type": "api_key"
}
```

Successful response:

```json
{
    "registration_id": "reg_...",
    "registration_type": "anonymous",
    "credential_type": "api_key",
    "credential": "apify_api_...",
    "credential_expires": null,
    "scopes": ["actor.read", "actor.run", "dataset.read"],
    "claim_url": "https://api.apify.com/v2/agent/auth/claim",
    "claim_token": "clm_...",
    "claim_token_expires": "2026-05-21T17:26:32.915Z",
    "post_claim_scopes": ["actor.read", "actor.run", "dataset.read"]
}
```

Use the credential immediately. If the user wants to keep the account, continue to the claim ceremony.

### Verified email

```http
POST https://api.apify.com/v2/agent/auth
Content-Type: application/json

{
    "type": "identity_assertion",
    "assertion_type": "verified_email",
    "assertion": "user@example.com",
    "requested_credential_type": "api_key"
}
```

Successful response:

```json
{
    "registration_id": "reg_...",
    "registration_type": "email-verification",
    "claim_url": "https://api.apify.com/v2/agent/auth/claim",
    "claim_token": "clm_...",
    "claim_token_expires": "2026-05-21T17:31:25.994Z",
    "post_claim_scopes": ["actor.read", "actor.run", "dataset.read"]
}
```

Apify emails the user. Keep `claim_token` in memory only and continue to the claim ceremony.

### ID-JAG

ID-JAG support is planned for the next phase. If Apify does not list your issuer as trusted, fall back to verified email or anonymous registration.

When enabled, mint the assertion with:

- `aud`: `https://api.apify.com/v2/`
- `iss`: your provider issuer URL
- `email_verified: true` or `phone_number_verified: true`
- Fresh `jti`
- Near-term `exp`

```http
POST https://api.apify.com/v2/agent/auth
Content-Type: application/json

{
    "type": "identity_assertion",
    "assertion_type": "urn:ietf:params:oauth:token-type:id-jag",
    "assertion": "<ID-JAG>",
    "requested_credential_type": "access_token"
}
```

## Step 4 - Claim ceremony

For anonymous registrations, trigger the claim email:

```http
POST https://api.apify.com/v2/agent/auth/claim
Content-Type: application/json

{
    "claim_token": "clm_...",
    "email": "user@example.com"
}
```

Successful response:

```json
{
    "registration_id": "reg_...",
    "claim_attempt_id": "cla_...",
    "status": "initiated",
    "expires_at": "2026-05-21T17:36:32.915Z"
}
```

Ask the user: "Check your email and tell me the 6-digit code."

Submit the OTP:

```http
POST https://api.apify.com/v2/agent/auth/claim/complete
Content-Type: application/json

{
    "claim_token": "clm_...",
    "otp": "123456"
}
```

Successful anonymous response:

```json
{
    "registration_id": "reg_...",
    "status": "claimed"
}
```

The existing pre-claim API key keeps working. Its account ownership is upgraded in place.

Successful verified-email response:

```json
{
    "registration_id": "reg_...",
    "status": "claimed",
    "credential_type": "api_key",
    "credential": "apify_api_...",
    "credential_expires": null,
    "scopes": ["actor.read", "actor.run", "dataset.read"]
}
```

## Step 5 - Use the credential

Send the credential as a bearer token:

```http
GET https://api.apify.com/v2/acts
Authorization: Bearer <credential>
```

Useful starting points:

- API reference: `https://docs.apify.com/api/v2`
- Actor discovery: `https://apify.com/store`
- MCP server: `https://mcp.apify.com`
- Agent guide: `https://apify.com/.well-known/agents.md`

If an API call returns `401` for a previously working credential, drop the credential and restart discovery.

## Errors

| Code | Where | What to do |
| --- | --- | --- |
| `invalid_signature` | `/agent/auth` ID-JAG | Mint a fresh ID-JAG. |
| `replay_detected` | `/agent/auth` ID-JAG | Mint a fresh ID-JAG with a new `jti`. |
| `audience_mismatch` | `/agent/auth` ID-JAG | Mint with `aud` set to `https://api.apify.com/v2/`. |
| `credential_expired` | `/agent/auth` ID-JAG | Mint a fresh assertion. |
| `anonymous_not_enabled` | `/agent/auth` | Pick verified email or use a fallback path. |
| `verified_email_not_enabled` | `/agent/auth` | Pick anonymous or use a fallback path. |
| `issuer_not_enabled` | `/agent/auth` | Pick verified email or anonymous registration. |
| `unsupported_credential_type` | `/agent/auth` | Re-read metadata and choose a supported credential type. |
| `rate_limited` | any | Back off and retry later. |
| `invalid_claim_token` | `/agent/auth/claim` or `/agent/auth/claim/complete` | Restart registration. |
| `otp_invalid` | `/agent/auth/claim/complete` | Ask the user to re-read the code. |
| `otp_expired` | `/agent/auth/claim/complete` | Re-trigger the claim email or restart registration. |
| `claim_expired` | `/agent/auth/claim/complete` | Restart registration. |
| `previously_claimed` | `/agent/auth/claim/complete` | Restart if you need a fresh credential. |

Retry 5xx responses with exponential backoff. Do not retry the same 4xx payload unless the error table says to.

## Revocation

Agents do not initiate revocation. If a credential stops working and the API returns `401`, discard it and restart discovery.

Provider-driven revocation for ID-JAG flows is expected at:

```http
POST https://api.apify.com/v2/agent/auth/revoke
Content-Type: application/logout+jwt
```
