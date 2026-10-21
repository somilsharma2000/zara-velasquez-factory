#!/bin/bash
# ZARA VELASQUEZ FACTORY — SETUP SCRIPT
# Run: bash scripts/setup.sh
# One-command environment initialization

set -e  # Exit on error

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

echo "🚀 ZARA VELASQUEZ FACTORY — SETUP"
echo "=================================="

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

check_command() {
    if command -v "$1" &> /dev/null; then
        echo -e "  ${GREEN}✅${NC} $1"
        return 0
    else
        echo -e "  ${RED}❌${NC} $1 - MISSING"
        return 1
    fi
}

# 1. Check prerequisites
echo -e "\n📋 Checking prerequisites..."
MISSING=0
for cmd in python3 git node npm; do
    check_command "$cmd" || MISSING=1
done

if [ $MISSING -eq 1 ]; then
    echo -e "\n${YELLOW}⚠️  Install missing prerequisites:${NC}"
    echo "  Windows (winget):"
    echo "    winget install Python.Python.3.11"
    echo "    winget install OpenJS.NodeJS"
    echo "    winget install Git.Git"
    echo "  Mac (brew):"
    echo "    brew install python@3.11 node git"
    echo "  Linux (apt):"
    echo "    sudo apt update && sudo apt install python3 python3-pip nodejs npm git"
    exit 1
fi

# 2. Python dependencies
echo -e "\n🐍 Installing Python dependencies..."
pip3 install --quiet --upgrade pip
pip3 install --quiet \
    notion-client \
    requests \
    python-dotenv \
    fal-client \
    openai \
    anthropic \
    pandas \
    schedule \
    2>/dev/null || echo -e "  ${YELLOW}⚠️  Some packages may need manual install${NC}"

echo -e "  ${GREEN}✅${NC} Python packages installed"

# 3. Node setup
echo -e "\n📦 Setting up Node..."
if [ ! -f package.json ]; then
    cat > package.json << 'EOF'
{
  "name": "zara-velasquez-factory",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "echo 'No dev server configured'",
    "build": "echo 'No build step configured'"
  },
  "devDependencies": {}
}
EOF
    echo -e "  ${GREEN}✅${NC} Created package.json"
fi

# 4. Environment file
echo -e "\n🔐 Setting up environment..."
if [ ! -f .env.example ]; then
    cat > .env.example << 'EOF'
# ZARA VELASQUEZ FACTORY — ENVIRONMENT VARIABLES
# Copy to .env and fill in your values

# NOTION
NOTION_TOKEN=your_notion_integration_token
NOTION_DATABASE_CONTACTS=your_contacts_db_id
NOTION_DATABASE_DEALS=your_deals_db_id
NOTION_DATABASE_CONTENT=your_content_db_id
NOTION_DATABASE_FANVUE=your_fanvue_db_id
NOTION_DATABASE_AFFILIATE=your_affiliate_db_id
NOTION_DATABASE_METRICS=your_metrics_db_id

# SOCIAL PLATFORMS (for API access)
INSTAGRAM_ACCESS_TOKEN=your_ig_graph_api_token
TIKTOK_ACCESS_TOKEN=your_tiktok_business_token
YOUTUBE_API_KEY=your_youtube_data_api_key
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_SECRET=your_twitter_access_secret
LINKEDIN_ACCESS_TOKEN=your_linkedin_token

# FANVUE
FANVUE_API_KEY=your_fanvue_key

# CONVERTKIT
CONVERTKIT_API_KEY=your_convertkit_key
CONVERTKIT_FORM_ID=your_form_id

# AFFILIATE TRACKING
DUB_API_KEY=your_dub_co_key
DUB_DOMAIN=zara.velasquez.link

# VIDEO GENERATION
FAL_KEY=your_fal_ai_key
HEDRA_API_KEY=your_hedra_key

# AI SERVICES
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key

# STRIPE (invoicing)
STRIPE_SECRET_KEY=your_stripe_secret
STRIPE_WEBHOOK_SECRET=your_webhook_secret

# MAKE.COM / ZAPIER
MAKE_WEBHOOK_URL=your_make_webhook_url

# TIMEZONE
TZ=Europe/Lisbon
EOF
    echo -e "  ${GREEN}✅${NC} Created .env.example"
fi

if [ ! -f .env ]; then
    cp .env.example .env
    echo -e "  ${GREEN}✅${NC} Created .env from example — EDIT THIS FILE!"
fi

# 5. Git initialization
echo -e "\n📁 Initializing Git..."
if [ ! -d .git ]; then
    git init -q
    echo -e "  ${GREEN}✅${NC} Git initialized"
else
    echo -e "  ${GREEN}✅${NC} Git already initialized"
fi

# 6. Create .gitignore
if [ ! -f .gitignore ]; then
    cat > .gitignore << 'EOF'
# Environment
.env
.env.local
.env.*.local

# Python
__pycache__/
*.py[cod]
*$py.class
.pytest_cache/
.coverage
htmlcov/
.venv/
venv/
env/

# Node
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Assets (large files - use Git LFS or external storage)
assets/references/master_faces/
assets/references/pose_library/
assets/references/final_assets/
assets/references/video_library/
assets/references/video_sources/

# Logs
*.log
logs/

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo

# Temporary
tmp/
temp/
*.tmp

# Notion exports (contains data)
notion_exports/

# Analytics exports
analytics_exports/
EOF
    echo -e "  ${GREEN}✅${NC} Created .gitignore"
fi

