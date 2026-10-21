# ZARA VELASQUEZ FACTORY
**Complete AI Influencer System — From Zero to $10K MRR**

---

## 🎯 WHAT THIS IS

A production-ready, professional-grade system for creating, operating, and monetizing an AI influencer (**Zara Velasquez** — Colombian-Spanish digital nomad, solo founder, building in public).

**Built for:** Solo operators who want professional team-level output without the team.

**Philosophy:** Systems > talent. Consistency > virality. Vulnerability > perfection.

---

## 📁 PROJECT STRUCTURE

```
zara-velasquez-factory/
├── CHARACTER_BIBLE.md              # Complete character specification (READ FIRST)
├── README.md                       # This file
├── .env.example                    # Environment template (copy to .env)
├── .gitignore
├── zara                            # CLI wrapper (./zara images|video|batch|setup)
│
├── assets/
│   ├── identity/
│   │   ├── zara.json               # Machine-readable identity card
│   │   ├── voice.md                # Voice DNA & patterns
│   │   ├── visual.md               # Visual style guide
│   │   ├── memory_boundaries.md    # What Zara knows/doesn't know
│   │   ├── content_backlog.md      # 100+ content ideas
│   │   └── handoff.json            # Pipeline handoff format
│   │
│   └── references/
│       ├── master_faces/           # 15 Picovix master references
│       ├── pose_library/           # Leonardo AI generated poses
│       ├── final_assets/           # Face-swapped, curated assets
│       └── video_library/          # Hedra, Veo2, Kling, Colab videos
│
├── prompts/
│   ├── master_prompt.txt           # 15 Picovix prompts + negative
│   ├── json_template.json          # Leonardo AI structured template
│   ├── scene_prompts/              # 13 reusable scene configs
│   ├── caption_templates/          # 4 pillars × multiple templates
│   └── video_prompts/              # Hedra scripts, Veo2/Kling/Colab prompts
│
├── pipeline/
│   ├── generate_images.py          # Leonardo + InsightFace batch
│   ├── generate_video.py           # Hedra/Veo2/Kling/Colab batch
│   └── batch_content.py            # Weekly content planner
│
├── monetization/
│   ├── fanvue_setup.md             # Complete Fanvue configuration
│   ├── affiliate_links.md          # 20+ programs, tracking, automation
│   └── digital_products/           # Notion templates, courses
│
├── contracts/
│   └── ugc_contract.md             # Professional UGC contract template
│
├── crm/
│   └── README.md                   # Notion CRM schema + workflows
│
├── media_kit/
│   └── README.md                   # Professional press kit
│
├── platform_checklists/
│   └── README.md                   # Pre-flight checks per platform
│
├── content_calendar/
│   └── weekly_template.md          # Sunday 2-hour batch template
│
├── analytics/
│   └── dashboard.md                # Metrics, visualization, alerts
│
├── scripts/
│   ├── setup.sh                    # One-command environment setup
│   ├── daily_cron.sh               # Daily metrics sync + alerts
│   └── weekly_batch.sh             # Sunday 2-hour production runner
│
└── automation/                     # Make.com/Zapier scenarios (to be added)
```

---

## 🚀 QUICK START

### 1. Clone & Setup
```bash
cd zara-velasquez-factory
bash scripts/setup.sh
```

### 2. Configure Environment
```bash
nano .env
# Fill in ALL API keys (Notion, Instagram, TikTok, Fanvue, ConvertKit, etc.)
```

### 3. Create Notion Databases
Follow `analytics/dashboard.md` to create databases, copy IDs to `.env`

### 4. Generate Master Faces (Picovix)
```bash
# Go to picovix.app/characters
# Use prompts from prompts/master_prompt.txt (15 angles)
# Save to assets/references/master_faces/
```

### 5. Run First Weekly Batch
```bash
./zara batch --week 1 --focus BALANCED
# This runs: content plan → image prompts → video configs
```

### 6. Manual Asset Generation (30-60 min)
- Leonardo AI: Use prompts from `assets/references/pose_library/`
- InsightFace Discord: Run commands from generated `insightface_commands_*.txt`
- Hedra: Generate 5 lip-sync videos from `prompts/video_prompts/`
- Veo2: Generate 10 cinematic clips at `aistudio.google.com`
- Colab: Run face-swap notebook for video sources

### 7. Finalize & Schedule
```bash
bash scripts/weekly_batch.sh 1 BALANCED
# Matches assets → Finalizes captions → Creates Buffer CSV → Git commit
```

### 8. Import to Buffer/Later
Upload `content_calendar/week_01/buffer_import_*.csv` to Buffer.com

