import json
import random
from pathlib import Path
from datetime import datetime

GENES_PATH = Path("logs/loop_genes.json")
SIMULATION_RESULT_PATH = Path("logs/loop_simulation_result.json")

def simulate_loop(loop_name, traits):
    # 간단한 시뮬레이션 점수 계산 로직
    success_prob = 0.6 + (traits.get("stability", 0.5) * 0.3) - (traits.get("aggressiveness", 0.5) * 0.2)
    run_time = round(random.uniform(0.5, 1.5 - traits.get("stability", 0.5)), 2)
    success = random.random() < success_prob
    score = round(success_prob * 0.5 + traits.get("collaboration", 0.5) * 0.3 + (1 - run_time / 2) * 0.2, 3)

    return {
        "loop": loop_name,
        "simulated_at": datetime.now().isoformat(),
        "success": success,
        "estimated_time": run_time,
        "score": score
    }

def run_simulation():
    if not GENES_PATH.exists():
        print("❌ 유전자 정보 없음")
        return

    genes = json.load(open(GENES_PATH, encoding="utf-8"))
    results = []

    for loop, traits in genes.items():
        result = simulate_loop(loop, traits)
        results.append(result)

    with open(SIMULATION_RESULT_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("✅ 루프 시뮬레이션 완료 → loop_simulation_result.json")
    return results

if __name__ == "__main__":
    run_simulation()