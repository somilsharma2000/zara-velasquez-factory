# CRM — ZARA VELASQUEZ
**Relationship management for brands, creators, fans, and partners**

---

## NOTION DATABASE STRUCTURE

### Database 1: CONTACTS (People & Companies)

| Property | Type | Options/Format |
|----------|------|----------------|
| **Name** | Title | Full name or company |
| **Type** | Select | Brand, Creator, Agency, Platform, Service, Fan (VIP), Mentor, Peer |
| **Status** | Select | Lead, Qualified, Negotiating, Active, Past, Dormant, Dead |
| **Email** | Email | Primary contact |
| **Phone/WhatsApp** | Phone | With country code |
| **Instagram** | URL | Profile link |
| **TikTok** | URL | Profile link |
| **X/Twitter** | URL | Profile link |
| **LinkedIn** | URL | Profile link |
| **Location** | Text | City, Country |
| **Timezone** | Text | e.g., WET, PST, WITA |
| **Notes** | Text | Key details, preferences, birthdays |
| **Last Contact** | Date | Auto-updated |
| **Next Action** | Date | Scheduled follow-up |
| **Action Type** | Select | Email, DM, Call, Meeting, Proposal, Invoice, Deliverable |
| **Pipeline Stage** | Select | New → Qualified → Proposal → Negotiation → Contract → Delivery → Paid → Nurture |
| **Value** | Number | Deal size (USD) |
| **Source** | Select | Inbound, Outbound, Referral, Event, Social, Cold |
| **Tags** | Multi-select | High-value, VIP, Recurring, Difficult, Friend, Family |

### Database 2: DEALS (Brand Collaborations)

| Property | Type | Options/Format |
|----------|------|----------------|
| **Deal Name** | Title | Brand - Campaign - Date |
| **Contact** | Relation | → CONTACTS |
| **Stage** | Select | Discovery, Proposal Sent, Negotiating, Contract, In Production, Delivered, Invoiced, Paid, Lost |
| **Value** | Number | Total contract value (USD) |
| **Deposit** | Number | 50% on signing |
| **Balance Due** | Formula | Value - Deposit |
| **Deliverables** | Text | List from contract |
| **Due Date** | Date | Final delivery |
| **Invoice Date** | Date | When invoiced |
| **Paid Date** | Date | When received |
| **Payment Terms** | Select | Net-15, Net-30, 50/50, Upfront |
| **Exclusivity** | Checkbox | Yes/No |
| **Exclusivity Fee** | Number | If applicable |
| **Spark Ads** | Checkbox | Yes/No |
| **Whitelisting** | Checkbox | Yes/No |
| **Usage Rights** | Select | Standard, Extended, Custom |
| **Contract Signed** | Checkbox | Yes/No |
| **Contract File** | File | PDF/MD |
| **Performance Metrics** | Text | Views, engagement, clicks, conversions |
| **Notes** | Text | Issues, feedback, renewal potential |

### Database 3: CONTENT PIPELINE (Production Tracking)

| Property | Type | Options/Format |
|----------|------|----------------|
| **Content ID** | Title | e.g., W01-B01-Reel |
| **Week** | Number | Week number |
| **Pillar** | Select | BUILD, LIVE, LEARN, FEEL |
| **Idea ID** | Text | From backlog (B01, L01, etc.) |
| **Format** | Select | Reel, Carousel, Thread, Hedra, Veo2, Kling, Colab, Stories, X, LinkedIn, Short |
| **Status** | Select | Idea, Scripted, Assets Ready, Produced, Captioned, Scheduled, Posted, Analyzed |
| **Platform(s)** | Multi-select | IG Feed, IG Reels, IG Stories, TikTok, YT Shorts, X, LinkedIn, Fanvue |
| **Scheduled Date** | Date | When it goes live |
| **Scheduled Time** | Text | e.g., 11:00 WET |
| **Caption** | Text | Final caption |
| **Hashtags** | Text | 3-5 niche tags |
| **Asset Path** | Text | File path in assets/ |
| **CTA** | Text | Link/CTA used |
| **UTM Campaign** | Text | e.g., build_reel_B01 |
| **Performance** | Text | Views, likes, comments, shares, saves, profile visits, link clicks |
| **Revenue Attribution** | Number | Affiliate/UG/Fanvue revenue from this piece |
| **Notes** | Text | What worked, what didn't, iterations |

