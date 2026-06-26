<!-- source: knock — https://knock.app/auth.md -->
# auth.md

You are an agent that wants to call Knock on a user's behalf — either the Knock API (to send and manage notifications) or the Management API and CLI (to manage notification resources). This file describes how to obtain credentials today and how to use them safely.

Knock is notification infrastructure: a single API for sending and managing product notifications across email, in-app feeds, push, SMS, chat, and more, with workflows, preferences, and templates managed from the Knock dashboard.

The hosts that matter:

- **Resource server (Knock API)** — `https://api.knock.app` — the REST API for sending notifications, triggering workflows, and managing recipients, preferences, and messages. Authenticated with an environment **API key** (`sk_…`).
- **Management API** — `https://control.knock.app` — the REST API for managing your Knock resources as code (workflows, templates, layouts, translations, partials, and commits/promotions between environments). Authenticated with an account **service token** (`knock_st_…`). This is also what the `knock` CLI uses.
- **Dashboard** — `https://dashboard.knock.app` — where the user manages their account, environments, API keys, and service tokens.
- **Docs** — `https://docs.knock.app` — reference for every endpoint, SDK, and concept.

## Which credential do I need?

Knock has two separate REST surfaces with two separate, non-interchangeable credentials. Pick the one that matches your task:

- **Sending or reading notification data** — trigger a workflow, identify a user, fetch messages or preferences → use the **Knock API** with a secret **API key** (`sk_…`).
- **Managing notification resources** — create or update workflows, templates, layouts, translations, or partials; commit and promote changes between environments → use the **Management API** (or the `knock` CLI) with a **service token** (`knock_st_…`).

A secret API key cannot call the Management API, and a service token cannot call the Knock API. They are not interchangeable.

## Current state

