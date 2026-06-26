<!-- source: render — https://render.com/pricing.md -->
# Render Pricing

## Pricing Tiers

| Tier | Price | Description |
|---|---|---|
| Hobby | $0/month + compute | For building personal projects and prototypes. |
| Pro | $25/month + compute | For deploying production-grade apps and agents. |
| Scale | $499/month + compute | For teams that need advanced governance and compliance. |
| Enterprise | Custom pricing | For teams that need dedicated support and uptime SLAs. |

### Hobby Features

*Connect your repo, and go*

- Deploy up to 25 services
- 5 GB of bandwidth included
- Single-service previews
- Global regions & CDN
- Custom domains
- Firewall & DDoS mitigation
- Database PITR
- Email support

### Pro Features

*All Hobby features, plus:*

- No service maximum
- 25 GB bandwidth included
- Full-stack previews
- Horizontal autoscaling
- Isolated environments
- Private links
- Workspace audit logs
- AWS OIDC Integration (Beta)
- Chat support

### Scale Features

*All Pro features, plus:*

- Multiple workspaces
- 1 TB of bandwidth included
- Extended metrics retention
- HIPAA-compliant workspaces
- SAML SSO & SCIM
- Advanced RBAC roles
- Organization audit logs

### Enterprise Features

*All Scale features, plus:*

- Contractual uptime SLAs
- Premium support
- Support response SLAs
- Technical account manager
- Private Slack channel

