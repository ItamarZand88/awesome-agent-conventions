<!-- source: webclaw — https://webclaw.io/auth.md -->
# webclaw auth

You are an agent that wants to call the webclaw Cloud API on a user's behalf.
This file describes how to obtain credentials today and how to handle them
safely.

Two hosts are relevant:

- **Resource server**: https://api.webclaw.io. This is the API you will call.
- **Dashboard**: https://webclaw.io. This is where the user manages keys, billing,
  and usage.

## Current state

webclaw supports OAuth 2.0 Device Authorization for agent onboarding. Agents
can request a short-lived scoped bearer token, show the user a code, and wait
while the user approves the request in the browser.

Dashboard-issued bearer API keys are still supported and are best for long
running backends, CI jobs, and MCP configs. Prefer agent-scoped keys with only
the endpoint scopes required for the task.

Do not claim a subscription silently.

## Use existing tooling first

Before you handle credentials directly, check whether the user has already
configured webclaw through a tool layer.

1. **webclaw MCP server**. If you are an MCP client, prefer the local
   `webclaw-mcp` server. The user can configure it once with
   `WEBCLAW_API_KEY`, and you can call the tools without seeing the key.
   Discovery: https://webclaw.io/.well-known/mcp/server-card.json. Docs:
   https://webclaw.io/docs/mcp.
2. **Agent skills**. Load the relevant webclaw skill before calling the API
   directly. Index: https://webclaw.io/.well-known/agent-skills/index.json.
3. **webclaw CLI**. If you are running shell commands, prefer `webclaw`
   over hand-written HTTP requests when it is already installed. The CLI reads
   `--api-key` and `WEBCLAW_API_KEY`. Docs: https://webclaw.io/docs/cli.
4. **SDKs**. For application code, prefer the official SDK for the user's
   language when available. Docs: https://webclaw.io/docs/sdks.

If one of these is already configured, use it and stop. Do not ask the user for
an API key you do not need.

## Authentication

Cloud API requests use bearer tokens in the Authorization header. A bearer token
can be either a dashboard API key or a short-lived device-flow access token.

```http
Authorization: Bearer wc_live_...
```

## OAuth device authorization for agents

Use this flow when you are an agent, CLI, IDE extension, or local tool and the
user has not already configured `WEBCLAW_API_KEY`.

1. Discover the authorization server:

   https://webclaw.io/.well-known/oauth-authorization-server

2. Start the device flow:

   ```http
   POST https://api.webclaw.io/oauth/device_authorization
   Content-Type: application/x-www-form-urlencoded

   client_id=your-agent-name&scope=scrape%20extract
   ```

3. Show the user `user_code` and `verification_uri_complete`.
4. Poll `https://api.webclaw.io/oauth/token` with
   `grant_type=urn:ietf:params:oauth:grant-type:device_code` and the returned
   `device_code`. Respect `interval`, `authorization_pending`, and
   `slow_down`.
5. Store the returned `access_token` in the agent or tool secret manager. It is
   a short-lived scoped bearer token.

Device-flow tokens expire after one hour. For persistent production services,
ask the user to create a dashboard API key instead.

API keys are created and revoked from the dashboard:

https://webclaw.io/dashboard/api-keys

For agent integrations, create an **agent-scoped key** and select only the
endpoint scopes needed for the task. Prefer an expiration date for temporary
agents, CI jobs, demos, and one-off workflows.

## How to pick up the key

Look for a key in this order. Stop at the first source that exists:

1. `WEBCLAW_API_KEY` in your process environment.
2. The MCP client configuration, if you are calling through `webclaw-mcp`.
3. `--api-key` passed directly to the `webclaw` CLI for this invocation.
4. A project `.env` file only if the user has explicitly told you to read it.
5. The user's tool or platform secret manager.

If none of these exists and you genuinely need API access, do not ask the user
to paste the key into chat. Tell them to:

1. Open https://webclaw.io/dashboard/api-keys.
2. Create an agent-scoped key.
3. Select the smallest endpoint scopes needed for the task.
4. Add the key to `WEBCLAW_API_KEY`, the MCP client config, CI secrets, or the
   relevant secret manager.
5. Resume the task once the secret is available.

## How to use the key

Present it as a bearer token:

```http
POST /v1/scrape HTTP/1.1
Host: api.webclaw.io
Authorization: Bearer $WEBCLAW_API_KEY
Content-Type: application/json
```

Read the key from the environment or secret store at call time. Do not print it,
log it, store it in source code, commit it, include it in PR descriptions,
screenshots, traces, or debug reports.

## New users

New cloud users must subscribe to a paid plan (Starter from $19/mo) before API
usage. A payment card is required. Agents should send users to:

https://webclaw.io/dashboard

Agents must not attempt to create billable subscriptions silently.

## Endpoint scopes

Agent-scoped keys can be limited to these API areas:

| Scope | Allows |
| --- | --- |
| `scrape` | `POST /v1/scrape` |
| `crawl` | `POST /v1/crawl`, crawl status and crawl pages |
| `map` | `POST /v1/map` |
| `batch` | `POST /v1/batch` |
| `search` | `POST /v1/search` |
| `extract` | `POST /v1/extract` |
| `summarize` | `POST /v1/summarize` |
| `brand` | `POST /v1/brand` |
| `diff` | `POST /v1/diff` |
| `research` | `POST /v1/research` and research status |

When a workflow needs multiple endpoints, select only those scopes. Example:
an agent that extracts structured data from one URL usually needs `extract`,
and may also need `scrape` if it first fetches page content directly.

## Credential types

- **Full-access bearer API key** for trusted backends controlled by the user.
- **Agent-scoped bearer API key** for agents, MCP clients, CI jobs, and
  integrations that only need selected endpoints.

## Errors

| Status | Meaning | What to do |
| --- | --- | --- |
| `401` on first use | Missing, malformed, revoked, or wrong API key. | Re-read the key from the configured secret source. Ask the user to refresh the secret there, not in chat. |
| `401` on a previously working key | The key was revoked or rotated. | Drop any cached value and re-read from the secret source. |
| `402` | Subscription or credits are required. | Send the user to https://webclaw.io/dashboard. Do not start a paid flow silently. |
| `403` | The key is valid but does not have the required scope. | Ask the user to create or update an agent-scoped key with the missing endpoint scope. |
| `429` | Rate limited. | Back off and retry later. Honor retry headers when present. |

## Revocation and rotation

The user revokes or rotates keys from:

https://webclaw.io/dashboard/api-keys

Treat revocation as final. If a key stops working, do not keep retrying with
the same secret indefinitely and do not ask the user to paste a replacement into
chat.

## Discovery

- API docs: https://webclaw.io/docs/api
- OpenAPI: https://webclaw.io/openapi.json
- API catalog: https://webclaw.io/.well-known/api-catalog
- OAuth protected resource metadata: https://webclaw.io/.well-known/oauth-protected-resource
- OAuth authorization server metadata: https://webclaw.io/.well-known/oauth-authorization-server
- MCP server card: https://webclaw.io/.well-known/mcp/server-card.json
- Agent skills: https://webclaw.io/.well-known/agent-skills/index.json
