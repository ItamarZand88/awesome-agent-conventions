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
