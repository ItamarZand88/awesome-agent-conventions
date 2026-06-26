<!-- source: nanogpt — https://nano-gpt.com/auth.md -->
# auth.md

NanoGPT supports agent and app access through user-approved API keys. OAuth-aware clients should use authorization-code + PKCE. Agents can also use the browser-approved device login flow for CLI-style handoff.

Resource server: `https://nano-gpt.com/api/v1`
Issuer origin: `https://nano-gpt.com`

## 1. Discover

Fetch protected resource metadata:

```http
GET /.well-known/oauth-protected-resource HTTP/1.1
Host: nano-gpt.com
```

The metadata points to:

- Protected resource metadata: `https://nano-gpt.com/.well-known/oauth-protected-resource`
- Agent registration metadata: `https://nano-gpt.com/.well-known/nanogpt-agent-auth`
- OAuth authorization server metadata: `https://nano-gpt.com/.well-known/oauth-authorization-server`
- Agent capability manifest: `https://nano-gpt.com/api/v1/agent-capabilities`
- API docs: `https://nano-gpt.com/api`
- MCP setup: `https://nano-gpt.com/mcp`

NanoGPT also returns this discovery hint on Chat Completions authentication failures:

```http
WWW-Authenticate: Bearer resource_metadata="https://nano-gpt.com/.well-known/oauth-protected-resource"
```

## 2. Pick A Method

Use one of these methods:

- OAuth key handoff shortcut: Redirect the user to `https://nano-gpt.com/auth?callback_url=...` with S256 PKCE, then exchange the code at `https://nano-gpt.com/api/v1/auth/keys`.
- OAuth PKCE: Redirect the user to `https://nano-gpt.com/oauth/authorize`, then exchange the code at `https://nano-gpt.com/oauth/token`.
- Existing API key: If the user already has a NanoGPT API key, send it as `Authorization: Bearer <key>`.
- User-claimed device login: If the user needs a key, start a device login and ask the user to approve it in the browser.

NanoGPT does not currently support anonymous spend-capable credentials. Agent-verified ID-JAG registration is not enabled yet.

## 3. Scopes

- `models.read`: Read public NanoGPT model catalogs and pricing metadata.
- `api.use`: Use NanoGPT API endpoints with a user-approved API key, bounded by account balance and per-key settings.

OAuth grants use these scopes. NanoGPT API keys are account credentials. Actual access is bounded by account balance, subscriptions, per-key spend and token limits, expiration, allowed origins, and allowed model settings.

Because NanoGPT's OAuth access token is a dedicated API key in this MVP, OAuth authorization requests must include `api.use`. `models.read` can be requested alongside it.

## 4. OAuth Key Handoff Shortcut

For clients that want a short browser-based key handoff, build a URL like:

```text
https://nano-gpt.com/auth?callback_url=http%3A%2F%2F127.0.0.1%3A8000%2Fcallback&code_challenge=...&code_challenge_method=S256&state=...
```

`callback_url` must be HTTPS, or loopback HTTP with an explicit port. NanoGPT requires S256 PKCE for this shortcut. After approval, exchange the returned code:

```http
POST /api/v1/auth/keys HTTP/1.1
Host: nano-gpt.com
Content-Type: application/json
```

```json
{
  "code": "...",
  "code_verifier": "..."
}
```

Success response includes both `key` and OAuth-style `access_token` fields:

```json
{
  "key": "sk-nano-...",
  "access_token": "sk-nano-...",
  "token_type": "Bearer",
  "scope": "models.read api.use",
  "user_id": "..."
}
```

Authenticated clients can also create a one-time authorization code for a downstream app:

```http
POST /api/v1/auth/keys/code HTTP/1.1
Host: nano-gpt.com
Authorization: Bearer sk-nano-...
Content-Type: application/json
```

```json
{
  "redirect_uri": "http://127.0.0.1:8000/callback",
  "code_challenge": "...",
  "code_challenge_method": "S256",
  "limit": 20,
  "usage_limit_type": "weekly",
  "expires_at": "2099-07-01T00:00:00.000Z",
  "key_label": "Local coding agent"
}
```

`limit` is USD and can be `daily`, `weekly`, or `monthly`. `key_label`, `limit`, and `expires_at` are applied to the dedicated API key when the code is exchanged.

The response includes top-level fields and a nested `data` object:

```json
{
  "id": "...",
  "code": "...",
  "app_id": "ngpt_callback_...",
  "user_id": "...",
  "expires_at": "...",
  "data": {
    "id": "...",
    "code": "...",
    "app_id": "ngpt_callback_...",
    "user_id": "...",
    "expires_at": "..."
  }
}
```

