import json
from pathlib import Path
from random import random, choice
from datetime import datetime

GENES_PATH = Path("logs/loop_genes.json")
SURVIVORS_PATH = Path("logs/loop_survivors_species.json")

def simulate_species_competition(rounds=5):
    if not GENES_PATH.exists():
        print("❌ 유전자 정보 없음")
        return

    genes = json.load(open(GENES_PATH, encoding="utf-8"))
    loops = list(genes.keys())
    species_pool = {loop: {"score": 1.0} for loop in loops}

    for round_num in range(rounds):
        for loop in loops:
            trait = genes.get(loop, {})
            stability = trait.get("stability", 0.5)
            aggression = trait.get("aggressiveness", 0.5)
            chance = stability * 0.5 + (1 - aggression) * 0.5
            survival = random() < chance
            species_pool[loop]["score"] += 1 if survival else -1

    survivors = [loop for loop, v in species_pool.items() if v["score"] > 0]

    with open(SURVIVORS_PATH, "w", encoding="utf-8") as f:
        json.dump({"survivors": survivors, "evaluated_at": datetime.now().isoformat()}, f, indent=2, ensure_ascii=False)

    print(f"⚔️ 종 간 생존 시뮬레이션 완료 → {SURVIVORS_PATH.name}")
    print(f"✅ 생존 루프: {survivors}")
    return survivors

if __name__ == "__main__":
    simulate_species_competition()