### Database 4: FANVUE SUBSCRIBERS (VIP Tracking)

| Property | Type | Options/Format |
|----------|------|----------------|
| **Username** | Title | Fanvue handle |
| **Tier** | Select | Builder's Brew, Inner Circle, Founder's Table |
| **Join Date** | Date | Subscription start |
| **Renewal Date** | Date | Next billing |
| **Status** | Select | Active, Past Due, Cancelled, Paused |
| **LTV** | Number | Lifetime value (USD) |
| **PPV Purchases** | Number | Count |
| **PPV Revenue** | Number | Total PPV spend |
| **Custom Requests** | Number | Count |
| **Last DM** | Date | Last interaction |
| **Engagement Score** | Formula | (DMs + PPV + Customs) / Tenure |
| **Tags** | Multi-select | Superfan, Whale, Content Requester, Referral Source |
| **Notes** | Text | Preferences, birthdays, content requests |

---

## WORKFLOWS

### BRAND DEAL PIPELINE

```
NEW LEAD (Inbound DM / Cold Email / Referral)
    │
    ▼
QUALIFY (15-min call / email exchange)
    │  ├─ Budget confirmed? → Yes → PROPOSAL
    │  ├─ Timeline fits? → Yes → PROPOSAL
    │  ├─ Values align? → Yes → PROPOSAL
    │  └─ No → NURTURE / DEAD
    ▼
PROPOSAL SENT (Rate card + scope + contract template)
    │
    ▼
NEGOTIATING (Scope/price revisions — max 2 rounds)
    │
    ▼
CONTRACT SIGNED (Both parties + deposit received)
    │
    ▼
IN PRODUCTION (Asset creation per timeline)
    │
    ▼
DELIVERED (Files sent + Spark Ads authorized)
    │
    ▼
INVOICED (Balance due per terms)
    │
    ▼
PAID (Mark complete → NURTURE for renewal)
```

### AUTOMATED ACTIONS (Notion + Zapier/Make)

| Trigger | Action |
|---------|--------|
| Deal stage = "Contract" | Create invoice in Stripe → Email to brand |
| Deal stage = "Delivered" | Set reminder: "Request Spark Ads access" |
| Deal stage = "Paid" | Update Contact: "Last Contact = today", "Next Action = 30 days (renewal check)" |
| Contact "Next Action" = Today | Daily email digest: "Today's follow-ups" |
| Fanvue subscriber "Renewal Date" = 3 days | Tag for retention DM |
| Content "Scheduled Date" = Tomorrow | Slack/Discord reminder: "Tomorrow's posts" |
| Content "Posted" = Today | Set reminder: "Check analytics in 24h" |

---

## OUTREACH TEMPLATES

### Cold Email to Brand (Decision Maker)
```
Subject: Zara Velasquez × [Brand] — UGC for [Product/Campaign]

Hi [Name],

Been using [Product] for [timeframe] — genuinely love [specific feature].

I'm Zara (@zaravelasquez), a solo founder building CreatorOS while documenting the nomad journey to 35K+ creators across IG/TikTok/X. My audience: 60% women 22-35, 70% US/EU, high intent for creator tools/travel/productivity.

I'd love to create a Reel + Story sequence showing how [Product] fits my workflow. My rate card attached — flexible on scope.

Open to a 10-min call this week?

Best,
Zara
[Media Kit Link]
[Rate Card Link]
```

### Follow-Up (3 days)
```
Subject: Re: Zara Velasquez × [Brand]

Hi [Name],

Floating this to top of inbox — know you're busy.

Quick question: Is [Product] a priority for creator/influencer marketing this quarter? If not, happy to reconnect later.

Either way, keep building 🫶

Zara
```

### Post-Delivery (7 days)
```
Subject: [Brand] × Zara — 7-day performance

Hi [Name,

First 7 days for the [Campaign] Reel:
- Views: [X]
- Engagement: [Y]%
- Profile visits: [Z]
- Link clicks: [W]

[Screenshot attached]

Happy to discuss renewal for Q[next] — thinking [concept idea].

Best,
Zara
```

