#!/usr/bin/env python3
"""
ZARA VELASQUEZ — SETUP SCRIPT
One-command environment initialization for the entire factory.
Run: bash setup.sh
"""

import os
import sys
import subprocess
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

def run_cmd(cmd, cwd=None, check=True):
    """Run command and return result"""
    print(f"  $ {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd or PROJECT_ROOT, capture_output=True, text=True)
    if result.stdout:
        print(f"    {result.stdout.strip()}")
    if result.stderr and check:
        print(f"    ERROR: {result.stderr.strip()}")
    return result

def check_command(cmd):
    """Check if command exists"""
    result = subprocess.run(f"which {cmd}", shell=True, capture_output=True)
    return result.returncode == 0

def main():
    print("🚀 ZARA VELASQUEZ FACTORY — SETUP")
    print("=" * 50)
    
    # 1. Check prerequisites
    print("\n📋 Checking prerequisites...")
    prereqs = ["python3", "git", "node", "npm"]
    missing = []
    for p in prereqs:
        if check_command(p):
            print(f"  ✅ {p}")
        else:
            print(f"  ❌ {p} - MISSING")
            missing.append(p)
    
    if missing:
        print(f"\n⚠️  Install missing: {', '.join(missing)}")
        if "python3" in missing:
            print("  Windows: winget install Python.Python.3.11")
        if "node" in missing:
            print("  Windows: winget install OpenJS.NodeJS")
        if "git" in missing:
            print("  Windows: winget install Git.Git")
        sys.exit(1)
    
    # 2. Python dependencies
    print("\n🐍 Installing Python dependencies...")
    requirements = [
        "notion-client",
        "requests",
        "python-dotenv",
        "fal-client",  # for Kling video
        "openai",      # for caption generation
        "anthropic",   # alternative
        "pandas",      # analytics
        "schedule",    # cron jobs
    ]
    
    for pkg in requirements:
        print(f"  Installing {pkg}...")
        result = run_cmd(f"pip install {pkg}", check=False)
        if result.returncode != 0:
            print(f"    ⚠️  Failed: {pkg} (may need manual install)")
    
    # 3. Node dependencies (for any build tools)
    print("\n📦 Checking Node dependencies...")
    package_json = PROJECT_ROOT / "package.json"
    if not package_json.exists():
        pkg = {
            "name": "zara-velasquez-factory",
            "version": "1.0.0",
            "private": True,
            "scripts": {
                "dev": "echo 'No dev server'",
                "build": "echo 'No build step'"
            },
            "devDependencies": {}
        }
        with open(package_json, "w") as f:
            json.dump(pkg, f, indent=2)
        print("  Created package.json")
    
    # 4. Environment file
    print("\n🔐 Setting up environment...")
    env_file = PROJECT_ROOT / ".env"
    env_example = PROJECT_ROOT / ".env.example"
    
    if not env_example.exists():
        env_content = """# ZARA VELASQUEZ FACTORY — ENVIRONMENT VARIABLES
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
"""
        with open(env_example, "w") as f:
            f.write(env_content)
        print("  Created .env.example")
    
    if not env_file.exists():
        import shutil
        shutil.copy(env_example, env_file)
        print("  Created .env from example — EDIT THIS FILE!")
    
    # 5. Git initialization
    print("\n📁 Initializing Git...")
    if not (PROJECT_ROOT / ".git").exists():
        run_cmd("git init")
        run_cmd("git add .gitignore 2>/dev/null || echo 'No .gitignore'")
        print("  Git initialized")
    else:
        print("  Git already initialized")
    
    # 6. Create .gitignore
    gitignore = PROJECT_ROOT / ".gitignore"
    if not gitignore.exists():
        ignore_content = """# Environment
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
"""
        with open(gitignore, "w") as f:
            f.write(ignore_content)
        print("  Created .gitignore")
    
    # 7. Verify directory structure
    print("\n📂 Verifying directory structure...")
    required_dirs = [
        "assets/identity",
        "assets/references/master_faces",
        "assets/references/pose_library",
        "assets/references/final_assets",
        "assets/references/video_library",
        "assets/references/video_sources",
        "prompts/scene_prompts",
        "prompts/caption_templates",
        "prompts/video_prompts",
        "pipeline",
        "monetization/digital_products",
        "analytics",
        "scripts",
        "contracts",
        "crm",
        "media_kit",
        "platform_checklists",
        "content_calendar",
        "brand_deals",
        "automation",
    ]
    
    for d in required_dirs:
        path = PROJECT_ROOT / d
        if path.exists():
            print(f"  ✅ {d}")
        else:
            path.mkdir(parents=True, exist_ok=True)
            print(f"  ➕ Created {d}")
    
    # 8. Make scripts executable
    print("\n🔧 Making scripts executable...")
    scripts = [
        "pipeline/generate_images.py",
        "pipeline/generate_video.py",
        "pipeline/batch_content.py",
    ]
    for script in scripts:
        path = PROJECT_ROOT / script
        if path.exists():
            os.chmod(path, 0o755)
            print(f"  ✅ {script}")
    
    # 9. Summary
    print("\n" + "=" * 50)
    print("✅ SETUP COMPLETE!")
    print("=" * 50)
    print("""
📋 NEXT STEPS:

1. EDIT .env FILE:
   nano .env
   # Fill in ALL API keys and tokens

2. CREATE NOTION DATABASES:
   - Go to notion.so
   - Create databases per analytics/dashboard.md
   - Copy database IDs to .env

3. GENERATE MASTER FACES:
   - Go to picovix.app/characters
   - Use master_prompt.txt prompts (15 angles)
   - Save to assets/references/master_faces/

4. RUN FIRST IMAGE BATCH:
   python pipeline/generate_images.py --week 1 --pillar ALL

5. RUN FIRST VIDEO BATCH:
   python pipeline/generate_video.py --week 1

6. RUN FIRST CONTENT BATCH:
   python pipeline/batch_content.py --week 1 --focus BALANCED

7. SET UP SCHEDULING:
   - Buffer.com (free) → Connect Instagram, TikTok, X, LinkedIn
   - Later.com (free) → Alternative
   - Import buffer_schedule.json from content_calendar/week_01/

8. LAUNCH FANVUE:
   - Follow monetization/fanvue_setup.md
   - Launch at 3K+ followers

📚 KEY FILES TO READ:
- CHARACTER_BIBLE.md (complete character spec)
- assets/identity/zara.json (machine-readable identity)
- pipeline/generate_images.py (image pipeline)
- pipeline/generate_video.py (video pipeline)
- pipeline/batch_content.py (content batching)
- monetization/fanvue_setup.md (monetization)
- contracts/ugc_contract.md (brand deals)
- media_kit/README.md (pitch deck)
- platform_checklists/README.md (pre-flight checks)
- content_calendar/weekly_template.md (weekly planning)
- analytics/dashboard.md (metrics tracking)

🎯 WEEK 1 GOAL:
- 15 master faces generated
- 30 pose variations prompted
- 5 Hedra scripts configured
- 10 Veo2 prompts ready
- Week 1 content calendar filled
- Buffer scheduled
- Fanvue account created

Good luck! 🚀
""")

if __name__ == "__main__":
    main()