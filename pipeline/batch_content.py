#!/usr/bin/env python3
"""
ZARA VELASQUEZ — CONTENT BATCH PRODUCER
Orchestrates weekly content production: selects ideas, generates assets, writes captions, schedules.
Run: python batch_content.py --week 1
"""

import argparse
import json
import os
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import random

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

class ZaraContentBatcher:
    def __init__(self):
        self.project_root = PROJECT_ROOT
        self.content_dir = self.project_root / "content_calendar"
        self.content_dir.mkdir(parents=True, exist_ok=True)
        self.assets_dir = self.project_root / "assets" / "references"
        self.backlog = self.load_backlog()
        self.templates = self.load_templates()
    
    def load_backlog(self) -> Dict:
        """Load content ideas from research-validated backlog (content_strategy_2026.md)"""
        # 100+ ideas organized by pillar with specific hooks
        return {
            "BUILD": [
                "B01: I quit my $60K marketing job with €3K savings. Here's the spreadsheet.",
                "B02: Day 1 of CreatorOS: Blank Next.js repo. What I'm building and why.",
                "B03: My €3K runway breakdown: Rent, food, tools, buffer. Real numbers.",
                "B04: Choosing Supabase over Firebase. The 3 AM debugging session that decided it.",
                "B05: First user interview: 'I'd pay $29/mo for this.' Validation or delusion?",
                "B06: Setting up Stripe test mode. Why I'm not live yet.",
                "B07: My Notion workspace for founder ops. Free template in bio.",
                "B08: The feature I built that zero users asked for. Deleting it today.",
                "B09: Coffee shop hopping for 'vibe coding.' Does environment change output?",
                "B10: Week 1 metrics: 0 users, 0 revenue, 47 commits. The honest start.",
                "B11: First paying customer! €19/mo. The 6-week journey to 'yes.'",
                "B12: Pricing page iterations: $9 → $19 → $29 → $49. What converted.",
                "B13: Churn analysis: Why 2 beta users cancelled. The exit interview.",
                "B14: Building in public vs building in private. What I'd tell month-1 me.",
                "B15: My tech stack deep dive: Next.js + Supabase + Stripe + Tailwind + Vercel.",
                "B16: The $0 marketing strategy: SEO content + Twitter + newsletter. No ads.",
                "B17: Hiring a contractor for the first time. €500 for auth refactor. Worth it.",
                "B18: Database migration disaster. 4 hours downtime. What I learned.",
                "B19: Feature prioritization framework: RICE scoring for solo founders.",
                "B20: Month 3 revenue report: $347 MRR. The good, bad, ugly."
            ],
            "LIVE": [
                "L01: Apartment tour: €850/mo Alfama walkup. The good, the mold, the view.",
                "L02: My 5:30 AM routine: Matcha, journal, 90 min deep work. No phone until 7.",
                "L03: Best pastel de nata in Lisbon: 7 tested, 1 winner. (Not the famous one.)",
                "L04: Lisbon coworking: €150/mo vs €300/mo vs cafe hopping. My verdict.",
                "L05: Visa appointment day: The paperwork, the wait, the €80 fee, the coffee after.",
                "L06: Sunday market routine: Fresh fish, flowers, ceramics. My weekend ritual.",
                "L07: Learning Portuguese: The app, the tutor, the embarrassing mistakes.",
                "L08: Lisbon hills = free gym. My legs after 3 months. Before/after.",
                "L09: Digital nomad community: The WhatsApp group, the meetups, the drama.",
                "L10: Packing for Bali: 2 suitcases, 6 months. What stays, what goes.",
                "L11: Villa tour: $600/mo Canggu. Rice field view, gecko roommates.",
                "L12: Bali morning: Coconut, rice field walk, 7 AM deep work session.",
                "L13: Canggu cafe crawl: 5 spots, best wifi, best food, best vibe.",
                "L14: Visa run to Singapore: 24 hours, $200, worth it for 6 more months.",
                "L15: Bali belly: The reality nobody posts. Hydration, meds, 3 days down.",
                "L16: Scooter life: The crash (minor), the rental, the traffic, the freedom.",
                "L17: Ubud weekend: Yoga, waterfalls, monkey forest, digital detox attempt.",
                "L18: Balinese ceremonies: What I've learned, what I respect, what I don't get.",
                "L19: Timezone juggling: Lisbon team, US customers, Bali life. My calendar.",
                "L20: 6-month Bali reflection: What changed, what didn't, what's next."
            ],
            "LEARN": [
                "T01: Notion for founders: My workspace template (free duplicate).",
                "T02: CapCut for Reels: 10 min edit workflow. No premiere needed.",
                "T03: Linear for solo dev: Issue tracking that doesn't suck.",
                "T04: ConvertKit automation: Welcome sequence, broadcast, tagging.",
                "T05: Supabase auth + Row Level Security: The tutorial I needed.",
                "T06: Stripe Checkout + Portal: Subscription management in 30 min.",
                "T07: Vercel preview deployments: The workflow that saves my ass.",
                "T08: Canva for non-designers: Brand kit, templates, batch create.",
                "T09: Obsidian for knowledge: Zettelkasten lite for founders.",
                "T10: AI tools I actually use: ChatGPT, Perplexity, Cursor, Hedra. Honest review.",
                "T11: Founder finances: Personal vs business accounts, paying myself, taxes.",
                "T12: Bootstrap budget: €3K → $10K MRR. Every expense tracked.",
                "T13: Affiliate income breakdown: $200/mo from 12 links. Not passive.",
                "T14: UGC rate card: How I price, negotiate, invoice. Template included.",
                "T15: Fanvue setup: KYC, pricing, content strategy, first $100.",
                "T16: Newsletter monetization: Sponsors, paid subs, affiliate. $500/mo at 2K subs.",
                "T17: Contractor vs employee: Portugal vs Indonesia vs remote. Legal costs.",
                "T18: Currency management: Wise, Revolut, local banks. Fees optimized.",
                "T19: Retirement as a nomad: Pension, investments, compound interest.",
                "T20: Financial freedom number: Mine is €3K/mo. Yours?"
            ],
            "FEEL": [
                "F01: The day I wanted to quit. €147 in Stripe. The email that changed it.",
                "F02: Imposter syndrome at 2 AM: 'Who am I to build this?'",
                "F03: Comparison trap: Peer hit $50K MRR. I'm at $300. Spiral.",
                "F04: Burnout signs I ignored: Sleep, irritability, zero creativity. The reset.",
                "F05: Loneliness of solo founding: No cofounder, no team, just me and the code.",
                "F06: Fear of success: What if it works? What if I can't handle it?",
                "F06: The rejection: Investor said 'too early.' Customer said 'too expensive.'",
                "F08: Identity crisis: Am I a founder? A creator? A nomad? All? None?",
                "F09: Money anxiety: €3K → €1.2K → €400. The runway countdown.",
                "F10: Therapy for founders: Why I started, what we talk about, cost."
            ]
        }
    
    def load_templates(self) -> Dict:
        """Load research-validated caption templates (content_strategy_2026.md)"""
        return {
            "BUILD": [
                "B1_metric: Hook → Value → Vulnerable Detail → Question",
                "B2_failure: Hook → Mistake → Cost → Pivot → Question",
                "B3_tool_stack: Hook → Tool List → Vulnerable Detail → CTA",
                "B4_public_moment: Hook → Context → Action → Internal Monologue → Question"
            ],
            "LIVE": [
                "L1_location: Hook → Numbered Tips → Vulnerable Detail → CTA",
                "L2_routine: Hook → Timeline → Vulnerable Detail → Question",
                "L3_travel: Hook → What Stays/Goes → System → Vulnerable Detail → Question"
            ],
            "LEARN": [
                "T1_tutorial: Hook Slide → Context → Framework → Deep Dive Slides → Template CTA",
                "T2_money: Hook → Revenue Breakdown → Costs → Vulnerable Detail → CTA",
                "T3_book: Hook → Quote → 3 Takeaways → Vulnerable Detail → Question"
            ],
            "FEEL": [
                "F1_vulnerable_video: Hook → Context → Story → Lesson → Close + Question",
                "F2_story_sequence: 10-frame vulnerable story sequence with interactive elements"
            ]
        }
    
    def select_weekly_ideas(self, week: int, pillar_focus: str = "BALANCED") -> Dict[str, List[str]]:
        """Select 7 ideas for the week based on pillar distribution"""
        
        # Pillar distribution per week
        distributions = {
            "BALANCED": {"BUILD": 2, "LIVE": 2, "LEARN": 2, "FEEL": 1},
            "BUILD_HEAVY": {"BUILD": 3, "LIVE": 1, "LEARN": 2, "FEEL": 1},
            "LIVE_HEAVY": {"BUILD": 1, "LIVE": 3, "LEARN": 2, "FEEL": 1},
            "LAUNCH_WEEK": {"BUILD": 3, "LIVE": 1, "LEARN": 1, "FEEL": 2}
        }
        
        dist = distributions.get(pillar_focus, distributions["BALANCED"])
        
        selected = {}
        for pillar, count in dist.items():
            available = self.backlog[pillar]
            # In production: filter out recently used (last 4 weeks)
            selected[pillar] = random.sample(available, min(count, len(available)))
        
        return selected
    
    def assign_formats(self, ideas: Dict[str, List[str]]) -> List[Dict]:
        """Assign content formats to each idea"""
        format_map = {
            "BUILD": [("Reel", "9:16"), ("Carousel", "4:5"), ("Thread", "16:9")],
            "LIVE": [("Reel", "9:16"), ("Carousel", "4:5"), ("Stories", "9:16")],
            "LEARN": [("Carousel", "4:5"), ("Thread", "16:9"), ("Template", "link")],
            "FEEL": [("Hedra_Video", "9:16"), ("Story_Sequence", "9:16")]
        }
        
        assignments = []
        for pillar, idea_list in ideas.items():
            formats = format_map[pillar]
            for i, idea in enumerate(idea_list):
                fmt, aspect = formats[i % len(formats)]
                assignments.append({
                    "id": idea,
                    "pillar": pillar,
                    "primary_format": fmt,
                    "aspect_ratio": aspect,
                    "secondary_formats": [f for f, a in formats if f != fmt]
                })
        
        return assignments
    
    def generate_captions(self, assignments: List[Dict]) -> Dict[str, Dict]:
        """Generate research-validated captions for each assignment (content_strategy_2026.md)"""
        # Research-validated hooks per pillar
        hooks = {
            "BUILD": [
                "Hot take: Your morning coffee order says more about your business than your pitch deck.",
                "Unpopular opinion: Most 'build in public' is performative. Real build in public = sharing the L's.",
                "Nobody talks about the 47 commits before the first user. The Stripe declines. The 3am bugs.",
                "The honest truth: Bootstrap validation looks like €147 in Stripe and 3 rejected investors.",
                "POV: You're 24, €3K savings, blank Next.js repo. What's your first commit?"
            ],
            "LIVE": [
                "Unpopular opinion: Digital nomad visa is the easy part. The hard part? Timezone calls at 11pm.",
                "Nobody talks about the loneliness of the 'dream life.' 4am wakeups. Solo security lines.",
                "Real talk: Bali isn't paradise 24/7. It's humidity, scooter crashes, visa runs. But also this.",
                "The honest truth: 5:30am isn't aesthetic. It's survival. The only time nobody needs anything.",
                "POV: You're packing 6 months of life into 35L. What stays? What goes?"
            ],
            "LEARN": [
                "Stop paying for Notion templates. I'll give you mine free. Spent 6 months building this.",
                "Hot take: Blog posts are a waste of time for early-stage SaaS. Here's why I only make TikToks.",
                "My €3K runway → $1K MRR. Every expense tracked. Free spreadsheet in bio.",
                "Unpopular opinion: Your Notion setup is procrastination. Ship the feature instead.",
                "3 takeaways from $100M Offers that changed how I price. Slide 3 saved me $10K."
            ],
            "FEEL": [
                "Hot take: The loneliness isn't the travel. It's the 3am Stripe decline.",
                "The honest truth: I almost quit last month. Packed a bag. Looked at flights home.",
                "Unpopular opinion: Freedom is responsibility wearing a bikini. Worth it? Most days.",
                "Nobody posts the visa rejection letter. The Bali belly. The 3am panic. Here's mine.",
                "Real talk: Still figuring it out. But the builder part? This I choose."
            ]
        }
        
        captions = {}
        for item in assignments:
            pillar = item["pillar"]
            idea_id = item["id"]
            template_key = random.choice(self.templates[pillar])
            
            # Select hook based on idea_id hash for consistency
            hook_idx = hash(idea_id) % len(hooks[pillar])
            hook = hooks[pillar][hook_idx]
            
            caption = {
                "idea_id": idea_id,
                "pillar": pillar,
                "template": template_key,
                "hook": hook,
                "body": f"[RESEARCH-VALIDATED VALUE for {idea_id} - use {template_key} structure]",
                "vulnerable_detail": f"[RESEARCH-VALIDATED VULNERABLE DETAIL for {idea_id}]",
                "cta": "What would you do? / Agree or disagree? / Drop your take 👇 / Saving this for later → / Real talk: what's your version?",
                "hashtags": self.get_hashtags(pillar),
                "platform_adaptations": self.adapt_for_platforms(idea_id, pillar)
            }
            captions[idea_id] = caption
        
        return captions
    
    def get_hashtags(self, pillar: str) -> List[str]:
        """Research-validated hashtag banks (content_strategy_2026.md)"""
        banks = {
            "BUILD": ["#buildinpublic", "#saasfounder", "#bootstrapped", "#indiehacker", "#mrr", "#founderjourney", "#startuplessons", "#nocode", "#solopreneur"],
            "LIVE": ["#digitalnomad", "#lisbonlife", "#balilife", "#slowtravel", "#nomadlife", "#remotework", "#portugallife", "#indonesia", "#visalife"],
            "LEARN": ["#foundertools", "#notiontemplate", "#creatorconomy", "#affiliatemarketing", "#ugccreator", "#fanvue", "#newslettergrowth", "#productivity"],
            "FEEL": ["#foundermentalhealth", "#impostersyndrome", "#burnoutrecovery", "#solofounder", "#vulnerability", "#authenticity", "#realentrepreneurship"]
        }
        # Return 5 random from the appropriate bank
        import random
        return random.sample(banks.get(pillar, []), min(5, len(banks.get(pillar, []))))
    
    def adapt_for_platforms(self, idea_id: str, pillar: str) -> Dict:
        """Create platform-specific adaptations"""
        return {
            "instagram_feed": {"format": "Carousel/Reel", "caption_length": "medium", "hashtags": 5},
            "instagram_reels": {"format": "Reel", "caption_length": "short", "hashtags": 3, "text_overlay": True},
            "tiktok": {"format": "Reel", "caption_length": "short", "hashtags": 3, "native_text": True},
            "youtube_shorts": {"format": "Reel", "caption_length": "short", "hashtags": 3, "pinned_comment": True},
            "x_twitter": {"format": "Thread", "caption_length": "thread", "hashtags": 2, "quote_tweet": False},
            "linkedin": {"format": "Post/Article", "caption_length": "long", "hashtags": 3, "professional_frame": True},
            "fanvue": {"format": "Exclusive", "caption_length": "long", "hashtags": 0, "dm_cta": True}
        }
    
    def create_weekly_calendar(self, week: int, assignments: List[Dict], captions: Dict) -> Dict:
        """Create day-by-day posting calendar"""
        start_date = datetime.now() + timedelta(weeks=week-1)
        start_monday = start_date - timedelta(days=start_date.weekday())
        
        calendar = {}
        assignment_idx = 0
        
        # Daily posting schedule
        schedule = [
            {"day": "Monday", "pillar": "BUILD", "slots": ["Reel", "Carousel", "Thread", "Stories x2"]},
            {"day": "Tuesday", "pillar": "LIVE", "slots": ["Reel", "Stories x3"]},
            {"day": "Wednesday", "pillar": "LEARN", "slots": ["Carousel", "Thread", "Stories x2"]},
            {"day": "Thursday", "pillar": "FEEL", "slots": ["Hedra_Video", "Story_Sequence x10"]},
            {"day": "Friday", "pillar": "BUILD", "slots": ["Reel", "Thread", "Stories x2"]},
            {"day": "Saturday", "pillar": "LIVE", "slots": ["Carousel", "Stories x3"]},
            {"day": "Sunday", "pillar": "BATCH", "slots": ["Stories x2"]}
        ]
        
        for i, day_sched in enumerate(schedule):
            date = start_monday + timedelta(days=i)
            day_content = {
                "date": date.strftime("%Y-%m-%d"),
                "day": day_sched["day"],
                "pillar_focus": day_sched["pillar"],
                "posts": []
            }
            
            # Assign main content
            if day_sched["pillar"] != "BATCH" and assignment_idx < len(assignments):
                item = assignments[assignment_idx]
                caption = captions.get(item["id"], {})
                day_content["posts"].append({
                    "type": "MAIN",
                    "idea_id": item["id"],
                    "format": item["primary_format"],
                    "caption": caption,
                    "status": "draft"
                })
                assignment_idx += 1
            
            # Add stories
            for slot in day_sched["slots"]:
                if "Stories" in slot:
                    count = int(slot.split("x")[1]) if "x" in slot else 1
                    day_content["posts"].append({
                        "type": "STORIES",
                        "count": count,
                        "theme": day_sched["pillar"],
                        "status": "draft"
                    })
            
            # Daily X/Twitter post
            day_content["posts"].append({
                "type": "X_TWITTER",
                "format": "Single/Thread",
                "pillar": day_sched["pillar"],
                "status": "draft"
            })
            
            # LinkedIn (Mon/Wed/Fri)
            if day_sched["day"] in ["Monday", "Wednesday", "Friday"]:
                day_content["posts"].append({
                    "type": "LINKEDIN",
                    "format": "Post",
                    "pillar": day_sched["pillar"],
                    "status": "draft"
                })
            
            calendar[date.strftime("%Y-%m-%d")] = day_content
        
        return calendar
    
    def create_buffer_schedule(self, calendar: Dict) -> List[Dict]:
        """Create Buffer/Later compatible schedule"""
        buffer_posts = []
        
        for date_str, day in calendar.items():
            for post in day["posts"]:
                if post["type"] in ["MAIN", "X_TWITTER", "LINKEDIN"]:
                    # Determine optimal time (would be from analytics)
                    optimal_times = {
                        "instagram": "11:00",
                        "tiktok": "19:00",
                        "x_twitter": "09:00",
                        "linkedin": "08:00",
                        "youtube": "17:00"
                    }
                    
                    platforms = self.get_platforms_for_post(post)
                    for platform in platforms:
                        buffer_posts.append({
                            "platform": platform,
                            "date": date_str,
                            "time": optimal_times.get(platform, "12:00"),
                            "content_type": post.get("format", "Post"),
                            "caption": post.get("caption", {}),
                            "media_path": f"[TO BE FILLED: {post.get('idea_id', 'unknown')}]",
                            "status": "pending"
                        })
        
        return buffer_posts
    
    def get_platforms_for_post(self, post: Dict) -> List[str]:
        """Determine which platforms get this content"""
        fmt = post.get("format", "")
        pillar = post.get("pillar", "")
        
        if "Reel" in fmt or "Hedra" in fmt:
            return ["instagram_reels", "tiktok", "youtube_shorts"]
        elif "Carousel" in fmt:
            return ["instagram_feed", "linkedin", "x_twitter"]
        elif "Thread" in fmt:
            return ["x_twitter", "linkedin"]
        elif post["type"] == "X_TWITTER":
            return ["x_twitter"]
        elif post["type"] == "LINKEDIN":
            return ["linkedin"]
        return ["instagram_feed"]
    
    def run_weekly_batch(self, week: int, pillar_focus: str = "BALANCED") -> Dict:
        """Run complete weekly content batching"""
        print(f"\n📅 WEEK {week} CONTENT BATCH — FOCUS: {pillar_focus}")
        print("=" * 50)
        
        # 1. Select ideas
        print("\n🎯 Selecting weekly ideas...")
        ideas = self.select_weekly_ideas(week, pillar_focus)
        print(f"   Selected: {sum(len(v) for v in ideas.values())} ideas")
        for pillar, items in ideas.items():
            print(f"   {pillar}: {', '.join(items)}")
        
        # 2. Assign formats
        print("\n📐 Assigning formats...")
        assignments = self.assign_formats(ideas)
        for a in assignments:
            print(f"   {a['id']} ({a['pillar']}) → {a['primary_format']} ({a['aspect_ratio']})")
        
        # 3. Generate captions
        print("\n✍️ Generating captions...")
        captions = self.generate_captions(assignments)
        print(f"   Generated: {len(captions)} caption sets")
        
        # 4. Create calendar
        print("\n📆 Creating weekly calendar...")
        calendar = self.create_weekly_calendar(week, assignments, captions)
        total_posts = sum(len(d["posts"]) for d in calendar.values())
        print(f"   {len(calendar)} days | {total_posts} total posts (incl. stories)")
        
        # 5. Create Buffer schedule
        print("\n📤 Creating Buffer schedule...")
        buffer_schedule = self.create_buffer_schedule(calendar)
        print(f"   {len(buffer_schedule)} platform-specific posts")
        
        # 6. Save all artifacts
        week_dir = self.content_dir / f"week_{week:02d}"
        week_dir.mkdir(parents=True, exist_ok=True)
        
        artifacts = {
            "ideas_selected": ideas,
            "format_assignments": assignments,
            "captions": captions,
            "calendar": calendar,
            "buffer_schedule": buffer_schedule
        }
        
        for name, data in artifacts.items():
            filepath = week_dir / f"{name}.json"
            with open(filepath, "w") as f:
                json.dump(data, f, indent=2, default=str)
            print(f"   💾 {name}.json")
        
        # Create human-readable calendar markdown
        md_path = week_dir / "calendar.md"
        self.write_calendar_markdown(calendar, md_path, week)
        print(f"   📄 calendar.md")
        
        print(f"\n✅ Week {week} batch complete!")
        print(f"📁 Artifacts in: {week_dir}")
        
        return {
            "week": week,
            "pillar_focus": pillar_focus,
            "ideas_count": sum(len(v) for v in ideas.values()),
            "assignments_count": len(assignments),
            "calendar_days": len(calendar),
            "buffer_posts": len(buffer_schedule),
            "artifacts_dir": str(week_dir)
        }
    
    def write_calendar_markdown(self, calendar: Dict, path: Path, week: int):
        """Write human-readable calendar"""
        lines = [f"# WEEK {week} CONTENT CALENDAR", f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}", ""]
        
        for date_str in sorted(calendar.keys()):
            day = calendar[date_str]
            lines.append(f"## {day['day']} ({date_str}) — {day['pillar_focus']}")
            lines.append("")
            
            for post in day["posts"]:
                if post["type"] == "MAIN":
                    lines.append(f"### 🎬 MAIN: {post['idea_id']} | {post['format']}")
                    cap = post.get("caption", {})
                    lines.append(f"**Hook:** {cap.get('hook', 'TBD')}")
                    lines.append(f"**CTA:** {cap.get('cta', 'TBD')}")
                    lines.append(f"**Hashtags:** {' '.join(cap.get('hashtags', []))}")
                elif post["type"] == "STORIES":
                    lines.append(f"### 📱 STORIES x{post['count']} — Theme: {post['theme']}")
                elif post["type"] == "X_TWITTER":
                    lines.append(f"### 🐦 X/TWITTER — Pillar: {post['pillar']}")
                elif post["type"] == "LINKEDIN":
                    lines.append(f"### 💼 LINKEDIN — Pillar: {post['pillar']}")
                lines.append("")
        
        with open(path, "w") as f:
            f.write("\n".join(lines))


def main():
    parser = argparse.ArgumentParser(description="Zara Velasquez Content Batcher")
    parser.add_argument("--week", type=int, default=1, help="Week number")
    parser.add_argument("--focus", type=str, default="BALANCED", 
                       choices=["BALANCED", "BUILD_HEAVY", "LIVE_HEAVY", "LAUNCH_WEEK"])
    args = parser.parse_args()
    
    batcher = ZaraContentBatcher()
    result = batcher.run_weekly_batch(args.week, args.focus)
    
    print(f"\n📋 NEXT STEPS:")
    print(f"1. Review: {result['artifacts_dir']}/calendar.md")
    print("2. Match assets from final_assets/video_library to each idea_id")
    print("3. Fill in caption templates with real content")
    print("4. Import buffer_schedule.json to Buffer/Later")
    print("5. Schedule Stories manually (Buffer free doesn't support Stories)")


if __name__ == "__main__":
    main()