Compute costs: Pay only for provisioned resources, with transparent pricing based on CPU and service activation prorated to the second.
View our [compute pricing](#compute-pricing) and [FAQs](#frequently-asked-questions)

## Compute pricing

Sensible, scalable, prorated by the second.

### Static Sites

Starting price: $0/month

- Lightning-fast CDN
- Automatic continuous deploys from Git
- Instant cache invalidation
- Custom domains with fully managed TLS

### Services

Starting price: From $0/month

- Web services with HTTP/2 and full TLS
- Node, Python, Go, Rust, Ruby, and Elixir
- Private services
- Custom Docker containers
- Background workers
- [SSDs](https://docs.render.com/disks) for $0.25/GB per month

#### Web Services

| Instance Type | Pricing | RAM | CPU |
|---|---|---|---|
| Free | $0/month | 512 MB | 0.1 |
| Starter | $7/month | 512 MB | 0.5 |
| Standard | $25/month | 2 GB | 1 |
| Pro | $85/month | 4 GB | 2 |
| Pro Plus | $175/month | 8 GB | 4 |
| Pro Max | $225/month | 16 GB | 4 |
| Pro Ultra | $450/month | 32 GB | 8 |
| Custom | Contact sales | Up to 512 GB | Up to 64 |

#### Private Services

| Instance Type | Pricing | RAM | CPU |
|---|---|---|---|
| Starter | $7/month | 512 MB | 0.5 |
| Standard | $25/month | 2 GB | 1 |
| Pro | $85/month | 4 GB | 2 |
| Pro Plus | $175/month | 8 GB | 4 |
| Pro Max | $225/month | 16 GB | 4 |
| Pro Ultra | $450/month | 32 GB | 8 |
| Custom | Contact sales | Up to 512 GB | Up to 64 |

#### Background Workers

| Instance Type | Pricing | RAM | CPU |
|---|---|---|---|
| Starter | $7/month | 512 MB | 0.5 |
| Standard | $25/month | 2 GB | 1 |
| Pro | $85/month | 4 GB | 2 |
| Pro Plus | $175/month | 8 GB | 4 |
| Pro Max | $225/month | 16 GB | 4 |
| Pro Ultra | $450/month | 32 GB | 8 |
| Custom | Contact sales | Up to 512 GB | Up to 64 |

### Render Postgres

Starting price: From $0/month

- Fully managed PostgreSQL databases
- Logical backup retention **(paid only)**
- Connect from anywhere
- Expandable storage ($0.30/GB) **(paid only)**
- High availability **(Pro and above)**
- Point-in-time-recovery (PITR) **(paid only)**

| Tier | Instance Type | Pricing | CPU | RAM | Connection Limit |
|---|---|---|---|---|---|
| Free | Free | $0 (30-day limit) | 0.1 | 256 MB | 100 connections |
| Basic | Basic-256mb | $6/month | 0.1 | 256 MB | 100 connections |
| Basic | Basic-1gb | $19/month | 0.5 | 1 GB | 100 connections |
| Basic | Basic-4gb | $75/month | 2 | 4 GB | 100 connections |
| Pro | Pro-4gb | $55/month | 1 | 4 GB | 100 connections |
| Pro | Pro-8gb | $100/month | 2 | 8 GB | 200 connections |
| Pro | Pro-16gb | $200/month | 4 | 16 GB | 400 connections |
| Pro | Pro-32gb | $400/month | 8 | 32 GB | 500 connections |
| Pro | Pro-64gb | $800/month | 16 | 64 GB | 500 connections |
| Pro | Pro-128gb | $1,700/month | 32 | 128 GB | 500 connections |
| Pro | Pro-192gb | $2,500/month | 48 | 192 GB | 500 connections |
| Pro | Pro-256gb | $3,000/month | 64 | 256 GB | 500 connections |
| Pro | Pro-384gb | $4,600/month | 96 | 384 GB | 500 connections |
| Pro | Pro-512gb | $6,200/month | 128 | 512 GB | 500 connections |
| Accelerated | Accelerated-16gb | $160/month | 2 | 16 GB | 400 connections |
| Accelerated | Accelerated-32gb | $350/month | 4 | 32 GB | 500 connections |
| Accelerated | Accelerated-64gb | $750/month | 8 | 64 GB | 500 connections |
| Accelerated | Accelerated-128gb | $1,500/month | 16 | 128 GB | 500 connections |
| Accelerated | Accelerated-256gb | $2,500/month | 32 | 256 GB | 500 connections |
| Accelerated | Accelerated-384gb | $4,500/month | 48 | 384 GB | 500 connections |
| Accelerated | Accelerated-512gb | $6,000/month | 64 | 512 GB | 500 connections |
| Accelerated | Accelerated-768gb | $9,000/month | 96 | 768 GB | 500 connections |
| Accelerated | Accelerated-1024gb | $11,000/month | 128 | 1024 GB | 500 connections |

### Render Key Value

Starting price: From $0/month

- Fully managed Redis®-compatible caching
- Connect from anywhere
- Maximize availability by queueing jobs
- Reduce primary DB's load
- Cache pages, results, fragments

| Instance Type | Pricing | RAM | High CPU | Connection Limit | Persistence |
|---|---|---|---|---|---|
| Free | $0/month | 25 MB |  | 50 connections | - |
| Starter | $10/month | 256 MB |  | 250 connections | ✓ |
| Standard | $32/month | 1 GB |  | 1,000 connections | ✓ |
| Pro | $135/month | 5 GB |  | 5,000 connections | ✓ |
| Pro Plus | $250/month | 10 GB |  | 10,000 connections | ✓ |
| Pro Max | $550/month | 20 GB | ✓ | 20,000 connections | ✓ |
| Pro Ultra | $1100/month | 40 GB | ✓ | 40,000 connections | ✓ |
| Custom | Contact sales | Up to 512 GB | ✓ | Contact sales | ✓ |

### Cron Jobs

Starting price: From $1/month

- Run any command or script periodically
- Failure notifications
- Full support for cron expressions
- Prorated by the second
- Live cron job logs

| Instance Type | Pricing | RAM | CPU |
|---|---|---|---|
| Starter | $0.00016/minute | 512 MB | 0.5 |
| Standard | $0.00058/minute | 2 GB | 1 |
| Pro | $0.00197/minute | 4 GB | 2 |
| Pro Plus | $0.00405/minute | 8 GB | 4 |
| Custom | Contact sales |  Up to 512 GB | Up to 64 |

### Workflows (Beta)

Starting price: From $1/month

- Fully-managed durable execution
- Run 1000s of parallel, async tasks
- Sub-second task spin-up
- Automatic task retries

| Task compute | $/Hour | CPU | RAM |
|---|---|---|---|
| Starter | $0.05  | 0.5 | 512MB |
| Standard | $0.20 | 1 | 2GB |
| Pro | $0.40 | 2 | 4GB |
| Pro Plus | $1.00 | 4 | 8GB |
| Pro Max | $2.00 | 4 | 16GB |
| Pro Ultra | $7.00 | 8 | 32GB |

## Workspace features

Compare features across workspace plans.

| Tier | Action |
|---|---|
| Hobby | [Start deploying](https://dashboard.render.com/register?next=%2Fselect-plan%3Fplan%3Dhobby) |
| Pro | [Select plan](https://dashboard.render.com/register?next=%2Fselect-plan%3Fplan%3Dprofessional) |
| Scale | [Select plan](https://dashboard.render.com/register?next=%2Fselect-plan%3Fplan%3Dorganization) |
| Enterprise | Get in touch |

### Render Services & Storage

| Feature | Hobby | Pro | Scale | Enterprise |
|---|---|---|---|---|
| Maximum services (The total number of services you can create in your workspace) | 25 | Unlimited | Unlimited | Unlimited |
| Static Sites | ✓ | ✓ | ✓ | ✓ |
| Standard services | ✓ | ✓ | ✓ | ✓ |
| - Web services | ✓ | ✓ | ✓ | ✓ |
| - Private services | ✓ | ✓ | ✓ | ✓ |
| - Background workers | ✓ | ✓ | ✓ | ✓ |
| - Persistent disks (Provision high-speed SSDs to attach to your web services, private services, and background workers) | $0.25 per GB per month | $0.25 per GB per month | $0.25 per GB per month | $0.25 per GB per month |
| Postgres databases | ✓ | ✓ | ✓ | ✓ |
| - Expandable storage | $0.30 per GB | $0.30 per GB | $0.30 per GB | $0.30 per GB |
| - Point-in-time recovery window | 3 days | 7 days | 7 days | 7 days |
| - Read-only replicas | ✓ | ✓ | ✓ | ✓ |
| - High availability | ✓ | ✓ | ✓ | ✓ |
| Key-value (Redis-compatible) | ✓ | ✓ | ✓ | ✓ |
| Cron jobs | ✓ | ✓ | ✓ | ✓ |
| Workflows | ✓ | ✓ | ✓ | ✓ |
| - Concurrent task runs (The maximum number of task runs that can execute concurrently in your workspace. More concurrency allows higher throughput.) | 20 task runs | 50 task runs (then $10/mo per 50) | 100 task runs (then $10/mo per 50) | Custom |
| - Task compute plans | Up to Pro | Up to Pro Ultra | Up to Pro Ultra | Custom |
| Service scaling | ✓ | ✓ | ✓ | ✓ |
| - Vertical scaling (Run your most compute-intensive workloads on instances with up to 64 CPUs and 512 GB of RAM.) | ✓ | ✓ | ✓ | ✓ |
| - Horizontal autoscaling (Automatically scale services based on target CPU and memory utilization—or configure custom autoscaling rules with Render’s API. Load balancing automatically distributes traffic among instances of your services.) | - | ✓ | ✓ | ✓ |

### Networking

| Feature | Hobby | Pro | Scale | Enterprise |
|---|---|---|---|---|
| Automatic private networking | ✓ | ✓ | ✓ | ✓ |
| Bandwidth | 5 GB included per month (then $0.15 per GB) | 25 GB included per month (then $0.15 per GB) | 1 TB included per month (then $0.15 per GB) | Custom |
| Global regions | ✓ | ✓ | ✓ | ✓ |
| Zero-config CDN (We cache your content on network edges around the world, ensuring the fastest possible load times for your users.) | ✓ | ✓ | ✓ | ✓ |
| Edge caching for web services | ✓ | ✓ | ✓ | ✓ |
| Custom domains | 2 included (then $0.25/domain/month) | 15 included (then $0.25/domain/month) | 25 included (then $0.25/domain/month) | Custom |
| - Automatic TLS | ✓ | ✓ | ✓ | ✓ |
| - Wildcard domains | ✓ | ✓ | ✓ | ✓ |
| WebSockets | ✓ | ✓ | ✓ | ✓ |
| Service discovery | ✓ | ✓ | ✓ | ✓ |
| Dedicated IPs | - | $100 per month (for each IP set) | $100 per month (for each IP set) | Custom |
| AWS private links (Securely connect to AWS-hosted cloud services.) | - | $30 per month (Includes up to 3 links) | $30 per month (Includes up to 3 links) | Custom |
| - Private link outbound bandwidth | - | $0.03 per GB | $0.03 per GB | Custom |

### Protection

| Feature | Hobby | Pro | Scale | Enterprise |
|---|---|---|---|---|
| Automatic DDoS mitigation | ✓ | ✓ | ✓ | ✓ |
| Firewall | ✓ | ✓ | ✓ | ✓ |
| HTTPS only | ✓ | ✓ | ✓ | ✓ |
| Inbound IP rules (Allow incoming connections only from specified IP ranges) | Datastores only (Postgres and Key Value) | Datastores only (Postgres and Key Value) | ✓ | ✓ |
| Network-isolated environments | - | ✓ | ✓ | ✓ |

### Build & Deploy

| Feature | Hobby | Pro | Scale | Enterprise |
|---|---|---|---|---|
| Automatic builds | ✓ | ✓ | ✓ | ✓ |
| - Standard build pipeline | 500 mins per month (then $5 per 1K mins) | 1K mins per month (then $5 per 1K mins) | 5K mins per workspace per mo. (then $5 per 1K mins) | Custom |
| - Performance build pipeline (Run your builds on machines with significantly more CPU and memory) | - | $25 per 1000 mins | $25 per 1000 mins | Custom |
| - Native runtimes | ✓ | ✓ | ✓ | ✓ |
| - Docker builds | ✓ | ✓ | ✓ | ✓ |
| - Environment variables & secret files | ✓ | ✓ | ✓ | ✓ |
| - Monorepo support | ✓ | ✓ | ✓ | ✓ |
| Previews | ✓ | ✓ | ✓ | ✓ |
| - Single-service previews | ✓ | ✓ | ✓ | ✓ |
| - Full-stack preview environments | - | ✓ | ✓ | ✓ |
| Deploy orchestration | ✓ | ✓ | ✓ | ✓ |
| - Auto-deploys | ✓ | ✓ | ✓ | ✓ |
| - Zero-downtime deploys | ✓ | ✓ | ✓ | ✓ |
| - Deploy hooks | ✓ | ✓ | ✓ | ✓ |
| - Pre-deploy command | ✓ | ✓ | ✓ | ✓ |
| - Instant rollbacks | 5 builds retained | 15 builds retained | 30 builds retained | 30 builds retained |
| Projects | Unlimited | Unlimited | Unlimited | Unlimited |
| Environments | 2 per project | Unlimited | Unlimited | Unlimited |
| - Protected environments | ✓ | ✓ | ✓ | ✓ |
| Infrastructure as code (Express your application architecture as code in a render.yaml blueprint) | ✓ | ✓ | ✓ | ✓ |

### Monitoring

| Feature | Hobby | Pro | Scale | Enterprise |
|---|---|---|---|---|
| SSH access | ✓ | ✓ | ✓ | ✓ |
| Health checks | ✓ | ✓ | ✓ | ✓ |
| Service metrics | ✓ | ✓ | ✓ | ✓ |
| Notifications | ✓ | ✓ | ✓ | ✓ |
| Log retention | 7 days | 14 days | 30 days | 30 days |
| Log streams | ✓ | ✓ | ✓ | ✓ |
| HTTP request logs | - | ✓ | ✓ | ✓ |
| OpenTelemetry metrics stream | - | ✓ | ✓ | ✓ |

### Platform Access & Security

| Feature | Hobby | Pro | Scale | Enterprise |
|---|---|---|---|---|
| Team seats | 1 | Unlimited | Unlimited | Unlimited |
| Workspaces | 1 | 1 | Unlimited | Unlimited |
| 2FA & Google login | ✓ | ✓ | ✓ | ✓ |
| - Enforce 2FA & Google login | - | ✓ | ✓ | ✓ |
| Workspace user roles | - | Admin, Developer | Admin, Developer, Contributor, Viewer, Billing | Admin, Developer, Contributor, Viewer, Billing |
| Organization user roles | - | - | Owner, Member, Guest | Owner, Member, Guest |
| SAML SSO | - | - | ✓ | ✓ |
| SCIM | - | - | ✓ | ✓ |
| AWS OIDC Integration (Beta) | - | ✓ | ✓ | ✓ |
| Audit logs | - | Workspace | Workspace and organization | Workspace and organization |

### Compliance

| Feature | Hobby | Pro | Scale | Enterprise |
|---|---|---|---|---|
| GDPR DPA | ✓ | ✓ | ✓ | ✓ |
| SOC 2 Type II | ✓ | ✓ | ✓ | ✓ |
| ISO 27001 | ✓ | ✓ | ✓ | ✓ |
| SOC 2 & ISO documentation (Access Render's SOC 2 Type II report and ISO 27001 certification through our compliance center) | - | ✓ | ✓ | ✓ |
| HIPAA BAA | - | - | 20% compute premium for enabled workspaces | 20% compute premium for enabled workspaces |

### Support

| Feature | Hobby | Pro | Scale | Enterprise |
|---|---|---|---|---|
| Community | ✓ | ✓ | ✓ | ✓ |
| Email | ✓ | ✓ | ✓ | ✓ |
| Chat | - | ✓ | ✓ | ✓ |
| Premium support | - | Add-on | Add-on | ✓ |
| - Private Slack channel | - | Add-on | Add-on | ✓ |
| - Dedicated technical account manager | - | Add-on | Add-on | ✓ |
| - Support response SLAs | - | Add-on | Add-on | ✓ |
| - Migration assistance & architecture review | - | Add-on | Add-on | ✓ |

## Frequently Asked Questions

### How does billing work?

Render charges for three things: your workspace plan (flat subscription), metered features like bandwidth (usage-based), and [compute](https://render.com/pricing#compute) for your applications (usage-based). 

### How am I billed for compute?

[Compute plans](https://render.com/pricing#compute) are set at a per-service basis, and billing is prorated to the second. If you create a web service on a paid compute plan and turn it off 24 hours later, you are only billed for 24 hours of compute. This also applies to service types that spin up and shut down automatically, like Cron Jobs and Workflows. You are only billed for compute when these services are actively running your workload.

### My Pro or Scale workspace did not have any activity or services this month. Will I still be charged for the workspace subscription? 

If a workspace has no services (live or suspended) and no activity during a month, the workspace subscription fee for that month will be waived.

### I run a large agency with developers on multiple teams. What does this mean for us?

Scale and Enterprise plans let you create multiple workspaces within the same organization to better manage multiple teams. Our team is happy to help you determine the best way to organize your teams on Render. [Contact us](https://render.com/contact) here.

### What are build pipeline minutes, and how can I track my usage?

Your workspace's builds and other pre-deploy tasks use Render compute resources. [Pipeline minutes](https://docs.render.com/build-pipeline#pipeline-minutes) track the duration of these tasks. You can view your pipeline usage from your dashboard's Billing page.

With a Professional plan or higher, you can enable the [Performance pipeline](https://docs.render.com/build-pipeline#pipeline-tiers) to run builds on larger compute instances, with an additional corresponding charge for pipeline minutes.

### How do free compute plans work?

With Render’s [Free compute plans](https://render.com/docs/free), you can spin up [web services](https://docs.render.com/free#free-web-services), [Render Key Value instances](https://docs.render.com/free#free-key-value), and [Render Postgres databases](https://render.com/docs/free#free-postgres) at no charge. Free compute plans types have usage limits and are designed to help you to explore new tech, build personal projects, and preview Render's developer experience.

### Which payment methods do you accept?

We accept all major credit and debit cards. Your payment info is stored and processed securely by [Stripe](https://stripe.com/) and never touches our servers.

### Why was I charged $1 after adding a credit card?

A $1 USD transaction is performed as a credit security check to ensure your card details are correct and authorized. The charge is refunded after the transaction completes.

### I have an infrequently asked question.

Great! We're always around to help. You can email us any time at [support@render.com](mailto:support@render.com), or talk to us in our [user community](https://community.render.com/).
