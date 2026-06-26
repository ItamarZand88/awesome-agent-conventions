<!-- source: tigerdata — https://www.tigerdata.com/pricing.md -->
---
title: "Tiger Cloud Pricing. Scale Further. Spend Less."
description: "Flexible and transparent PostgreSQL cloud pricing. Optimized data storage with 95% compression and lightning-fast performance. Pay only for what you use."
url: "https://www.tigerdata.com/pricing"
---


# Tiger Pricing

Discover the perfect plan to fuel your projects. Whether you're an early-stage startup or a growing enterprise, we've got the solution for you.

## Plans

### Performance

Starting at $30/month

For new applications and internal tools that need strong performance without complexity. Hourly billing with zero friction to get started.

**Solid Performance:**
  - 4 database services
  - Up to 8 CPU and 32 GB memory per service
  - Up to 16 TB disk storage per service
  - Up to 5K IOPS, 250 MB/s throughput

**Basic Security:**
  - 1 VPC
  - 1 IP Allow-list

**Reliability and monitoring:**
  - Single-node high-availability replicas
  - Point-in-time-recovery to 3 days
  - Performance Insights
  - Basic support (9-5 ET)

### Scale

Starting at $36/month

For high-volume, resource-intensive applications that demand production-grade performance and scalability. Pay-as-you-go flexibility. 

**High Performance and Scalability:**
  - Unlimited database services
  - Up to 32 CPU and 128 GB memory per service
  - Up to 64 TB disk storage per service
  - Up to 40K IOPS, 1,500 MB/s throughput
  - Unlimited Tiered Storage
  - Horizontal read scaling with read replicas

**Security and Compliance:**
  - AWS Transit Gateway
  - Private endpoints
  - Unlimited VPC
  - Unlimited IP Allow lists
  - SOC 2 report

**Advanced Reliability and Monitoring:**
  - Multi-node high-availability replicas
  - Point-in-time-recovery to 14 days
  - Integrations with observability tools

### Enterprise

Custom pricing

For mission-critical applications that require 24/7 business continuity, advanced security and full compliance. Customized for your exacting standards.

**Higher Performance and Scalability:**
  - Up to 64 CPU and 256 GB memory per service
  - Up to 64 TB disk storage per service
  - Up to 80K IOPS, 2,000 MB/s throughput

**Advanced Security and Compliance:**
  - SAML Single-sign-on (SSO)
  - HIPAA compliance
  - Security questionnaire

**Mission-Critical Reliability and Monitoring:**
  - Cross-region backups for disaster recovery
  - Enterprise SLAs
  - Production support (24x7, 1 hour response time for Sev 1 issues)

**Enterprise Expert Services:**
  - Integration and migration services

## Why Tiger Pricing

### Only pay for what you use

Hourly billing for your configured compute and actual storage used, no hidden fees. Cancel anytime.

### High performance, low overhead

Millisecond query response times on terabytes of data with hybrid row-columnar engine, automatic partitioning and incremental materialized views. Reduce storage costs with columnar compression and tiered storage.

### Fast start, full control

Spin up services in minutes (no credit card needed), track usage and billing in real time, and tune your stack as your workloads evolve.

## FAQ

### How does billing work?

Tiger Cloud charges based on consumption. Compute is metered on an hourly basis, and you can scale it up or down at any time. Storage is metered based on your average GB consumption per hour; it grows and shrinks automatically with your data.

So if at the end of the month, your database service has been running for 500 hours, of which 375 are with 2 CPU and 125 with 4 CPU, then your compute cost is (375 x hourly price for 2 CPU) + (125 * hourly price for 4 CPU). Your monthly price for storage is computed similarly. Certain add-on features may incur additional charges to increase functionality – such as HA replicas, IO boost, tiered storage and production support.

### When will I be billed?

You’ll be billed at the end of each month in arrears, based on your actual usage that month.  Your monthly invoice will include an itemized cost accounting for each database service (compute and storage) and any additional charges (e.g., VPC peering, tiered storage, production support).

### Can I upgrade or downgrade my plan at any time?

You can easily upgrade or downgrade between the Performance and Scale plans whenever you want.  If you switch your plan mid-month, your prices are pro-rated to when you switch.  And your services won’t be interrupted if you switch, so you can keep working without any hassle. 

### Is there a free trial of Tiger Cloud and its different tiers?

Yes! We offer new users a free, 30-day trial period (no credit card required) of our Performance plan. During your trial, you can contact us request more information about, and access to, our Scale plan to determine how it fits your needs. And once you become a paying user, we can make certain features of higher plans available to you for testing without upgrading your entire plan.

### How do I monitor my usage and costs?

Your account console shows your resource usage and dashboards with performance insights, which allows you to closely monitor your services’ performance and any need to scale your services or upgrade your plan.

Your console also shows your month-to-date accrued charges, as well as a forecast of your expected month-end bill. Your previous invoices are also available as PDFs for download in the console.

### How should I size my services?

Compute requirements are highly dependent on the workload. Tiger Cloud is very efficient and generally needs less compute than other databases to deliver the same performance (check out RTA Bench for performance comparisons). The best way to size your needs is to sign-up for a free trial and to test with a realistic workload.

You don’t need to worry about sizing storage. Tiger Cloud just charges by the actual storage used, unlike Amazon RDS or self-managed infrastructure where you pre-provision disk and pay for its allocation. As your data volume grows, we also autoscale IOPS and storage bandwidth to meet those needs (at no additional cost within your plan’s range).

### Is there a limit on how much I can store?

We make it easy for you to store unlimited amounts of data using tiered storage composed of a high-performance storage tier and a low-cost bottomless storage tier. You can keep up to 64 TB compressed in the high-performance storage tier, and configure less-frequently accessed data to be moved to our low-cost storage tier built on object storage.

### Do you charge differently between regions?

Storage is priced the same across all regions, but compute prices will vary depending on the region. We do so because our cloud providers price infrastructure differently based on region.

### How much more does it cost to add database replicas?

HA and read replicas are both charged at the same rate as your primary service, based on the compute and primary storage consumed by your replicas. Data tiered to our bottomless storage tier is shared by all database replicas; replicas accessing tiered storage will not add to your bill.

### Do all plans get support?

Yes! We run a global support organization that covers all timezones, and is even fully staffed for weekend hours. Customer Satisfaction (CSAT) scores above 99%. All plans have free Developer Support, via email and with a target response time of 1 business day (although often faster). But if you need 24x7 responsiveness, talk to us about Production Support.
