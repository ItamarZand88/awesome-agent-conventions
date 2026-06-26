<!-- source: hookdeck — https://hookdeck.com/pricing.md -->
---
title: "Event Gateway Pricing - Hookdeck"
description: "Everything you need to build, deploy, operate and observe robust, production-ready event-driven applications. Free sign up. No credit card required - Hookdeck"
product: event-gateway
---

# Event Gateway Pricing

A scalable, observable gateway for managing webhooks and events

## Plans

### Developer

**Always** $0 /month

Features

- Up to 10,000 events
- 3-day retention
- 1 user
- SoC2 compliance

### Team

**Starts at** $39 /month

Everything in Developer, plus

- Pay-as-you-go
- 7-day retention
- Unlimited users
- Integrations (ie. Slack)

### Growth

**Starts at** $499 /month

Everything in Team, plus

- Uptime & latency SLAs
- 30-day retention
- Metrics Export (ie. Datadog)
- Read-only user role
- SSO, SAML and SCIM
- Startup discount available: We offer Growth plan discounts for eligible startups. [Contact us](/contact) for more information.

### Enterprise

**Inquire for plans** Custom

Everything in Growth, plus

- Premium support
- Support manager
- Slack Connect channel
- Custom security compliance
- Custom SLAs
- Custom contracts

## Pay-as-you-go events

Each plan includes **10,000 events/month**. Additional delivered events are metered in tiers:

| Volume (events/month) | Price per 100k |
| --- | --- |
| Up to 5,000,000 | $3.00 |
| 5,000,001 – 10,000,000 | $2.00 |
| 10,000,001 – 20,000,000 | $1.00 |
| 20,000,001 – 200,000,000 | $0.75 |
| 200,000,001 – 500,000,000 | $0.50 |
| Over 500,000,000 | $0.35 |

Event pricing can be as low as **$0.33 per 100k** at high volumes. Retries are included in event pricing.

## Additional throughput

Each project includes **5 events/second** of delivery throughput. Higher throughput is available in tiers (billed pro-rated when changed mid-month):

| Throughput (events/sec) | Price per event/sec |
| --- | --- |
| Up to 5 events/sec (included) | Included |
| 6 – 25 events/sec | $3.00 |
| 26 – 50 events/sec | $2.00 |
| 51 – 200 events/sec | $1.80 |
| 201 – 500 events/sec | $1.60 |
| 501 – 1000 events/sec | $1.20 |
| Over 1000 events/sec | $1.00 |

## Plan comparison

| Feature | Developer (Always $0/month) | Team (Starts at $39/month) | Growth (Starts at $499/month) | Enterprise (Custom) |
| --- | --- | --- | --- | --- |
| **Usage** | | | | |
| Included monthly events ([event docs](/docs/events)) | 10,000 | 10,000 | 10,000 | Custom |
| Additional events ([event docs](/docs/events)) | — | Metered billing | Metered billing | Metered billing |
| Included monthly discarded requests ([request docs](/docs/requests)) | 100,000 | 100,000 | 100,000 | Custom |
| Additional discarded requests ([request docs](/docs/requests)) | — | +$2.50 per million | +$2.50 per million | +$2.50 per million |
| **Features** | | | | |
| Users | 1 | Unlimited | Unlimited | Unlimited |
| Data Retention | 3 days | 7 days | 30 days | Custom |
| Connections ([connections docs](/docs/connections)) | Unlimited | Unlimited | Unlimited | Unlimited |
| Transformations ([transformations docs](/docs/transformations)) | Unlimited | Unlimited | Unlimited | Unlimited |
| Issues Management ([issues docs](/docs/issues)) | Yes | Yes | Yes | Yes |
| Metrics ([metrics docs](/docs/metrics)) | Yes | Yes | Yes | Yes |
| Metrics Export ([metrics export docs](/docs/metrics#metrics-export)) | — | — | Yes | Yes |
| Static IP Add-on ([static IP docs](/docs/platform/event-gateway-projects#delivery-with-static-ips)) | + $100 | + $100 | + $100 | + $100 |
| **Service Level** | | | | |
| Service Level | Basic | Standard | Priority | Priority |
| Uptime SLA | — | — | 99.999% | 99.999% |
| Latency SLA | — | — | 99.99% | 99.99% |
| **Support** | | | | |
| Slack Channel | Community | Community | Community | Slack Connect |
| Email & Live Chat | Basic | Standard | Standard | Premium |
| Support SLA | — | — | + Add-on | + Add-on |
| Solution Engineering & Onboarding | — | — | + Add-on | + Add-on |
| **Security and Compliance** | | | | |
| SoC2 Type 2 | [Request report](https://trust.hookdeck.com) | [Request report](https://trust.hookdeck.com) | [Request report](https://trust.hookdeck.com) | [Request report](https://trust.hookdeck.com) |
| GDPR | Yes | Yes | Yes | Yes |
| CCPA | Yes | Yes | Yes | Yes |
| PIPEDA | Yes | Yes | Yes | Yes |
| Multi-factor Authentication (MFA) | Yes | Yes | Yes | Yes |
| Single Sign-On (ie. SAML, OIDC) | — | — | Yes | Yes |
| Directory Sync (ie. SCIM) | — | — | Yes | Yes |
| Read-only user role | — | — | Yes | Yes |

## FAQs

### Is there a trial period?

There's a 14 days trial to invite team members to your organization. The Free Developer plan usage limits still apply during the trial.

### Is a credit card required?

No. You can sign up for an account without a credit card.

### What's the difference between a request and an event?

We count any inbound HTTP request from one of your sources as a request. When one of these incoming requests is delivered to a destination, we count it as an event. A request can result in 0, 1 or multiple events based on your connection configuration.

### Are event retries free?

Yes. The price of an event includes all its retries.

### What if I exceed 10,000 events on the Developer plan?

You will continue receiving your events but the dashboard will become locked until you upgrade your plan or enter a new billing period. In the case of excessive overages, we reserve the right to stop processing all requests and events.

### How is project throughput changes charged?

Project throughput changes are charged pro-rated for the remaining days of the month. When you upgrade your throughput you are charged for the full pro-rated value for the remainder of your billing period and the renews automatically on your next invoice. In the case of a downgrade, you will be credited the pro-rated amount for the remainder of the month. Changing throughput takes effect immeditately.

### What if I exceed my project throughput limits?

Don't worry, you won't miss any events. When these rates are exceeded, we safely queue additional events and process them at the throughput speeds selected for your project. Changing throughput takes effect immeditately.

### Where can I see how many requests and events I've received?

You can find the number of requests and events on the organization billing page.

### What does retention mean?

Retention refers to the number of days we store your event data. Increasing your retention does not guarantee that you will be able to access all of your previous pre-rentention change data. We reserve the right to delete data older than your retention period at any time.

### What if I switch my plan in the middle of the month?

You will be billed for your pro-rated charge for the remainder of your billing period. If you downgrade your plan, you will be credited the pro-rated difference.

### How granular is your billing rate?

The usage billing is pro-rated by 10k. For example the price for 10,000 events on our team plan is 0$, 10,001 events is 0.3$ and 20,000 events is (still) 0.3$ and 20,001 events is 0.6$.

### Where do I find Outpost pricing?

You can find Outpost pricing [here](/outpost/pricing).
