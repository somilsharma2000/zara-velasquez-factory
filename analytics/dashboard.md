# ANALYTICS DASHBOARD — ZARA VELASQUEZ
**Metrics tracking, visualization, and decision-making framework**

---

## NOTION DASHBOARD STRUCTURE

### Page: "Zara Analytics Dashboard"
**URL:** `notion.so/zaravelasquez/analytics`

---

### DATABASE 1: DAILY METRICS (Auto-updated via API where possible)

| Property | Type | Source |
|----------|------|--------|
| **Date** | Title | YYYY-MM-DD |
| **Week** | Number | Auto-calc |
| **Platform** | Select | IG Feed, IG Reels, IG Stories, TikTok, YT Shorts, X, LinkedIn, Fanvue, Newsletter |
| **Content ID** | Relation | → CONTENT PIPELINE |
| **Impressions** | Number | Platform API |
| **Reach** | Number | Platform API |
| **Views** | Number | Platform API |
| **Likes** | Number | Platform API |
| **Comments** | Number | Platform API |
| **Shares** | Number | Platform API |
| **Saves** | Number | Platform API |
| **Profile Visits** | Number | Platform API |
| **Link Clicks** | Number | Platform API / UTM |
| **Followers Gained** | Number | Platform API |
| **Followers Lost** | Number | Platform API |
| **Net Followers** | Formula | Gained - Lost |
| **Engagement Rate** | Formula | (Likes+Comments+Shares+Saves) / Reach |
| **Completion Rate** | Number | Video only (Platform API) |
| **Avg Watch Time** | Number | Video only (seconds) |
| **Revenue Attributed** | Number | Affiliate + UGC + Fanvue + Products |
| **Cost** | Number | Tools, contractor, ads, time value |
| **ROI** | Formula | Revenue / Cost |
| **Notes** | Text | Anomalies, events, learnings |

---

### DATABASE 2: WEEKLY ROLLUPS (Auto-calculated from Daily)

| Property | Type | Description |
|----------|------|-------------|
| **Week** | Title | W01, W02, etc. |
| **Date Range** | Text | MM/DD - MM/DD |
| **Total Impressions** | Rollup | Sum |
| **Total Reach** | Rollup | Sum |
| **Total Engagement** | Rollup | Sum |
| **Avg Engagement Rate** | Rollup | Average |
| **Total Followers Gained** | Rollup | Sum |
| **Content Pieces Published** | Rollup | Count |
| **Revenue** | Rollup | Sum |
| **Cost** | Rollup | Sum |
| **ROI** | Formula | Revenue / Cost |
| **Top Performing Content** | Relation | → Top 3 by engagement |
| **Worst Performing Content** | Relation | → Bottom 3 by engagement |
| **Key Learnings** | Text | Bullet points |
| **Adjustments for Next Week** | Text | Bullet points |

---

### DATABASE 3: MONTHLY BUSINESS REVIEW

| Property | Type | Description |
|----------|------|-------------|
| **Month** | Title | YYYY-MM |
| **Total Followers (All Platforms)** | Number | Sum |
| **Follower Growth %** | Formula | (Current - Previous) / Previous |
| **Total Revenue** | Number | Sum all streams |
| **Revenue Growth %** | Formula | MoM growth |
| **Revenue by Stream** | Text | JSON: {fanvue, ugc, affiliate, products, ads} |
| **Top 3 Content Pieces** | Relation | → CONTENT PIPELINE |
| **Brand Deals Closed** | Number | Count |
| **Pipeline Value** | Number | Sum of negotiated deals |
| **Fanvue Subscribers** | Number | Current active |
| **Fanvue Churn Rate** | Formula | Cancelled / Started |
| **Email Subscribers** | Number | ConvertKit |
| **Email Open Rate** | Number | ConvertKit |
| **Email Click Rate** | Number | ConvertKit |
| **Time Invested (Hours)** | Number | Tracked via Toggl/RescueTime |
| **Revenue per Hour** | Formula | Total Revenue / Hours |
| **Strategic Decisions** | Text | Major pivots, investments, hires |

