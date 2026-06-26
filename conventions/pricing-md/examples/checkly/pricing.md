<!-- source: checkly — https://www.checklyhq.com/pricing.md -->
# Checkly Pricing

**Source**: https://checklyhq.com/pricing

Checkly offers monitoring, status pages, and AI-powered diagnostics across four plans: **Hobby** (free), **Starter**, **Team**, and **Enterprise**. Pricing is organized into three product modules — Detect, Communicate, and Resolve — each priced independently. Annual billing offers approximately 20% savings.

---

## How to Use This Document

To quote pricing for a customer, follow these steps in order:

1. **Identify their plan tier:** Match required features against the Feature Comparison tables to determine the minimum plan (Hobby, Starter, Team, or Enterprise).
2. **Determine billing cycle:** Monthly or Annual. Annual billing saves ~20%.
3. **Look up base prices for each module:**
   - **Detect:** Base plan price for uptime + synthetic monitoring.
   - **Communicate:** Status pages + dashboards pricing.
   - **Resolve:** AI Root Cause Analysis pricing.
4. **Add any resource add-ons (Detect only):** Check if the customer needs additional monitors, browser checks, or API checks beyond included amounts. Look up each add-on price from the explicit tables.
5. **Calculate total cost:** Total = Detect Base Price + Communicate Price + Resolve Price + sum of all applicable add-on prices.
6. **Account for overages:** If the customer may exceed purchased add-ons, note the overage rates per plan.
7. **Enterprise:** If any component requires custom pricing, direct the customer to Checkly sales.

---

## Key Definitions

- **Uptime Monitors:** Continuously check the availability of your websites, APIs, and services using HTTPS, TCP, DNS, ICMP, or Heartbeat protocols.
- **Browser Checks:** Simulate real user interactions using a headless Playwright browser to validate critical user flows like logins, checkouts, and form submissions.
- **Playwright Check Suites:** Group multiple related browser checks into a single scheduled suite.
- **API Checks:** Monitor API endpoints with HTTP requests. Multistep checks chain multiple API calls to test complex workflows.
- **Status Pages:** Public or private pages that communicate the real-time operational status of your services to users and stakeholders.
- **Dashboards:** Custom dashboards to visualize and share monitoring data with your team or stakeholders.
- **AI Root Cause Analysis (RCA):** AI-powered diagnostics that automatically analyze check failures to identify the root cause.
- **Public Locations:** Checkly-managed global data center locations from which checks are executed. 6 locations on Hobby/Starter, all 22 on Team/Enterprise.
- **Private Locations:** Run checks from within your own infrastructure to monitor internal services not exposed to the public internet. Available on Team and Enterprise.

---

## Plans Overview

| Plan | Detect (Monthly) | Detect (Annual) | Communicate (Monthly) | Communicate (Annual) | Resolve (Monthly) | Resolve (Annual) | Users |
|------|-------------------|-----------------|----------------------|---------------------|--------------------|-------------------|-------|
| Hobby | $0 | $0 | $0 | $0 | $0 | $0 | 1 |
| Starter | $29 | $24 | $12 | $9 | $19 | $12 | 3 |
| Team | $80 | $64 | $34 | $30 | $49 | $39 | 10 |
| Enterprise | Custom | Custom | Custom | Custom | Custom | Custom | Custom |

---

## Detect Module Pricing

The Detect module covers Uptime Monitoring and Synthetic Monitoring (browser checks + API checks).

### Detect Base Prices

| Plan | Monthly | Annual | Included Monitors | Included Browser Checks | Included API Checks |
|------|---------|--------|-------------------|------------------------|---------------------|
| Hobby | $0 | $0 | 10 | 1,000 | 10,000 |
| Starter | $29 | $24 | 50 | 3,000 | 25,000 |
| Team | $80 | $64 | 75 | 12,000 | 100,000 |
| Enterprise | Custom | Custom | Custom | Custom | Custom |

### Additional Monitors

Purchase additional monitors in blocks of 25. Available on Starter and Team plans.

| | Monthly | Annual |
|---|---------|--------|
| Per 25 monitors | $10 | $8 |

- Starter: up to 225 additional monitors (275 total)
- Team: up to 450 additional monitors (525 total)

### Additional Browser Check / Playwright Check Suite Runs

Purchase additional browser check runs in blocks of 1,000. Available on Starter and Team plans.