### 9. Launch Fanvue
Follow `monetization/fanvue_setup.md` — launch at 3K+ followers

---

## ⚙️ DAILY OPERATIONS

### Automated (via cron/Make.com)
```bash
# Daily 6:00 AM WET
bash scripts/daily_cron.sh
# - Syncs metrics from all platforms
# - Checks brand deal deadlines
# - Monitors Fanvue renewals
# - Alerts on threshold breaches
# - Creates backup
```

### Manual (15 min/day)
- Reply to ALL comments/DMs < 1 hour
- Engage 50 relevant posts (comment, don't just like)
- DM 3 creators for collabs
- Check Buffer queue for tomorrow
- Post Stories (15 frames from template)

---

## 📅 WEEKLY OPERATIONS (Sunday, 2 Hours)

```bash
bash scripts/weekly_batch.sh 2 BALANCED
```

**Produces:**
- 7 main content pieces (2 BUILD, 2 LIVE, 2 LEARN, 1 FEEL)
- 14 Story frames (2/day)
- 7 X/Twitter posts
- 3 LinkedIn posts
- 3 YouTube Shorts (repurposed)
- Fanvue exclusives (3/week)
- Buffer import CSV ready

---

## 💰 MONETIZATION STACK

| Stream | Launch | Month 6 Target | Month 12 Target |
|--------|--------|----------------|-----------------|
| **Fanvue** | 3K followers | $1,800/mo | $8,000/mo |
| **UGC Deals** | 5K followers | $1,800/mo | $5,000/mo |
| **Affiliate** | Day 1 | $2,500/mo | $15,000/mo |
| **Digital Products** | 10K followers | $450/mo | $5,000/mo |
| **Ad Revenue** | 10K followers | $150/mo | $500/mo |
| **TOTAL** | — | **$6,700/mo** | **$33,500/mo** |

---

## 🛠️ TOOL STACK (ALL FREE TIERS)

| Category | Primary | Backup |
|----------|---------|--------|
| **Base Identity** | Picovix (browser, no signup) | Dropshot |
| **Pose Variations** | Leonardo AI (150 credits/day) | Tensor.art |
| **Face Consistency** | Discord InsightFace (unlimited) | Roop Unleashed |
| **Lip-Sync Video** | Hedra (300 credits signup) | Kling 2.6 |
| **Cinematic Motion** | Veo 2 (3/day free) | Kling 3.0 |
| **Video Face Swap** | Google Colab + InsightFace | Replicate |
| **Scheduling** | Buffer Free (10 posts/mo) | Later Free |
| **Email** | ConvertKit Free (1K subs) | Beehiiv Free |
| **Analytics** | Notion Dashboard | Google Sheets |

**Total Cost: $0/month** (optional: Make.com $9, Dub.co $0-29)

---

## 🎭 CHARACTER: ZARA VELASQUEZ

| Attribute | Value |
|-----------|-------|
| **Age** | 24 |
| **Ethnicity** | Colombian-Spanish (mestiza) |
| **Location** | Lisbon 🇵🇹 (6mo) / Bali 🇮🇩 (6mo) |
| **Languages** | Spanish (native), English (fluent), Portuguese (conversational) |
| **Archetype** | Relatable Builder — aspirational but accessible |
| **Niche** | Solo female founder / digital nomad / build in public |
| **Pillars** | BUILD (30%) · LIVE (30%) · LEARN (25%) · FEEL (15%) |

**Visual Anchors (NEVER CHANGE):**
- Beauty mark left of mouth
- Acne scar right cheek
- Nose bridge bump
- Asymmetric brows
- Visible pores/freckles
- Gold herringbone chain (always)
- White Sambas (only sneakers)
- Compass tattoo (ribs)

---

## 📊 KEY DIFFERENTIATORS (WHY THIS WINS)

1. **Reference-locked consistency** — Not prompt engineering. Picovix master → Leonardo poses → InsightFace swap = same face every time.

2. **Bilingual/bicultural** — Spanish/English/Portuguese = 3x addressable market (LatAm + EU + US).

3. **Build-in-public niche** — Untapped in AI influencer space. Most are fashion/fitness. Founders = high CPM, loyal audience.

4. **Vulnerability as strategy** — Shares failures, anxiety, €147 Stripe balance. Builds trust > perfection.

5. **Systems over talent** — 2-hour Sunday batch → 7 days content. No daily decision fatigue.

6. **Multi-stream monetization** — Not dependent on brand deals. Fanvue + affiliate + products = recurring revenue.

7. **Professional contracts** — UGC contract with kill fees, usage limits, revision caps. No scope creep.

8. **Analytics-driven** — Weekly reviews, monthly strategy, quarterly deep dives. Data > gut.

---

## 📈 12-MONTH ROADMAP

| Month | Focus | Milestone |
|-------|-------|-----------|
| 1 | Foundation | 15 master faces, 30 poses, 5 videos, 3 platforms live |
| 2 | Consistency | Daily posting, 1K followers, first affiliate $ |
| 3 | Fanvue Launch | 3K followers, $200/mo Fanvue, first UGC deal |
| 4 | Systems | Batch process smooth, 10K followers, $1K/mo |
| 5 | Scale | 20K followers, Tier 2 Fanvue, digital product #1 |
| 6 | Revenue | 35K followers, $6.7K/mo, hire VA for DMs |
| 7-9 | Optimize | A/B test everything, 60K followers, $15K/mo |
| 10-12 | Portfolio | Launch Persona #2, 100K followers, $33K/mo |

---

## ⚠️ CRITICAL RULES (NEVER BREAK)

1. **Face consistency** — Master references are LAW. No regenerating base face.
2. **AI disclosure** — Every platform, every post: #aiinfluencer #virtualinfluencer
3. **Original character only** — Zero real person likeness. Ever.
4. **No OnlyFans** — Fanvue only for AI creators.
5. **Batch everything** — Sunday 2 hours = 1 week. No daily production.
6. **Contracts for everything** — UGC, affiliate, custom content. No verbal.
7. **Track everything** — If not in Notion, it didn't happen.
8. **Vulnerability > perfection** — The acne scar stays. The €147 Stripe balance stays.

---

## 🔧 CUSTOMIZATION

### To Create Persona #2:
1. Copy `zara-velasquez-factory/` → `persona2-name-factory/`
2. Edit `CHARACTER_BIBLE.md` with new identity
3. Run `bash scripts/setup.sh` in new folder
4. Generate new master faces on Picovix
5. Update `.env` with new Notion DBs
6. Run weekly batch

### To Add Platforms:
1. Add platform spec to `assets/identity/handoff.json`
2. Add checklist to `platform_checklists/README.md`
3. Add API sync to `scripts/daily_cron.sh`
4. Add metrics to `analytics/dashboard.md`

---

## 📚 DOCUMENTATION INDEX

| Need | Read |
|------|------|
| **Understand the character** | `CHARACTER_BIBLE.md` |
| **Generate images** | `pipeline/generate_images.py` + `prompts/master_prompt.txt` |
| **Generate videos** | `pipeline/generate_video.py` + `prompts/video_prompts/` |
| **Plan weekly content** | `pipeline/batch_content.py` + `content_calendar/weekly_template.md` |
| **Set up monetization** | `monetization/fanvue_setup.md` + `monetization/affiliate_links.md` |
| **Pitch brands** | `media_kit/README.md` + `contracts/ugc_contract.md` |
| **Post correctly** | `platform_checklists/README.md` |
| **Track metrics** | `analytics/dashboard.md` |
| **Automate operations** | `scripts/daily_cron.sh` + `scripts/weekly_batch.sh` |

---

## 🤝 CONTRIBUTING / FORKING

This system is designed to be **forked and adapted**. 

**MIT License** — Use commercially, modify freely, attribute if you share.

**If you build something cool on top:** Open a PR or tag @zaravelasquez — I'd love to see it.

---

## 🙏 CREDITS & INSPIRATION

**Repos studied & patterns borrowed from:**
- `0xAnni/ugc-creator` — JSON identity + 6-layer prompts
- `SamurAIGPT/AI-Influencer-Generator` — Local SD + SadTalker pipeline
- `ArmaghanRazaChaudhary/AI-Influencer` — Character packages + factory pattern
- `terminills/gator` — Full platform architecture
- `metrosir/consistent-ai-character-prompts` — Scene prompt library
- `prodcastmediaa-cyber/ai-influencer-talking-head-v31` — Telegram automation

**Competitors analyzed:** Lil Miquela, Aitana Lopez, Lu do Magalu, Imma, Emily Pellegrini, Mia Zelu, Kyra

**Tools vetted:** Picovix, Leonardo AI, InsightFace, Hedra, Veo 2, Kling, Fanvue, ConvertKit, Buffer, Notion, Make.com, Dub.co

---

## 📞 SUPPORT

**Issues:** Check `scripts/daily_cron.sh` logs first
**Questions:** DM @zaravelasquez (when live)
**Customization help:** See `CHARACTER_BIBLE.md` — everything derives from there

---

**Built with:** Systems thinking, obsessive documentation, and the belief that one person with the right pipeline can outproduce a team without one.

**Version:** 1.0 | **Date:** 2026-10-21 | **Operator:** You

---

**Now go build.** 🚀