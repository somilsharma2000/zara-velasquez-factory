# AFFILIATE LINKS & TRACKING — ZARA VELASQUEZ
**Complete affiliate program setup, tracking, and optimization**

---

## APPROVED AFFILIATE PROGRAMS (VETTED, USED BY ZARA)

### Tier 1: Core Stack (High Commission, Recurring)
| Program | Commission | Cookie | Payout | Tracking ID | Status |
|---------|------------|--------|--------|-------------|--------|
| **ConvertKit** | 30% recurring | 30 days | Net-30 | `zaravelasquez_ck` | ✅ Active |
| **Beehiiv** | 50% first year | 30 days | Net-30 | `zaravelasquez_bh` | ✅ Active |
| **Notion** | $10/referral | 90 days | Net-30 | `zaravelasquez_nt` | ✅ Active |
| **CapCut Pro** | 20% recurring | 30 days | Net-30 | `zaravelasquez_cp` | ✅ Active |
| **Canva Pro** | $36/referral | 30 days | Net-30 | `zaravelasquez_cv` | ✅ Active |
| **Linear** | $50/referral | 90 days | Net-30 | `zaravelasquez_ln` | ✅ Active |
| **Vercel** | $30/referral | 30 days | Net-30 | `zaravelasquez_vc` | ✅ Active |

### Tier 2: Creator Tools (Medium Commission)
| Program | Commission | Cookie | Payout | Tracking ID | Status |
|---------|------------|--------|--------|-------------|--------|
| **Fanvue** | 5% lifetime | Lifetime | Net-7 | `zaravelasquez_fv` | ✅ Active |
| **LTK (LikeToKnowIt)** | 5-15% | 30 days | Net-60 | `zaravelasquez_ltk` | ⏳ Pending |
| **Amazon Associates** | 1-4% | 24 hrs | Net-60 | `zaravelasquez_amz` | ✅ Active |
| **Skillshare** | $10/signup | 30 days | Net-30 | `zaravelasquez_sk` | ✅ Active |
| **Udemy** | 8-15% | 7 days | Net-30 | `zaravelasquez_ud` | ✅ Active |

### Tier 3: Travel & Lifestyle (Lower Commission, High Volume)
| Program | Commission | Cookie | Payout | Tracking ID | Status |
|---------|------------|--------|--------|-------------|--------|
| **Airbnb** | 2-5% | 30 days | Net-30 | `zaravelasquez_ab` | ✅ Active |
| **Booking.com** | 4% | Session | Net-30 | `zaravelasquez_bk` | ✅ Active |
| **SafetyWing** | 10% recurring | 30 days | Net-30 | `zaravelasquez_sw` | ✅ Active |
| **Genki Insurance** | 15% | 30 days | Net-30 | `zaravelasquez_gk` | ✅ Active |
| **Wise** | £50/referral | 30 days | Instant | `zaravelasquez_ws` | ✅ Active |
| **Revolut** | €30/referral | 30 days | Instant | `zaravelasquez_rv` | ✅ Active |

### Tier 4: Future / High-Ticket
| Program | Commission | Notes |
|---------|------------|-------|
| **Supabase** | $100/referral | Apply via partner program |
| **Stripe** | $500/referral | Invite only |
| **Webflow** | $300/referral | Partner program |
| **Framer** | $150/referral | Partner program |

---

## TRACKING INFRASTRUCTURE

### UTM Parameter Standard
```
Base URL: https://product.com/landing
UTM: ?utm_source=zaravelasquez&utm_medium=social&utm_campaign={pillar}&utm_content={format}&utm_term={idea_id}

Examples:
- Instagram Reel (BUILD): ?utm_source=zaravelasquez&utm_medium=instagram_reel&utm_campaign=build&utm_content=reel&utm_term=B01
- TikTok (LIVE): ?utm_source=zaravelasquez&utm_medium=tiktok&utm_campaign=live&utm_content=video&utm_term=L01
- X Thread (LEARN): ?utm_source=zaravelasquez&utm_medium=twitter_thread&utm_campaign=learn&utm_content=thread&utm_term=T01
- Newsletter: ?utm_source=zaravelasquez&utm_medium=email&utm_campaign=newsletter&utm_content=issue_01&utm_term=resources
```

### Link Shortener: Dub.co (or Bitly)
- Custom domain: `zara.velasquez.link` (or `go.zaravelasquez.com`)
- Each affiliate link gets custom slug: `zara.velasquez.link/convertkit`, `zara.velasquez.link/notion-template`
- Tracks: clicks, referrers, geography, device, time

### Notion Tracking Database
**Database: "Affiliate Tracking"**

| Property | Type | Description |
|----------|------|-------------|
| Program | Select | ConvertKit, Notion, CapCut, etc. |
| Tracking ID | Text | `zaravelasquez_ck` |
| Short Link | URL | `zara.velasquez.link/convertkit` |
| Full UTM Link | URL | Full parameterized URL |
| Pillar | Select | BUILD, LIVE, LEARN, FEEL |
| Content Piece | Relation | Links to Content Calendar |
| Platform | Multi-select | Instagram, TikTok, X, LinkedIn, Newsletter, Fanvue |
| Clicks | Number | From Dub.co API |
| Conversions | Number | From affiliate dashboard |
| Revenue | Number | Calculated: Conversions × Commission |
| Status | Select | Active, Paused, Testing, Archived |
| Notes | Text | Campaign notes, A/B test details |

---

