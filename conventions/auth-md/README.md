# auth.md 🟠 Emerging

> A Markdown file that tells an agent how to authenticate with a service - discovery of auth endpoints and flows. Shipped by WorkOS as a real, working convention, but adoption beyond it is still early.

- **Read by:** Agents discovering how to authenticate to a service (early adopters)
- **Location:** Site root or .well-known: /auth.md
- **Spec:** [https://workos.com/auth-md](https://workos.com/auth-md)
- **Files:** `auth.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `auth.md`

| Source | File | Provenance |
| --- | --- | --- |
| `workos.com` | [`workos.com.auth.md`](examples/workos.com.auth.md) | [source](https://workos.com/auth.md) |

## Field notes

### The protocol
WorkOS formalized auth.md (May 2026) as an open protocol over OAuth standards (RFC 7523 JWT-bearer + the ID-JAG draft), published at the domain root `https://service.com/auth.md`. A well-formed file is a numbered walkthrough in canonical order: **Discover -> Pick a Method -> Register -> Claim Ceremony -> Exchange the Assertion -> Use the Access Token -> Errors -> Revocation**.

- **Three registration methods (a decision tree):** `identity_assertion` (the agent already has a session exchangeable for an ID-JAG bound to this service), `service_auth` (only the user's email - requires a claim ceremony / OTP), or `anonymous` (credential issued immediately at pre-claim scope, claimable later).
- **Two endpoints:** `POST /agent/identity` (returns a service-signed assertion) and `POST /oauth2/token` (RFC 7523 grant -> `access_token`).
- **Errors are protocol strings**, not exit codes: `invalid_issuer`, `invalid_signature`, `expired`, `replay_detected`, `invalid_audience`, `authorization_pending`, `slow_down`, etc.

### Composition
The vendored WorkOS example is the clearest live instance:
- **Addressed to the agent**, second person: *"You are an agent. This document tells you how to register a credential..."* - forking immediately: *"Not an agent? You might be looking for workos.com/auth-md."*
- **Ordered steps** ("do not skip ahead") for the anonymous-provision -> later-claim flow.
- **A CLI shortcut *and* a raw-HTTP fallback**, so it works whether or not Node is present. The CLI affordances it documents (agent-context detection via `CLAUDECODE` / `CURSOR_AGENT` / `CODEX_SANDBOX`, structured JSON, `gh`-style exit codes `0/1/2/4`) belong to the WorkOS CLI it recommends, not to the wire protocol.

### Anti-patterns
- Assuming a human reader - WorkOS explicitly branches instead.
- Offering only a CLI with no HTTP fallback for environments without Node.
- Unordered or branchy instructions an agent can't follow deterministically.

### Edge cases
- **🟠 Emerging:** a real published protocol, but essentially one polished implementation (WorkOS). Treat the shape as indicative, not an industry standard yet.
- Placement is `/auth.md` at the domain root (not `.well-known/`); the registration method varies (`identity_assertion` / `service_auth` / `anonymous`).
