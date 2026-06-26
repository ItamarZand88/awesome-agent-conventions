<!-- source: monday — https://monday.com/auth.md -->
# auth.md

This file tells agents how to register for monday.com on behalf of a user.

monday.com is the most advanced AI Work OS that powers teams to run projects and workflows with confidence.

- **Resource server**: `https://api.monday.com`
- **Authorization server**: `https://signup-logic.monday.com`

## 1. Discover

### Protected Resource Metadata

Fetch `GET https://monday.com/.well-known/oauth-protected-resource`

### Authorization Server Metadata

Fetch `GET https://monday.com/.well-known/oauth-authorization-server`

The `agent_auth` block tells you:
- `register_uri` — where to POST registration requests
- `identity_types_supported` — `["anonymous"]`
- `credential_types_supported` — `["api_key"]`
- `skill` — URL to the detailed registration skill

## 2. Pick a Method

monday.com currently supports **captcha-verified registration**. The agent solves a server-side challenge to prove it is a capable agent, then creates an account.

| Agent has | Method |
|-----------|--------|
| Nothing | Captcha challenge → account creation |

## 3. Register

Registration is a 3-step flow:

### Step 1: Get a captcha challenge

```http
POST /signup-logic/agent-captcha/challenge/v1 HTTP/1.1
Host: signup-logic.monday.com
Content-Type: application/json

{}
```

Returns a `challenge` object with `id`, `type`, `prompt`, and a `challengeToken` (30s TTL).

Challenge types: `binary`, `string`, `count`, `sort`, `math`, `expression`.

### Step 2: Verify your answer

```http
POST /signup-logic/agent-captcha/verify/v1 HTTP/1.1
Host: signup-logic.monday.com
Content-Type: application/json

{
  "answer": "<your_answer>",
  "challengeToken": "<token_from_step_1>"
}
```

Returns a `verificationToken` (60s TTL, single-use).

### Step 3: Create the account

```http
POST /signup-logic/agent-signup/account/v1 HTTP/1.1
Host: signup-logic.monday.com
Content-Type: application/json

{
  "verificationToken": "<token_from_step_2>",
  "agreed_to_terms": true
}
```

Optional fields: `email`, `password`, `name`, `source`.

Returns: `email`, `password`, `api_token`, `account_url`, `login_url`, `board_id`.

## 4. Use the Credential

```http
POST /v2 HTTP/1.1
Host: api.monday.com
Content-Type: application/json
Authorization: <api_token>

{"query": "{ me { id name email } }"}
```

Note: monday.com uses `Authorization: <token>` without the "Bearer" prefix.

On any 401 from a previously-working credential, drop it and restart at Step 1.

## 5. Errors

| Error | Endpoint | Action |
|-------|----------|--------|
| `wrong_answer` | /verify | Get a new challenge |
| `expired` | /verify | Challenge expired (30s) — get a new one |
| `invalid_token` | /verify | Malformed token — get a new challenge |
| 400 (missing verificationToken) | /account | Restart from step 1 |
| 403 (expired/used token) | /account | Restart from step 1 |
| 429 | Any | Rate limited — wait 60s |
| 503 | /account | Service temporarily down |

## 6. Detailed Skill Reference

For full field descriptions, onboarding parameters, and post-creation flows, see:
https://monday.com/.well-known/agent-skills/signup-for-agents/SKILL.md

## 7. Links

- [monday.com API Documentation](https://developer.monday.com/api-reference)
- [Terms of Service](https://monday.com/terms-of-service)
- [Privacy Policy](https://monday.com/privacy-policy)