| | Monthly | Annual |
|---|---------|--------|
| Per 1,000 runs | $5 | $4 |

- Starter: up to 117,000 additional runs (120,000 total)
- Team: up to 282,000 additional runs (294,000 total)

### Additional API Check Runs

Purchase additional API check runs in blocks of 10,000. Available on Starter and Team plans.

| | Monthly | Annual |
|---|---------|--------|
| Per 10,000 runs | $2 | $1.80 |

- Starter: up to 550,000 additional runs (575,000 total)
- Team: up to 2,200,000 additional runs (2,300,000 total)

### Overage Pricing

Overages are charged automatically when you exceed your purchased check runs (base + add-ons).

| | Starter | Team |
|---|---------|------|
| Browser Check Overages (per 1,000) | $6.50 | $6.25 |
| API Check Overages (per 10,000) | $2.60 | $2.50 |

---

## Communicate Module Pricing

The Communicate module covers Status Pages and Dashboards.

### Communicate Base Prices

| Plan | Monthly | Annual |
|------|---------|--------|
| Hobby | $0 | $0 |
| Starter | $12 | $9 |
| Team | $34 | $30 |
| Enterprise | Custom | Custom |

### Included Resources by Plan

| Resource | Hobby | Starter | Team | Enterprise |
|----------|-------|---------|------|------------|
| Services | 20 | 25 | 50 | 100 |
| Subscribers | 250 | 500 | 1,000 | 2,000 |
| Dashboards | 1 | 1 | 10 | Custom |
| Custom Domain | No | Yes | Yes | Yes |
| Custom CSS | No | No | Yes | Yes |
| Password Protection | No | No | Yes | Yes |
| Incident Management | No | No | Yes | Yes |
| Maintenance Windows | No | No | Yes | Yes |
| White Labeled (remove Checkly branding) | No | No | No | Yes |

---

## Resolve Module Pricing

The Resolve module covers AI-powered Root Cause Analysis.

### Resolve Base Prices

| Plan | Monthly | Annual |
|------|---------|--------|
| Hobby | $0 | $0 |
| Starter | $19 | $12 |
| Team | $49 | $39 |
| Enterprise | Custom | Custom |

### Included Resources by Plan

| Resource | Hobby | Starter | Team | Enterprise |
|----------|-------|---------|------|------------|
| AI RCA Invocations | 10 | 50 | 150 | Custom |
| Automated RCA | Yes | Yes | Yes | Yes |

---

## Feature Comparison

### Detect — Uptime Monitoring

| Feature | Hobby | Starter | Team | Enterprise |
|---------|-------|---------|------|------------|
| Protocol Support | HTTPS, TCP, DNS, ICMP, Heartbeat | HTTPS, TCP, DNS, ICMP, Heartbeat | HTTPS, TCP, DNS, ICMP, Heartbeat | HTTPS, TCP, DNS, ICMP, Heartbeat |
| Uptime Monitors | 10 | 50 | 75 | Custom |
| Additional Monitors (25) | — | $10/$8 mo/ann | $10/$8 mo/ann | Custom |
| Scheduling | Round Robin | Round Robin | Round Robin | Round Robin & Parallel |
| Public Locations | 6 | 6 | All 22 Locations | All 22 Locations |
| Private Locations | No | No | Yes | Yes |
| Automatic Retries | No | Yes | Yes | Yes |

### Detect — Synthetic Monitoring

| Feature | Hobby | Starter | Team | Enterprise |
|---------|-------|---------|------|------------|
| Browser Checks | Yes | Yes | Yes | Yes |
| Playwright Check Suites | Yes | Yes | Yes | Yes |
| Browser Check / Playwright Runs (included) | 1,000 | 3,000 | 12,000 | Custom |
| Additional Browser Runs (per 1k) | — | $5/$4 mo/ann | $5/$4 mo/ann | Custom |
| Browser Check Overages (per 1k) | — | $6.50 | $6.25 | Custom |
| API & Multistep Checks | Yes | Yes | Yes | Yes |
| API Check Runs (included) | 10,000 | 25,000 | 100,000 | Custom |
| Additional API Runs (per 10k) | — | $2/$1.80 mo/ann | $2/$1.80 mo/ann | Custom |
| API Check Overages (per 10k) | — | $2.60 | $2.50 | Custom |
| Automatic Retries | Yes | Yes | Yes | Yes |
| Scheduling | Round Robin & Parallel | Round Robin & Parallel | Round Robin & Parallel | Round Robin & Parallel |
| Public Locations | 6 | 6 | All 22 Locations | All 22 Locations |
| Private Locations | No | No | Yes | Yes |
| SSL Monitoring | Yes | Yes | Yes | Yes |
| 10 Second Frequency | No | No | Yes | Yes |
| Visual Regression Testing | No | No | Yes | Yes |

