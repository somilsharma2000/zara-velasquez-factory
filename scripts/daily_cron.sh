#!/bin/bash
# ZARA VELASQUEZ FACTORY — DAILY CRON
# Run: Daily at 6:00 AM WET via systemd/cron/Make.com
# Purpose: Sync metrics, check pipeline, trigger alerts

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

LOG_DIR="$PROJECT_ROOT/logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/daily_$(date +%Y%m%d).log"

exec > >(tee -a "$LOG_FILE") 2>&1

echo "========================================"
echo "🌅 DAILY CRON — $(date '+%Y-%m-%d %H:%M:%S %Z')"
echo "========================================"

# Load environment
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# 1. Sync metrics from platforms (via Make.com webhook)
echo -e "\n📊 [1/6] Triggering metrics sync..."
if [ -n "$MAKE_WEBHOOK_URL" ]; then
    curl -s -X POST "$MAKE_WEBHOOK_URL" \
        -H "Content-Type: application/json" \
        -d '{"trigger": "daily_metrics_sync", "date": "'$(date -I)'"}' \
        && echo "  ✅ Make.com webhook triggered" \
        || echo "  ⚠️  Make.com webhook failed"
else
    echo "  ⏭️  MAKE_WEBHOOK_URL not set, skipping"
fi

# 2. Check content scheduled for today
echo -e "\n📅 [2/6] Checking today's content..."
TODAY=$(date -I)
WEEK_DIR=$(ls -d content_calendar/week_* 2>/dev/null | sort | tail -1)
if [ -n "$WEEK_DIR" ] && [ -f "$WEEK_DIR/calendar.json" ]; then
    python3 -c "
import json, sys
with open('$WEEK_DIR/calendar.json') as f:
    cal = json.load(f)
today = '$TODAY'
if today in cal:
    day = cal[today]
    print(f'  📝 {day[\"day\"]} ({today}) — {day[\"pillar_focus\"]}')
    for post in day['posts']:
        if post['type'] == 'MAIN':
            print(f'    🎬 {post[\"idea_id\"]} | {post[\"format\"]}')
        elif post['type'] == 'STORIES':
            print(f'    📱 STORIES x{post[\"count\"]} | {post[\"theme\"]}')
        elif post['type'] in ['X_TWITTER', 'LINKEDIN']:
            print(f'    🐦 {post[\"type\"]} | {post[\"pillar\"]}')
else:
    print('  ⚠️  No calendar entry for today')
"
else
    echo "  ⚠️  No calendar found"
fi

# 3. Check brand deal deadlines
echo -e "\n🤝 [3/6] Checking brand deal deadlines..."
if [ -f crm/README.md ]; then
    python3 -c "
import json, sys, os
from datetime import datetime, timedelta

deals_file = 'crm/deals.json'
if os.path.exists(deals_file):
    with open(deals_file) as f:
        deals = json.load(f)
    today = datetime.now().date()
    for deal in deals:
        due = datetime.fromisoformat(deal.get('Due Date', '2099-12-31')).date()
        days = (due - today).days
        if days <= 3 and days >= 0:
            print(f'  🔥 URGENT: {deal[\"Deal Name\"]} due in {days} day(s)')
        elif days <= 7 and days > 3:
            print(f'  ⚠️  SOON: {deal[\"Deal Name\"]} due in {days} days')
else:
    print('  ⏭️  No deals database found')
"
else
    echo "  ⏭️  CRM not set up"
fi

# 4. Check Fanvue renewals/churn
echo -e "\n💜 [4/6] Checking Fanvue subscribers..."
if [ -f crm/README.md ]; then
    python3 -c "
import json, sys, os
from datetime import datetime, timedelta

fans_file = 'crm/fanvue_subscribers.json'
if os.path.exists(fans_file):
    with open(fans_file) as f:
        fans = json.load(f)
    today = datetime.now().date()
    for fan in fans:
        if fan.get('Status') != 'Active':
            continue
        renewal = datetime.fromisoformat(fan.get('Renewal Date', '2099-12-31')).date()
        days = (renewal - today).days
        if days <= 3 and days >= 0:
            print(f'  🔄 RENEWAL: {fan[\"Username\"]} ({fan[\"Tier\"]}) in {days} day(s)')
        elif days < 0:
            print(f'  💔 CHURNED: {fan[\"Username\"]} (overdue by {abs(days)} days)')
