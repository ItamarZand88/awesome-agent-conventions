<!-- source: pinecone — https://www.pinecone.io/pricing.md -->
# Pricing

## Start free, scale effortlessly

Pinecone runs on fully managed infrastructure that scales with you. Start building today with product and support plans tailored to your needs.

**Also available on your cloud marketplace:**

- [AWS](https://aws.amazon.com/marketplace/pp/prodview-xhgyscinlz4jk?trk=95b758bd-2bf2-4def-81d3-911b0f6514fe&sc_channel=el&source=pinecone%20systems)
- [GCP](https://console.cloud.google.com/marketplace/product/pinecone-public/pinecone)
- [Microsoft](https://marketplace.microsoft.com/product/saas/pineconesystemsinc1688761585469.pineconesaas)

## Starter

For trying out and for small applications.

[Start for Free](https://app.pinecone.io/organizations/-/settings/billing)

**Free**

- Pinecone Database [On-Demand](https://docs.pinecone.io/guides/organizations/manage-cost/understanding-cost.md)
- Pinecone [Inference](https://docs.pinecone.io/guides/inference/understanding-inference.md)
- Pinecone [Assistant](https://docs.pinecone.io/guides/assistant/understanding-assistant.md)
- Dense, Sparse, and Full-Text Indexes
- Console Metrics
- Community Support via [Discord](https://discord.gg/qU3yVdqRda)

## Builder (NEW)

For solo developers and small teams.

[Get Started](https://app.pinecone.io/organizations/-/settings/billing)

**$20/month flat**

- Everything in Starter
- Increased usage limits
- Choose your cloud and region (coming soon)
- Multiple projects and users
- Prometheus and Datadog monitoring

Includes Free support. Response SLAs available via Developer or Pro support add-on.

## Standard (POPULAR)

For production applications at any scale.

[Start Free Trial](https://app.pinecone.io/organizations/-/settings/billing)

**$50/month min. usage** — You'll be charged a minimum of $50/month. Once your usage exceeds this amount, you'll pay as you go.

3 week trial includes $300 credits.

- Everything in Builder
- Pay-as-you-go for Database On-Demand, Inference, and Assistant Usage
- Choose your cloud and region
- [Dedicated Read Nodes (DRN)](https://docs.pinecone.io/guides/index-data/dedicated-read-nodes.md)
- Import from object storage
- Backup and Restore
- User and API Key RBAC
- SAML SSO
- [HIPAA add-on](https://docs.pinecone.io/guides/manage-cost/understanding-cost.md)

Includes Free support. Response SLAs available via Developer or Pro support add-on.

## Enterprise

For mission-critical production applications.

[Get Started](https://app.pinecone.io/organizations/-/settings/billing)

[Request Trial](https://www.pinecone.io/contact/?contact_form_inquiry_type=Enterprise+Trial#contact-form)

**$500/month min. usage** — You'll be charged a minimum of $500/month. Once your usage exceeds this amount, you'll pay as you go.

- Everything in Standard
- 99.95% Uptime SLA
- Private Networking
- Customer Managed Encryption Keys
- Audit Logs
- Service Accounts
- Admin APIs
- HIPAA Compliance
- Pro support included

Estimate your costs with our [pricing calculator](https://www.pinecone.io/pricing/estimate/).

## Bring your own cloud

For organizations requiring the highest level of security and control.

[Get Started](https://github.com/pinecone-io/pulumi-pinecone-byoc)

- Pinecone in your cloud account
- Zero-access operations – no SSH, VPN, or inbound access required
- Outbound-only operations with an auditable trail
- Pro support included

[Bring-your-own-cloud (BYOC)](https://docs.pinecone.io/guides/operations/bring-your-own-cloud.md) runs Pinecone in your cloud account and VPC. Pinecone does not need SSH, VPN, or inbound network access to operate the system. You can use public endpoints or private-only connectivity via AWS PrivateLink, GCP Private Service Connect, or Azure Private Link.

[Contact us](https://www.pinecone.io/contact/?contact_form_inquiry_type=Enterprise%20Pricing) for assistance sizing and pricing your BYOC deployment.

## What you can build on the Starter plan

### Recommendation engine

Given an e-commerce site with:

- 50K products
- 10KB metadata per product
- Using 1024 dimensions embeddings

Starter plan gives you:

- ~ 44K recommendations per day
- ~ 2K product updates per day

### Semantic search

Given a knowledge base of:

- ~ 30K documents
- 20KB document size on average
- Using 1024 dimensions embeddings

Starter plan gives you:

- ~ 15k searches per day
- ~ 660 document updates per day

### Forum answering bot (RAG)

Given a user forum with:

- ~ 10 categories
- 5KB post size on average
- Using 1024 dimensions embeddings

Starter plan gives you:

- ~ 130K category-scoped chats per day
- ~ 3K messages indexed per day

**Disclaimer:** Examples are illustrative only, not quotes or binding offers. Database usage only; excludes Inference (embeddings/reranking) and Assistant usage, as well as initial data import. Subject to change.

## Explore products

- **On-Demand**: The foundation for knowledgeable AI. Backed by distributed object storage for scalable, highly available serverless indexes. [Docs](https://docs.pinecone.io/guides/get-started/overview.md)
- **DRN**: Dedicated Read Nodes. Exclusive infrastructure for queries, with provisioned nodes reserved for your index – no noisy neighbors, no shared queues, no read rate limits. [Docs](https://docs.pinecone.io/guides/index-data/dedicated-read-nodes.md)
- **BYOC**: Bring Your Own Cloud. Managed Pinecone in your cloud with a zero-access operating model. [Docs](https://docs.pinecone.io/guides/production/bring-your-own-cloud.md)
- **Nexus**: Pinecone Nexus is a knowledge engine for agents. It offloads retrieval, assembly, and reasoning from the LLM to a dedicated knowledge layer – done once when your data changes, not on every agent call.  [Early Access](https://www.pinecone.io/lp/nexus-ea)
- **Inference**: Pinecone Inference is a service that gives you access to embedding and reranking models hosted on Pinecone's infrastructure. [Docs](https://docs.pinecone.io/guides/inference/understanding-inference.md)
- **Assistant**: Pinecone Assistant is a service that allow you to build production-grade chat and agent-based applications quickly. [Docs](https://docs.pinecone.io/guides/assistant/overview.md)
- **Support**: Pinecone Support provides various tiers of assistance to ensure your application's success, from community support to dedicated engineering resources.

### Usage-based pricing

$50 monthly minimum that's applied to your usage. Anything over $50 is billed pay-as-you-go.

### Committed Use Contracts

The larger your usage commitments, the greater your benefits—unlock bigger discounts and support.

[Contact Us](https://www.pinecone.io/contact/?contact_form_inquiry_type=Sales)

## Plan comparison

### Database Features

| Feature                              | Starter                  | Builder                                | Standard                       | Enterprise                     |
|--------------------------------------|--------------------------|----------------------------------------|--------------------------------|--------------------------------|
| Cloud Availability                   | AWS                      | AWS (all clouds coming soon)           | AWS, Azure, GCP                | AWS, Azure, GCP                |
| Region Availability                  | us-east-1                | us-east-1 (all regions coming soon)    | All available regions          | All available regions          |
| Dedicated Read Nodes                 | —                        | —                                      | ✓                              | ✓                              |
| Index Types                          | Dense, Sparse, Full-Text | Dense, Sparse, Full-Text               | Dense, Sparse, Full-Text       | Dense, Sparse, Full-Text       |
| Indexes                              | Up to 5                  | 10 per project                         | 20 per project                 | 200 per project                |
| Namespaces per Index                 | 100                      | 1,000                                  | 100,000                        | 100,000                        |
| Embedding Models                     | All available models     | All available models                   | All available models           | All available models           |
| Reranking Models                     | bge-reranker-v2-m3 only  | bge-reranker-v2-m3 only                | All available models           | All available models           |
| Console Index Metrics                | ✓                        | ✓                                      | ✓                              | ✓                              |
| Prometheus and Datadog Monitoring    | —                        | ✓                                      | ✓                              | ✓                              |
| Uptime SLA                           | —                        | —                                      | —                              | 99.95%                         |

### Pricing Dimensions — Database

| Dimension                  | Starter        | Builder         | Standard                                    | Enterprise                                  |
|----------------------------|----------------|-----------------|---------------------------------------------|---------------------------------------------|
| Storage                    | Up to 2 GB     | Up to 10 GB     | Unlimited — $0.33/GB/mo                     | Unlimited — $0.33/GB/mo                     |
| Write Units                | Up to 2M/mo    | Up to 5M/mo     | Unlimited — $4–$4.50 per million (varies by cloud and region) | Unlimited — $6–$6.75 per million (varies by cloud and region) |
| Read Units                 | Up to 1M/mo    | Up to 2M/mo     | Unlimited — $16–$18 per million (varies by cloud and region) | Unlimited — $24–$27 per million (varies by cloud and region) |
| Import from object storage | —              | —               | ✓ ($0.25 per GB)                               | ✓ ($0.25 per GB)                               |
| Backups                    | —              | —               | ✓ ($0.10/GB/mo)                             | ✓ ($0.10/GB/mo)                             |
| Restore from backup        | —              | —               | ✓ ($0.15 per GB)                            | ✓ ($0.15 per GB)                            |

### Pricing Dimensions — Assistant

| Dimension                    | Starter                                       | Builder                | Standard                                | Enterprise                              |
|------------------------------|-----------------------------------------------|------------------------|-----------------------------------------|-----------------------------------------|
| Document Limit               | Unlimited                                     | Unlimited              | Unlimited                               | Unlimited                               |
| Storage                      | 1GB Storage included                          | 3GB Storage included   | Unlimited ($3/GB/mo)                    | Unlimited ($3/GB/mo)                    |
| Input Tokens                 | 500k/mo included (1M/mo until June 30, 2026)  | 2M/mo included         | Unlimited ($8 per million)              | Unlimited ($8 per million)              |
| Output Tokens                | 300k/mo included                              | 1M/mo included         | Unlimited ($15 per million)             | Unlimited ($15 per million)             |
| Context Processed Tokens     | 500k/mo included                              | 2M/mo included         | Unlimited ($5 per million)              | Unlimited ($5 per million)              |
| Evaluation Processed Tokens  | —                                             | —                      | Unlimited ($8 per million)              | Unlimited ($8 per million)              |
| Evaluation Output Tokens     | —                                             | —                      | Unlimited ($15 per million)             | Unlimited ($15 per million)             |
| Ingestion Units              | 1,000/mo included                             | 10K/mo included        | $0.0005/unit / $0.001 multi-modal       | $0.0005/unit / $0.001 multi-modal       |
| Region                       | USA                                           | USA (more coming soon) | Any                                     | Any                                     |

### Pricing Dimensions — Inference: Embedding

| Model                       | Starter             | Builder              | Standard            | Enterprise          |
|-----------------------------|---------------------|----------------------|---------------------|---------------------|
| llama-text-embed-v2         | 5M tokens/mo incl.  | 10M tokens/mo incl.  | $0.16/M tokens      | $0.16/M tokens      |
| multilingual-e5-large       | 5M tokens/mo incl.  | 10M tokens/mo incl.  | $0.08/M tokens      | $0.08/M tokens      |
| pinecone-sparse-english-v0  | 5M tokens/mo incl.  | 10M tokens/mo incl.  | $0.08/M tokens      | $0.08/M tokens      |

### Pricing Dimensions — Inference: Reranking

| Model               | Starter                       | Builder                         | Standard          | Enterprise        |
|---------------------|-------------------------------|---------------------------------|-------------------|-------------------|
| pinecone-rerank-v0  | —                             | —                               | $2/1k requests    | $2/1k requests    |
| bge-reranker-v2-m3  | 500 requests/mo incl.         | 1,000 requests/mo incl.         | $2/1k requests    | $2/1k requests    |
| cohere-rerank-v3.5  | —                             | —                               | $2/1k requests    | $2/1k requests    |

### Org Management

| Feature           | Starter  | Builder              | Standard              | Enterprise            |
|-------------------|----------|----------------------|-----------------------|-----------------------|
| Projects          | 1        | 5                    | 20                    | 100                   |
| Users             | Up to 2  | Up to 5              | Unlimited             | Unlimited             |
| SAML SSO          | —        | —                    | ✓                     | ✓                     |
| Service Accounts  | —        | —                    | —                     | ✓                     |
| Admin API         | —        | —                    | ✓                     | ✓                     |
| Support           | —        | Free support included| Free support included | Pro support included  |

### Security and Compliance

| Feature                            | Starter | Builder | Standard | Enterprise |
|------------------------------------|---------|---------|----------|------------|
| Encryption at rest and in transit  | ✓       | ✓       | ✓        | ✓          |
| User RBAC                          | —       | —       | ✓        | ✓          |
| API Key RBAC                       | —       | —       | ✓        | ✓          |
| Audit Logs                         | —       | —       | —        | ✓          |
| Private Endpoints                  | —       | —       | —        | ✓          |
| Customer Managed Encryption Keys   | —       | —       | —        | ✓          |
| SOC 2                              | ✓       | ✓       | ✓        | ✓          |
| GDPR                               | —       | ✓       | ✓        | ✓          |
| ISO 27001                          | —       | ✓       | ✓        | ✓          |
| HIPAA                              | —       | —       | $190/mo  | ✓          |

## Support pricing

### Free

$0/mo · Start building with basic support · Included with Standard

### Developer

$29/mo · Direct access for growing projects

[Select](https://app.pinecone.io/organizations/-/settings/support/plans)

### Pro

$250/mo · For production applications at any scale

[Select](https://app.pinecone.io/organizations/-/settings/support/plans)

### Premium

Enterprise only · Premium support for Enterprise users

[Contact Sales](https://www.pinecone.io/contact/?contact_form_inquiry_type=Enterprise+Pricing)

| Feature                          | Free   | Developer                                                       | Pro                                                              | Premium                                                                |
|----------------------------------|--------|-----------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------------|
| On-call availability             | —      | Business hours                                                  | 24/7/365                                                         | 24/7/365                                                               |
| First response SLAs              | —      | Sev 1: 8h, Sev 2: 12h, Sev 3: 2d, Sev 4: 3d                     | Sev 1: 2h (24/7), Sev 2: 4h, Sev 3: 12h, Sev 4: 2d               | Sev 1: 30m (24/7), Sev 2: 2h, Sev 3: 8h, Sev 4: 12h                    |
| Ticket Portal                    | ✓      | ✓                                                               | ✓                                                                | ✓                                                                      |
| Support Bot                      | ✓      | ✓                                                               | ✓                                                                | ✓                                                                      |
| Community Forum                  | ✓      | ✓                                                               | ✓                                                                | ✓                                                                      |
| Slack channel                    | —      | —                                                               | ✓                                                                | ✓                                                                      |
| Zoom/Meet/Teams                  | —      | —                                                               | ✓                                                                | ✓                                                                      |
| Email                            | —      | —                                                               | ✓                                                                | ✓                                                                      |
| Dedicated Customer Success Eng.  | —      | —                                                               | —                                                                | ✓                                                                      |
| General architectural guidance   | ✓      | ✓                                                               | ✓                                                                | ✓                                                                      |
| Use-case specific guidance       | —      | ✓                                                               | ✓                                                                | ✓                                                                      |
| Code reviews                     | —      | —                                                               | ✓                                                                | ✓                                                                      |
| Live consultations               | —      | —                                                               | —                                                                | ✓                                                                      |

## Start building knowledgeable AI today

Create your first index for free, then pay as you go when you're ready to scale.

[Start Building](https://app.pinecone.io/)

[Get a Demo](https://www.pinecone.io/contact/?contact_form_inquiry_type=Sales)
