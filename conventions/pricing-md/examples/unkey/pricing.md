<!-- source: unkey — https://www.unkey.com/pricing.md -->
# Unkey Pricing

Start for free and scale on demand with predictable usage-based pricing.

Unkey has two products with independent pricing:

- **Unkey Deploy** — Run APIs as containers. Pay for the CPU, memory, and egress you actually use.
- **API Management** — Issue, verify, and manage API keys with tiered request volume plans.

Source: https://unkey.com/pricing

---

## Unkey Deploy

Deploy your code as containers across AWS regions. Deploy is a paid product — start on Starter at $5/mo. All plans include monthly usage credits that offset usage-based charges; beyond the included credits, you pay for average actual vCPU seconds and memory GB-seconds (not the ceilings you configured) plus egress GB. Unused credits do not roll over.

### Plans

| Plan       | Price  | Included Usage | Max vCPU / Instance | Max RAM / Instance | Custom Domains | Regions |
| ---------- | ------ | -------------- | ------------------- | ------------------ | -------------- | ------- |
| Starter    | $5/mo  | $5             | 2                   | 2 GB               | 1              | 3       |
| Pro        | $25/mo | $25            | 8                   | 8 GB               | 10             | All     |
| Business   | $50/mo | $50            | 32                  | 32 GB              | 100            | All     |
| Enterprise | Custom | Custom         | Custom              | Custom             | Custom         | All     |

### Usage Rates (Pay-as-you-go)

Included credits offset usage each month. Beyond credits, additional usage is billed at:

| Resource             | Rate         |
| -------------------- | ------------ |
| vCPU / second        | $0.000006944 |
| Memory / GB / second | $0.000003472 |
| Egress / GB          | $0.05        |

Both vCPU and memory are billed on average actual usage, not the ceilings you configured. You only pay for CPU time when your code is actually executing, not while idle waiting on I/O. Memory is billed on average GB-seconds actually used by your instance. Egress is billed by the gigabyte. Preview deployments are billed at the same rates as production.

### Deploy Plan Limits

| Limit               | Starter   | Pro       | Business  |
| ------------------- | --------- | --------- | --------- |
| Projects            | Unlimited | Unlimited | Unlimited |
| Concurrent Builds   | 1         | 1         | 1         |
| Team members        | 1         | Unlimited | Unlimited |
| Log retention       | 3 days    | 7 days    | 14 days   |
| Audit log retention | 7 days    | 14 days   | 30 days   |
| Support             | Email     | Email     | Email     |

### Deploy Plan Highlights

**Starter** — Ship small production workloads with simple usage-based billing.

- Up to 2 vCPU / 2 GB per Instance
- 1 concurrent build
- Custom domains
- Includes $5/mo usage credits
- Email support

**Pro** — Run production APIs with more compute and headroom.

- Up to 8 vCPU / 8 GB per Instance
- 1 concurrent build
- Custom domains
- Includes $25/mo usage credits
- Email support

**Business** — For higher workloads and growing teams at global scale.

- Up to 16 vCPU / 32 GB per Instance
- 1 concurrent build
- Custom domains
- Includes $50/mo usage credits
- Email support

---

## API Management

Issue and verify API keys for your services. The Pro plan is sold in fixed monthly tiers based on included valid requests per month. Invalid requests (rate-limited, bad keys, etc.) are not counted toward your quota.

### Plans

| Plan       | Price     | Valid Requests / mo | API Keys | Log Retention | Audit Log |
| ---------- | --------- | ------------------- | -------- | ------------- | --------- |
| Free       | $0/mo     | 150K                | 1k       | 1 day         | 3 days    |
| Pro        | $25/mo    | 250K                | 1M       | 7 days        | 14 days   |
| Pro        | $50/mo    | 500K                | 1M       | 7 days        | 14 days   |
| Pro        | $75/mo    | 1M                  | 1M       | 7 days        | 14 days   |
| Pro        | $100/mo   | 2M                  | 1M       | 7 days        | 14 days   |
| Pro        | $250/mo   | 10M                 | 1M       | 7 days        | 14 days   |
| Pro        | $500/mo   | 50M                 | 1M       | 7 days        | 14 days   |
| Pro        | $1,000/mo | 100M                | 1M       | 7 days        | 14 days   |
| Enterprise | Custom    | Custom              | Custom   | Custom        | Custom    |