# 7. Verify directory structure
echo -e "\n📂 Verifying directory structure..."
DIRS=(
    "assets/identity"
    "assets/references/master_faces"
    "assets/references/pose_library"
    "assets/references/final_assets"
    "assets/references/video_library"
    "assets/references/video_sources"
    "prompts/scene_prompts"
    "prompts/caption_templates"
    "prompts/video_prompts"
    "pipeline"
    "monetization/digital_products"
    "analytics"
    "scripts"
    "contracts"
    "crm"
    "media_kit"
    "platform_checklists"
    "content_calendar"
    "brand_deals"
    "automation"
)

for dir in "${DIRS[@]}"; do
    if [ -d "$dir" ]; then
        echo -e "  ${GREEN}✅${NC} $dir"
    else
        mkdir -p "$dir"
        echo -e "  ${GREEN}➕${NC} Created $dir"
    fi
done

# 8. Make Python scripts executable
echo -e "\n🔧 Making scripts executable..."
SCRIPTS=(
    "pipeline/generate_images.py"
    "pipeline/generate_video.py"
    "pipeline/batch_content.py"
    "scripts/setup.py"
)
for script in "${SCRIPTS[@]}"; do
    if [ -f "$script" ]; then
        chmod +x "$script"
        echo -e "  ${GREEN}✅${NC} $script"
    fi
done

# 9. Create bash wrapper for python scripts
echo -e "\n🔗 Creating command aliases..."
cat > zara << 'EOF'
#!/bin/bash
# Zara Velasquez Factory CLI
# Usage: ./zara <command> [args]

cd "$(dirname "$0")"

case "$1" in
    images)
        shift
        python3 pipeline/generate_images.py "$@"
        ;;
    video)
        shift
        python3 pipeline/generate_video.py "$@"
        ;;
    batch)
        shift
        python3 pipeline/batch_content.py "$@"
        ;;
    setup)
        python3 scripts/setup.py "$@"
        ;;
    *)
        echo "Zara Velasquez Factory CLI"
        echo "Usage: ./zara <command> [args]"
        echo ""
        echo "Commands:"
        echo "  images  -- Generate image prompts (week, pillar, variations)"
        echo "  video   -- Generate video configs (week, type)"
        echo "  batch   -- Generate weekly content batch (week, focus)"
        echo "  setup   -- Run setup"
        echo ""
        echo "Examples:"
        echo "  ./zara images --week 1 --pillar ALL"
        echo "  ./zara video --week 1 --type hedra veo2"
        echo "  ./zara batch --week 1 --focus BALANCED"
        ;;
esac
EOF
chmod +x zara
echo -e "  ${GREEN}✅${NC} Created ./zara CLI wrapper"

# 10. Final summary
echo -e "\n${GREEN}=================================="
echo -e "✅ SETUP COMPLETE!"
echo -e "==================================${NC}"
echo ""
echo -e "${YELLOW}📋 NEXT STEPS:${NC}"
echo ""
echo "1. EDIT .env FILE:"
echo "   nano .env"
echo "   # Fill in ALL API keys and tokens"
echo ""
echo "2. CREATE NOTION DATABASES:"
echo "   - Go to notion.so"
echo "   - Create databases per analytics/dashboard.md"
echo "   - Copy database IDs to .env"
echo ""
echo "3. GENERATE MASTER FACES:"
echo "   - Go to picovix.app/characters"
echo "   - Use prompts from prompts/master_prompt.txt (15 angles)"
echo "   - Save to assets/references/master_faces/"
echo ""
echo "4. RUN FIRST IMAGE BATCH:"
echo "   ./zara images --week 1 --pillar ALL"
echo ""
echo "5. RUN FIRST VIDEO BATCH:"
echo "   ./zara video --week 1"
echo ""
echo "6. RUN FIRST CONTENT BATCH:"
echo "   ./zara batch --week 1 --focus BALANCED"
echo ""
echo "7. SET UP SCHEDULING:"
echo "   - Buffer.com (free) → Connect Instagram, TikTok, X, LinkedIn"
echo "   - Later.com (free) → Alternative"
echo "   - Import buffer_schedule.json from content_calendar/week_01/"
echo ""
echo "8. LAUNCH FANVUE:"
echo "   - Follow monetization/fanvue_setup.md"
echo "   - Launch at 3K+ followers"
echo ""
echo -e "${YELLOW}📚 KEY FILES TO READ:${NC}"
echo "  CHARACTER_BIBLE.md          # Complete character spec"
echo "  assets/identity/zara.json   # Machine-readable identity"
echo "  pipeline/generate_images.py # Image pipeline"
echo "  pipeline/generate_video.py  # Video pipeline"
echo "  pipeline/batch_content.py   # Content batching"
echo "  monetization/fanvue_setup.md # Monetization"
echo "  contracts/ugc_contract.md   # Brand deals"
echo "  media_kit/README.md         # Pitch deck"
echo "  platform_checklists/README.md # Pre-flight checks"
echo "  content_calendar/weekly_template.md # Weekly planning"
echo "  analytics/dashboard.md      # Metrics tracking"
echo ""
echo -e "${YELLOW}🎯 WEEK 1 GOAL:${NC}"
echo "  • 15 master faces generated (Picovix)"
echo "  • 30 pose variations prompted (Leonardo)"
echo "  • 5 Hedra scripts configured"
echo "  • 10 Veo2 prompts ready"
echo "  • Week 1 content calendar filled"
echo "  • Buffer scheduled"
echo "  • Fanvue account created"
echo ""
echo -e "${GREEN}Good luck! 🚀${NC}"