## 5. OAuth PKCE With Dynamic Registration

Register a public PKCE client:

```http
POST /oauth/register HTTP/1.1
Host: nano-gpt.com
Content-Type: application/json
```

```json
{
  "client_name": "my-agent",
  "redirect_uris": ["http://127.0.0.1:8000/callback"],
  "grant_types": ["authorization_code"],
  "response_types": ["code"],
  "token_endpoint_auth_method": "none"
}
```

Build an authorization URL with `response_type=code`, `client_id`, exact `redirect_uri`, `scope`, `state`, `code_challenge`, and `code_challenge_method=S256`. After approval, exchange the returned code:

```http
POST /oauth/token HTTP/1.1
Host: nano-gpt.com
Content-Type: application/x-www-form-urlencoded
```

```text
grant_type=authorization_code&client_id=ngpt_...&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Fcallback&code=...&code_verifier=...
```

Success response:

```json
{
  "access_token": "sk-nano-...",
  "token_type": "Bearer",
  "scope": "models.read api.use"
}
```

The access token is a dedicated NanoGPT API key for that app and user. It can spend from the user's NanoGPT balance until revoked or constrained in API key settings.

## 6. Register With User-Claimed Device Login

Start a login request:

```http
POST /api/cli-login/start HTTP/1.1
Host: nano-gpt.com
Content-Type: application/json
```

```json
{
  "client_name": "my-agent"
}
```

Success response:

```json
{
  "device_code": "opaque-device-code",
  "user_code": "ABCD-2345",
  "verification_uri": "https://nano-gpt.com/cli-login/verify",
  "verification_uri_complete": "https://nano-gpt.com/cli-login/verify?code=ABCD-2345",
  "expires_in": 600,
  "interval": 2
}
```

Tell the user to open `verification_uri_complete` and approve the request. Then poll:

```http
POST /api/cli-login/poll HTTP/1.1
Host: nano-gpt.com
Content-Type: application/json
```

```json
{
  "device_code": "opaque-device-code"
}
```

While the user has not approved yet, NanoGPT returns:

```json
{
  "status": "authorization_pending"
}
```

After approval, NanoGPT returns the API key exactly once:

```json
{
  "status": "approved",
  "key": "sk-nano-..."
}
```

Store the key securely and use it as:

```http
Authorization: Bearer sk-nano-...
```

## 7. Use The Credential

Call NanoGPT APIs with bearer auth. The primary agent surfaces are:

- `POST /api/v1/chat/completions`
- `POST /api/v1/responses`
- `POST /api/v1/messages`
- `GET /api/v1/models`
- `GET /api/v1/image-models`
- `GET /api/v1/video-models`
- `GET /api/v1/audio-models`
- `GET /api/v1/agent-capabilities`

For the full endpoint matrix, fetch `https://nano-gpt.com/api/v1/agent-capabilities`.

## 8. Errors

| Endpoint | Error | Meaning | Agent action |
| --- | --- | --- | --- |
| `/auth` | `invalid_request` | The callback URL or PKCE challenge is invalid | Rebuild the authorization URL |
| `/api/v1/auth/keys` | `invalid_grant` | The code is expired, already used, or the PKCE verifier does not match | Restart OAuth |
| `/oauth/authorize` | `invalid_request` | The request is missing a required OAuth parameter, has an invalid redirect URI, or does not use PKCE S256 | Rebuild the authorization URL |
| `/oauth/token` | `invalid_grant` | The code is expired, already used, or the PKCE verifier does not match | Restart OAuth |
| `/api/cli-login/start` | `rate_limited` | Too many login attempts | Wait and retry later |
| `/api/cli-login/poll` | `authorization_pending` | User has not approved yet | Wait `interval` seconds and poll again |
| `/api/cli-login/poll` | `expired` | Device code expired | Restart the device login flow |
| `/api/cli-login/poll` | `consumed` | Key was already returned | Restart if the key was not saved |
| `/api/cli-login/poll` | `key_revoked` | Approved key was revoked before retrieval | Restart registration |
| API endpoints | `missing_api_key` | No bearer credential | Register or ask user for a key |
| API endpoints | `invalid_api_key` | Credential is invalid, inactive, expired, or blocked | Drop the key and restart registration |
| API endpoints | `api_key_origin_not_allowed` | Browser Origin is not allowed for that key | Ask the user to update key settings |

## 9. Revocation

OAuth apps and agents do not revoke credentials through auth.md. Users can delete, block, expire, or constrain API keys from NanoGPT settings. If a previously working key returns 401, discard it and restart discovery.
