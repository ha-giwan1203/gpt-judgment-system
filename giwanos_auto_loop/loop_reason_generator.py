import json
from pathlib import Path

FEEDBACK_PATH = Path("logs/loop_feedback_log.json")
MODEL_PATH = Path("logs/loop_recommendation_model.json")

def generate_reason(loop_name):
    model = json.load(open(MODEL_PATH, encoding="utf-8")) if MODEL_PATH.exists() else {}
    feedback = json.load(open(FEEDBACK_PATH, encoding="utf-8")) if FEEDBACK_PATH.exists() else []

    m = model.get(loop_name)
    if not m:
        return f"❌ 루프 '{loop_name}'의 추천 모델 정보가 없습니다."

    total = m["recommend_shown"]
    executed = m["executed_when_recommended"]
    acc = m["recommend_accuracy"]

    reason = f"✅ 루프 `{loop_name}` 추천 사유:\n"
    reason += f"- 이 루프는 총 {total}회 추천되었고, {executed}회 실행되었습니다.\n"
    reason += f"- 추천 정확도는 **{acc * 100:.1f}%**입니다.\n"

    if acc >= 0.8:
        reason += "- 이 루프는 신뢰성이 매우 높아 반복 추천이 적절합니다.\n"
    elif acc >= 0.6:
        reason += "- 최근 성공률은 양호하며 실행 가능성이 높습니다.\n"
    else:
        reason += "- 정확도는 낮지만 보완 또는 테스트 목적의 추천일 수 있습니다.\n"

    return reason

if __name__ == "__main__":
    print(generate_reason("loop_recommender.py"))