### Detect — Alerting

| Feature | Hobby | Starter | Team | Enterprise |
|---------|-------|---------|------|------------|
| Email Alerts | Yes | Yes | Yes | Yes |
| Slack Alerts | Yes | Yes | Yes | Yes |
| Webhook Alerts | Yes | Yes | Yes | Yes |
| Incident.io, Rootly & more | No | No | Yes | Yes |
| SMS Alerts | 0 | 100/month | 200/month | Custom |
| Phone Alerts | 0 | 0 | 200/month | Custom |

### Communicate — Status Pages

| Feature | Hobby | Starter | Team | Enterprise |
|---------|-------|---------|------|------------|
| Services | 20 | 25 | 50 | 100 |
| Subscribers | 250 | 500 | 1,000 | 2,000 |
| Custom Domain | No | Yes | Yes | Yes |
| Custom CSS | No | No | Yes | Yes |
| Password Protection | No | No | Yes | Yes |
| White Labeled | No | No | No | Yes |
| Incident Management | No | No | Yes | Yes |

### Communicate — Dashboards

| Feature | Hobby | Starter | Team | Enterprise |
|---------|-------|---------|------|------------|
| Dashboards | 1 | 1 | 10 | Custom |

### Resolve — AI Root Cause Analysis

| Feature | Hobby | Starter | Team | Enterprise |
|---------|-------|---------|------|------------|
| Invocations | 10 | 50 | 150 | Custom |
| Automated RCA | Yes | Yes | Yes | Yes |

### Platform — General

| Feature | Hobby | Starter | Team | Enterprise |
|---------|-------|---------|------|------------|
| Users | 1 | 3 | 10 | Custom |

### Platform — Data Retention

| Feature | Hobby | Starter | Team | Enterprise |
|---------|-------|---------|------|------------|
| Raw Data Retention | 7 days | 7 days | 30 days | 180 days |
| Aggregated Data Retention | 30 days | 30 days | 1 year | 25 months |

### Platform — Integrations

| Feature | Hobby | Starter | Team | Enterprise |
|---------|-------|---------|------|------------|
| Checkly CLI | Yes | Yes | Yes | Yes |
| Terraform Provider | Yes | Yes | Yes | Yes |
| Pulumi Provider | Yes | Yes | Yes | Yes |
| Prometheus Endpoint | No | No | Yes | Yes |

### Platform — Customer Support

| Feature | Hobby | Starter | Team | Enterprise |
|---------|-------|---------|------|------------|
| Premium Support | No | No | No | Yes |
| Onboarding Support | No | No | No | Yes |
| Dedicated Customer Success Engineer | No | No | No | Yes |
| 24x7 Phone Escalation | No | No | No | Yes |
| Contracts & Invoicing | No | No | No | Yes |
| Security Review | No | No | No | Yes |

### Platform — Security & Privacy

| Feature | Hobby | Starter | Team | Enterprise |
|---------|-------|---------|------|------------|
| SOC 2 Type II Compliant | Yes | Yes | Yes | Yes |
| Multi-Factor Auth | Yes | Yes | Yes | Yes |
| SAML/SSO | No | No | No | Yes |
| 99.9% Uptime SLA | No | No | No | Yes |
| Client Certificates | No | No | No | Yes |
| Service API Keys | No | No | No | Yes |

---

## Notes

- Annual billing is approximately 20% cheaper than monthly billing.
- The Hobby plan is free forever with no credit card required.
- Enterprise plan pricing is custom; contact Checkly sales at https://checklyhq.com/contact-sales.
- Overages are charged automatically and are separate from purchased add-on blocks.
- All plans include automated RCA for the Resolve module; the difference is the number of invocations.
- Public locations for Hobby and Starter plans: N. Virginia, N. California, Frankfurt, London, Singapore, Sydney.
- Team and Enterprise plans have access to all 22 global locations.
