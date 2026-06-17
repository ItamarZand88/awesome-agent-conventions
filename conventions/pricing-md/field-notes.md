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
