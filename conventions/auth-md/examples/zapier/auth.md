<!-- source: zapier — https://zapier.com/auth.md -->
# auth.md — Authentication for Agents

Zapier uses OAuth 2.0 Authorization Code with PKCE (S256). Request only the scopes your agent needs.

## Discovery

- `mcp.zapier.com/.well-known/oauth-authorization-server` — RFC 8414 authorization server metadata
- `mcp.zapier.com/.well-known/oauth-protected-resource` — RFC 9728 protected resource metadata
- `zapier.com/.well-known/jwks.json` — JSON Web Key Set for token verification

## Authorization Flow (PKCE)

**1. Generate a code verifier and challenge**

```
code_verifier  = base64url(random_bytes(32))
code_challenge = base64url(sha256(code_verifier))
```

**2. Redirect the user to the authorization endpoint**

```
GET https://mcp.zapier.com/oauth/authorize?
  response_type=code
  &client_id=YOUR_CLIENT_ID
  &redirect_uri=YOUR_REDIRECT_URI
  &scope=mcp:run+offline_access
  &code_challenge=CODE_CHALLENGE
  &code_challenge_method=S256
  &state=RANDOM_STATE
```

**3. Exchange the code for tokens**

```
POST https://mcp.zapier.com/api/v1/oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code
&code=AUTHORIZATION_CODE
&redirect_uri=YOUR_REDIRECT_URI
&client_id=YOUR_CLIENT_ID
&code_verifier=CODE_VERIFIER
```

For confidential clients (with a client secret), also include `&client_secret=YOUR_CLIENT_SECRET`. Public clients using PKCE should omit it.

**4. Call a protected endpoint**

```
GET https://mcp.zapier.com/mcp
Authorization: Bearer ACCESS_TOKEN
```

## Token Refresh

```
POST https://mcp.zapier.com/api/v1/oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=refresh_token
&refresh_token=REFRESH_TOKEN
&client_id=YOUR_CLIENT_ID
&client_secret=YOUR_CLIENT_SECRET
```

For public clients using PKCE, omit `client_secret`.

## Token Revocation

```
POST https://mcp.zapier.com/api/v1/oauth/revoke
Content-Type: application/x-www-form-urlencoded

token=TOKEN
&client_id=YOUR_CLIENT_ID
&client_secret=YOUR_CLIENT_SECRET
```

For public clients using PKCE, omit `client_secret`.

## Scopes

Request the narrowest scope for the task.

| Scope | Description |
|-------|-------------|
| `mcp:run` | Execute actions via the Zapier MCP server |
| `zap` | Read Zaps |
| `zap:all` | Read and trigger Zaps |
| `zap:write` | Create and update Zaps |
| `zap:runs` | Read Zap run history |
| `action:run` | Execute individual actions |
| `connection:read` | Read connected app credentials |
| `connection:write` | Manage connected app credentials |
| `user:read` | Read user profile |
| `offline_access` | Receive a refresh token (required for PKCE refresh) |

## Register an Application

https://developer.zapier.com

## Further Reading

- MCP quickstart: https://docs.zapier.com/mcp/quickstart
- API authentication: https://docs.zapier.com/powered-by-zapier/authentication/getting-started
