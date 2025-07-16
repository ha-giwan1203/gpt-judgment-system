import json
from pathlib import Path
from collections import defaultdict
from statistics import mean

FEEDBACK_PATH = Path("logs/loop_feedback_log.json")
TRAINED_MODEL_PATH = Path("logs/loop_recommendation_model.json")

def train_recommender_model():
    if not FEEDBACK_PATH.exists():
        print("❌ 피드백 로그 없음")
        return

    data = json.load(open(FEEDBACK_PATH, encoding="utf-8"))
    stats = defaultdict(lambda: {"shown": 0, "executed": 0})

    for entry in data:
        loop = entry["executed_loop"]
        stats[loop]["shown"] += 1
        if entry["matched"]:
            stats[loop]["executed"] += 1

    model = {}
    for loop, s in stats.items():
        accuracy = s["executed"] / s["shown"] if s["shown"] > 0 else 0
        model[loop] = {
            "recommend_shown": s["shown"],
            "executed_when_recommended": s["executed"],
            "recommend_accuracy": round(accuracy, 3)
        }

    with open(TRAINED_MODEL_PATH, "w", encoding="utf-8") as f:
        json.dump(model, f, indent=2, ensure_ascii=False)

    print(f"✅ 추천 모델 학습 완료 → {TRAINED_MODEL_PATH.name}")
    return model

if __name__ == "__main__":
    train_recommender_model()