---

## KEY METRICS & TARGETS

### Growth Metrics (Leading Indicators)
| Metric | Month 1 | Month 3 | Month 6 | Month 12 | Frequency |
|--------|---------|---------|---------|----------|-----------|
| **Total Followers** | 1,000 | 10,000 | 35,000 | 100,000 | Weekly |
| **Follower Growth Rate** | 20%/wk | 10%/wk | 5%/wk | 3%/wk | Weekly |
| **Engagement Rate (Blended)** | 4% | 5% | 6% | 5% | Weekly |
| **Content Volume** | 35/wk | 49/wk | 49/wk | 49/wk | Weekly |
| **Content Consistency** | 80% | 95% | 100% | 100% | Weekly |

### Revenue Metrics (Lagging Indicators)
| Metric | Month 1 | Month 3 | Month 6 | Month 12 | Frequency |
|--------|---------|---------|---------|----------|-----------|
| **Total Monthly Revenue** | $0 | $500 | $4,400 | $18,000 | Monthly |
| **Fanvue Revenue** | $0 | $200 | $1,800 | $8,000 | Monthly |
| **UGC Revenue** | $0 | $300 | $1,800 | $5,000 | Monthly |
| **Affiliate Revenue** | $50 | $150 | $2,500 | $15,000 | Monthly |
| **Digital Products** | $0 | $100 | $450 | $5,000 | Monthly |
| **Ad Revenue** | $0 | $0 | $150 | $500 | Monthly |
| **Revenue per Follower** | $0 | $0.05 | $0.13 | $0.18 | Monthly |

### Efficiency Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| **Batch Production Time** | 2 hours/week | Stopwatch |
| **Cost per Content Piece** | <$5 | (Tools + Contractor) / Pieces |
| **Revenue per Content Piece** | >$50 (Month 6+) | Revenue / Pieces |
| **Time to First Dollar** | < 90 days | Calendar |
| **Fanvue CAC** | <$5 | Ad spend / Sub (if ads) |
| **Brand Deal Close Rate** | >30% | Closed / Proposals |

---

## VISUALIZATION CHARTS (Notion / Google Sheets / Grafana)

### 1. Follower Growth Waterfall
- **X:** Week
- **Y:** Cumulative followers per platform (stacked area)
- **Annotations:** Viral posts, platform changes, campaigns

### 2. Revenue Stacked Bar
- **X:** Month
- **Y:** Revenue by stream (stacked)
- **Target line:** $10K MRR

### 3. Engagement Heatmap
- **X:** Day of week
- **Y:** Hour of day
- **Color:** Engagement rate
- **Insight:** Optimal posting times

### 4. Content Performance Scatter
- **X:** Impressions
- **Y:** Engagement rate
- **Size:** Revenue attributed
- **Color:** Pillar
- **Quadrants:** High reach/low engagement, etc.

### 5. Funnel: Social → Fanvue
```
Impressions → Profile Visits → Link Clicks → Fanvue Landing → Subscribe
     100%         5%              1%             50%           10%
```
- Track each stage weekly
- Identify biggest drop-off

### 6. Brand Deal Pipeline
- **Stages:** Discovery → Proposal → Negotiation → Contract → Delivery → Paid
- **Metrics:** Count, Value, Velocity (days/stage), Conversion %

### 7. Content Pillar Balance
- **Pie chart:** % of content per pillar (Target: 30/30/25/15)
- **Overlay:** Revenue per pillar

### 8. ROI by Platform
- **X:** Platform
- **Y:** Revenue / Hour invested
- **Bubble size:** Total revenue

---

## AUTOMATED DATA COLLECTION

