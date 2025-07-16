import json
from pathlib import Path

PRIORITY_PATH = Path("logs/loop_priority_model.json")
RL_WEIGHTS_PATH = Path("logs/loop_rl_trained_weights.json")
ADJUSTED_PATH = Path("logs/loop_priority_model_adjusted.json")

def adjust_weights():
    if not PRIORITY_PATH.exists() or not RL_WEIGHTS_PATH.exists():
        print("❌ 기존 모델 또는 학습된 강화 weight 없음")
        return

    priority = json.load(open(PRIORITY_PATH, encoding="utf-8"))
    rl_weights = json.load(open(RL_WEIGHTS_PATH, encoding="utf-8"))

    adjusted = {}
    for loop, base in priority.items():
        rl = rl_weights.get(loop, 0.0)
        new_weight = round((base.get("weight", 0.5) * 0.7 + rl * 0.3), 3)
        adjusted[loop] = {
            **base,
            "adjusted_weight": new_weight
        }

    with open(ADJUSTED_PATH, "w", encoding="utf-8") as f:
        json.dump(adjusted, f, indent=2, ensure_ascii=False)

    print(f"✅ 추천 우선순위 weight 조정 완료 → {ADJUSTED_PATH.name}")
    return adjusted

if __name__ == "__main__":
    adjust_weights()