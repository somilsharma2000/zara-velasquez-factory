#!/bin/bash
# ZARA VELASQUEZ FACTORY — WEEKLY BATCH SCRIPT
# Run: Every Sunday 10:00 AM WET (or manually)
# Purpose: Complete weekly content production in 2 hours

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

LOG_DIR="$PROJECT_ROOT/logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/weekly_batch_$(date +%Y%m%d).log"

exec > >(tee -a "$LOG_FILE") 2>&1

echo "========================================"
echo "📅 WEEKLY BATCH — $(date '+%Y-%m-%d %H:%M:%S %Z')"
echo "========================================"

# Load environment
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# Parse arguments
WEEK=${1:-$(date +%V | sed 's/^0*//')}  # Current week number
FOCUS=${2:-BALANCED}

echo "Week: $WEEK | Focus: $FOCUS"

# 1. Run content batching
echo -e "\n📝 [1/8] Generating weekly content plan..."
python3 pipeline/batch_content.py --week "$WEEK" --focus "$FOCUS"

# 2. Run image generation prompts
echo -e "\n🎨 [2/8] Generating image prompts..."
python3 pipeline/generate_images.py --week "$WEEK" --pillar ALL

# 3. Run video generation configs
echo -e "\n🎬 [3/8] Generating video configs..."
python3 pipeline/generate_video.py --week "$WEEK"

# 4. Manual step: Generate assets
echo -e "\n🖼️  [4/8] MANUAL STEP REQUIRED:"
echo "   → Open Leonardo AI, use prompts from assets/references/pose_library/"
echo "   → Download generated images to assets/references/pose_library/"
echo "   → Run InsightFace swaps using commands from assets/references/insightface_commands_week${WEEK}_*.txt"
echo "   → Curate best results to assets/references/final_assets/"
echo "   → Generate Hedra videos at hedra.com using scripts from prompts/video_prompts/"
echo "   → Generate Veo2 videos at aistudio.google.com using configs from assets/references/video_library/"
echo "   → Run Colab face swaps for video sources"
echo ""
read -p "   Press ENTER when assets are ready in final_assets/ and video_library/..."

# 5. Match assets to calendar
echo -e "\n🔗 [5/8] Matching assets to calendar..."
WEEK_DIR="content_calendar/week_$(printf "%02d" "$WEEK")"
if [ -f "$WEEK_DIR/calendar.json" ]; then
    python3 -c "
import json, os, glob

with open('$WEEK_DIR/calendar.json') as f:
    cal = json.load(f)

# Find available assets
images = glob.glob('assets/references/final_assets/*.png') + glob.glob('assets/references/final_assets/*.jpg')
videos = glob.glob('assets/references/video_library/*.mp4')

print(f'  📸 {len(images)} final images available')
print(f'  🎥 {len(videos)} videos available')

# Check each day's main content
for date_str, day in cal.items():
    for post in day['posts']:
        if post['type'] == 'MAIN':
            idea = post['idea_id']
            # Try to find matching asset
            matches = [f for f in images + videos if idea.lower() in f.lower()]
            if matches:
                post['asset_path'] = matches[0]
                print(f'    ✅ {idea} → {os.path.basename(matches[0])}')
            else:
                print(f'    ⚠️  {idea} — NO ASSET FOUND')

# Save updated calendar
with open('$WEEK_DIR/calendar.json', 'w') as f:
    json.dump(cal, f, indent=2, default=str)
"
else
    echo "  ⚠️  Calendar not found"
fi

# 6. Generate final captions (interactive)
echo -e "\n✍️  [6/8] Finalizing captions..."
if [ -f "$WEEK_DIR/captions.json" ]; then
    echo "  Opening caption editor for each main post..."
    python3 -c "
import json, os

with open('$WEEK_DIR/captions.json') as f:
    captions = json.load(f)

with open('$WEEK_DIR/calendar.json') as f:
    cal = json.load(f)

