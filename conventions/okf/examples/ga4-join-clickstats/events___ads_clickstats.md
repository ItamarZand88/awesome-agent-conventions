<!-- source: ga4-join-clickstats — https://raw.githubusercontent.com/GoogleCloudPlatform/knowledge-catalog/main/okf/bundles/ga4/references/joins/events___ads_clickstats.md -->
---
type: Reference
resource: https://developers.google.com/analytics/bigquery/basic-queries
title: Join Google Analytics Events to Google Ads Clicks
description: Join Google Analytics event data with Google Ads click data.
tags:
- join
- Google Ads
timestamp: '2026-05-28T22:51:46+00:00'
---

Join Google Analytics event data with Google Ads click data.

```sql
GA_EVENTS.collected_traffic_source.gclid = ADS_CLICKS.gclid
```

# Citations
- https://developers.google.com/analytics/bigquery/basic-queries