else:
    print('  ⏭️  No Fanvue database found')
"
else
    echo "  ⏭️  CRM not set up"
fi

# 5. Check invoice status
echo -e "\n💰 [5/6] Checking invoices..."
if [ -f crm/README.md ]; then
    python3 -c "
import json, sys, os
from datetime import datetime, timedelta

deals_file = 'crm/deals.json'
if os.path.exists(deals_file):
    with open(deals_file) as f:
        deals = json.load(f)
    today = datetime.now().date()
    for deal in deals:
        if deal.get('Stage') == 'Invoiced' and not deal.get('Paid Date'):
            invoice_date = datetime.fromisoformat(deal.get('Invoice Date', '2099-12-31')).date()
            days = (today - invoice_date).days
            terms = deal.get('Payment Terms', 'Net-15')
            net_days = int(terms.replace('Net-', '')) if 'Net-' in terms else 15
            if days > net_days:
                overdue = days - net_days
                print(f'  🔴 OVERDUE: {deal[\"Deal Name\"]} — {overdue} days past {terms}')
            elif days == net_days:
                print(f'  🟡 DUE TODAY: {deal[\"Deal Name\"]} — {terms}')
            elif days >= net_days - 3:
                print(f'  ⏰ COMING DUE: {deal[\"Deal Name\"]} — {net_days - days} days')
else:
    print('  ⏭️  No deals database found')
"
else
    echo "  ⏭️  CRM not set up"
fi

# 6. Alert on thresholds
echo -e "\n🚨 [6/6] Checking alert thresholds..."
python3 -c "
import json, sys, os
from datetime import datetime, timedelta

# Check latest weekly rollup
weekly_dir = 'analytics/weekly'
if os.path.exists(weekly_dir):
    weeks = sorted([d for d in os.listdir(weekly_dir) if d.startswith('week_')])
    if weeks:
        latest = weeks[-1]
        with open(os.path.join(weekly_dir, latest, 'rollup.json')) as f:
            rollup = json.load(f)
        
        engagement = rollup.get('Avg Engagement Rate', 0)
        if engagement < 0.03:
            print(f'  🔴 CRITICAL: Engagement rate {engagement:.1%} < 3%')
        elif engagement < 0.04:
            print(f'  🟡 WARNING: Engagement rate {engagement:.1%} < 4%')
        
        growth = rollup.get('Total Followers Gained', 0)
        if growth < 100:
            print(f'  🟡 WARNING: Follower growth {growth} < 100/week')
        
        roi = rollup.get('ROI', 0)
        if roi < 1:
            print(f'  🔴 CRITICAL: ROI {roi:.2f}x < 1x')
        elif roi < 2:
            print(f'  🟡 WARNING: ROI {roi:.2f}x < 2x')
else:
    print('  ⏭️  No weekly rollups yet')
"

# 7. Backup
echo -e "\n💾 [7/7] Creating daily backup..."
BACKUP_DIR="$PROJECT_ROOT/backups/daily"
mkdir -p "$BACKUP_DIR"
BACKUP_FILE="$BACKUP_DIR/backup_$(date +%Y%m%d_%H%M%S).tar.gz"
tar -czf "$BACKUP_FILE" \
    --exclude='backups' \
    --exclude='node_modules' \
    --exclude='__pycache__' \
    --exclude='.git' \
    --exclude='assets/references/pose_library' \
    --exclude='assets/references/video_library' \
    . 2>/dev/null && echo "  ✅ Backup: $BACKUP_FILE" || echo "  ⚠️  Backup failed"

# Cleanup old backups (keep 30 days)
find "$BACKUP_DIR" -name "backup_*.tar.gz" -mtime +30 -delete 2>/dev/null

echo -e "\n========================================"
echo "✅ DAILY CRON COMPLETE — $(date '+%H:%M:%S')"
echo "========================================"