### API Integrations (Priority Order)
| Platform | API | Metrics | Frequency | Tool |
|----------|-----|---------|-----------|------|
| Instagram | Graph API | All | Daily | Make/Zapier |
| TikTok | Business API | All | Daily | Make/Zapier |
| YouTube | Data API v3 | All | Daily | Make/Zapier |
| X/Twitter | API v2 | All | Daily | Make/Zapier |
| LinkedIn | Marketing API | All | Daily | Make/Zapier |
| Fanvue | Custom/CSV | Subs, Revenue | Daily | Manual/Script |
| ConvertKit | API | Subs, Opens, Clicks | Daily | Make/Zapier |
| Affiliate Networks | Various | Clicks, Conversions | Weekly | Manual CSV |
| Stripe | API | Revenue, Invoices | Daily | Make/Zapier |

### Make.com Scenario: "Daily Metrics Sync"
```
Schedule: Daily 6:00 AM WET
│
├─ Instagram Graph API → Get Insights → Update Notion Daily Metrics
├─ TikTok Business API → Get Video Metrics → Update Notion
├─ YouTube Data API → Get Shorts Metrics → Update Notion
├─ Twitter API v2 → Get Tweet Metrics → Update Notion
├─ LinkedIn API → Get Post Metrics → Update Notion
├─ ConvertKit API → Get Subscriber Stats → Update Notion
├─ Stripe API → Get Revenue → Update Notion
└─ Fanvue → Manual CSV Import (or API if available)
```

### Manual Weekly Imports (Sunday Batch)
- [ ] Affiliate network CSVs → Notion Affiliate Tracking
- [ ] Brand deal performance screenshots → Deals database
- [ ] Fanvue subscriber export → Fanvue Subscribers database
- [ ] Time tracking export (Toggl) → Monthly Review

---

## WEEKLY ANALYTICS REVIEW TEMPLATE (Sunday, 15 min)

### Section 1: The Numbers (5 min)
```
Week [X] Summary:
- Total Impressions: [X] ([+/-]% vs last week)
- Total Reach: [X] ([+/-]%)
- Blended Engagement Rate: [X]% (Target: >5%)
- Net Followers: +[X] (Target: >[Y])
- Revenue: $[X] (Target: $[Y])
- ROI: [X]x (Target: >3x)
```

### Section 2: Top & Bottom (5 min)
```
TOP 3 This Week:
1. [Content ID] — [Platform] — [Metric] — Why: [Insight]
2. [Content ID] — [Platform] — [Metric] — Why: [Insight]
3. [Content ID] — [Platform] — [Metric] — Why: [Insight]

BOTTOM 3 This Week:
1. [Content ID] — [Platform] — [Metric] — Why: [Insight]
2. [Content ID] — [Platform] — [Metric] — Why: [Insight]
3. [Content ID] — [Platform] — [Metric] — Why: [Insight]
```

### Section 3: Decisions (5 min)
```
NEXT WEEK ADJUSTMENTS:
1. [Specific change based on data]
2. [Specific change based on data]
3. [Specific change based on data]

PILLAR FOCUS: [BALANCED / BUILD_HEAVY / LIVE_HEAVY / LAUNCH_WEEK]

ASSET PRIORITIES:
- Generate: [Specific assets needed]
- Repurpose: [High performers to adapt]
- Archive: [Low performers to retire]
```

---

## MONTHLY BUSINESS REVIEW (1st of Month, 60 min)

### Agenda
1. **Revenue Review** (15 min) — P&L, stream breakdown, projections
2. **Growth Review** (15 min) — Followers, engagement, content performance
3. **Pipeline Review** (10 min) — Brand deals, partnerships, opportunities
4. **Operations Review** (10 min) — Tools, contractor, time, bottlenecks
5. **Strategy Decisions** (10 min) — Pivots, investments, hiring, experiments

### Output: Monthly Strategy Doc
- **File:** `analytics/monthly_reviews/YYYY-MM_strategy.md`
- **Template:** See below

---

## MONTHLY STRATEGY DOC TEMPLATE

