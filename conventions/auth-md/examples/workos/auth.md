<!-- source: workos.com — https://workos.com/auth.md -->
# auth.md

Not an agent? You might be looking for https://workos.com/auth-md.

You are an agent. This document tells you how to register a credential for **WorkOS one-shot environments** — temporary, anonymous WorkOS environments you can provision without an account and (optionally) have the user claim later to make permanent. Follow the steps in order; do not skip ahead.

This is the **user claimed** flow: provision anonymously, work immediately, claim when the user is available. There is no agent-verified or email-verified registration today.

Endpoints live at `https://api.workos.com`. The claim ceremony happens at `https://dashboard.workos.com`.

## Shortcut: use the `workos` CLI (recommended when Node is available)

If the host has **Node.js ≥ 22.11**, prefer the `workos` CLI — it performs every step in this document, plus writes credentials to your project's `.env.local` / `.env`, detects your framework (Next.js, React Router, TanStack, etc.), and wires up the AuthKit integration.

```bash
# Provision a one-shot environment and install AuthKit into the current project.
npx workos@latest install

# Later, when the user is available, claim the environment.
npx workos@latest env claim
```

The CLI auto-detects non-TTY / agent contexts (`CLAUDECODE`, `CURSOR_AGENT`, `CODEX_SANDBOX`) and emits structured JSON to stdout — you do not need to pass `--json`. Exit codes follow `gh` conventions (`0` success, `1` error, `2` cancelled, `4` auth required).

If Node is not available, or you need finer-grained control, follow the raw HTTP steps below.

## Step 1 — Provision the environment

*CLI shortcut: `npx workos@latest install` (Node ≥ 22.11).*

```http
POST /x/one-shot-environments HTTP/1.1
Host: api.workos.com
```

No request body. No authentication.

Response (200):

```json
{
  "clientId": "client_01ABC123...",
  "apiKey": "sk_test_...",
  "claimToken": "clm_...",
  "authkitDomain": "<subdomain>.authkit.app"
}
```

The API may respond in snake_case (`client_id`, `api_key`, `claim_token`, `authkit_domain`) — accept either.

What each field is:

- `apiKey` — your bearer credential for the WorkOS API. Use it immediately ([Step 2](#step-2--use-the-credential)).
- `clientId` — identifies the environment. Required for the claim flow ([Step 3](#step-3--claim-ceremony-optional)) and for any AuthKit integration you configure.
- `claimToken` — single-use handle for the claim ceremony. Returned **exactly once** — persist it alongside `apiKey` (e.g. as `WORKOS_CLAIM_TOKEN`); do not log it. Without it, the environment cannot be claimed.
- `authkitDomain` — the hosted AuthKit subdomain for this environment. Informational; you don't pass it in auth requests.

## Step 2 — Use the credential

```http
GET /<resource> HTTP/1.1
Host: api.workos.com
Authorization: Bearer <apiKey>
```

The credential works against the WorkOS API the moment it's issued — full scope, no degraded mode. Endpoints may surface a warning that the environment is unclaimed; that's informational, not an auth failure.

If you get a 401 on a previously-working `apiKey`: the environment was revoked or claimed away. Drop the credential and restart at [Step 1](#step-1--provision-the-environment). Do not stash and retry.

## Step 3 — Claim ceremony (optional)

*CLI shortcut: `npx workos@latest env claim` (Node ≥ 22.11).*

Claim links the environment to a user's WorkOS account, making the credential permanent and giving the user a place to manage it. Skip this if the user isn't available — the unclaimed credential keeps working.

### 3a. Mint a claim nonce

```http
POST /x/one-shot-environments/claim-nonces HTTP/1.1
Host: api.workos.com
Content-Type: application/json

{
  "client_id": "<clientId>",
  "claim_token": "<claimToken>"
}
```

Response (200):

```json
{ "nonce": "..." }
```

If the response is 409, the environment is already claimed. Stop the ceremony — the credential is already permanent.

### 3b. Send the user to the dashboard

Construct the claim URL:

```
https://dashboard.workos.com/claim?nonce=<nonce>
```

Surface this in your agent UI. Suggested prompts:

- Default ask: "Open this link to claim the environment to your WorkOS account: `<URL>`"
- If the user has no WorkOS account: "You'll be prompted to sign in or create a free account first — that's expected."
- If the user can't open the link in-place: "Paste this URL into a browser: `<URL>`"

### 3c. Poll for completion

The user signs in and confirms the claim in the dashboard. To detect completion, re-POST the request from [3a](#3a-mint-a-claim-nonce) every 5 seconds with the same `client_id` and `claim_token`:

- 200 with a fresh `nonce` → still pending; keep polling. Discard these nonces — only the one from 3a is bound to the URL you gave the user.
- 409 → claimed. Stop polling; the credential is permanent.
- 401 → claim token invalidated by the claim. Also means claimed. Stop polling.

Time out polling after ~5 minutes. If it hasn't completed, give the user the URL again and stop blocking — they can finish asynchronously, and `apiKey` keeps working unclaimed in the meantime.

## Errors

| Status | Where                                   | Meaning                                                | What to do                                                                          |
| ------ | --------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| 401    | `/x/one-shot-environments/claim-nonces` | `claim_token` invalid, or invalidated by a prior claim | If you've already started a claim, treat as success. Otherwise restart at Step 1.   |
| 404    | `/x/one-shot-environments/claim-nonces` | Environment not found for that `client_id`             | Restart at Step 1.                                                                  |
| 409    | `/x/one-shot-environments/claim-nonces` | Environment already claimed                            | Stop the ceremony — the credential is permanent.                                    |
| 429    | any                                     | Rate limited                                           | Exponential backoff, retry.                                                         |
| 5xx    | any                                     | Transient server error                                 | Exponential backoff, retry the same request.                                        |

Retry policy:

- 5xx → exponential backoff, retry the same request.
- 4xx other than 429 → do not retry the same payload; act on the table above.
- 401 on a previously-working `apiKey` → drop the credential and restart at [Step 1](#step-1--provision-the-environment).

Full API reference: <https://workos.com/docs/reference>.
