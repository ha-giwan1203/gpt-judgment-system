import json
import random
from pathlib import Path
from statistics import mean, stdev

GENES_PATH = Path("logs/loop_genes.json")
TRACKER_PATH = Path("logs/loop_score_tracker.json")

def simulate_score(traits):
    base = 0.6 + traits.get("stability", 0.5) * 0.3 - traits.get("aggressiveness", 0.5) * 0.2
    collab = traits.get("collaboration", 0.5)
    return round(base * 0.5 + collab * 0.3 + random.uniform(0.1, 0.2), 3)

def run_benchmark(runs=20):
    if not GENES_PATH.exists():
        print("❌ 유전자 정보 없음")
        return

    genes = json.load(open(GENES_PATH, encoding="utf-8"))
    result = {}

    for loop, traits in genes.items():
        scores = [simulate_score(traits) for _ in range(runs)]
        result[loop] = {
            "average_score": round(mean(scores), 3),
            "stdev": round(stdev(scores), 4) if len(scores) > 1 else 0,
            "runs": runs,
            "scores": scores
        }

    with open(TRACKER_PATH, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print("✅ 루프 벤치마크 완료 → loop_score_tracker.json")

if __name__ == "__main__":
    run_benchmark()