## CONTENT INTEGRATION STRATEGY

### "My Gear" Notion Page (PUBLIC)
**URL:** `zara.velasquez.link/gear` (redirects to Notion public page)

**Structure:**
```
# Zara's Gear & Tools 🛠️

## 💻 Tech Stack (What I Actually Use)
| Tool | Purpose | Cost | My Link | Why |
|------|---------|------|---------|-----|
| Notion | Brain/OS | $0 | [link] | Free tier sufficient |
| CapCut Pro | Video editing | $8/mo | [link] | Best mobile editor |
| ConvertKit | Email | $0-29/mo | [link] | Creator-focused |
| Linear | Issues | $0 | [link] | Clean, fast |
| Vercel | Hosting | $0 | [link] | Hobby tier free |

## 🎒 Travel Gear
| Item | Link | Why |
|------|------|-----|
| 35L Backpack | [link] | Carry-on only life |
| White Sambas | [link] | Only shoes I own |
| Leica M6 | [link] | Film ritual |

## 📚 Learning
| Resource | Link | Format |
|----------|------|--------|
| Notion Template Pack | [link] | Free duplicate |
| SaaS Finance Tracker | [link] | $27 |
| Newsletter Course | [link] | $197 |
```

### Content Integration Rules
1. **Every tool mention = affiliate link** (in bio, Stories, caption, thread)
2. **Disclosure:** "Affiliate link" or "🔗" in every post
3. **Only link what you use** — authenticity = conversions
4. **Track per content piece** — know which Reel drove which conversion

---

## AUTOMATION: DUB.CO API + NOTION SYNC

### Weekly Sync Script (Run Sundays)
```python
# sync_affiliate_data.py
import requests
from notion_client import Client

# 1. Fetch clicks from Dub.co
dub_response = requests.get(
    "https://api.dub.co/v1/links/analytics",
    headers={"Authorization": "Bearer DUB_API_KEY"},
    params={"startDate": "7d", "groupBy": "link"}
)

# 2. Fetch conversions from affiliate dashboards (manual CSV import for now)
# 3. Update Notion database
notion = Client(auth=os.environ["NOTION_TOKEN"])
for link_data in dub_response.json():
    notion.pages.update(
        page_id=link_data["notion_page_id"],
        properties={
            "Clicks": {"number": link_data["clicks"]},
            "Last Sync": {"date": {"start": datetime.now().isoformat()}}
        }
    )
```

---

## REVENUE PROJECTIONS (CONSERVATIVE)

| Month | Followers | Est. Clicks | Conversion | Programs Active | Monthly Rev |
|-------|-----------|-------------|------------|-----------------|-------------|
| 1 | 1,000 | 500 | 2% | 5 | $50 |
| 2 | 3,000 | 1,500 | 2.5% | 7 | $150 |
| 3 | 5,000 | 3,000 | 3% | 10 | $400 |
| 4 | 10,000 | 8,000 | 3.5% | 12 | $1,000 |
| 5 | 20,000 | 18,000 | 4% | 15 | $2,500 |
| 6 | 35,000 | 35,000 | 4.5% | 18 | $5,000 |
| 12 | 100,000 | 100,000 | 5% | 20 | $15,000 |

**Key Insight:** Affiliate becomes #1 revenue stream at ~6 months due to compounding recurring commissions.

---

## OPTIMIZATION PLAYBOOK

### A/B Test Framework
| Test | Variable | Duration | Success Metric |
|------|----------|----------|----------------|
| Bio link | "My Gear" vs "Free Templates" | 2 weeks | Click-through rate |
| Caption CTA | "Link in bio" vs "zara.velasquez.link/notion" | 1 week | Clicks per impression |
| Story CTA | Swipe up vs Link sticker | 1 week | Swipe rate |
| Email CTA | Button vs Text link | 2 weeks | Click rate |

### Monthly Optimization (1st of Month)
1. Export Dub.co analytics → Notion
2. Identify top 3 performing links
3. Identify bottom 3 (pause or improve)
4. Test new placement for top performers
5. Update "My Gear" page with current stack
6. Negotiate higher rates for top programs (>100 conversions)

---

## COMPLIANCE CHECKLIST

- [ ] Every affiliate link disclosed (#ad, #affiliate, "affiliate link")
- [ ] FTC-compliant: Clear, conspicuous, unavoidable
- [ ] Platform-specific: Instagram "Paid Partnership" tag when applicable
- [ ] Fanvue: No affiliate links in DMs (platform policy)
- [ ] Email: Unsubscribe link + "This contains affiliate links" footer
- [ ] Records: Screenshots of disclosures for 3 years

---

## QUICK REFERENCE: TOP 10 LINKS TO MEMORIZE

1. `zara.velasquez.link/convertkit` — Email marketing
2. `zara.velasquez.link/notion` — Templates + workspace
3. `zara.velasquez.link/capcut` — Video editing
4. `zara.velasquez.link/fanvue` — Exclusive content
5. `zara.velasquez.link/gear` — Full gear page
6. `zara.velasquez.link/saas-tracker` — Finance template ($27)
7. `zara.velasquez.link/newsletter-course` — Course ($197)
8. `zara.velasquez.link/airbnb` — Travel credit
9. `zara.velasquez.link/wise` — Currency transfer
10. `zara.velasquez.link/safetywing` — Nomad insurance

---

**NEXT:** See `contracts/ugc_contract.md` for brand deal contracts, `media_kit/` for pitch deck.