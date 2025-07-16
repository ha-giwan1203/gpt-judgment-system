import json
from datetime import datetime
from pathlib import Path

def load_priority_model(path="logs/loop_priority_model.json"):
    try:
        return json.load(open(path, encoding="utf-8"))
    except:
        return {}

def get_current_context():
    # 가상 현재 시간 및 요일 기준 (확장 가능)
    now = datetime.now()
    hour = now.hour
    weekday = now.weekday()  # 0=월 ~ 6=일
    return {"hour": hour, "weekday": weekday}

def schedule_next_loop():
    model = load_priority_model()
    context = get_current_context()

    print("🧠 루프 우선순위 계산 시작")
    ranked = []
    for loop, info in model.items():
        weight = info.get("weight", 1.0)
        usage = info.get("recent_usage", 0.5)
        accuracy = info.get("accuracy", 0.7)
        # 단순 가중치 모델 (확장 가능)
        score = weight * 0.5 + usage * 0.2 + accuracy * 0.3
        ranked.append((loop, score))

    ranked.sort(key=lambda x: -x[1])

    print("📊 루프 우선순위 순위:")
    for i, (loop, score) in enumerate(ranked, 1):
        print(f"{i}. {loop} → {score:.3f}")

    return ranked[0][0] if ranked else "휴식 루프"

if __name__ == "__main__":
    selected = schedule_next_loop()
    print(f"✅ 다음 실행 추천 루프: {selected}")