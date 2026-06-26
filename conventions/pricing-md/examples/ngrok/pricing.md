<!-- source: ngrok — https://ngrok.com/pricing.md -->
# ngrok Pricing

> Machine-readable version of <https://ngrok.com/pricing>, intended for AI assistants and automated agents. Dollar amounts for paid plans are fetched live from the ngrok billing service; all other values are hand-maintained in the frontend repo and should match the canonical HTML page.

- Canonical page: <https://ngrok.com/pricing>
- All prices in USD. "Not included" means the feature is unavailable on that plan.
- Usage-based items show the included amount first, then the overage rate.

## Plans at a glance

| Plan               | Monthly cost                                                    | Included monthly usage     | Overage                           | Best for                               |
| ------------------ | --------------------------------------------------------------- | -------------------------- | --------------------------------- | -------------------------------------- |
| Free               | $0                                                              | $5 one-time credit         | Not included — stops at credit    | Trying ngrok; free online endpoints    |
| Hobbyist (monthly) | $10                                                | $10 of credit | Not included — stops at credit    | Solo devs, home labs, game servers     |
| Hobbyist (annual)  | $8 / month billed as $96 / year | $10 of credit | Not included — stops at credit    | Solo devs who want the annual discount |
| Pay-as-you-go      | $20 base                                           | $20 of credit | Billed monthly at the rates below | Teams shipping production traffic      |

Custom / Enterprise: available for healthcare, finance, and government with volume pricing, SLAs, BAAs (HIPAA), on-call escalation, custom legal terms, and on-prem deployments. Minimum spend $10,000. Contact <https://ngrok.com/contact>.

## Gateway

### Endpoints

| Feature                           | Free                                        | Hobbyist       | Pay-as-you-go  |
| --------------------------------- | ------------------------------------------- | -------------- | -------------- |
| Online endpoints                  | 3                                           | 3              | Unlimited      |
| Development endpoint hours        | Unlimited                                   | Unlimited      | Unlimited      |
| Active endpoint hours             | Not included (can spend credit at $0.02/hr) | $0.02 per hour | $0.02 per hour |
| Endpoint protocols                | HTTP; TCP with credit card verification     | HTTP, TCP      | HTTP, TCP, TLS |
| Load balancing (endpoint pooling) | Included                                    | Included       | Included       |

### Domains

| Feature                       | Free         | Hobbyist     | Pay-as-you-go                       |
| ----------------------------- | ------------ | ------------ | ----------------------------------- |
| Development domain            | 1            | 1            | 1                                   |
| ngrok-branded domains         | Not included | 10           | Included                            |
| Bring-your-own custom domains | Not included | Not included | 744 hours included, then $0.0134/hr |
| Wildcard domains              | Not included | Not included | Included                            |

### TCP addresses

| Feature       | Free                                            | Hobbyist | Pay-as-you-go                |
| ------------- | ----------------------------------------------- | -------- | ---------------------------- |
| TCP addresses | Random assignment with credit card verification | 1        | 100 (contact sales for more) |

### Network transfer

| Feature           | Free | Hobbyist                     | Pay-as-you-go                                                                   |
| ----------------- | ---- | ---------------------------- | ------------------------------------------------------------------------------- |
| Data transfer out | 1 GB | 5 GB included, then $0.10/GB | 5 GB included, then $0.10/GB; volume discounts: 50TB+ $0.09/GB, 50TB+ $0.085/GB |

### Traffic

| Feature               | Free                                  | Hobbyist                        | Pay-as-you-go                                                                                  |
| --------------------- | ------------------------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------- |
| HTTP/S requests       | 20k (can spend credit at $2 per 100k) | 100k included, then $1 per 100k | 100k included, then $1 per 100k; volume discounts: 10M+ $0.75, 100M+ $0.55, 1B+ $0.35 per 100k |
| TCP / TLS connections | 5k (can spend credit at $2 per 100k)  | 5k included, then $2 per 100k   | 5k included, then $2 per 100k; volume discounts: 10M+ $1.50, 100M+ $1.00, 1B+ $0.75 per 100k   |

### Rate limits

| Feature         | Free    | Hobbyist | Pay-as-you-go                      |
| --------------- | ------- | -------- | ---------------------------------- |
| HTTP requests   | 4k/min  | 20k/min  | 20k/min (contact sales for higher) |
| TCP connections | 100/min | 150/min  | 600/min (contact sales for higher) |

### TLS

| Feature                     | Free         | Hobbyist     | Pay-as-you-go                  |
| --------------------------- | ------------ | ------------ | ------------------------------ |
| Bring-your-own certificates | Not included | Not included | $200 per cert per month        |
| End-to-end TLS              | Not included | Not included | Contact sales                  |
| Mutual TLS                  | Not included | Not included | Via Traffic Policy — see below |