for date_str, day in cal.items():
    for post in day['posts']:
        if post['type'] == 'MAIN':
            idea = post['idea_id']
            if idea in captions:
                cap = captions[idea]
                print(f'\n--- {idea} ({date_str}) ---')
                print(f'Template: {cap[\"template\"]}')
                print(f'Hook: {cap[\"hook\"]}')
                print(f'Body: {cap[\"body\"]}')
                print(f'Vulnerable: {cap[\"vulnerable_detail\"]}')
                print(f'CTA: {cap[\"cta\"]}')
                print(f'Hashtags: {\" \".join(cap[\"hashtags\"])}')
                print()
                input('Press ENTER to continue (or Ctrl+C to skip)...')
"
else
    echo "  ⚠️  Captions not found"
fi

# 7. Import to Buffer/Later
echo -e "\n📤 [7/8] Preparing Buffer import..."
if [ -f "$WEEK_DIR/buffer_schedule.json" ]; then
    BUFFER_FILE="$WEEK_DIR/buffer_import_$(date +%Y%m%d).csv"
    python3 -c "
import json, csv

with open('$WEEK_DIR/buffer_schedule.json') as f:
    posts = json.load(f)

with open('$BUFFER_FILE', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Platform', 'Date', 'Time', 'Text', 'Media Path', 'UTM Campaign'])
    for post in posts:
        cap = post.get('caption', {})
        text_parts = []
        if cap.get('hook'): text_parts.append(cap['hook'])
        if cap.get('body'): text_parts.append(cap['body'])
        if cap.get('vulnerable_detail'): text_parts.append(cap['vulnerable_detail'])
        if cap.get('cta'): text_parts.append(cap['cta'])
        if cap.get('hashtags'): text_parts.append(' '.join(cap['hashtags']))
        text = '\n\n'.join(text_parts)
        
        media = post.get('media_path', '[TO BE FILLED]')
        utm = post.get('caption', {}).get('utm_campaign', '')
        
        writer.writerow([
            post['platform'],
            post['date'],
            post['time'],
            text,
            media,
            utm
        ])

print(f'  ✅ Buffer CSV: $BUFFER_FILE ({len(posts)} posts)')
"
    echo "  📋 Import $BUFFER_FILE to Buffer.com → Import CSV"
else
    echo "  ⚠️  Buffer schedule not found"
fi

# 8. Weekly review & commit
echo -e "\n📋 [8/8] Weekly review & Git commit..."

# Show summary
python3 -c "
import json, os

week_dir = '$WEEK_DIR'
if os.path.exists(week_dir):
    files = os.listdir(week_dir)
    print(f'  📁 Artifacts in {week_dir}:')
    for f in sorted(files):
        size = os.path.getsize(os.path.join(week_dir, f))
        print(f'    {f} ({size} bytes)')
"

# Git commit
if [ -d .git ]; then
    git add -A
    git commit -m "Week $WEEK batch: $FOCUS focus

- Content calendar generated
- Image prompts created (Leonardo + InsightFace)
- Video configs created (Hedra, Veo2, Kling, Colab)
- Captions drafted
- Buffer schedule prepared
- Assets matched to calendar" 2>/dev/null && echo "  ✅ Git committed" || echo "  ⏭️  No changes to commit"
fi

echo -e "\n========================================"
echo "✅ WEEKLY BATCH COMPLETE — $(date '+%H:%M:%S')"
echo "========================================"
echo ""
echo "📋 POST-BATCH CHECKLIST:"
echo "  [ ] Assets generated and curated in final_assets/"
echo "  [ ] Videos generated in video_library/"
echo "  [ ] Captions finalized in calendar"
echo "  [ ] Buffer CSV imported to Buffer/Later"
echo "  [ ] Stories planned for each day"
echo "  [ ] Fanvue exclusives scheduled"
echo "  [ ] Brand deal deliverables on track"
echo "  [ ] Analytics dashboard updated"
echo ""
echo "🎯 NEXT WEEK: ./zara batch --week $((WEEK+1)) --focus BALANCED"