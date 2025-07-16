import json
from itertools import combinations
from random import uniform
from pathlib import Path

GENES_PATH = Path("logs/loop_genes.json")
COLLAB_SCORE_PATH = Path("logs/loop_collaboration_score.json")

def simulate_collaboration():
    if not GENES_PATH.exists():
        print("❌ 유전자 정보 없음")
        return

    genes = json.load(open(GENES_PATH, encoding="utf-8"))
    loops = list(genes.keys())
    results = {}

    for loop1, loop2 in combinations(loops, 2):
        traits1 = genes[loop1]
        traits2 = genes[loop2]
        synergy = round(
            (traits1.get("collaboration", 0.5) + traits2.get("collaboration", 0.5)) / 2
            + uniform(-0.1, 0.1), 3)
        key = f"{loop1} + {loop2}"
        results[key] = max(min(synergy, 1.0), 0.0)

    with open(COLLAB_SCORE_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"🤝 루프 협업 시뮬레이션 완료 → {COLLAB_SCORE_PATH.name}")
    return results

if __name__ == "__main__":
    simulate_collaboration()