# pricing.md 🟢 Adopted

> The Markdown twin of a pricing page - same URL with a .md suffix - so an agent gets structured plans and numbers instead of scraping marketing HTML. A concrete, shipping instance of the page.md pattern.

- **Read by:** Agents and LLM browsers fetching a clean, parse-able pricing page
- **Location:** Site path mirroring the HTML page: /pricing.md
- **Spec:** [https://resend.com/pricing.md](https://resend.com/pricing.md)
- **Files:** `pricing.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `pricing.md`

| Source | File | Provenance |
| --- | --- | --- |
| `auth0.com` | [`auth0.com.pricing.md`](examples/auth0.com.pricing.md) | [source](https://auth0.com/pricing.md) |
| `resend.com` | [`resend.com.pricing.md`](examples/resend.com.pricing.md) | [source](https://resend.com/pricing.md) |
| `workos.com` | [`workos.com.pricing.md`](examples/workos.com.pricing.md) | [source](https://workos.com/pricing.md) |

## Field notes

### Composition
- **H1 + one-line intro + Markdown tables.** Resend's leads with `# Resend Pricing` then a `Plan / Price / Emails/mo / Overage` table and a worked "high-volume examples" section - numbers an agent can parse directly, no scraping.
- The URL mirrors the HTML page exactly: the marketing page at `/pricing` has a machine twin at `/pricing.md`.

### Anti-patterns
- **Stale numbers.** The `.md` and the HTML page can diverge; if they do, the agent quotes the wrong price with full confidence.
- Prose paragraphs instead of tables - that throws away the parse-ability that justifies the file.
- Dropping units/currency/billing period from cells ("$20" vs "$20/mo").

### Edge cases
- This is one instance of the broader **`page.md`** pattern - any HTML page can grow a `.md` twin (`/pricing.md`, `/docs.md`, …).
- It's **served by the site**, not committed to a repo, so it can be generated per-request and may differ by region/currency.
- Footnotes matter: Resend's free-tier daily cap lives in a line under the table, easy for a parser to miss.
