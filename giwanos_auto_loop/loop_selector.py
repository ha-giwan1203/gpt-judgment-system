import json
from pathlib import Path

PRIORITY_PATH = Path("logs/loop_priority_model.json")
EVAL_PATH = Path("logs/loop_evaluation_score.json")
INTERACTION_PATH = Path("logs/loop_interaction_matrix.json")

def select_best_loop():
    priority = json.load(open(PRIORITY_PATH, encoding="utf-8")) if PRIORITY_PATH.exists() else {}
    evals = json.load(open(EVAL_PATH, encoding="utf-8")) if EVAL_PATH.exists() else {}
    interactions = json.load(open(INTERACTION_PATH, encoding="utf-8")) if INTERACTION_PATH.exists() else {}

    # 합산 점수 계산: base_score + 연계 점수 평균
    scores = {}
    for loop, eval_score in evals.items():
        base = eval_score["score"]
        linked = interactions.get(loop, {})
        if linked:
            avg_link = sum(linked.values()) / len(linked)
        else:
            avg_link = 0.5
        final_score = round(base * 0.7 + avg_link * 0.3, 4)
        scores[loop] = final_score

    ranked = sorted(scores.items(), key=lambda x: -x[1])
    if ranked:
        best = ranked[0]
        print(f"✅ 추천 루프: {best[0]} → 점수: {best[1]}")
    else:
        print("❌ 추천할 루프가 없습니다.")

    return ranked

if __name__ == "__main__":
    select_best_loop()