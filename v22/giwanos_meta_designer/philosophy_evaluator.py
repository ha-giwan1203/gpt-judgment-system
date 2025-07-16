# philosophy_evaluator.py

import json
from datetime import datetime

def load_philosophies(*paths):
    combined = {}
    for path in paths:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            combined.update(data)
        except:
            continue
    return combined

def evaluate_philosophy(philosophies, threshold=0.6):
    evaluated = {}
    for name, info in philosophies.items():
        score = 0.0
        if info.get("importance", 0) >= 0.6:
            score += 0.5
        if "reason" in info and len(info["reason"]) >= 10:
            score += 0.3
        if info.get("mandatory") or "mutated_from" in info:
            score += 0.2
        evaluated[name] = {
            "score": round(score, 3),
            "approved": score >= threshold,
            "evaluated_at": datetime.now().isoformat()
        }
    return evaluated

def save_evaluation(results, path="giwanos_meta_designer/design_outcome_log.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    paths = [
        "giwanos_self_awareness/loop_philosophy.json",
        "giwanos_self_evolution/replicated_loops.json"
    ]
    combined = load_philosophies(*paths)
    results = evaluate_philosophy(combined)
    save_evaluation(results)
    print("✅ 철학 평가 완료:")
    for k, v in results.items():
        print(f"→ {k}: {'✅ 승인' if v['approved'] else '❌ 기각'} (점수: {v['score']})")
