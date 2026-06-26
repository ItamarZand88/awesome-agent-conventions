# auth.md 🟠 Emerging

> A Markdown file that tells an agent how to authenticate with a service - discovery of auth endpoints and flows. Shipped by WorkOS as a real, working convention, but adoption beyond it is still early.

- **Read by:** Agents discovering how to authenticate to a service (early adopters)
- **Location:** Site root or .well-known: /auth.md
- **Spec:** [https://workos.com/auth-md](https://workos.com/auth-md)
- **Evidence:** WorkOS publishes both the auth.md spec page and a live auth.md file, but adoption beyond that ecosystem remains early.
- **Last verified:** 2026-06-26
- **Files:** `auth.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `auth.md`

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `apify` | [`apify.com`](https://apify.com) | [`examples/apify/auth.md`](examples/apify/auth.md) | [source](https://apify.com/auth.md) |
| `firecrawl` | [`firecrawl.dev`](https://firecrawl.dev) | [`examples/firecrawl/auth.md`](examples/firecrawl/auth.md) | [source](https://firecrawl.dev/auth.md) |
| `headless-domains` | [`headlessdomains.com`](https://headlessdomains.com) | [`examples/headless-domains/auth.md`](examples/headless-domains/auth.md) | [source](https://headlessdomains.com/auth.md) |
| `knock` | [`knock.app`](https://knock.app) | [`examples/knock/auth.md`](examples/knock/auth.md) | [source](https://knock.app/auth.md) |
| `lurkers` | [`lurkers.ntedvs.com`](https://lurkers.ntedvs.com) | [`examples/lurkers/auth.md`](examples/lurkers/auth.md) | [source](https://lurkers.ntedvs.com/auth.md) |
| `monday` | [`monday.com`](https://monday.com) | [`examples/monday/auth.md`](examples/monday/auth.md) | [source](https://monday.com/auth.md) |
| `nanogpt` | [`nano-gpt.com`](https://nano-gpt.com) | [`examples/nanogpt/auth.md`](examples/nanogpt/auth.md) | [source](https://nano-gpt.com/auth.md) |
| `resend` | [`resend.com`](https://resend.com) | [`examples/resend/auth.md`](examples/resend/auth.md) | [source](https://resend.com/auth.md) |
| `webclaw` | [`webclaw.io`](https://webclaw.io) | [`examples/webclaw/auth.md`](examples/webclaw/auth.md) | [source](https://webclaw.io/auth.md) |
| `workos.com` | [`workos.com`](https://workos.com) | [`examples/workos/auth.md`](examples/workos/auth.md) | [source](https://workos.com/auth.md) |
| `zapier` | [`zapier.com`](https://zapier.com) | [`examples/zapier/auth.md`](examples/zapier/auth.md) | [source](https://zapier.com/auth.md) |

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

### Adoption / maturity
- WorkOS publishes auth.md as an open protocol and a reference implementation. The repository separates three roles: an agent acting for a user, an agent provider that can mint identity assertions, and a service that accepts assertions or runs a claim ceremony before issuing credentials.
- The protocol composes existing OAuth/OIDC-era building blocks: Protected Resource Metadata, Authorization Server Metadata, JWT bearer exchange (RFC 7523), revocation, and ID-JAG-style identity assertions. That makes the design credible even though ecosystem adoption is early.

### Related conventions
- `auth.md` is about registration and credential issuance. It complements MCP remote-server auth and A2A Agent Cards, but does not replace either.
- `pricing.md` and `llms.txt` are discovery/documentation files; `auth.md` is a procedural protocol document agents follow step by step.

### Sources checked
- [WorkOS auth.md product page](https://workos.com/auth-md)
- [WorkOS app implementation guide](https://workos.com/auth-md/docs/apps)
- [workos/auth.md reference implementation](https://github.com/workos/auth.md)
- [Agent Registration with Auth.md announcement](https://workos.com/blog/agent-registration-with-auth-md)
