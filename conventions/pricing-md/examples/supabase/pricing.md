<!-- source: supabase — https://supabase.com/pricing.md -->
# Supabase Pricing

> Start for free, scale as you grow. Pay only for what you use.

Supabase offers four plans: Free, Pro, Team, and Enterprise. All plans include unlimited API requests.

## How billing works

Supabase uses organization-based billing. You choose a plan (Pro, Team, or Enterprise) for your organization, then each project within it runs on its own compute instance. The plan subscription covers platform features and usage quotas. Compute is billed separately per project.

Pro and Team plans include $10/month in compute credits, which covers one Micro instance. Additional projects each add their own compute cost. For example, a Pro org with 2 projects on Micro compute costs: $25 (plan) + $10 (project 1) + $10 (project 2) - $10 (credits) = $35/month.

For current pricing, visit https://supabase.com/pricing.

## Plan Tiers

### Free - from $0/month
- Unlimited API requests
- 50,000 monthly active users
- 500 MB database size (Shared CPU • 500 MB RAM)
- 5 GB egress
- 5 GB cached egress
- 1 GB file storage
- Community support
- Note: Free projects are paused after 1 week of inactivity. Limit of 2 active projects.

### Pro - from $25/month
- 100,000 monthly active users (then $0.00325 per MAU)
- 8 GB disk size per project (then $0.125 per GB)
- 250 GB egress (then $0.09 per GB)
- 250 GB cached egress (then $0.03 per GB)
- 100 GB file storage (then $0.0213 per GB)
- Email support
- Daily backups stored for 7 days
- 7-day log retention
- Add Log Drains (additional $60 per drain, per project)

### Team - from $599/month
- SOC2 & ISO 27001
- Project-scoped and read-only access
- HIPAA available as paid add-on
- SSO for Supabase Dashboard
- Priority email support & SLAs
- Daily backups stored for 14 days
- 28-day log retention

### Enterprise - custom pricing
- Designated Support manager
- Uptime SLAs
- BYO Cloud supported
- 24×7×365 premium enterprise support
- Private Slack channel
- Custom Security Questionnaires

## Compute Add-Ons

All projects run on a compute instance. Pro and Team plans include Micro compute in the base price.

| Size   | $/month    | CPU         | Dedicated | RAM    | Direct Connections | Pooler Connections |
| ------ | ---------- | ----------- | --------- | ------ | ------------------ | ------------------ |
| Micro  | $10        | 2-core ARM  | No        | 1 GB   | 60                 | 200                |
| Small  | $15        | 2-core ARM  | No        | 2 GB   | 90                 | 400                |
| Medium | $60        | 2-core ARM  | No        | 4 GB   | 120                | 600                |
| Large  | $110       | 2-core ARM  | Yes       | 8 GB   | 160                | 800                |
| XL     | $210       | 4-core ARM  | Yes       | 16 GB  | 240                | 1,000              |
| 2XL    | $410       | 8-core ARM  | Yes       | 32 GB  | 380                | 1,500              |
| 4XL    | $960       | 16-core ARM | Yes       | 64 GB  | 480                | 3,000              |
| 8XL    | $1,870     | 32-core ARM | Yes       | 128 GB | 490                | 6,000              |
| 12XL   | $2,800     | 48-core ARM | Yes       | 192 GB | 500                | 9,000              |
| 16XL   | $3,730     | 64-core ARM | Yes       | 256 GB | 500                | 12,000             |
| >16XL  | Contact Us | Custom      | Yes       | Custom | Custom             | Custom             |

Compute is billed hourly. Each project runs its own instance. Pro and Team plans include $10/month in compute credits (covers one Micro instance). Additional projects add their full compute cost.

## Disk Storage

### General Purpose
- Max size: 16 TB
- Size: 8 GB included, then $0.125 per GB
- IOPS: 3,000 IOPS included, then $0.024 per IOPS
- Throughput: 125 MB/s included, then $0.095 per MB/s
- Durability: 99.9%

### High Performance
- Max size: 60 TB
- Size: $0.195 per GB
- IOPS: $0.119 per IOPS
- Throughput: Scales automatically with IOPS
- Durability: 99.999%

## Add-Ons

| Add-on                        | Price                                                                       |
| ----------------------------- | --------------------------------------------------------------------------- |
| Point-in-Time Recovery (PITR) | $100 per month per 7 days retention                                         |
| Custom Domain                 | $10 per domain per month per project add on                                 |
| Database Branching            | $0.01344 per branch, per hour                                               |
| Advanced MFA (Phone)          | $75 per month for first project, then $10 per month per additional projects |
| SAML/SSO Auth                 | 50 included, then $0.015 per MAU                                            |
| Log Drains                    | $60 per drain per month, + $0.20 per million events, + $0.09 per GB egress  |
| Image Transformations         | 100 origin images included, then $5 per 1000 origin images                  |

## Full Feature Comparison

### Database