Knock does not support agentic OAuth registration today. There is no `identity_assertion`, `service_auth`, or `anonymous` claim flow, and no `/agent/identity` endpoint. Credentials are issued by the user out of band; this file tells you how to pick them up and use them without putting them at risk. When Knock ships the [auth.md](https://workos.com/auth-md/docs) agent-registration flows, this document and the Protected Resource Metadata at `https://api.knock.app/.well-known/oauth-protected-resource` will be the source of truth.

## Use the existing tooling first

Before you do anything credential-shaped, check whether the user has already wired Knock into your environment.

1. **Knock MCP server** — if you are an MCP client (Claude, Cursor, Codex, etc.), Knock ships an official MCP server that exposes workflows, messages, recipients, guides, and more as tools. The user configures it once with their key; you call the tools without ever seeing the key. See `https://docs.knock.app/ai/mcp-server`.
2. **Knock AI agent** — an in-dashboard agent that can build and manage Knock resources for a signed-in user. See `https://docs.knock.app/ai/agent`.
3. **Knock CLI** — if you are running shell commands, prefer the `knock` CLI over hand-rolled `curl`. It handles auth resolution and environment selection. The CLI authenticates against the Management API with a **service token** (`knock_st_…`), not an API key. See `https://docs.knock.app/cli/overview`.

If any of these is already configured, use it and stop. Do not ask the user for an API key you do not need.

## Knock API: API key, supplied out of band

Use this when your task is sending or reading notification data (triggering workflows, identifying recipients, fetching messages or preferences) against `https://api.knock.app`.

The credential is a Knock secret API key (prefix `sk_`). The user issues it from the API keys page of their environment at `https://dashboard.knock.app` and supplies it to you through a secure channel — never by pasting it into chat.

Key types and scope:

- **Secret keys (`sk_test_…`, `sk_live_…`)** — full server-side access, scoped to a single environment (e.g. development or production). This is what you authenticate the REST API with.
- **Public keys (`pk_test_…`, `pk_live_…`)** — safe for client-side use only (e.g. rendering in-app feeds). They cannot perform server-side actions; do not use them to call the API on a user's behalf.

There are no granular OAuth scopes today. A secret key carries the full permissions of its environment, so prefer a **test/development** key and switch to a production key only when the task genuinely requires production data.

### How to pick the key up

Look for it in this order. Stop at the first one that exists:

1. `--api-key` (or equivalent flag) on the `knock` CLI, if the user passed one for this invocation.
2. `KNOCK_API_KEY` (or `KNOCK_SECRET_API_KEY`) in your process environment.
3. A project `.env` file the user has told you to read.
4. The MCP server's environment, if you are calling through it.

If none of the above is set and you genuinely need a key, **do not ask the user to paste it into the conversation**. Instead, tell them to:

- Create one in the Knock dashboard for the narrowest environment that fits the task (a development key rather than a production key whenever possible).
- Put it in `KNOCK_API_KEY` in their shell, `.env`, or MCP client config — whichever matches how they invoke you.
- Resume the task once it is set.

This keeps the key out of your transcript, out of any logs the user shares, and out of the model provider's training data.

### How to use the key

Present it as a bearer token:

```http
POST /v1/workflows/welcome/trigger HTTP/1.1
Host: api.knock.app
Authorization: Bearer $KNOCK_API_KEY
Content-Type: application/json
```

Read it from the environment at the moment of the call. Do not copy it into variables you log, do not echo it back to the user, do not include it in commit messages, PR descriptions, error reports, or screenshots. If you are running a shell command, never interpolate the key inline — reference the environment variable so it does not appear in command history.

The key does not expire on its own. Treat a `401` on a previously-working key as revocation: drop it from memory and ask the user to refresh whichever source you read it from.

### Errors

| Status | Meaning | What to do |
| --- | --- | --- |
| `401` on first use | Key is malformed, revoked, or for the wrong environment (e.g. a public key, or a test key against production data). | Ask the user to confirm the value in their `KNOCK_API_KEY` / config is a current secret key for the right environment. |
| `401` on a previously-working key | Revoked or rotated. | Drop the cached value and ask the user to refresh it from their secret store, not from chat. |
| `403` | Key lacks access to the requested resource or environment. | Ask the user to use a key for the correct environment, or to grant the needed access. |
| `422` | Request is well-formed but invalid (bad params, missing recipient, etc.). | Fix the request per the error body; do not retry unchanged. |
| `429` | Rate limited. | Back off and retry. Honor `Retry-After` if present. |

## Management API and CLI: service token, supplied out of band

Use this when your task is managing notification resources (creating or updating workflows, templates, layouts, translations, or partials; committing and promoting changes between environments) against `https://control.knock.app`, or when you are driving the `knock` CLI.

The credential is a Knock service token (prefix `knock_st_`). The user generates it from **Settings → Service tokens** in the dashboard and supplies it to you through a secure channel — never by pasting it into chat.

Scope and privilege:

- A service token is scoped to the whole **account** (not a single environment) and **inherits the owner/admin privilege** of the user who created it. There are no granular scopes today, so treat it as a high-privilege credential with full access to the Management API.
- Only account **owners or admins** can generate or revoke service tokens.
- A service token authenticates the **Management API and CLI only**. It cannot call the Knock API (`api.knock.app`), and a secret API key cannot call the Management API.

### How to pick the service token up

Look for it in this order. Stop at the first one that exists:

1. `--service-token` (or equivalent flag) on the `knock` CLI, if the user passed one for this invocation.
2. `KNOCK_SERVICE_TOKEN` in your process environment.
3. The CLI's own stored credentials, if the user has already run the CLI's login/auth flow (let the CLI resolve auth itself rather than reading the token directly).
4. A project `.env` file the user has told you to read.

If none of the above is set and you genuinely need one, **do not ask the user to paste it into the conversation**. Instead, tell them to:

- Generate one in the dashboard under **Settings → Service tokens** (owners/admins only). It is shown **once** at creation and cannot be retrieved again, so they must copy it to a secure location immediately.
- Put it in `KNOCK_SERVICE_TOKEN` in their shell, `.env`, or CLI config — whichever matches how they invoke you.
- Resume the task once it is set.

### How to use the service token

Present it as a bearer token against the Management API host:

```http
GET /v1/workflows HTTP/1.1
Host: control.knock.app
Authorization: Bearer $KNOCK_SERVICE_TOKEN
Content-Type: application/json
```

The same secret-handling rules apply as for API keys: read it from the environment at the moment of the call, never log or echo it, never interpolate it inline in shell commands, and keep it out of commit messages, PR descriptions, error reports, and screenshots. Changes made with a service token are attributed to it in the account's audit logs.

### Exchanging a service token for an API key

If you have a service token but the task you need to perform is on the **Knock API** (the data plane), you do not need the user to issue a separate `sk_` key. The Management API can exchange a service token for a secret API key scoped to a given environment:

```http
POST /v1/api_keys/exchange?environment=development HTTP/1.1
Host: control.knock.app
Authorization: Bearer $KNOCK_SERVICE_TOKEN
```

The `environment` query parameter is the environment slug (e.g. `development` or `production`) and is required. A successful response returns the secret key:

```json
{ "api_key": "sk_1234567890" }
```

Use the returned `sk_…` key as the bearer token against `https://api.knock.app` per the Knock API section above, and apply the same secret-handling rules. This is an explicit, deliberate bridge from the control plane to the data plane — the service token itself still cannot call the Knock API directly.

## Revocation

The user revokes and rotates **API keys** from the API keys page of each environment, and **service tokens** from Settings → Service tokens, in the Knock dashboard. Deleting a service token immediately revokes its access to the Management API and CLI. You will discover revocation as a `401` on a previously-working credential — drop it and re-read from the same source you loaded it from.

## More information

- Pricing: `https://knock.app/pricing`
- Terms of service: `https://knock.app/legal/terms`
- Privacy policy: `https://knock.app/legal/privacy`
- Knock API reference: `https://docs.knock.app/api-reference/overview`
- Management API reference: `https://docs.knock.app/mapi-reference/overview`
- Service tokens: `https://docs.knock.app/developer-tools/service-tokens`

## Contact

If you are integrating with Knock and something here is wrong or missing, reach out at `support@knock.app`.
