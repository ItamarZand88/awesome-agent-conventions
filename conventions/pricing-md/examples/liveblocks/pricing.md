<!-- source: liveblocks — https://liveblocks.io/pricing.md -->
# Liveblocks pricing

Liveblocks provides the realtime infrastructure to handle concurrent edits on shared data, so people and AI agents can collaborate without breaking your app.

## How pricing works

Every plan includes a monthly bundle of **credits** that apply toward metered infrastructure usage (collaboration minutes, comments, storage, notifications, and file storage). Credits reset at the start of each billing cycle and do not roll over.

- **Free:** No base price. Each meter has a hard included cap; when exceeded, that feature pauses until the next cycle.
- **Pro and Team:** A fixed monthly base price includes a credit bundle. Usage beyond credits is billed at the same pay-as-you-go (PAYG) rates with no markup.
- **Enterprise:** Custom pricing, credit allocations, and volume discounts.
- **Annual billing:** Pro and Team annual plans include 2 months free (pay for 10 months, get 12).

Monitor usage on the [dashboard usage page](https://liveblocks.io/dashboard/usage).

## Plans at a glance

| Plan       | Monthly price | Annual price (per month)     | Monthly credits                            | Highlights                                           |
| ---------- | ------------- | ---------------------------- | ------------------------------------------ | ---------------------------------------------------- |
| Free       | $0            | —                            | Free monthly credits (hard caps per meter) | Prototyping; Liveblocks branding required            |
| Pro        | $30/mo        | $25/mo billed annually       | $30                                        | Remove branding; PAYG overage after credits          |
| Team       | From $600/mo  | From $500/mo billed annually | From $600                                  | Everything in Pro + SSO, SOC 2, private Slack        |
| Enterprise | Custom        | Custom                       | Custom                                     | Multi-region, Management API, SCIM, volume discounts |

## Team plan tiers

Team offers five credit tiers. Higher tiers include more monthly credits; annual billing saves 2 months.

| Monthly price | Annual price (per month)  | Monthly credits |
| ------------- | ------------------------- | --------------- |
| $600          | $500/mo billed annually   | $600            |
| $900          | $750/mo billed annually   | $1000           |
| $1,500        | $1,250/mo billed annually | $1750           |
| $2,250        | $1,875/mo billed annually | $2750           |
| $3,750        | $3,125/mo billed annually | $5000           |

## Metered usage rates

These rates apply on Pro and Team once monthly credits are consumed. Free uses the included amounts as hard caps instead.

| Meter                               | What it measures                                                                                                                                                                                                                                               | Pro / Team rate   | Free included   |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | --------------- |
| Realtime collaboration minutes      | When 2+ people or agents are in the same room, each user-minute counts. Solo sessions cost $0.                                                                                                                                                                 | $0.002 per minute | 3,000 minutes   |
| Comments created                    | The number of comments created in rooms.                                                                                                                                                                                                                       | $0.01 per comment | 200 comments    |
| Realtime data storage updates       | Number of Liveblocks Storage row updates in the selected period, aggregated across the projects you include in the filter.                                                                                                                                     | $1 per 1M updates | 3M updates      |
| Realtime data stored                | This is a cumulative calculation that represents all data that is currently stored. It does not reset monthly, and the total usage will continue to accrue over time as you add more content and data.                                                         | $0.15 per GB      | 1 GB            |
| Monthly collaboration notifications | Notifications triggered by collaborative events (mentions, replies, reactions)                                                                                                                                                                                 | Unlimited         | Unlimited       |
| Monthly custom notifications        | Non-collaborative notifications triggered from your own code.                                                                                                                                                                                                  | $0.01 per event   | 200 events      |
| File storage                        | This is a cumulative calculation that represents all files that are stored with Liveblocks. It does not reset monthly, and the total usage will continue to accrue over time as you add more files. Files can be uploaded as comment attachments for instance. | $0.15 per GB      | 512 MB included |

## What you'll pay

**Formula:** `monthly bill = base plan price + max(0, metered usage cost − monthly credits) + extra dashboard seats`

Dashboard seats beyond the included count on Pro and Team cost **$10/seat/month**.

**Example (Pro, $30/month credits):** If you use only collaboration minutes at $0.002 per minute, your credits cover **15,000 minutes** before overage. If you use only comments at $0.01 per comment, credits cover **3,000 comments**. Mixed usage draws from the same credit pool at each meter's PAYG rate.

On **Free**, each meter has a hard cap (see table above). When a cap is reached, that feature pauses until the next billing cycle. On **Pro** and **Team**, usage continues and overage is billed at the same PAYG rates.

## Add-ons

| Add-on    | Available on | Price (USD)              |
| --------- | ------------ | ------------------------ |
| HIPAA BAA | Team         | $350/month billed yearly |

SOC 2 and SAML SSO are included on Team and Enterprise (not sold as separate add-ons on current plans).

## Feature highlights

- **Free:** For personal development, prototyping, and testing. Hard caps per meter (3,000 collaboration minutes, 200 comments, 1 GB realtime storage, 512 MB file storage). **10** projects, **3** dashboard seats, **10** simultaneous connections per room.
- **Pro:** For developers shipping collaborative features. **$30/month** credits applied to metered usage; remove Liveblocks branding. **3** dashboard seats included (**$10/seat/mo** overage). **20** simultaneous connections per room, **30 days** version history.
- **Team:** For teams shipping collaborative features at scale. Starts at **$600/month** credits (higher tiers available). Same metered rates as Pro. **10** dashboard seats included. SAML SSO, SOC 2, and private Slack included. **50** simultaneous connections per room, **90 days** version history.
- **Enterprise:** For organizations with premium security and partnership needs. Custom credits and allocations. **100** simultaneous connections per room. Multi-region hosting, Management API, SCIM, advanced permissions, volume discounts, premium support.

All plans include: Realtime Infrastructure and collaboration features like Multiplayer, Comments, AI Collaboration, AI Copilots, and Notifications.

## Plan limits (comparison)

Side-by-side limits by category (**—** means not available on that plan).

### Connections and scale

| Limit                                      | Free      | Pro       | Team      | Enterprise |
| ------------------------------------------ | --------- | --------- | --------- | ---------- |
| Simultaneous connections per room (max)    | 10        | 20        | 50        | 100        |
| Simultaneous connections per project (max) | Unlimited | Unlimited | Unlimited | Unlimited  |
| Anonymous connections per month (max)      | 3,000     | 3,000     | 3,000     | Custom     |

### Projects, team, and environments

| Limit                      | Free                    | Pro                          | Team                         | Enterprise              |
| -------------------------- | ----------------------- | ---------------------------- | ---------------------------- | ----------------------- |
| Projects (included)        | 10                      | 10                           | 10                           | Custom                  |
| Projects (max)             | 10                      | 10                           | 10                           | 500                     |
| Dashboard seats (included) | 3                       | 3                            | 10                           | Custom                  |
| Dashboard seats (max)      | 3                       | Unlimited                    | Unlimited                    | Unlimited               |
| Dashboard seats (overage)  | —                       | then $10 per additional seat | then $10 per additional seat | —                       |
| Environments               | Development, Production | Development, Production      | Development, Production      | Development, Production |

### Storage and uploads

| Limit                       | Free  | Pro   | Team  | Enterprise |
| --------------------------- | ----- | ----- | ----- | ---------- |
| Storage size per room (max) | 10 MB | 10 MB | 50 MB | Custom     |
| Max file upload size        | 50 MB | 1 GB  | 1 GB  | 500 GB     |

### Notifications and AI

| Limit                                             | Free      | Pro       | Team      | Enterprise |
| ------------------------------------------------- | --------- | --------- | --------- | ---------- |
| Collaboration notification events per month (max) | Unlimited | Unlimited | Unlimited | Unlimited  |
| AI copilot messages per month (max)               | Unlimited | Unlimited | Unlimited | Unlimited  |

### Retention and webhooks

| Limit                   | Free       | Pro        | Team       | Enterprise |
| ----------------------- | ---------- | ---------- | ---------- | ---------- |
| Version history         | 24 hours   | 30 days    | 90 days    | Custom     |
| Event log retention     | 24 hours   | 7 days     | 30 days    | Custom     |
| Webhook event frequency | 60 seconds | 60 seconds | 30 seconds | Custom     |

### Security and support

| Feature                      | Free | Pro | Team                              | Enterprise |
| ---------------------------- | ---- | --- | --------------------------------- | ---------- |
| SAML SSO                     | —    | —   | Included                          | Included   |
| SOC 2 report                 | —    | —   | Included                          | Included   |
| HIPAA BAA                    | —    | —   | Add-on ($350/mo (yearly billing)) | Included   |
| Private Slack channel        | —    | —   | Included                          | Included   |
| Dedicated solutions engineer | —    | —   | —                                 | Included   |
| Support SLA                  | —    | —   | —                                 | Included   |

## Enterprise

For organizations with premium security and partnership needs. Custom credit allocations, multi-region hosting, Management API, SCIM & directory sync, advanced permissions, volume discounts, and premium support. [Contact sales](https://liveblocks.io/contact).

## Frequently asked questions

### How does pricing work in Liveblocks?

Each plan includes a monthly credit allowance you spend across all features. Credits reset at the start of each billing cycle and don't roll over. Pro is $30/month with $30 of credits, and Team plans range from $600 to $3,750/month with up to $5,000 of credits. Once you've used your credits, additional usage on Pro and Team is billed at metered rates. Free hits hard limits per feature instead.

For full per-metric rates and worked examples, see our [pricing overview](https://liveblocks.io/docs/pricing/overview).

### What counts as a realtime collaboration minute?

Collaboration minutes measure time when two or more people or agents are in the same room together. Each connected user-minute counts. Two users in a room for 5 minutes is 10 collaboration minutes, billed at $0.002 each.

Solo sessions cost $0.

For what counts as connected, when billing pauses, and background tabs, see our [pricing FAQ](https://liveblocks.io/docs/pricing/faqs#What-counts-as-a-realtime-collaboration-minute). Track usage on your [dashboard usage page](https://liveblocks.io/dashboard/usage).

### Which Liveblocks plan should I choose?

Liveblocks offers four plans to support developers and teams of all sizes:

- **Free:** Personal projects and prototyping
- **Pro:** Indie devs and small teams shipping commercial apps
- **Team:** Teams that need SSO, SOC 2, and more than 3 seats
- **Enterprise:** Larger orgs needing volume discounts, multi-region hosting, and custom terms

Compare features in detail: [Free](https://liveblocks.io/docs/pricing/plans/free), [Pro](https://liveblocks.io/docs/pricing/plans/pro), [Team](https://liveblocks.io/docs/pricing/plans/team), [Enterprise](https://liveblocks.io/docs/pricing/plans/enterprise).

### What comes with my Liveblocks subscription?

Every plan includes the full platform: [Presence](https://liveblocks.io/docs/ready-made-features/presence), [Storage](https://liveblocks.io/docs/collaboration-features/multiplayer/sync-engine/liveblocks-storage), [Comments](https://liveblocks.io/docs/ready-made-features/comments), [Custom Notifications](https://liveblocks.io/docs/ready-made-features/notifications/concepts#Custom-notifications), [Feeds](https://liveblocks.io/docs/collaboration-features/ai-collaboration), [AI Copilots](https://liveblocks.io/docs/ready-made-features/ai-copilots), the [dashboard](https://liveblocks.io/dashboard), SDKs, and APIs. What changes between plans is your monthly credit allowance, seat count, and the security and support features you get. After you've used your credits, you keep using Liveblocks. Pro and Team are charged for overage at the same metered rates. Free plans hit hard limits per feature.

For a full plan-by-plan breakdown, see the [plans docs](https://liveblocks.io/docs/pricing/plans).

### Can I try Liveblocks before paying for it?

Yes. The Free plan is permanently free, no credit card required. You can build, test, and even ship commercial apps on Free as long as the Liveblocks watermark stays visible. To remove the watermark and unlock overage, upgrade to Pro at $30/month. [Get started for free](https://liveblocks.io/auth/signup).

### Are there discounts for startups, nonprofits, or students?

We offer a discount for early-stage startups. [Learn more and apply](https://liveblocks.io/startups).

### What happens when I run out of Liveblocks credits?

On Free, you'll hit hard limits per metric and the affected feature pauses until your credits reset. On Pro and Team, additional usage is billed at metered rates with no markup. We send automated email alerts as you approach your limits.

See [usage limits](https://liveblocks.io/docs/pricing/limits) for full details.

### How do I track and control my Liveblocks spending?

The [usage page](https://liveblocks.io/dashboard/usage) in your dashboard shows real-time usage broken down by metric, current credit consumption, and projected month-end spend. We also send automated email alerts as you approach your limits. For predictable spend, your monthly credits give you a fixed ceiling unless you allow overage, and annual Team plans lock in a fixed monthly cost while saving up to 38% versus monthly billing.

### Can I pay by invoice instead of credit card?

Yes, on Enterprise plans. [Contact sales](https://liveblocks.io/contact/sales) to set this up.

### Does Liveblocks support multi-region hosting?

Yes, on Enterprise. We currently support EU and US, with more coming. [Reach out to sales](https://liveblocks.io/contact) to discuss upgrading to an Enterprise plan.

### How secure and reliable is Liveblocks?

We run on edge infrastructure with 99.99% uptime, monitored on our [status page](https://liveblocks.statuspage.io). We're SOC 2 and HIPAA compliant, and GDPR-compliant with a Data Processing Agreement (DPA) available on request. Enterprise plans support data residency in specific regions. For more, see our [security page](https://liveblocks.io/security) and [data storage docs](https://liveblocks.io/docs/platform/data-storage).
