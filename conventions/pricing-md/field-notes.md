### Composition
- **H1 + one-line intro + Markdown tables.** Resend's leads with `# Resend Pricing` then a `Plan / Price / Emails/mo / Overage` table and a worked "high-volume examples" section — numbers an agent can parse directly, no scraping.
- The URL mirrors the HTML page exactly: the marketing page at `/pricing` has a machine twin at `/pricing.md`.

### Anti-patterns
- **Stale numbers.** The `.md` and the HTML page can diverge; if they do, the agent quotes the wrong price with full confidence.
- Prose paragraphs instead of tables — that throws away the parse-ability that justifies the file.
- Dropping units/currency/billing period from cells ("$20" vs "$20/mo").

### Edge cases
- This is one instance of the broader **`page.md`** pattern — any HTML page can grow a `.md` twin (`/pricing.md`, `/docs.md`, …).
- It's **served by the site**, not committed to a repo, so it can be generated per-request and may differ by region/currency.
- Footnotes matter: Resend's free-tier daily cap lives in a line under the table, easy for a parser to miss.
