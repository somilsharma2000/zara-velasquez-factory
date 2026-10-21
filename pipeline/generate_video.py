#!/usr/bin/env python3
"""
ZARA VELASQUEZ — VIDEO GENERATION PIPELINE
Generates Hedra lip-sync, Veo2 cinematic, Kling, and Colab face-swap videos.
Run: python generate_video.py --week 1 --type hedra
"""

import argparse
import json
import os
import sys
import subprocess
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

class ZaraVideoPipeline:
    def __init__(self):
        self.project_root = PROJECT_ROOT
        self.video_dir = self.project_root / "assets" / "references" / "video_library"
        self.video_dir.mkdir(parents=True, exist_ok=True)
        self.scripts = self.load_scripts()
    
    def load_scripts(self) -> Dict:
        """Load Hedra scripts from research-enhanced prompts (research_enhanced_prompts.md)"""
        return {
            "H01": {
                "name": "Founder Reality Check",
                "pillar": "FEEL",
                "duration": 60,
                "script": "[0-3s HOOK - Visual + Audio Sync + Native Text]\n\"Hot take: Nobody tells you the loneliness isn't the travel. It's the 3am Stripe decline.\"\n[TEXT OVERLAY: \"The loneliness isn't the travel 📉\"]\n\n[3-8s CONTEXT - Problem]\n\"Everyone sees the Lisbon content. The Bali reels. The 'dream life.'\"\n[TEXT: \"Everyone sees the highlight reel ✨\"]\n\n[8-15s VULNERABLE DETAIL - The Reality]\n\"They don't see the €147 in the business account. The rejected investor emails. The feature nobody used.\"\n[TEXT: \"€147 in Stripe. 3 rejected investors. 0 users on v1.\"]\n\n[15-25s PERSONAL STORY]\n\"Last month I almost quit. Really. Packed a bag. Looked at flights home to Medellín.\"\n[TEXT: \"Almost bought a one-way ticket home 🇨🇴\"]\n\n[25-35s TURNING POINT]\n\"Then a user emailed: 'Your tool saved my launch.' One email. Changed the trajectory.\"\n[TEXT: \"One email changed everything 📧\"]\n\n[35-50s LESSON - Raw, Not Toxic Positivity]\n\"Not saying it's magic. Still hard. Still scared. But *this* — the builder part — this I choose.\"\n[TEXT: \"Still scared. Still building. 🏗️\"]\n\n[50-60s CTA - Genuine Question]\n\"What's the thing you almost quit on? Real answers only.\"\n[TEXT: \"What almost made you quit? 👇\"]",
                "settings": {"voice": "Natural Female - Warm", "speed": 0.95, "emotion": "Contemplative"},
                "format": "Problem-Solution (TikTok/Reels optimized)",
                "text_overlays": True,
                "native_text": True
            },
            "H02": {
                "name": "Tool Tutorial Intro",
                "pillar": "LEARN",
                "duration": 45,
                "script": "[0-2s HOOK]\n\"Stop paying for Notion templates. I'll give you mine free. 🧵\"\n[TEXT: \"Free Notion template in bio 🔗\"]\n\n[2-8s VALUE DEMO]\n\"Spent 6 months building my founder workspace. Content cal, brand CRM, revenue tracker, sprint planner.\"\n[SCREEN RECORDING: Quick scroll through workspace]\n[TEXT: \"Content Cal | Brand CRM | Revenue Tracker | Sprint Planner\"]\n\n[8-18s SPECIFIC BENEFIT]\n\"Duplicates in 1 click. Customizes in 5 min. Saves me 10 hrs/week. No joke.\"\n[TEXT: \"1 click duplicate → 5 min customize → 10 hrs saved/week ⏰\"]\n\n[18-30s CTA + PROOF]\n\"Link in bio. Steal it. Break it. Make it yours. Tag me when you do — I check every one.\"\n[TEXT: \"Link in bio → Duplicate → Tag me @zaravelasquez\"]\n\n[30-40s AUTHORITY PROOF]\n\"Oh — and the revenue tracker? That's how I hit $1K MRR. Data > vibes.\"\n[TEXT: \"Revenue tracker = $1K MRR 📊\"]\n\n[40-45s ENGAGEMENT BAIT]\n\"What's the one template you wish existed? Building it next.\"\n[TEXT: \"What template should I build next? 👇\"]",
                "settings": {"voice": "Natural Female - Energetic", "speed": 1.0, "emotion": "Excited"},
                "format": "Steal This (TikTok/Reels optimized)",
                "text_overlays": True,
                "native_text": True
            },
            "H03": {
                "name": "Nomad Truth Bomb",
                "pillar": "LIVE",
                "duration": 50,
                "script": "[0-3s HOOK]\n\"Unpopular opinion: Digital nomad visa is the easy part. The hard part?\"\n[TEXT: \"Visa = easy. The rest? 😅\"]\n\n[3-10s REALITY CHECK]\n\"Timezone calls at 11pm. Friendships that fade. Dating apps in 3 languages.\"\n[TEXT: \"11pm calls 🌙 | Fading friendships 💔 | 3 dating apps 📱\"]\n\n[10-20s DEEPER REALITY]\n\"Tax residency rules written for 1950. Healthcare in a language you barely speak.\"\n[TEXT: \"1950 tax laws 📜 | Healthcare in Bahasa 🇮🇩\"]\n\n[20-30s THE TRUTH]\n\"The 'freedom' everyone sells? It's responsibility wearing a bikini.\"\n[TEXT: \"Freedom = Responsibility in a bikini 👙\"]\n\n[30-40s BALANCED TRUTH]\n\"But also: pastel de nata at 8am. Rice field sunsets. Code deploying from a villa.\"\n[TEXT: \"But also: Pastel de nata ☕ | Rice field sunsets 🌾 | Villa deploys 💻\"]\n\n[40-50s CTA]\n\"Worth it? Most days. Today? Ask me at 3am.\"\n[TEXT: \"Worth it? Ask me at 3am 🫠\"]",
                "settings": {"voice": "Natural Female - Conversational", "speed": 1.0, "emotion": "Thoughtful"},
                "format": "Anti-Glamour (TikTok/Reels optimized)",
                "text_overlays": True,
                "native_text": True
            },
            "H04": {
                "name": "Money Transparency",
                "pillar": "BUILD",
                "duration": 75,
                "script": "[0-3s HOOK]\n\"Month 6 revenue report. No fluff. Just numbers.\"\n[TEXT: \"Month 6 Revenue Report 📊 No fluff.\"]\n\n[3-12s REVENUE BREAKDOWN]\n\"SaaS MRR: $347. Affiliate: $203. UGC: $450. Fanvue: $0 (launching next month). Total: $1,000.\"\n[TEXT: \"SaaS: $347 | Affiliate: $203 | UGC: $450 | Fanvue: $0 | TOTAL: $1,000\"]\n\n[12-25s COSTS & NET]\n\"Costs: Tools $87. Contractor $500. Living $1,200. Travel $400. Net: -$183. Still negative.\"\n[TEXT: \"Tools: $87 | Contractor: $500 | Living: $1,200 | Travel: $400 | NET: -$183 📉\"]\n\n[25-40s RUNWAY REALITY]\n\"Runway: 2.3 months. Scary? Yes. Motivating? Also yes. Nothing focuses like a deadline.\"\n[TEXT: \"Runway: 2.3 months ⏳ Scary? Yes. Motivating? Yes.\"]\n\n[40-55s UGC PROOF]\n\"The $450 UGC? Two brand deals. 4 hours work. Same tools I use for my content.\"\n[TEXT: \"UGC = 2 deals, 4 hrs, same tools 🛠️\"]\n\n[55-65s NEXT TARGET]\n\"Next month target: $2K MRR. SaaS launch + Fanvue + 3 UGC deals. Math is mathing.\"\n[TEXT: \"Target: $2K MRR 🎯 SaaS + Fanvue + 3 UGC\"]\n\n[65-75s CTA]\n\"Your turn. What's your revenue reality? Anonymous replies welcome.\"\n[TEXT: \"Your revenue reality? Anonymous OK 👇\"]",
                "settings": {"voice": "Natural Female - Direct", "speed": 1.05, "emotion": "Confident"},
                "format": "Revenue Report (TikTok/Reels optimized)",
                "text_overlays": True,
                "native_text": True
            },
            "H05": {
                "name": "Abuela Wisdom",
                "pillar": "FEEL",
                "duration": 40,
                "script": "[0-3s HOOK]\n\"Abuela calls every Sunday. Same question: 'Mija, ¿cómo estás?'\"\n[TEXT: \"Abuela calls every Sunday 📞\"]\n\n[3-12s VULNERABLE MOMENT]\n\"Last week I said: 'Cansada, abuela. El negocio... es difícil.'\"\n[TEXT: \"'Cansada, abuela. El negocio es difícil.' 😔\"]\n\n[12-22s WISDOM]\n\"She paused. Said: 'Mi niña, los árboles no crecen apurados. Pero crecen.'\"\n[TEXT: \"'Los árboles no crecen apurados. Pero crecen.' 🌳\"]\n\n[22-32s TRANSLATION + MEANING]\n\"Trees don't grow rushed. But they grow. She's never used a computer. Knows more than my investors.\"\n[TEXT: \"Never used a computer. Knows more than my investors. 💛\"]\n\n[32-40s CTA + CULTURAL ANCHOR]\n\"Wearing her chain today. My compass. My anchor. What's yours?\"\n[TEXT: \"Wearing her chain. My compass. What's yours? 💛\"]",
                "settings": {"voice": "Natural Female - Warm", "speed": 0.9, "emotion": "Tender"},
                "format": "Cultural Anchor (TikTok/Reels optimized)",
                "text_overlays": True,
                "native_text": True
            }
        }
    
    def get_veo2_prompts(self) -> List[Dict]:
        """Veo 2 cinematic motion prompts (Research-Enhanced from visual_trends_2026.md + lifestyle_elements_2026.md)"""
        # Universal motion parameters (add to all)
        UNIVERSAL_MOTION = (
            ", subtle natural movement: hair in breeze, steam rising from matcha, pages turning, "
            "fingers typing, head tilt thinking, sip drink, glance at window, stretch, walk, "
            "ambient life: tram passing, gecko on wall, offering smoke, scooter passing, "
            "cinematic slow motion for hero moments, real-time for authentic moments, "
            "camera: handheld slight shake for POV, steady cam for environmental, "
            "lighting changes naturally: clouds passing, sun moving, golden hour shift, "
            "Analog Revival aesthetic, film grain maintained, Kodak Portra 400 texture, "
            "Earth Tone Warmth palette preserved, vertical-first 9:16 composition"
        )
        
        return [
            {"id": "V01", "name": "Cafe Work - Subtle Life", "pillar": "BUILD/LIVE", "duration": 5,
             "prompt": f"Starting frame: Zara at cafe table, laptop open, matcha beside her, window left, Notion revenue dashboard visible. {UNIVERSAL_MOTION}"},
            {"id": "V02", "name": "Lisbon Street - Walking", "pillar": "LIVE", "duration": 7,
             "prompt": f"Starting frame: Zara walking on Alfama cobblestones, leather tote, white Sambas, golden hour, Tram 28 approaching. {UNIVERSAL_MOTION}"},
            {"id": "V03", "name": "Morning Routine - Wake Up", "pillar": "LIVE/FEEL", "duration": 6,
             "prompt": f"Starting frame: Zara in bed, sheer curtains, morning light, journal on nightstand, matcha tin on nightstand. {UNIVERSAL_MOTION}"},
            {"id": "V04", "name": "Rooftop Sunset - Perspective", "pillar": "FEEL", "duration": 8,
             "prompt": f"Starting frame: Zara at Miradouro railing, Alfama rooftops behind, sunset, silhouette with rim light on hair. {UNIVERSAL_MOTION}"},
            {"id": "V05", "name": "Deep Work - Focus", "pillar": "BUILD", "duration": 5,
             "prompt": f"Starting frame: Zara at desk, typing, second monitor showing Linear board, plants, window right, matcha cooling. {UNIVERSAL_MOTION}"},
            {"id": "V06", "name": "Bali Rice Fields - Immersion", "pillar": "LIVE", "duration": 10,
             "prompt": f"Starting frame: Zara on path between rice terraces in Sidemen, coconut, bright tropical light, green layers. {UNIVERSAL_MOTION}"},
            {"id": "V07", "name": "Mirror OOTD - Raw", "pillar": "LIVE", "duration": 4,
             "prompt": f"Starting frame: Zara in bedroom mirror, iPhone raised, messy bed behind, cream cardigan, Levi's, Sambas. {UNIVERSAL_MOTION}"},
            {"id": "V08", "name": "Bookstore - Curiosity", "pillar": "LEARN", "duration": 6,
             "prompt": f"Starting frame: Zara browsing shelf at Ler Devagar, pulls book, opens, reads, finger traces line. {UNIVERSAL_MOTION}"},
            {"id": "V09", "name": "Airport - Transition", "pillar": "LIVE", "duration": 5,
             "prompt": f"Starting frame: Zara at Lisbon airport gate, laptop on knees, boarding pass on phone, runway view. {UNIVERSAL_MOTION}"},
            {"id": "V10", "name": "Evening Cozy - Wind Down", "pillar": "FEEL", "duration": 7,
             "prompt": f"Starting frame: Zara on sofa, lamp light, book, cooled matcha, messy bun, gold chain visible. {UNIVERSAL_MOTION}"}
        ]
    
    def get_kling_prompts(self) -> List[Dict]:
        """Kling 3.0/2.6 video prompts (Research-Enhanced)"""
        # Universal Kling parameters
        UNIVERSAL_KLING = (
            ", natural hand gestures, head tilts, eyebrow raises, natural blink rate, "
            "lip sync to audio, upper body movement, photorealistic, consistent identity, "
            "Analog Revival texture maintained, Kodak Portra 400 grain preserved, "
            "Earth Tone Warmth palette, vertical-first 9:16"
        )
        
        return [
            {"id": "K01", "name": "Talking Head with Gestures", "pillar": "ALL", "duration": 10,
             "prompt": f"Starting frame: Zara front-facing, seated at cafe, good window light, matcha visible. {UNIVERSAL_KLING}"},
            {"id": "K02", "name": "Laptop to Camera Transition", "pillar": "BUILD", "duration": 8,
             "prompt": f"Starting frame: Zara typing on laptop, profile view, three-quarter left, deep focus. {UNIVERSAL_KLING}"},
            {"id": "K03", "name": "Walking and Talking", "pillar": "LIVE", "duration": 12,
             "prompt": f"Starting frame: Zara walking on Alfama street toward camera, phone in hand, tote bag, Sambas. {UNIVERSAL_KLING}"},
            {"id": "K04", "name": "Coffee Ritual", "pillar": "LIVE/FEEL", "duration": 10,
             "prompt": f"Starting frame: Zara at kitchen counter, matcha whisk, ceramic bowl, oat milk, morning light. {UNIVERSAL_KLING}"},
            {"id": "K05", "name": "Packing Suitcase", "pillar": "LIVE", "duration": 15,
             "prompt": f"Starting frame: Zara beside open 35L carry-on, packing cubes on bed, organized. {UNIVERSAL_KLING}"}
        ]
    
    def get_colab_categories(self) -> List[Dict]:
        """Colab face swap source video categories (Research-Enhanced from lifestyle_elements_2026.md)"""
        return [
            {"category": "walking_lisbon", "search": "woman walking cobblestone street Lisbon vertical", "duration": "10-15s", "use_for": "Alfama commute, tram background", "visual_notes": "Cobblestones, yellow tram, hills"},
            {"category": "walking_bali", "search": "woman walking rice field path Bali vertical", "duration": "10-15s", "use_for": "Sidemen/Jatiluwih paths", "visual_notes": "Green terraces, narrow path"},
            {"category": "working_cafe", "search": "woman typing laptop cafe window light vertical", "duration": "8-12s", "use_for": "Deep work, coworking, hotel", "visual_notes": "Window side-light, matcha visible"},
            {"category": "pilates", "search": "woman pilates reformer vertical", "duration": "10-15s", "use_for": "Gym/wellness content", "visual_notes": "Reformer, sage activewear"},
            {"category": "coffee_ritual", "search": "woman making matcha ceramic bowl vertical", "duration": "8-10s", "use_for": "Morning ritual, matcha ceremony", "visual_notes": "Whisk, steam, ceramic"},
            {"category": "airport_transit", "search": "woman airport terminal laptop vertical", "duration": "10-15s", "use_for": "Visa runs, transitions", "visual_notes": "Boarding pass, runway view"},
            {"category": "reading_journal", "search": "woman reading book journaling vertical", "duration": "8-12s", "use_for": "LEARN pillar, evening wind-down", "visual_notes": "Cozy, lamp light"},
            {"category": "stretching", "search": "woman stretching morning yoga vertical", "duration": "8-10s", "use_for": "Reset content, body pillar", "visual_notes": "Natural light, flow"},
            {"category": "laughing_connection", "search": "woman laughing candid friends vertical", "duration": "5-8s", "use_for": "FEEL pillar, community", "visual_notes": "Genuine joy, connection"},
            {"category": "scooter_bali", "search": "woman scooter rice fields Bali POV vertical", "duration": "10-15s", "use_for": "Bali transport, commute", "visual_notes": "Helmet, green tunnel, POV"}
        ]
    
    def generate_hedra_batch(self, script_ids: List[str] = None) -> List[Dict]:
        """Generate Hedra video configurations"""
        if script_ids is None:
            script_ids = list(self.scripts.keys())
        
        results = []
        for sid in script_ids:
            script = self.scripts[sid]
            config = {
                "id": sid,
                "name": script["name"],
                "pillar": script["pillar"],
                "duration": script["duration"],
                "script": script["script"],
                "settings": script["settings"],
                "source_image": "assets/references/master_faces/zara_master_front.png",
                "output_path": f"assets/references/video_library/zara_hedra_{sid.lower()}_{datetime.now().strftime('%Y%m%d')}.mp4",
                "status": "config_ready",
                "hedra_url": "https://hedra.com",
                "credits_estimate": max(1, script["duration"] // 10)  # ~10s per credit
            }
            
            # Save config
            config_file = self.video_dir / f"hedra_{sid.lower()}_{datetime.now().strftime('%Y%m%d')}.json"
            with open(config_file, "w") as f:
                json.dump(config, f, indent=2)
            
            results.append(config)
            print(f"✅ Hedra config: {sid} - {script['name']} ({script['duration']}s)")
        
        return results
    
    def generate_veo2_batch(self, video_ids: List[str] = None) -> List[Dict]:
        """Generate Veo 2 video configurations"""
        all_videos = {v["id"]: v for v in self.get_veo2_prompts()}
        
        if video_ids is None:
            video_ids = list(all_videos.keys())
        
        results = []
        for vid in video_ids:
            video = all_videos[vid]
            config = {
                "id": vid,
                "name": video["name"],
                "pillar": video["pillar"],
                "duration": video["duration"],
                "prompt": video["prompt"],
                "source_image": f"assets/references/final_assets/zara_final_{vid.lower()}.png",  # Will map to actual final asset
                "output_path": f"assets/references/video_library/zara_veo2_{vid.lower()}_{datetime.now().strftime('%Y%m%d')}.mp4",
                "status": "config_ready",
                "platform": "Google AI Studio",
                "url": "https://aistudio.google.com",
                "daily_limit": 3,
                "generation_order": video_ids.index(vid) + 1
            }
            
            config_file = self.video_dir / f"veo2_{vid.lower()}_{datetime.now().strftime('%Y%m%d')}.json"
            with open(config_file, "w") as f:
                json.dump(config, f, indent=2)
            
            results.append(config)
            print(f"✅ Veo2 config: {vid} - {video['name']} ({video['duration']}s)")
        
        return results
    
    def generate_kling_batch(self, video_ids: List[str] = None) -> List[Dict]:
        """Generate Kling video configurations"""
        all_videos = {v["id"]: v for v in self.get_kling_prompts()}
        
        if video_ids is None:
            video_ids = list(all_videos.keys())
        
        results = []
        for vid in video_ids:
            video = all_videos[vid]
            config = {
                "id": vid,
                "name": video["name"],
                "pillar": video["pillar"],
                "duration": video["duration"],
                "prompt": video["prompt"],
                "source_image": f"assets/references/final_assets/zara_final_{vid.lower()}.png",
                "output_path": f"assets/references/video_library/zara_kling_{vid.lower()}_{datetime.now().strftime('%Y%m%d')}.mp4",
                "status": "config_ready",
                "platform": "Fal.ai / WritingMate",
                "model": "Kling 3.0",
                "api_required": True,
                "fal_key_needed": True
            }
            
            config_file = self.video_dir / f"kling_{vid.lower()}_{datetime.now().strftime('%Y%m%d')}.json"
            with open(config_file, "w") as f:
                json.dump(config, f, indent=2)
            
            results.append(config)
            print(f"✅ Kling config: {vid} - {video['name']} ({video['duration']}s)")
        
        return results
    
    def generate_colab_batch(self) -> List[Dict]:
        """Generate Colab face swap configurations"""
        categories = self.get_colab_categories()
        
        results = []
        for cat in categories:
            config = {
                "category": cat["category"],
                "search_terms": cat["search"],
                "target_duration": cat["duration"],
                "use_for": cat["use_for"],
                "source_video_path": f"assets/references/video_sources/{cat['category']}_source.mp4",
                "reference_face": "assets/references/master_faces/zara_master_front.png",
                "output_path": f"assets/references/video_library/zara_colab_{cat['category']}_{datetime.now().strftime('%Y%m%d')}.mp4",
                "status": "config_ready",
                "colab_notebook": "https://colab.research.google.com/github/deepinsight/insightface/blob/master/examples/face_swap_video.ipynb",
                "gpu": "T4 (free)",
                "estimated_time": "5-10 min"
            }
            
            config_file = self.video_dir / f"colab_{cat['category']}_{datetime.now().strftime('%Y%m%d')}.json"
            with open(config_file, "w") as f:
                json.dump(config, f, indent=2)
            
            results.append(config)
            print(f"✅ Colab config: {cat['category']} ({cat['duration']})")
        
        return results
    
    def create_colab_notebook(self) -> str:
        """Create a ready-to-run Colab notebook for face swapping"""
        notebook = {
            "nbformat": 4,
            "nbformat_minor": 0,
            "metadata": {
                "colab": {
                    "name": "Zara Velasquez Face Swap",
                    "provenance": [],
                    "authorship_tag": "ABX9TyMxz0q3"
                },
                "kernelspec": {
                    "name": "python3",
                    "display_name": "Python 3"
                },
                "language_info": {"name": "python"}
            },
            "cells": [
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "# Zara Velasquez — Video Face Swap Pipeline\n",
                        "\n",
                        "Run this notebook to swap Zara's face onto source videos using InsightFace.\n",
                        "\n",
                        "## Prerequisites\n",
                        "- Upload `zara_master_front.png` (512x512, aligned face)\n",
                        "- Upload source videos to `video_sources/`\n",
                        "- Enable GPU: Runtime → Change runtime type → T4 GPU\n",
                        "\n",
                        "## Usage\n",
                        "1. Run all cells in order\n",
                        "2. Check outputs in `video_library/`\n",
                        "3. Download results"
                    ]
                },
                {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        "!git clone https://github.com/deepinsight/insightface.git\n",
                        "%cd insightface\n",
                        "!pip install -r requirements.txt\n",
                        "!pip install onnxruntime-gpu\n"
                    ]
                },
                {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        "import cv2\n",
                        "import numpy as np\n",
                        "from insightface.app import FaceAnalysis\n",
                        "from insightface.model_zoo import get_model\n",
                        "import os\n",
                        "\n",
                        "# Initialize face analyzer\n",
                        "app = FaceAnalysis(name='buffalo_l')\n",
                        "app.prepare(ctx_id=0, det_size=(640, 640))\n",
                        "\n",
                        "# Load face swap model\n",
                        "swapper = get_model('inswapper_128.onnx', download=True)\n",
                        "\n",
                        "# Load reference face (Zara)\n",
                        "ref_img = cv2.imread('/content/zara_master_front.png')\n",
                        "ref_faces = app.get(ref_img)\n",
                        "ref_face = ref_faces[0]\n",
                        "\n",
                        "print(f'Reference face loaded: {ref_face.bbox}')"
                    ]
                },
                {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        "# Process each source video\n",
                        "import glob\n",
                        "\n",
                        "source_dir = '/content/video_sources'\n",
                        "output_dir = '/content/video_library'\n",
                        "os.makedirs(output_dir, exist_ok=True)\n",
                        "\n",
                        "video_files = glob.glob(os.path.join(source_dir, '*.mp4'))\n",
                        "\n",
                        "for video_path in video_files:\n",
                        "    filename = os.path.basename(video_path)\n",
                        "    output_path = os.path.join(output_dir, f'zara_swapped_{filename}')\n",
                        "    \n",
                        "    print(f'Processing: {filename}')\n",
                        "    \n",
                        "    cap = cv2.VideoCapture(video_path)\n",
                        "    fps = cap.get(cv2.CAP_PROP_FPS)\n",
                        "    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))\n",
                        "    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))\n",
                        "    \n",
                        "    fourcc = cv2.VideoWriter_fourcc(*'mp4v')\n",
                        "    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))\n",
                        "    \n",
                        "    frame_count = 0\n",
                        "    while True:\n",
                        "        ret, frame = cap.read()\n",
                        "        if not ret:\n",
                        "            break\n",
                        "        \n",
                        "        # Detect faces in frame\n",
                        "        faces = app.get(frame)\n",
                        "        \n",
                        "        if faces:\n",
                        "            # Swap first detected face\n",
                        "            frame = swapper.get(frame, faces[0], ref_face, paste_back=True)\n",
                        "        \n",
                        "        out.write(frame)\n",
                        "        frame_count += 1\n",
                        "        \n",
                        "        if frame_count % 30 == 0:\n",
                        "            print(f'  Processed {frame_count} frames...')\n",
                        "    \n",
                        "    cap.release()\n",
                        "    out.release()\n",
                        "    print(f'✅ Saved: {output_path} ({frame_count} frames)')"
                    ]
                },
                {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        "# Download results\n",
                        "from google.colab import files\n",
                        "import zipfile\n",
                        "\n",
                        "zip_path = '/content/zara_videos.zip'\n",
                        "with zipfile.ZipFile(zip_path, 'w') as zipf:\n",
                        "    for root, dirs, filenames in os.walk('/content/video_library'):\n",
                        "        for filename in filenames:\n",
                        "            filepath = os.path.join(root, filename)\n",
                        "            arcname = os.path.relpath(filepath, '/content/video_library')\n",
                        "            zipf.write(filepath, arcname)\n",
                        "\n",
                        "files.download(zip_path)\n",
                        "print('✅ All videos zipped and ready for download')"
                    ]
                }
            ]
        }
        
        notebook_path = self.video_dir / "zara_face_swap_colab.ipynb"
        with open(notebook_path, "w") as f:
            json.dump(notebook, f, indent=2)
        
        print(f"✅ Colab notebook created: {notebook_path}")
        return str(notebook_path)
    
    def run_weekly_video_batch(self, week: int, video_types: List[str] = None) -> Dict:
        """Run complete weekly video generation batch"""
        if video_types is None:
            video_types = ["hedra", "veo2", "kling", "colab"]
        
        print(f"\n🎬 WEEK {week} VIDEO BATCH")
        print("=" * 50)
        
        results = {}
        
        if "hedra" in video_types:
            print("\n🎭 Generating Hedra lip-sync configs...")
            results["hedra"] = self.generate_hedra_batch()
        
        if "veo2" in video_types:
            print("\n🎥 Generating Veo 2 cinematic configs...")
            results["veo2"] = self.generate_veo2_batch()
        
        if "kling" in video_types:
            print("\n🎞️ Generating Kling configs...")
            results["kling"] = self.generate_kling_batch()
        
        if "colab" in video_types:
            print("\n🔄 Generating Colab face-swap configs...")
            results["colab"] = self.generate_colab_batch()
            self.create_colab_notebook()
        
        # Summary
        total = sum(len(v) for v in results.values())
        print(f"\n✅ Total video configs: {total}")
        for vtype, vlist in results.items():
            print(f"   {vtype.upper()}: {len(vlist)}")
        
        # Save batch log
        log_file = self.video_dir / f"video_batch_log_week{week}_{datetime.now().strftime('%Y%m%d')}.json"
        with open(log_file, "w") as f:
            json.dump({
                "week": week,
                "timestamp": datetime.now().isoformat(),
                "results": {k: len(v) for k, v in results.items()},
                "details": results
            }, f, indent=2)
        
        print(f"\n📋 Batch log: {log_file}")
        print("\n📋 NEXT STEPS:")
        if "hedra" in results:
            print("1. HEDRA: Go to hedra.com → upload front face → paste scripts → generate")
        if "veo2" in results:
            print("2. VEO2: Go to aistudio.google.com → upload final assets → paste prompts → generate (3/day limit)")
        if "kling" in results:
            print("3. KLING: Use Fal.ai or WritingMate with Kling 3.0 → upload image + prompt")
        if "colab" in results:
            print("4. COLAB: Open notebook → upload source videos + reference face → run all cells → download")
        print("5. Post-process: color grade, burn captions, resize for platforms")
        print("6. Schedule in Buffer/Later")
        
        return {"week": week, "results": results, "log_file": str(log_file)}


def main():
    parser = argparse.ArgumentParser(description="Zara Velasquez Video Generation Pipeline")
    parser.add_argument("--week", type=int, default=1, help="Week number")
    parser.add_argument("--type", nargs="+", choices=["hedra", "veo2", "kling", "colab"], 
                       default=["hedra", "veo2", "kling", "colab"], help="Video types to generate")
    args = parser.parse_args()
    
    pipeline = ZaraVideoPipeline()
    result = pipeline.run_weekly_video_batch(args.week, args.type)
    
    print(f"\n✅ Video batch complete for Week {args.week}")


if __name__ == "__main__":
    main()