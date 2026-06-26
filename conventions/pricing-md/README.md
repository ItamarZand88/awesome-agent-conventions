# pricing.md 🟢 Adopted

> The Markdown twin of a pricing page - same URL with a .md suffix - so an agent gets structured plans and numbers instead of scraping marketing HTML. A concrete, shipping instance of the page.md pattern.

- **Read by:** Agents and LLM browsers fetching a clean, parse-able pricing page
- **Location:** Site path mirroring the HTML page: /pricing.md
- **Spec:** [https://resend.com/pricing.md](https://resend.com/pricing.md)
- **Evidence:** Multiple production SaaS sites expose Markdown pricing pages at predictable .md URLs for agent-friendly retrieval.
- **Last verified:** 2026-06-26
- **Files:** `pricing.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `pricing.md`

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `amplitude` | [`amplitude.com`](https://amplitude.com) | [`examples/amplitude/pricing.md`](examples/amplitude/pricing.md) | [source](https://amplitude.com/pricing.md) |
| `assemblyai` | [`assemblyai.com`](https://www.assemblyai.com) | [`examples/assemblyai/pricing.md`](examples/assemblyai/pricing.md) | [source](https://www.assemblyai.com/pricing.md) |
| `auth0.com` | [`auth0.com`](https://auth0.com) | [`examples/auth0/pricing.md`](examples/auth0/pricing.md) | [source](https://auth0.com/pricing.md) |
| `betterstack` | [`betterstack.com`](https://betterstack.com) | [`examples/betterstack/pricing.md`](examples/betterstack/pricing.md) | [source](https://betterstack.com/pricing.md) |
| `checkly` | [`checklyhq.com`](https://www.checklyhq.com) | [`examples/checkly/pricing.md`](examples/checkly/pricing.md) | [source](https://www.checklyhq.com/pricing.md) |
| `clerk` | [`clerk.com`](https://clerk.com) | [`examples/clerk/pricing.md`](examples/clerk/pricing.md) | [source](https://clerk.com/pricing.md) |
| `firecrawl` | [`firecrawl.dev`](https://www.firecrawl.dev) | [`examples/firecrawl/pricing.md`](examples/firecrawl/pricing.md) | [source](https://www.firecrawl.dev/pricing.md) |
| `hookdeck` | [`hookdeck.com`](https://hookdeck.com) | [`examples/hookdeck/pricing.md`](examples/hookdeck/pricing.md) | [source](https://hookdeck.com/pricing.md) |
| `langfuse` | [`langfuse.com`](https://langfuse.com) | [`examples/langfuse/pricing.md`](examples/langfuse/pricing.md) | [source](https://langfuse.com/pricing.md) |
| `liveblocks` | [`liveblocks.io`](https://liveblocks.io) | [`examples/liveblocks/pricing.md`](examples/liveblocks/pricing.md) | [source](https://liveblocks.io/pricing.md) |
| `livekit` | [`livekit.com`](https://livekit.com) | [`examples/livekit/pricing.md`](examples/livekit/pricing.md) | [source](https://livekit.com/pricing.md) |
| `mintlify` | [`mintlify.com`](https://www.mintlify.com) | [`examples/mintlify/pricing.md`](examples/mintlify/pricing.md) | [source](https://www.mintlify.com/pricing.md) |
| `neon` | [`neon.com`](https://neon.com) | [`examples/neon/pricing.md`](examples/neon/pricing.md) | [source](https://neon.com/pricing.md) |
| `ngrok` | [`ngrok.com`](https://ngrok.com) | [`examples/ngrok/pricing.md`](examples/ngrok/pricing.md) | [source](https://ngrok.com/pricing.md) |
| `pinecone` | [`pinecone.io`](https://www.pinecone.io) | [`examples/pinecone/pricing.md`](examples/pinecone/pricing.md) | [source](https://www.pinecone.io/pricing.md) |
| `planetscale` | [`planetscale.com`](https://planetscale.com) | [`examples/planetscale/pricing.md`](examples/planetscale/pricing.md) | [source](https://planetscale.com/pricing.md) |
| `posthog` | [`posthog.com`](https://posthog.com) | [`examples/posthog/pricing.md`](examples/posthog/pricing.md) | [source](https://posthog.com/pricing.md) |
| `railway` | [`railway.com`](https://railway.com) | [`examples/railway/pricing.md`](examples/railway/pricing.md) | [source](https://railway.com/pricing.md) |
| `render` | [`render.com`](https://render.com) | [`examples/render/pricing.md`](examples/render/pricing.md) | [source](https://render.com/pricing.md) |
| `resend.com` | [`resend.com`](https://resend.com) | [`examples/resend/pricing.md`](examples/resend/pricing.md) | [source](https://resend.com/pricing.md) |
| `supabase` | [`supabase.com`](https://supabase.com) | [`examples/supabase/pricing.md`](examples/supabase/pricing.md) | [source](https://supabase.com/pricing.md) |
| `svix` | [`svix.com`](https://www.svix.com) | [`examples/svix/pricing.md`](examples/svix/pricing.md) | [source](https://www.svix.com/pricing.md) |
| `tigerdata` | [`tigerdata.com`](https://www.tigerdata.com) | [`examples/tigerdata/pricing.md`](examples/tigerdata/pricing.md) | [source](https://www.tigerdata.com/pricing.md) |
| `turso` | [`turso.tech`](https://turso.tech) | [`examples/turso/pricing.md`](examples/turso/pricing.md) | [source](https://turso.tech/pricing.md) |
| `unkey` | [`unkey.com`](https://www.unkey.com) | [`examples/unkey/pricing.md`](examples/unkey/pricing.md) | [source](https://www.unkey.com/pricing.md) |
| `weaviate` | [`weaviate.io`](https://weaviate.io) | [`examples/weaviate/pricing.md`](examples/weaviate/pricing.md) | [source](https://weaviate.io/pricing.md) |
| `workos.com` | [`workos.com`](https://workos.com) | [`examples/workos/pricing.md`](examples/workos/pricing.md) | [source](https://workos.com/pricing.md) |
| `xata` | [`xata.io`](https://xata.io) | [`examples/xata/pricing.md`](examples/xata/pricing.md) | [source](https://xata.io/pricing.md) |

## Field notes

### Structure
No formal schema - it's the **Markdown twin** of a pricing page (`/pricing` -> `/pricing.md`), an instance of the **`page.md`** pattern (Mintlify "Markdown serving" / content-negotiation, co-developed with Anthropic and folded into the llms.txt proposal). Typical shape: an H1, a one-line positioning intro, then **one or more Markdown plan tables** (Resend's now has separate Transactional Email, Marketing Email, and AI Credits tables), a feature/tier breakdown, add-on/enterprise sections, and inline limit notes. **Served by the site, not committed** - it can be generated per-request and vary by region/currency.

### Composition
- **H1 + intro + tables.** Resend's leads with `# Resend Pricing`, then plan tables (`Plan / Price / Emails/mo / Overage`) and a worked "high-volume examples" section - numbers an agent parses directly, no scraping.
- The URL mirrors the HTML page exactly: `/pricing` has a machine twin at `/pricing.md`.

### Anti-patterns
- **Stale numbers.** The `.md` and the HTML page can diverge; if they do, the agent quotes the wrong price with full confidence.
- Prose paragraphs instead of tables - that throws away the parse-ability that justifies the file.
- Dropping units/currency/billing period from cells ("$20" vs "$20/mo").

### Edge cases
- One instance of the broader **`page.md`** pattern - any HTML page can grow a `.md` twin (`/pricing.md`, `/docs.md`, ...).
- Limits are usually **inline notes** under a table (Resend's free-tier daily cap, "marketing needs existing contacts"), not formal footnotes - easy for a parser to miss but load-bearing.

### Adoption / maturity
- `pricing.md` is adopted as a live-site convention rather than a repo convention: the authoritative file is usually served by the product website at request time.
- The useful property is not the exact filename alone, but the URL symmetry: a human page at `/pricing` gets an agent-readable Markdown twin at `/pricing.md`. That symmetry lets an agent fetch the machine-readable page without scraping a JS-heavy pricing UI.

### Related conventions
- This is a concrete instance of the broader `.md twin` pattern described by the `llms.txt` proposal.
- Unlike `auth.md`, it does not define a protocol flow; it is a parseable representation of public business data.

### Sources checked
- [llms.txt proposal, page.md section](https://llmstxt.org/)
- [Resend pricing.md](https://resend.com/pricing.md)
- [Auth0 pricing.md](https://auth0.com/pricing.md)
- [WorkOS pricing.md](https://workos.com/pricing.md)
