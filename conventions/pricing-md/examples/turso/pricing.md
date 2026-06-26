<!-- source: turso — https://turso.tech/pricing.md -->
# Turso Pricing

> Start free today, no credit card required. Sign up at https://app.turso.tech

## Plans Overview

| Feature                  | Free | Developer | Scaler | Pro     | Enterprise |
| ------------------------ | ---- | --------- | ------ | ------- | ---------- |
| Monthly Price            | $0   | $5.99     | $29    | $499    | Custom     |
| Yearly Price (per month) | $0   | $4.99     | $24.92 | $416.58 | Custom     |
| Yearly Price (total)     | $0   | $59.88    | $299   | $4,999  | Custom     |

## Plan Details

### Free

- **Databases:** 100
- **Storage:** 5GB
- **Monthly Rows Read:** 500 Million
- **Monthly Rows Written:** 10 Million
- **Monthly Syncs:** 3GB
- **Point-In-Time Restore:** 1 day
- **Audit Logs:** No
- **DPA:** No
- **IP Allow Lists:** No
- **AWS VPC Allow Lists:** No
- **Teams:** No
- **SSO:** No
- **BYOK Encryption:** No
- **HIPAA:** No
- **SOC2:** No
- **Support:** Community

### Developer — $5.99/month ($4.99/month billed yearly)

- **Databases:** Unlimited
- **Storage:** 9GB (overage: $0.75 / GB)
- **Monthly Rows Read:** 2.5 Billion (overage: $1 / Billion)
- **Monthly Rows Written:** 25 Million (overage: $1 / Million)
- **Monthly Syncs:** 10GB (overage: $0.35 / GB)
- **Point-In-Time Restore:** 10 days
- **Audit Logs:** 3 Day Retention
- **DPA:** Yes
- **IP Allow Lists:** Yes
- **AWS VPC Allow Lists:** Yes
- **Teams:** No
- **SSO:** No
- **BYOK Encryption:** No
- **HIPAA:** No
- **SOC2:** No
- **Support:** Community

### Scaler — $29/month ($24.92/month billed yearly)

- **Databases:** Unlimited
- **Storage:** 24GB (overage: $0.50 / GB)
- **Monthly Rows Read:** 100 Billion (overage: $0.80 / Billion)
- **Monthly Rows Written:** 100 Million (overage: $0.80 / Million)
- **Monthly Syncs:** 24GB (overage: $0.25 / GB)
- **Point-In-Time Restore:** 30 days
- **Audit Logs:** 14 Day Retention
- **DPA:** Yes
- **IP Allow Lists:** Yes
- **AWS VPC Allow Lists:** Yes
- **Teams:** Yes
- **SSO:** No
- **BYOK Encryption:** No
- **HIPAA:** No
- **SOC2:** No
- **Support:** Community

### Pro — $499/month ($416.58/month billed yearly)

- **Databases:** Unlimited
- **Storage:** 50GB (overage: $0.45 / GB)
- **Monthly Rows Read:** 250 Billion (overage: $0.75 / Billion)
- **Monthly Rows Written:** 250 Million (overage: $0.75 / Million)
- **Monthly Syncs:** 100GB (overage: $0.15 / GB)
- **Point-In-Time Restore:** 90 days
- **Audit Logs:** 30 Day Retention
- **DPA:** Yes
- **IP Allow Lists:** Yes
- **AWS VPC Allow Lists:** Yes
- **Teams:** Yes
- **SSO:** Yes
- **BYOK Encryption:** Yes
- **HIPAA:** Yes
- **SOC2:** Yes
- **Support:** Priority Email & Slack

### Enterprise — Custom Pricing

White glove support including dedicated emergency email, unlimited usage, dedicated infrastructure, and everything in the Pro plan. Contact sales at https://tur.so/turso-enterprise-chat.

## Overage Pricing

| Resource     | Developer    | Scaler          | Pro             |
| ------------ | ------------ | --------------- | --------------- |
| Storage      | $0.75 / GB   | $0.50 / GB      | $0.45 / GB      |
| Rows Read    | $1 / Billion | $0.80 / Billion | $0.75 / Billion |
| Rows Written | $1 / Million | $0.80 / Million | $0.75 / Million |
| Syncs        | $0.35 / GB   | $0.25 / GB      | $0.15 / GB      |

Subscriptions after March 19, 2025 have overages enabled by default.

## FAQs

### When will I be billed for my plan?

If you are on a paid plan, you will be billed on the first day of each month.

### Will I be charged if I exceed my plan's usage limits?

- **Free plan:** You will need to upgrade to a paid plan.
- **Paid plans:** Subscriptions after March 19, 2025 have overages enabled by default. If you exceed your plan's usage limits, you will be charged for the overages.
- **Vegas Blackout:** Once per month, before your invoice closes, you can pick any single day and erase its usage from your bill. Use it on the day a runaway query, bot swarm, or other bad day blew up your numbers, and that day's reads, writes, storage, and syncs will not be billed.
- **Higher usage needs:** Contact the team at https://tur.so/turso-enterprise-chat to explore custom Enterprise plan options.

### If I hit the limit on one metric, am I blocked from using the others?

It depends on whether your plan blocks at quota or allows overages.

- **Free plan, or paid plan with Overages disabled:** Yes. Once you exceed the limit on any single metric (storage, rows read, rows written, or syncs), your databases are blocked, even if the other metrics are still well under quota.
- **Paid plan with Overages enabled:** No. You keep consuming your full plan quota across every metric, and at the end of the month you only pay overages for the metric or metrics you went over.

### How are "rows read" and "rows written" calculated?

Rows read and rows written are a proxy for compute. Every row touched while producing a response counts, not just the rows returned to your application.

For reads, this means:

- A lookup on an unindexed column has to scan the whole table, so it counts as many rows read as the table has.
- A lookup that can use an index touches just the matching index entries and rows, often as few as one row read.

For writes, this means a single `INSERT`, `UPDATE`, or `DELETE` on a table with indexes counts as more than one row written, because each affected index also has to be updated. Adding more indexes makes writes count more.

Designing your schema with the right indexes is the most direct way to keep usage low.

### How are "Embedded Syncs" calculated?

Embedded Syncs measure the amount of data, in pages, transferred between Turso Cloud and your local embedded database when syncing changes in either direction.

### How do I contact Turso if I have additional questions or problems with my bill?

There are multiple ways to get in touch with Turso, including [Discord](https://tur.so/discord) and [email](mailto:support@turso.tech).

### Does using Drizzle Studio from the Turso Dashboard incur plan usage?

Yes, Drizzle Studio needs to read your data to present it to you, and that counts as rows read. If you use Drizzle Studio to create new data or update existing data, that is counted as rows written.

### What happens when I enable Overages?

If you enable Overages you will automatically be topped up when you exceed usage limits, one increment at a time. While Overages are enabled, you will be charged for any extra usage charges you incur at the end of each month.

### What happens if I disable Overages?

If you have incurred extra usage charges while Overages were enabled, you will be charged for them when you disable Overages. If you are on the Scaler plan you will also be charged a prorated amount of your monthly subscription price at that time, and the remainder of your monthly subscription price will be charged at the end of the month as normal.

### Do point in time restores cost money?

Each point in time restore uses one of your available databases, and consumes your storage quota.

### Do Database Branches cost money?

Each Branch you create uses one of your available databases, and consumes your storage quota.
