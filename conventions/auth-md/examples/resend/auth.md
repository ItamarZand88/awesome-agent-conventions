<!-- source: resend — https://resend.com/auth.md -->
# auth.md

You are an agent that wants to call the Resend API on a user's behalf. This file describes how to obtain credentials today and how to handle them safely.

Two hosts are relevant:

- **Resource server** — `https://api.resend.com` — the API you will call.
- **Dashboard** — `https://resend.com` — where the user manages their account.

## Current state

Resend does not support agentic registration today. Credentials are issued by the user out of band; this file tells you how to pick them up and use them without putting them at risk.

## Use the existing tooling first

Before you do anything credential-shaped, check whether the user has already wired Resend into your environment.

1. **Resend MCP server** — if you are an MCP client (Claude, Cursor, Codex, etc.), Resend ships an official MCP server that exposes emails, contacts, broadcasts, domains, segments, and more as tools. The user configures it once with their key; you call the tools without ever seeing the key. Discovery: `https://resend.com/.well-known/mcp.json`. Repository: `https://github.com/resend/resend-mcp`.
2. **Resend Agent Skills** — guidance documents that teach you the gotchas (idempotency keys, webhook verification, template syntax, inbound-email safety, deliverability). Index: `https://resend.com/.well-known/agent-skills/index.json`. Load the relevant `SKILL.md` before calling the API directly.
3. **Resend CLI** — if you are running shell commands, prefer `resend` over hand-rolled `curl`. It handles auth resolution, retries, and non-interactive flags. Install: `curl -fsSL https://resend.com/install.sh | bash`. Repository: `https://github.com/resend/resend-cli`.

If any of these is already configured, use it and stop. Do not ask the user for an API key you do not need.

## Supported login option: API key, supplied out of band

The only credential is a Resend API key (prefix `re_`). The user issues it from `https://resend.com/api-keys` and supplies it to you through a secure channel — never by pasting it into chat.

### How to pick the key up

Look for it in this order. Stop at the first one that exists:

1. `--api-key` on the `resend` CLI, if the user passed one for this invocation.
2. `RESEND_API_KEY` in your process environment.
3. A project `.env` file the user has told you to read.
4. The user's CLI config, populated via `resend login --key` (used automatically when you invoke the `resend` CLI).
5. The MCP server's environment, if you are calling through it.

If none of the above is set and you genuinely need a key, **do not ask the user to paste it into the conversation**. Instead, tell them to:

- Create one at `https://resend.com/api-keys` with the narrowest scope that fits the task ("Sending access" rather than "Full access" when you only need to send mail; restrict to a single domain when possible).
- Put it in `RESEND_API_KEY` in their shell, `.env`, MCP client config, or `resend login --key` — whichever matches how they invoke you.
- Resume the task once it is set.

This keeps the key out of your transcript, out of any logs the user shares, and out of the model provider's training data.

### How to use the key

Present it as a bearer token:

```http
POST /emails HTTP/1.1
Host: api.resend.com
Authorization: Bearer $RESEND_API_KEY
Content-Type: application/json
```

Read it from the environment at the moment of the call. Do not copy it into variables you log, do not echo it back to the user, do not include it in commit messages, PR descriptions, error reports, or screenshots. If you are running a shell command, never interpolate the key inline — reference the environment variable so it does not appear in command history.

The key does not expire on its own. Treat a `401` on a previously-working key as revocation: drop it from memory and ask the user to refresh whichever source you read it from.

### Errors

| Status | Meaning | What to do |
| --- | --- | --- |
| `401` on first use | Key is malformed, revoked, or for a different environment. | Ask the user to confirm the value in their `RESEND_API_KEY` / config is current and active in the dashboard. |
| `401` on a previously-working key | Revoked or rotated. | Drop the cached value and ask the user to refresh it from their secret store, not from chat. |
| `403` | Key lacks permission for this resource. | Ask the user to re-issue with the required permission level or domain scope. |
| `429` | Rate limited. | Back off and retry. Honor `Retry-After` if present. |

## Revocation

The user revokes keys at `https://resend.com/api-keys`. You will discover revocation as a `401` on a previously-working credential — drop it and re-read from the same source you loaded it from.