## Traffic Policy

| Feature                                  | Free                                           | Hobbyist    | Pay-as-you-go                                                                                        |
| ---------------------------------------- | ---------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------- |
| Traffic Policy Units (TPUs)              | Not included (can spend credit at $1 per 100k) | $1 per 100k | $1 per 100k; volume discounts: 1M+ $0.75, 10M+ $0.55, 100M+ $0.35, 1B+ $0.25 per 100k                |
| Traffic Identities (OAuth/SAML/OIDC MAU) | 3 MAU                                          | 5 MAU       | 5 MAU included, then $1 each; volume discounts: 2500+ MAU $0.50, 10K+ MAU $0.25, >10K MAU $0.10 each |

## Traffic Observability

| Feature                                                           | Free                                                   | Hobbyist     | Pay-as-you-go                        |
| ----------------------------------------------------------------- | ------------------------------------------------------ | ------------ | ------------------------------------ |
| Traffic Inspector retention                                       | 24 hours                                               | 72 hours     | 72 hours (add-on available for more) |
| Traffic log exporting (S3, Datadog, Azure Logs, CloudWatch, etc.) | Not included (can spend credit at $0.25 per 2k events) | Not included | $0.25 per 2k events                  |

## Secure Tunnels

| Feature                        | Free          | Hobbyist      | Pay-as-you-go             |
| ------------------------------ | ------------- | ------------- | ------------------------- |
| Concurrent agents              | 3             | 3             | Unlimited                 |
| Dedicated agent connect IPs    | Not included  | Not included  | $900 per month per region |
| Custom agent connect URLs      | Not included  | Not included  | $250 per month per URL    |
| Remote agent update operations | Stop, Restart | Stop, Restart | Stop, Restart, Update     |

## Identity & Access

| Feature                                                                                              | Free         | Hobbyist     | Pay-as-you-go                             |
| ---------------------------------------------------------------------------------------------------- | ------------ | ------------ | ----------------------------------------- |
| Users                                                                                                | 1            | 1            | 3 included, then $5 per user              |
| Service users                                                                                        | Not included | Not included | Unlimited (do not count as users)         |
| SSO / RBAC                                                                                           | Not included | Not included | $10 per user/month (applied to all users) |
| Identity & Access Governance Suite (SCIM, domain controls, account-wide IP restrictions, audit logs) | Not included | Not included | $15 per user/month (for all users)        |
| Authtoken ACLs                                                                                       | Not included | Not included | Included                                  |

## Support

| Feature                                            | Free         | Hobbyist     | Pay-as-you-go  |
| -------------------------------------------------- | ------------ | ------------ | -------------- |
| Basic support (email, best-effort response)        | Included     | Included     | Included       |
| Slack / MS Teams channel (24-hour SLA)             | Not included | Not included | $200 per month |
| Dedicated on-call (committed uptime & support SLA) | Not included | Not included | Contact sales  |

## Compliance

| Feature                 | Free         | Hobbyist     | Pay-as-you-go                         |
| ----------------------- | ------------ | ------------ | ------------------------------------- |
| Region-specific routing | Not included | Not included | $0.02 per hour (billing enabled soon) |
| HIPAA / BAAs            | Not included | Not included | Contact sales — $10,000 minimum spend |
| SOC2                    | Not included | Not included | Contact sales — $10,000 minimum spend |
| Security questionnaires | Not included | Not included | Contact sales                         |
| Invoicing               | Not included | Not included | Contact sales — $10,000 minimum spend |

## Usage credits — how they work

- Free and Hobbyist plans give you a fixed pool of usage credit ($5 one-time for Free, $10/month for Hobbyist). When the pool is exhausted, usage stops — you are not charged overage.
- Pay-as-you-go includes $20 of credit per month. Usage beyond the credit is billed monthly at the overage rates above.
- Credits can be spent on any usage-based line item (endpoint hours, transfer, requests, TPUs, identities, log exports).

## Getting started

- Start free: <https://dashboard.ngrok.com/billing/choose-a-plan>
- Choose a paid plan: <https://dashboard.ngrok.com/billing/choose-a-plan>
- Contact sales: <https://ngrok.com/contact>
- Docs: <https://ngrok.com/docs>

If live prices could not be fetched, dollar values above may be rendered as `[see canonical /pricing page]` instead of a number. Treat that as a degraded response and use the canonical HTML page at <https://ngrok.com/pricing> for authoritative pricing in that case.