| Feature                     | Free                                      | Pro                                                                                  | Team                                                                                 | Enterprise                                                        |
| --------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| Dedicated Postgres Database | Included                                  | Included                                                                             | Included                                                                             | Included                                                          |
| Unlimited API requests      | Included                                  | Included                                                                             | Included                                                                             | Included                                                          |
| Database size               | 500 MB database size per project included | 8 GB disk size per project included, then $0.125 per GB                              | 8 GB disk size per project included, then $0.125 per GB                              | Custom                                                            |
| Advanced disk config        | Not included                              | Included                                                                             | Included                                                                             | Included                                                          |
| Automatic backups           | Not included                              | 7 days                                                                               | 14 days                                                                              | Custom                                                            |
| Point in time recovery      | Not included                              | $100 per month per 7 days retention                                                  | $100 per month per 7 days retention                                                  | $100 per month per 7 days retention, >28 days retention available |
| Pausing                     | After 1 week of inactivity                | Never                                                                                | Never                                                                                | Never                                                             |
| Branching                   | Not included                              | $0.01344 per branch, per hour                                                        | $0.01344 per branch, per hour                                                        | Custom                                                            |
| Egress                      | 5 GB included                             | 250 GB included, then $0.09 per GB                                                   | 250 GB included, then $0.09 per GB                                                   | Custom                                                            |
| Pipelines                   | Not included                              | $39 per pipeline per month, $3.00 per GB replicated data, $0.60 per GB backfill data | $39 per pipeline per month, $3.00 per GB replicated data, $0.60 per GB backfill data | Custom                                                            |

### Auth

| Feature                              | Free                                             | Pro                                                                         | Team                                                                        | Enterprise |
| ------------------------------------ | ------------------------------------------------ | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ---------- |
| Total Users                          | Unlimited                                        | Unlimited                                                                   | Unlimited                                                                   | Unlimited  |
| MAUs                                 | 50,000 included                                  | 100,000 included, then $0.00325 per MAU                                     | 100,000 included, then $0.00325 per MAU                                     | Custom     |
| User data ownership                  | Included                                         | Included                                                                    | Included                                                                    | Included   |
| Anonymous Sign-ins                   | Included                                         | Included                                                                    | Included                                                                    | Included   |
| Social OAuth providers               | Included                                         | Included                                                                    | Included                                                                    | Included   |
| Custom SMTP server                   | Included                                         | Included                                                                    | Included                                                                    | Included   |
| Remove Supabase branding from emails | Not included                                     | Included                                                                    | Included                                                                    | Included   |
| Auth Audit Logs                      | 1 hour                                           | 7 days                                                                      | 28 days                                                                     | Included   |
| Basic Multi-Factor Auth              | Included                                         | Included                                                                    | Included                                                                    | Included   |
| Advanced Multi-Factor Auth - Phone   | Not included                                     | $75 per month for first project, then $10 per month per additional projects | $75 per month for first project, then $10 per month per additional projects | Custom     |
| Third-Party MAUs                     | 50,000 included                                  | 100,000 included, then $0.00325 per MAU                                     | 100,000 included, then $0.00325 per MAU                                     | Custom     |
| Single Sign-On (SAML 2.0)            | Not included                                     | 50 included, then $0.015 per MAU                                            | 50 included, then $0.015 per MAU                                            | Contact Us |
| Leaked password protection           | Not included                                     | Included                                                                    | Included                                                                    | Included   |
| Single session per user              | Not included                                     | Included                                                                    | Included                                                                    | Included   |
| Session timeouts                     | Not included                                     | Included                                                                    | Included                                                                    | Included   |
| Auth Hooks                           | Custom Access Token (JWT), Send custom email/SMS | Custom Access Token (JWT), Send custom email/SMS                            | All                                                                         | All        |
| Advanced security features           | Not included                                     | Not included                                                                | Not included                                                                | Contact Us |

### Storage

| Feature                  | Free          | Pro                                                        | Team                                                       | Enterprise |
| ------------------------ | ------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------- |
| Storage                  | 1 GB included | 100 GB included, then $0.0213 per GB                       | 100 GB included, then $0.0213 per GB                       | Custom     |
| Cached Egress            | 5 GB included | 250 GB included, then $0.03 per GB                         | 250 GB included, then $0.03 per GB                         | Custom     |
| Custom access controls   | Included      | Included                                                   | Included                                                   | Included   |
| Max file upload size     | 50 MB         | 500 GB                                                     | 500 GB                                                     | Custom     |
| Content Delivery Network | Basic CDN     | Smart CDN                                                  | Smart CDN                                                  | Smart CDN  |
| Image Transformations    | Not included  | 100 origin images included, then $5 per 1000 origin images | 100 origin images included, then $5 per 1000 origin images | Custom     |

### Edge Functions

| Feature     | Free             | Pro                                       | Team                                      | Enterprise |
| ----------- | ---------------- | ----------------------------------------- | ----------------------------------------- | ---------- |
| Invocations | 500,000 included | 2 Million included, then $2 per 1 Million | 2 Million included, then $2 per 1 Million | Custom     |

### Realtime