### API Management Plan Highlights

**Free** — Everything you need to start fast, with the core tools to protect and manage your API.

- 1k API keys
- 150K valid requests / mo
- 1-day logs retention
- 3-day audit log retention
- Unlimited APIs

**Pro** — Predictable pricing without surprises, built for scaling APIs with clear usage-based billing.

- 1M API keys
- 250K valid requests / mo
- 7-day logs retention
- 14-day audit log retention
- Unlimited APIs
- Workspaces with team members

**Enterprise** — Need more support, or pricing doesn’t fit? Built for teams running mission-critical APIs at global scale.

- Custom quotas
- IP Whitelisting
- Dedicated Slack channel

---

## Enterprise

Connect with our team for higher resource limits, dedicated requirements, annual contracts, and more.

Enterprise includes:

- Custom limits
- Dedicated infrastructure
- Dedicated Slack channel
- IP whitelisting
- Annual contracts and SLAs
- SSO, SAML, and audit log exports on request

Contact sales: mailto:support@unkey.com?subject=Unkey%20Enterprise%20Quote

---

## FAQ

**How does usage-based billing work with included credits?**

Each paid plan includes a monthly credit allowance (e.g. $25/mo on Pro) that offsets your usage-based charges for compute and egress. Credits reset at the start of each billing cycle and do not roll over. Once credits are used up, additional usage is billed at the standard per-unit rates.

**How do I avoid runaway costs?**

Unlike serverless platforms that autoscale without bounds, Unkey Deploy runs containers with a max replica count you set per region, giving you a predictable compute ceiling. We bill for actual vCPU, memory, and egress, not per request.

**Can I try a paid plan, and can I downgrade later?**

There's no trial, but Starter is $5/mo and includes $5 in usage credits — enough to build and test Unkey Deploy end-to-end. You can upgrade anytime, and downgrades take effect at the end of your current billing cycle.

**How is compute metered?**

Both vCPU and memory are billed on average actual usage, not the ceilings you configured. You only pay for CPU time when your code is actually executing, not while it's idle waiting on I/O or network calls. Memory is billed by average GB-seconds actually used by your instance, so right-sizing for headroom doesn't penalize you. Egress is billed by the gigabyte. Unkey automatically scales your workload during low activity periods to optimize cost, without introducing cold starts.

**What happens when I hit my plan's limits?**

Each plan caps the max size of an Instance, the number of Instances, and total CPU and memory allocated across your workspace. If a new deployment would exceed any of these, it fails with a clear error. Running applications keep serving traffic without interruption, so you can upgrade or free up capacity before redeploying.

**Do preview deployments count against my usage?**

Yes, preview deployments are billed the same as production. Their vCPU, memory, and egress count against your included credits and then your usage-based rate. Preview environments do get a smaller Sentinel (1 replica instead of 3) to keep the overhead low.

**Can I migrate existing API keys from another provider?**

Yes. You can import pre-hashed keys from your current system into Unkey without requiring your users to generate new ones. Existing keys keep working, and Unkey never sees the plaintext. See https://unkey.com/docs/platform/apis/migrations/introduction for the full flow.

**Where are my workloads hosted, and can I pick regions?**

Unkey deploys on AWS across multiple regions. You pick which regions to deploy to and traffic routes to the nearest healthy region automatically. See https://unkey.com/docs/build-and-deploy/regions for the current list.

**Do you offer SOC 2 compliance?**

Yes, Unkey is SOC 2 compliant. Contact support@unkey.com if you need a copy of our report or have specific compliance requirements for your Enterprise deployment.

**How do I get SSO, SAML, or audit log exports?**

These are available on request. Reach out to support@unkey.com and we'll work with you to get them set up.
