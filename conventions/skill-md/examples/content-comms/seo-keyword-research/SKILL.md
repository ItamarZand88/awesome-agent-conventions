<!-- source: seo-keyword-research — https://raw.githubusercontent.com/aaron-he-zhu/seo-geo-claude-skills/main/research/keyword-research/SKILL.md -->
---
name: keyword-research
description: 'Use when the user asks to "find keywords", "挖词", or "搜什么词"; prioritizes search volume, keyword difficulty, intent, and topic clusters from provided or connected data. Not for competitor-relative coverage gaps — use content-gap-analysis. 关键词研究/内容选题'
version: "9.9.10"
license: Apache-2.0
compatibility: "Claude Code and compatible agent-skill hosts"
homepage: "https://github.com/aaron-he-zhu/seo-geo-claude-skills"
when_to_use: "Use when starting keyword research for a new page, topic, or campaign. Also when the user asks about search volume, keyword difficulty, topic clusters, long-tail keywords, what to write about, 关键词研究, 挖词, 内容选题, or 搜什么词."
argument-hint: "<topic or seed keyword> [market/language]"
metadata:
  author: aaron-he-zhu
  version: "9.9.10"
  geo-relevance: "medium"
  tags:
    - seo
    - geo
    - keyword-research
    - search-volume
    - keyword-difficulty
    - topic-clusters
    - search-intent
    - long-tail-keywords
    - 关键词研究
    - SEO关键词
    - キーワード調査
    - 키워드분석
    - palabras-clave
  triggers:
    - "keyword research"
    - "search volume analysis"
    - "what should I write about"
    - "give me keyword ideas"
    - "how competitive is this keyword"
    - "Ahrefs keyword explorer alternative"
    - "Google Keyword Planner alternative"
    - "关键词分析"
    - "长尾关键词"
    - "帮我挖词"
---

# Keyword Research

Discovers, scores, and clusters keywords for SEO and GEO planning.

## Quick Start

```
Research keywords for [topic/product/service]
```

```
What keywords is [competitor URL] ranking for that I should target?
```

## Skill Contract

**Expected output**: a prioritized keyword brief plus the standard handoff summary for `memory/research/`.

- **Reads**: topic or seed keyword, target market/language, business goal, site DR, and any user-provided or tool metrics.
- **Writes**: a user-facing research deliverable and reusable summary.
- **Promotes**: durable keyword priorities, competitor facts, and pending strategy decisions to `memory/hot-cache.md`, `memory/open-loops.md`, and `memory/research/`.
- **Done when**: every shortlisted keyword carries volume + difficulty + intent (or a labeled N/A); keywords are grouped into pillar + cluster hubs; and the deliverable names at least 3 prioritized Quick Win / Growth / GEO opportunities.
- **Primary next skill**: [competitor-analysis](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/research/competitor-analysis/SKILL.md) when the keyword set is ready for market comparison.

### Handoff Summary

> Emit the standard shape from [skill-contract.md §Handoff Summary Format](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/references/skill-contract.md).

## Data Sources

Optional integrations: ~~SEO tool, ~~search console. Without tools, ask for seed keywords, audience, goals, and any known metrics. See [CONNECTORS.md](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/CONNECTORS.md).

**Zero-dependency local helper** (no tool needed): `python3 scripts/connectors/suggest.py "<seed>" --expand` harvests free keyword ideas from Google Autocomplete (⚠️ unofficial endpoint). Search *volume / difficulty* still needs `~~SEO tool` or own Search Console data. See [scripts/connectors/README.md](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/scripts/connectors/README.md).

## Instructions

When a user requests keyword research, run eight phases and announce each as `[Phase X/8: Name]`:

1. **Scope** — clarify product, audience, business goal, DR, geography, and language.
2. **Discover** — seed from core, problem, solution, audience, and industry terms.
3. **Variations** — expand with modifiers and long-tail patterns.
4. **Classify** — tag by intent (informational, navigational, commercial, transactional).
5. **Score** — assign difficulty (1-100) and compute `Opportunity = (Volume × Intent Value) / Difficulty`, with Intent Value `1 / 1 / 2 / 3`.
6. **GEO-Check** — flag AI-answer-friendly queries such as questions, definitions, comparisons, lists, and how-tos.
7. **Cluster** — group keywords into pillar + cluster topic hubs.
8. **Deliver** — output an Executive Summary, Quick Wins / Growth / GEO opportunities, Topic Clusters, Content Calendar, and Next Steps.

Label every metric **Measured** (tool/export), **User-provided**, or **Estimated** (model inference); never present an estimate as measured; if a required metric is unavailable, mark it N/A — do not invent it.

**Quality bar**: every recommendation includes at least one specific number. Rewrite generic advice into a concrete keyword + volume + difficulty + reason.

> **Reference**: See [references/instructions-detail.md](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/research/keyword-research/references/instructions-detail.md) for the full 8-phase templates, expansion patterns, intent table, difficulty tiers, opportunity matrix, GEO indicators, cluster template, actionable-vs-generic examples, and advanced usage.

## Example

Example outcome: 150+ keywords analyzed, 23 high-priority opportunities, ~45K/month traffic potential across 3 focus areas. See the full sample in [references/example-report.md](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/research/keyword-research/references/example-report.md).

### Advanced Usage

Intent mapping, seasonal analysis, competitor gaps, and local keyword workflows live in [references/instructions-detail.md](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/research/keyword-research/references/instructions-detail.md#advanced-usage).

## Tips for Success

Start with seeds, respect intent, cluster tightly, prioritize quick wins, and review quarterly. Full notes live in [references/instructions-detail.md](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/research/keyword-research/references/instructions-detail.md#tips-for-success).

### Save Results

Write path: `memory/research/keyword-research/YYYY-MM-DD-<topic>.md`; promote durable keyword priorities to `memory/hot-cache.md`. See [Skill Contract](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/references/skill-contract.md) §Save Results Template.

## Reference Materials

- [Instructions Detail](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/research/keyword-research/references/instructions-detail.md) — Workflow, scoring, cluster template, advanced usage
- [Keyword Intent Taxonomy](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/research/keyword-research/references/keyword-intent-taxonomy.md) — Intent signals and content mapping
- [Topic Cluster Templates](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/research/keyword-research/references/topic-cluster-templates.md) — Pillar and cluster patterns
- [Keyword Prioritization Framework](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/research/keyword-research/references/keyword-prioritization-framework.md) — Scoring and prioritization rules
- [Example Report](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/research/keyword-research/references/example-report.md) — Worked sample

## Next Best Skill

Primary: [competitor-analysis](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/research/competitor-analysis/SKILL.md). Also: [content-gap-analysis](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/research/content-gap-analysis/SKILL.md) and [serp-analysis](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/research/serp-analysis/SKILL.md).