| Feature                     | Free               | Pro                                        | Team                                       | Enterprise                                        |
| --------------------------- | ------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------------- |
| Postgres Changes            | Included           | Included                                   | Included                                   | Included                                          |
| Concurrent Peak Connections | 200 included       | 500 included, then $10 per 1000            | 500 included, then $10 per 1000            | Custom concurrent connections and volume discount |
| Messages Per Month          | 2 Million included | 5 Million included, then $2.50 per Million | 5 Million included, then $2.50 per Million | Volume discounts on messages                      |
| Max Message Size            | 256 KB             | 3 MB                                       | 3 MB                                       | Custom                                            |

### Dashboard

| Feature      | Free      | Pro       | Team      | Enterprise |
| ------------ | --------- | --------- | --------- | ---------- |
| Team members | Unlimited | Unlimited | Unlimited | Unlimited  |

### Platform Security and Compliance

| Feature                        | Free                    | Pro                                                                        | Team                                                                       | Enterprise                     |
| ------------------------------ | ----------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------ |
| BYO cloud                      | Not included            | Not included                                                               | Not included                                                               | Included                       |
| Log retention (API & Database) | 1 day                   | 7 days                                                                     | 28 days                                                                    | 90 days                        |
| Log Drain                      | Not included            | $60 per drain per month, + $0.20 per million events, + $0.09 per GB egress | $60 per drain per month, + $0.20 per million events, + $0.09 per GB egress | Custom                         |
| Platform Audit Logs            | Not included            | Not included                                                               | Included                                                                   | Included                       |
| Metrics endpoint               | Not included            | Included                                                                   | Included                                                                   | Included                       |
| SOC2                           | Not included            | Not included                                                               | Included                                                                   | Included                       |
| ISO 27001                      | Not included            | Not included                                                               | Included                                                                   | Included                       |
| HIPAA                          | Not included            | Not included                                                               | Available as paid add-on                                                   | Available as paid add-on       |
| AWS PrivateLink                | Not included            | Not included                                                               | Included                                                                   | Included                       |
| SSO                            | Not included            | Not included                                                               | Contact Us                                                                 | Contact Us                     |
| Uptime SLAs                    | Not included            | Not included                                                               | Not included                                                               | Included                       |
| Access Roles                   | Owner, Admin, Developer | Owner, Admin, Developer                                                    | Owner, Admin, Developer, Read-only, Predefined project scoped roles        | Custom project scoped roles    |
| Vanity URLs                    | Not included            | Included                                                                   | Included                                                                   | Included                       |
| Custom Domains                 | Not included            | $10 per domain per month per project add on                                | $10 per domain per month per project add on                                | 1, additional $10/domain/month |

### Support

| Feature                          | Free         | Pro          | Team         | Enterprise |
| -------------------------------- | ------------ | ------------ | ------------ | ---------- |
| Community Support                | Included     | Included     | Included     | Included   |
| Email Support                    | Not included | Included     | Included     | Included   |
| Email Support SLA                | Not included | Not included | Included     | Included   |
| Designated support               | Not included | Not included | Not included | Included   |
| On Boarding Support              | Not included | Not included | Not included | Included   |
| Designated Customer Success Team | Not included | Not included | Not included | Included   |
| Security Questionnaire Help      | Not included | Not included | Included     | Included   |

## Frequently Asked Questions

### Can I cap my usage so my bill doesn't run over?

Yes. Spend caps are on by default on the Pro Plan. You can turn spend caps off for usage beyond the Plan limits to pay as you grow.

### I'm worried I could end up with a huge bill at the end of the month.

Spend caps are on by default and you need to toggle them off from your dashboard to enable pay as you grow pricing.

### When will I be billed?

Our Pro Plan is charged up front, and billed on a monthly basis. Additional usage costs are also billed at the end of the month.

### Does Supabase charge sales tax, VAT or GST?

Supabase applies sales tax, VAT, GST, and other indirect taxes where required by law, based on your billing address. For more details, see our [Billing FAQ](/docs/guides/platform/billing-faq#taxes).

### Are you going to change your pricing in the future?

Our pricing is in Beta. You can read more about our decisions in our [pricing blog post](/blog/2021/03/29/pricing). Pricing may change in the future, however as a team of developers we are committed to pricing being as developer friendly as possible.

### What happens if I cancel my subscription?

The organization is allocated credits for unused time during the billing month. Those credits can be used for other projects.

### Do I get a notification if I am approaching my usage limits?

Yes, we will email you when you are within 20% of your Plan limits.

### What if I need one project for development and one for production?

We are working on multi-environment projects. For now, you can create a project for your development backend and production backend. We give you 2 free projects as part of our Free Plan. This means you could have a development and a production server as part of your Free Plan.

### Can I self-host Supabase for free?

Yes, you can use the [Docker setup](https://supabase.com/docs/guides/hosting/docker) or the [Supabase CLI](https://github.com/supabase/cli). [Supabase Studio](https://supabase.com/blog/supabase-studio) is also available in the Docker setup.

### Can I pause a free project?

Yes, you can pause a project at any time. Our Free Plan gives you 2 free projects, but you can have as many paused projects as you want. Just pause and unpause them as needed.

## Links

- Pricing page: https://supabase.com/pricing
- Documentation: https://supabase.com/docs/guides/platform/org-based-billing
- Dashboard: https://supabase.com/dashboard
