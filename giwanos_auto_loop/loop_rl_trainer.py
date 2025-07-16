import json
from pathlib import Path

FEEDBACK_PATH = Path("logs/loop_feedback_log.json")
MODEL_PATH = Path("logs/loop_recommendation_model.json")
RL_MODEL_PATH = Path("logs/loop_rl_trained_weights.json")

def train_rl_weights():
    if not FEEDBACK_PATH.exists():
        print("❌ 피드백 로그 없음")
        return

    feedback = json.load(open(FEEDBACK_PATH, encoding="utf-8"))
    reward_map = {}

    for entry in feedback:
        loop = entry["executed_loop"]
        if loop not in reward_map:
            reward_map[loop] = {"total": 0, "count": 0}
        reward = 1 if entry["matched"] else -0.5
        reward_map[loop]["total"] += reward
        reward_map[loop]["count"] += 1

    rl_weights = {}
    for loop, val in reward_map.items():
        avg_reward = val["total"] / val["count"] if val["count"] else 0
        rl_weights[loop] = round(avg_reward, 3)

    with open(RL_MODEL_PATH, "w", encoding="utf-8") as f:
        json.dump(rl_weights, f, indent=2, ensure_ascii=False)

    print("✅ 강화 학습 추천 weight 학습 완료 → loop_rl_trained_weights.json")
    return rl_weights

if __name__ == "__main__":
    train_rl_weights()