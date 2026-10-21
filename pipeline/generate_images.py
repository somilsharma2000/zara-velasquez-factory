#!/usr/bin/env python3
"""
ZARA VELASQUEZ — IMAGE GENERATION PIPELINE
Batch generates pose variations via Leonardo AI, then face-swaps via InsightFace Discord bot.
Run: python generate_images.py --week 1 --pillar BUILD
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

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

class ZaraImagePipeline:
    def __init__(self):
        self.project_root = PROJECT_ROOT
        self.identity = self.load_identity()
        self.scene_prompts = self.load_scene_prompts()
        self.output_dir = self.project_root / "assets" / "references"
        self.master_faces = self.output_dir / "master_faces"
        self.pose_library = self.output_dir / "pose_library"
        self.final_assets = self.output_dir / "final_assets"
        
        # Ensure directories exist
        for d in [self.master_faces, self.pose_library, self.final_assets]:
            d.mkdir(parents=True, exist_ok=True)
    
    def load_identity(self) -> Dict:
        with open(self.project_root / "assets" / "identity" / "zara.json") as f:
            return json.load(f)
    
    def load_scene_prompts(self) -> Dict:
        """13 Research-validated scenes from lifestyle_elements_2026.md"""
        return {
            "cafe_work": {
                "location": "Comobá Lisbon - specialty cafe, corner table by large window",
                "background": "Exposed brick, plants on shelves, other remote workers blurred, chalkboard menu, matcha latte ceramic",
                "lighting": "Natural window side-light, 10am, soft shadows",
                "pose": "seated, holding_matcha, on_laptop, three_quarter_left, down_at_work",
                "outfit": "OVERSIZED_CREAM_CARDIGAN_VINTAGE_LEVIS",
                "aspect": "4:5",
                "pillar": "BUILD",
                "color_grade": "GOLDEN_HOUR_GLOW",
                "hook": "Hot take: Your morning coffee order says more about your business than your pitch deck."
            },
            "gym_pilates": {
                "location": "WIP Lisbon or local pilates studio, reformer visible",
                "background": "Clean white walls, natural wood floors, soft morning light",
                "lighting": "Natural window light, overcast day, even",
                "pose": "reformer_exercise, on_reformer_straps, three_quarter_right, candid_away",
                "outfit": "PILATES_SET_SAGE",
                "aspect": "9:16",
                "pillar": "LIVE",
                "color_grade": "EARTH_TONE_WARMTH",
                "hook": "Unpopular opinion: Pilates 3x/week built my business more than any productivity course."
            },
            "rooftop_sunset": {
                "location": "Miradouro de Santa Catarina Lisbon",
                "background": "Alfama rooftops, Tagus river, 25 de Abril bridge, sunset sky, silhouettes",
                "lighting": "Golden hour, backlit, rim light on hair, warm gradients",
                "pose": "standing, on_rail, three_quarter_left, candid_away",
                "outfit": "TRAVEL_OUTFIT_LINEN",
                "aspect": "16:9",
                "pillar": "LIVE",
                "color_grade": "CINEMATIC_OUTDOOR",
                "hook": "POV: You're 24, built a SaaS from €3K, watching the sun set over a city that isn't yours."
            },
            "bedroom_morning": {
                "location": "Alfama apartment bedroom, unmade bed, window with sheer curtains",
                "background": "Nightstand with journal/vitamins, clothes chair, plant, camera shelf, matcha tin",
                "lighting": "Soft morning window light, sheer curtain diffusion",
                "pose": "seated_on_bed, holding_matcha, front, direct_genuine",
                "outfit": "HOME_WEAR_OVERSIZED_TEE",
                "aspect": "4:5",
                "pillar": "LIVE",
                "color_grade": "GOLDEN_HOUR_GLOW",
                "hook": "The honest truth: 5:30am isn't aesthetic. It's the only time nobody needs anything from me."
            },
            "coworking_deepwork": {
                "location": "WIP Lisbon coworking, dedicated desk, dual monitor",
                "background": "Other founders working, whiteboard, plants, glass walls, Linear board visible",
                "lighting": "Mixed: overhead cool + window warm, balanced",
                "pose": "seated_at_desk, on_keyboard, three_quarter_right, down_at_work",
                "outfit": "OVERSIZED_CREAM_CARDIGAN_VINTAGE_LEVIS",
                "aspect": "4:5",
                "pillar": "BUILD",
                "color_grade": "HYPERREAL_MUNDANE",
                "hook": "Nobody talks about the 47 commits before the first user. The Stripe declines. The 3am bugs."
            },
            "bali_rice_fields": {
                "location": "Sidemen Bali rice field path / Canggu villa veranda",
                "background": "Green terraced rice fields, jungle, bright tropical sky, coconut",
                "lighting": "Bright midday tropical, managed shadows, golden hour option",
                "pose": "walking, holding_coconut, back_view, candid_away",
                "outfit": "SILK_SLIP_DRESS_TERRACOTTA",
                "aspect": "16:9",
                "pillar": "LIVE",
                "color_grade": "CINEMATIC_OUTDOOR",
                "hook": "Real talk: Bali isn't paradise 24/7. It's humidity, scooter crashes, visa runs. But also this."
            },
            "mirror_ootd": {
                "location": "Bedroom mirror, full length, messy bed visible",
                "background": "Messy bed, clothes rack with shawl, morning window light",
                "lighting": "Natural window + bathroom warm, mixed",
                "pose": "mirror_selfie, holding_phone, mirror, at_phone",
                "outfit": "OVERSIZED_CREAM_CARDIGAN_VINTAGE_LEVIS",
                "aspect": "4:5",
                "pillar": "LIVE",
                "color_grade": "GOLDEN_HOUR_GLOW",
                "hook": "OOTD: Same cream cardigan, 4th day this week. Real people repeat outfits."
            },
            "street_lisbon": {
                "location": "Alfama cobblestone streets, yellow Tram 28, azulejo facades",
                "background": "Iconic Lisbon architecture, locals, tourists, pastelaria queue, hills",
                "lighting": "Bright midday, golden hour on colored tiles",
                "pose": "walking, holding_pastel_nata, candid_walking, candid_away",
                "outfit": "TRAVEL_OUTFIT_LINEN",
                "aspect": "9:16",
                "pillar": "LIVE",
                "color_grade": "CINEMATIC_OUTDOOR",
                "hook": "3 places tourists never find in Lisbon. The pastelaria where locals queue."
            },
            "bookstore_reading": {
                "location": "Ler Devagar Lisbon, independent bookstore with cafe",
                "background": "Floor-to-ceiling books, reading lamps, other readers, coffee",
                "lighting": "Warm ambient + natural window, intimate",
                "pose": "seated_reading, holding_book, profile_left, down_at_book",
                "outfit": "LINEN_SHIRT_SHORTS",
                "aspect": "4:5",
                "pillar": "LEARN",
                "color_grade": "HYPERREAL_MUNDANE",
                "hook": "Currently reading: [Book]. The page that changed how I think about [topic]."
            },
            "autumn_park": {
                "location": "Jardim da Estrela Lisbon, autumn colors",
                "background": "Golden leaves, fallen foliage, trees, bench, path",
                "lighting": "Soft overcast, golden hour through leaves",
                "pose": "walking_path, holding_coffee, candid_joy",
                "outfit": "COAT_SCARF_TRENCH",
                "aspect": "4:5",
                "pillar": "LIVE",
                "color_grade": "EARTH_TONE_WARMTH",
                "hook": "Seasons change. So do metrics. So do I. The only constant: showing up."
            },
            "hotel_morning": {
                "location": "Boutique hotel Lisbon/Bali, window view, half-unpacked",
                "background": "Unmade bed, suitcase, city/sea view, desk, morning light",
                "lighting": "Morning window light, sheer curtains",
                "pose": "seated_by_window, holding_coffee, three_quarter_left, off_camera",
                "outfit": "HOME_WEAR_SILK_SLIP",
                "aspect": "4:5",
                "pillar": "LIVE",
                "color_grade": "GOLDEN_HOUR_GLOW",
                "hook": "Work from anywhere = work from everywhere. Including the bed at 7am before wifi connects."
            },
            "studio_hero": {
                "location": "Clean studio, seamless cream paper backdrop",
                "background": "Cream seamless, minimal, professional beauty lighting",
                "lighting": "Key + fill + rim, controlled, motivated practicals",
                "pose": "seated_stool, on_knee, front, direct_piercing",
                "outfit": "OVERSIZED_CREAM_CARDIGAN_VINTAGE_LEVIS",
                "aspect": "3:4",
                "pillar": "ALL",
                "color_grade": "CINEMATIC_ANAMORPHIC",
                "hook": "This is me. Builder. Nomad. Granddaughter. Friend. Still figuring it out."
            }
        }
    
    # Physical locked specs (from zara.json + research)
    PHYSICAL_LOCKED = {
        "face_shape": "heart-shaped, high cheekbones, soft jawline",
        "skin": "warm olive, visible pores, faint nose freckles",
        "eyes": "dark brown, almond, long lashes",
        "brows": "thick, natural, slightly asymmetric (left higher)",
        "nose": "straight, small bridge bump, delicate tip",
        "lips": "full, natural cupid's bow, tinted balm",
        "distinguishing_marks": ["beauty mark left of mouth", "acne scar right cheek"],
        "hair": "dark espresso with caramel balayage, mid-back, lived-in waves, curtain bangs",
        "build": "athletic-soft, 5'5\", pilates tone",
        "tattoos": ["compass coordinates right ribs", "wave left wrist", "sun behind left ear"]
    }
    
    # Research-enhanced universal prompt suffix
    RESEARCH_SUFFIX = (
        ", lifestyle photography, candid editorial, coastal grandmother meets digital nomad, "
        "lived-in not staged, imperfect beauty, asymmetry, natural texture, visible pores, "
        "film grain, Kodak Portra 400 color science, warm afternoon light, window side-light, "
        "golden hour glow, off-center composition, rule of thirds vertical, negative space for text overlay, "
        "handmade aesthetic, props that tell story: laptop + matcha + journal + gold herringbone chain + white Sambas, "
        "environmental storytelling: Lisbon cobblestones / Bali rice fields / cafe terrace, "
        "Analog Revival aesthetic, Earth Tone Warmth palette: cream sand sage terracotta navy charcoal white"
    )
    
    NEGATIVE_PROMPT = (
        "smooth skin, airbrushed, porcelain skin, doll-like, mannequin, perfect symmetry, "
        "centered composition, studio lighting, ring light, overexposed, flat lighting, "
        "no grain, no texture, plastic, artificial, hyper-polished, AI-generated look, "
        "flawless skin, symmetric face, generic influencer, staged, posed, "
        "minimalist beige, cold corporate blue, oversaturated, cartoon, illustration, "
        "3d render, cgi, fake, watermark, text, signature, logo, username, border, frame"
    )
    
    def build_leonardo_prompt(self, scene_key: str, variation: int = 1) -> Dict:
        """Build research-enhanced Leonardo AI prompt"""
        scene = self.scene_prompts[scene_key]
        phys = self.PHYSICAL_LOCKED
        
        # Physical description (LOCKED)
        physical_desc = (
            f"Zara Velasquez, 24, Colombian-Spanish mestiza, "
            f"{phys['face_shape']}, "
            f"{phys['skin']}, "
            f"{phys['eyes']}, "
            f"{phys['brows']}, "
            f"{phys['nose']}, "
            f"{phys['lips']}, "
            f"{', '.join(phys['distinguishing_marks'])}, "
            f"{phys['hair']}, "
            f"{phys['build']}, "
            f"tattoos: {', '.join(phys['tattoos'])}"
        )
        
        # Scene-specific with research enhancements
        scene_desc = (
            f"{scene['pose']}, "
            f"{scene['lighting']}, "
            f"wearing {scene['outfit'].lower().replace('_', ' ')}, "
            f"gold herringbone chain, "
            f"white Sambas when feet visible, "
            f"coastal grandmother x digital nomad aesthetic, lived-in not staged, "
            f"colors: cream, sand, sage, terracotta, navy, charcoal, white, "
            f"{scene['color_grade']} color grade, "
            f"Analog Revival aesthetic, Earth Tone Warmth palette"
        )
        
        # Camera specs
        camera_desc = (
            f"iPhone 15 Pro / Sony A7R IV, "
            f"vertical-first 9:16 composition, rule of thirds vertical, "
            f"negative space top/bottom for text overlay, "
            f"raw editorial candid style, imperfect skin, visible texture, "
            f"film grain, Kodak Portra 400 color science, "
            f"coarse grain in midtones, visible grain in shadows"
        )
        
        prompt = f"{physical_desc}, {scene_desc}, {camera_desc}{self.RESEARCH_SUFFIX}"
        
        # Aspect ratio dimensions
        aspect_dims = {
            "3:4": (768, 1024),
            "4:5": (768, 960),
            "9:16": (576, 1024),
            "16:9": (1024, 576),
            "1:1": (768, 768)
        }
        w, h = aspect_dims.get(scene["aspect"], (768, 1024))
        
        return {
            "prompt": prompt,
            "negative_prompt": self.NEGATIVE_PROMPT,
            "aspect_ratio": scene["aspect"],
            "model": "PhotoReal v2",
            "width": w,
            "height": h,
            "guidance_scale": 7,
            "num_inference_steps": 30,
            "seed": self.get_seed(scene_key, variation),
            "metadata": {
                "scene": scene_key,
                "pillar": scene["pillar"],
                "variation": variation,
                "hook": scene["hook"],
                "color_grade": scene["color_grade"],
                "location": scene["location"]
            }
        }
    
    def get_width(self, aspect: str) -> int:
        ratios = {"3:4": 768, "4:5": 768, "9:16": 576, "16:9": 1024, "1:1": 768}
        return ratios.get(aspect, 768)
    
    def get_height(self, aspect: str) -> int:
        ratios = {"3:4": 1024, "4:5": 960, "9:16": 1024, "16:9": 576, "1:1": 768}
        return ratios.get(aspect, 1024)
    
    def get_seed(self, scene_key: str, variation: int) -> int:
        """Deterministic seeds per scene + variation"""
        base_seeds = {
            "cafe_work": 1001,
            "gym_pilates": 2001,
            "rooftop_sunset": 3001,
            "bedroom_morning": 4001,
            "coworking_deepwork": 5001,
            "bali_rice_fields": 6001,
            "mirror_ootd": 7001,
            "street_lisbon": 8001,
            "bookstore_reading": 9001,
            "studio_hero": 9999
        }
        return base_seeds.get(scene_key, 1000) + variation
    
    def generate_leonardo_batch(self, scenes: List[str], variations: int = 3) -> List[Dict]:
        """Generate Leonardo AI prompts for batch (manual execution or API)"""
        results = []
        for scene in scenes:
            for v in range(1, variations + 1):
                prompt_data = self.build_leonardo_prompt(scene, v)
                filename = f"zara_leonardo_{scene}_v{v}_{datetime.now().strftime('%Y%m%d')}.json"
                filepath = self.pose_library / filename
                
                with open(filepath, "w") as f:
                    json.dump(prompt_data, f, indent=2)
                
                results.append({
                    "scene": scene,
                    "variation": v,
                    "prompt_file": str(filepath),
                    "status": "prompt_ready"
                })
                print(f"✅ Prompt ready: {filename}")
        
        return results
    
    def create_insightface_commands(self, pose_files: List[str]) -> List[str]:
        """Generate Discord InsightFace bot commands for face swapping"""
        commands = []
        
        # Master reference IDs (must be created first in Discord)
        master_ids = {
            "front": "zara_front",
            "three_quarter": "zara_3q",
            "profile": "zara_profile"
        }
        
        for pose_file in pose_files:
            # Determine which master ID to use based on pose orientation
            # This would need manual mapping or pose detection
            scene_name = pose_file.split("_")[2] if len(pose_file.split("_")) > 2 else "unknown"
            
            # Default to front, but map known scenes
            orientation_map = {
                "cafe_work": "three_quarter",
                "gym_pilates": "three_quarter",
                "rooftop_sunset": "three_quarter",
                "bedroom_morning": "front",
                "coworking_deepwork": "three_quarter",
                "bali_rice_fields": "profile",
                "mirror_ootd": "front",
                "street_lisbon": "three_quarter",
                "bookstore_reading": "profile",
                "studio_hero": "front"
            }
            
            master_id = master_ids.get(orientation_map.get(scene_name, "front"), "zara_front")
            output_name = pose_file.replace("leonardo", "final").replace(".json", ".png")
            
            cmd = f"/swapid {master_id} {pose_file} → {output_name}"
            commands.append(cmd)
        
        return commands
    
    def run_weekly_batch(self, week: int, pillar: str = "ALL") -> Dict:
        """Run complete weekly image generation batch"""
        print(f"\n🎬 WEEK {week} IMAGE BATCH — PILLAR: {pillar}")
        print("=" * 50)
        
        # Select scenes based on pillar
        pillar_scenes = {
            "BUILD": ["cafe_work", "coworking_deepwork", "studio_hero"],
            "LIVE": ["bedroom_morning", "rooftop_sunset", "street_lisbon", "bali_rice_fields", "mirror_ootd"],
            "LEARN": ["bookstore_reading", "cafe_work", "gym_pilates"],
            "FEEL": ["bedroom_morning", "rooftop_sunset"],
            "ALL": list(self.scene_prompts.keys())
        }
        
        scenes = pillar_scenes.get(pillar.upper(), pillar_scenes["ALL"])
        print(f"📸 Scenes: {', '.join(scenes)}")
        
        # Generate Leonardo prompts
        print("\n📝 Generating Leonardo AI prompts...")
        leonardo_results = self.generate_leonardo_batch(scenes, variations=3)
        
        # Create InsightFace commands
        print("\n🔄 Creating InsightFace swap commands...")
        pose_files = [r["prompt_file"] for r in leonardo_results]
        # Note: Actual pose images would be downloaded from Leonardo first
        # This creates the command list for manual Discord execution
        
        commands = self.create_insightface_commands([Path(f).name for f in pose_files])
        
        # Save command batch
        cmd_file = self.output_dir / f"insightface_commands_week{week}_{datetime.now().strftime('%Y%m%d')}.txt"
        with open(cmd_file, "w") as f:
            f.write("# INSIGHTFACE DISCORD COMMANDS\n")
            f.write(f"# Week {week} | {datetime.now().isoformat()}\n")
            f.write("# Run in InsightFace Discord: /saveid first, then /swapid\n\n")
            f.write("# MASTER IDs (create once):\n")
            f.write("/saveid zara_front → upload master_faces/zara_master_front.png\n")
            f.write("/saveid zara_3q → upload master_faces/zara_master_3q_left.png\n")
            f.write("/saveid zara_profile → upload master_faces/zara_master_profile_left.png\n\n")
            f.write("# SWAP COMMANDS:\n")
            for cmd in commands:
                f.write(f"{cmd}\n")
        
        print(f"\n✅ Commands saved: {cmd_file}")
        print(f"📋 Total prompts: {len(leonardo_results)}")
        print(f"🔄 Total swaps: {len(commands)}")
        
        return {
            "week": week,
            "pillar": pillar,
            "leonardo_prompts": len(leonardo_results),
            "insightface_swaps": len(commands),
            "command_file": str(cmd_file),
            "status": "prompts_ready"
        }


def main():
    parser = argparse.ArgumentParser(description="Zara Velasquez Image Generation Pipeline")
    parser.add_argument("--week", type=int, default=1, help="Week number")
    parser.add_argument("--pillar", type=str, default="ALL", choices=["BUILD", "LIVE", "LEARN", "FEEL", "ALL"])
    parser.add_argument("--variations", type=int, default=3, help="Variations per scene")
    parser.add_argument("--execute", action="store_true", help="Actually call APIs (not implemented)")
    args = parser.parse_args()
    
    pipeline = ZaraImagePipeline()
    result = pipeline.run_weekly_batch(args.week, args.pillar)
    
    # Save batch log
    log_file = PROJECT_ROOT / "assets" / "references" / f"batch_log_week{args.week}_{datetime.now().strftime('%Y%m%d')}.json"
    with open(log_file, "w") as f:
        json.dump(result, f, indent=2)
    
    print(f"\n📋 Batch log: {log_file}")
    print("\n📋 NEXT STEPS:")
    print("1. Copy prompts from pose_library/ to Leonardo AI")
    print("2. Download generated images to pose_library/")
    print(f"3. Run InsightFace commands from: {result['command_file']}")
    print("4. Curate best results → final_assets/")
    print("5. Update content_calendar/week_{week}.md with selected assets")


if __name__ == "__main__":
    main()