```markdown
# MONTHLY STRATEGY — [YYYY-MM]

## EXECUTIVE SUMMARY
[3 sentences: Where we are, what changed, what's next]

## REVENUE
| Stream | Actual | Target | Variance | Notes |
|--------|--------|--------|----------|-------|
| Fanvue | | | | |
| UGC | | | | |
| Affiliate | | | | |
| Products | | | | |
| Ads | | | | |
| **TOTAL** | | | | |

## GROWTH
| Platform | Followers | Growth | Engagement | Notes |
|----------|-----------|--------|------------|-------|
| IG | | | | |
| TikTok | | | | |
| YT Shorts | | | | |
| X | | | | |
| LinkedIn | | | | |

## TOP LEARNINGS
1. [Specific, actionable, data-backed]
2. [Specific, actionable, data-backed]
3. [Specific, actionable, data-backed]

## FAILED EXPERIMENTS
1. [What, hypothesis, result, lesson]
2. [What, hypothesis, result, lesson]

## NEXT MONTH FOCUS
**Theme:** [e.g., "Launch Month", "Bali Content Sprint", "Affiliate Optimization"]

**Priority 1:** [Specific goal + metric + deadline]
**Priority 2:** [Specific goal + metric + deadline]
**Priority 3:** [Specific goal + metric + deadline]

**Content Pillars:** [BALANCED / BUILD_HEAVY / etc.]

**Investments:** [Tools, contractor, ads, courses - with expected ROI]

**Risks:** [What could go wrong + mitigation]

---

**SIGNED:** _______________ **DATE:** _______________
```

---

## QUARTERLY DEEP DIVE (Every 90 Days)

### Analyses to Run
1. **Cohort Analysis** — Subscriber retention by acquisition month
2. **Content Lifecycle** — Performance decay curves by format
3. **Audience Evolution** — Demographic shifts, interest changes
4. **Competitive Benchmark** — Top 10 competitors, share of voice
5. **Platform Risk Assessment** — Policy changes, algorithm updates
6. **Financial Model Update** — Projections vs actual, unit economics

### Output: Quarterly Strategy Deck
- **Format:** Notion page + PDF export
- **Audience:** Operator (you), future investors/partners
- **Sections:** Performance, Learnings, Strategy, Financials, Team, Risks

---

## ALERTS & THRESHOLDS

| Metric | Warning | Critical | Action |
|--------|---------|----------|--------|
| Daily follower loss | > 50 | > 100 | Audit content, check shadowban |
| Engagement rate drop | < 3% | < 2% | Pivot format, check algorithm |
| Revenue drop (WoW) | > 20% | > 40% | Check deals, affiliate, Fanvue |
| Fanvue churn | > 8%/mo | > 12%/mo | Survey, win-back campaign |
| Email open rate | < 30% | < 20% | Clean list, test subject lines |
| Brand deal pipeline | < $5K | < $2K | Increase outbound |
| Content consistency | < 90% | < 80% | Fix batch process |

---

## TOOL STACK FOR ANALYTICS

| Function | Tool | Cost | Notes |
|----------|------|------|-------|
| **Primary Dashboard** | Notion | $0 | Custom databases + charts |
| **Automation** | Make.com | $9/mo | 10K ops/mo sufficient |
| **Time Tracking** | Toggl Track | $0 | Project: "Zara Content" |
| **UTM Tracking** | Dub.co | $0-29/mo | Custom domain |
| **Affiliate Aggregation** | Google Sheets | $0 | Manual weekly import |
| **Advanced Viz** | Grafana (self-hosted) | $0 | If needed later |
| **Competitor Tracking** | Phlanx / SocialBlade | $0-50/mo | Monthly manual |

---

## DATA GOVERNANCE

- **Retention:** Raw daily metrics 2 years, rollups 7 years (tax)
- **Backup:** Notion export weekly → Google Drive + Local
- **Access:** Operator only (no team yet)
- **Privacy:** No PII in analytics (aggregated only)
- **Accuracy:** Cross-reference platform UI weekly for drift

---

**NEXT:** See `automation/` for Make.com scenarios, `scripts/` for utility scripts.