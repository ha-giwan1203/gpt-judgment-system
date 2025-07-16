import json
from pathlib import Path

MEMORY_PATH = Path("logs/loop_execution_memory.json")
MODEL_PATH = Path("logs/loop_priority_model.json")
EVAL_PATH = Path("logs/loop_evaluation_score.json")

def evaluate_loops():
    scores = {}
    execution_data = json.load(open(MEMORY_PATH, encoding="utf-8")) if MEMORY_PATH.exists() else []
    priority_data = json.load(open(MODEL_PATH, encoding="utf-8")) if MODEL_PATH.exists() else {}

    loop_stats = {}
    for entry in execution_data:
        loop = entry["loop"]
        if loop not in loop_stats:
            loop_stats[loop] = {"success": 0, "fail": 0}
        if entry["result"] == "success":
            loop_stats[loop]["success"] += 1
        elif entry["result"] == "fail":
            loop_stats[loop]["fail"] += 1

    for loop, stat in loop_stats.items():
        total = stat["success"] + stat["fail"]
        success_rate = stat["success"] / total if total > 0 else 0
        priority = priority_data.get(loop, {})
        weight = priority.get("weight", 0.5)
        accuracy = priority.get("accuracy", 0.5)

        score = round(success_rate * 0.5 + weight * 0.25 + accuracy * 0.25, 4)
        scores[loop] = {
            "success_rate": round(success_rate, 3),
            "weight": weight,
            "accuracy": accuracy,
            "score": score
        }

    with open(EVAL_PATH, "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=2, ensure_ascii=False)

    print("✅ 루프 평가 완료 → logs/loop_evaluation_score.json")
    return scores

if __name__ == "__main__":
    evaluate_loops()