### Renewal Pitch (30 days before expiry)
```
Subject: Planning Q[next] — Zara × [Brand]

Hi [Name],

Our exclusivity/partnership wraps [Date]. Want to lock in next quarter before I open slots.

Last campaign: [X] views, [Y]% engagement, [Z] link clicks.

Ideas for next round:
1. [Concept A]
2. [Concept B]
3. [Concept C]

Rate card updated (attached) — loyal partner discount: 10% off.

Let me know if you want to continue?

Zara
```

---

## VIP FAN MANAGEMENT

### Tier: SUPERFAN (Top 1% by engagement)
- **Criteria:** Comments on 80%+ posts, DMs weekly, purchases PPV, refers others
- **Treatment:**
  - Monthly personalized voice note
  - Early access to all content (24hr before public)
  - Free custom content (1/quarter)
  - Birthday gift (digital: custom wallpaper/video)
  - Direct line: replies within 2 hours

### Tier: WHALE (Top 5% by spend)
- **Criteria:** LTV > $500, multiple PPV, custom requests
- **Treatment:**
  - All Superfan perks
  - Quarterly 15-min Zoom (Tier 3 perk extended)
  - Co-create: they choose next tutorial topic
  - Affiliate commission: 50% of their referrals
  - Name in credits (if they want)

### Tier: REFERRAL CHAMPION
- **Criteria:** 5+ referred subscribers
- **Treatment:**
  - Free month per 5 referrals
  - Exclusive referral-only content
  - Swag (stickers, postcard from current city)

---

## WEEKLY CRM REVIEW (Sunday, 30 min)

### Checklist
- [ ] **New Leads:** Add all inbound DMs/emails from week
- [ ] **Follow-Ups:** Move stalled deals, send nudges
- [ ] **Contracts:** Any expiring? Renewal pipeline?
- [ ] **Invoices:** Overdue? Send reminder (Net-15 → Day 16)
- [ ] **Deliverables:** Any due this week? Confirm assets ready
- [ ] **Fanvue:** Churned subscribers? Win-back DM
- [ ] **Creators:** Collabs due? Schedule
- [ ] **Mentors/Peers:** Value-add touchpoint (share their content, intro)

### Metrics to Track
| Metric | Target | Current |
|--------|--------|---------|
| Active Brand Deals | 3-5 | |
| Pipeline Value | $10K+ | |
| Avg Deal Size | $1,500+ | |
| Deal Velocity (days) | < 21 | |
| Fanvue Churn | < 5%/mo | |
| Superfan Count | 20+ | |
| Referral Subs/Month | 10+ | |

---

## TOOL STACK

| Function | Tool | Cost | Integration |
|----------|------|------|-------------|
| **Database** | Notion | $0 | Native |
| **Automation** | Make (formerly Integromat) | $9/mo | Notion → Email, Slack, Calendar |
| **Email Outreach** | Gmail + Streak | $0 | CRM in inbox |
| **Scheduling** | Calendly | $0 | Meeting links in proposals |
| **Invoicing** | Stripe Invoicing | 0.4% + €0.25 | Auto from Notion |
| **Contracts** | DocuSign / PandaDoc | $0-10/mo | E-sign |
| **File Sharing** | Google Drive / WeTransfer | $0 | Asset delivery |
| **Analytics** | Notion Dashboard | $0 | Manual entry + API |

---

## PRIVACY & COMPLIANCE

- [ ] GDPR: Legitimate interest for brand contacts, consent for fans
- [ ] Data Retention: Deal data 7 years (tax), Fan data 2 years post-churn
- [ ] Access Request: 30-day response via Notion export
- [ ] Deletion Request: Anonymize in Notion, remove from email lists
- [ ] Breach Plan: Notify within 72 hours, Notion audit log

---

## BACKUP & SYNC

- **Daily:** Notion auto-backup (built-in)
- **Weekly:** Export all databases → CSV → Google Drive / Local
- **Monthly:** Full workspace duplicate (Notion "Duplicate workspace")
- **Quarterly:** Test restore from CSV

---

**NEXT:** See `analytics/dashboard.md` for metrics dashboard, `automation/` for Make/Zapier scenarios.