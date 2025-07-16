import json
import os
from datetime import datetime

def collect_feedback():
    print("[루프 시작] 실행 목적: 피드백")

    logs_dir = "logs"
    os.makedirs(logs_dir, exist_ok=True)

    feedback_log_path = os.path.join(logs_dir, "loop_feedback_log.json")
    model_path = os.path.join(logs_dir, "loop_recommendation_model.json")

    loop = input("실제로 실행한 루프를 입력하세요: ").strip()
    if not loop:
        print("❌ 실행 루프가 입력되지 않았습니다.")
        return

    feedback = {
        "loop": loop,
        "matched": True,
        "feedback": "👍",
        "timestamp": datetime.now().isoformat()
    }

    # 기존 피드백 로그 불러오기
    feedback_log = []
    if os.path.exists(feedback_log_path):
        with open(feedback_log_path, encoding="utf-8") as f:
            feedback_log = json.load(f)
    feedback_log.append(feedback)

    with open(feedback_log_path, "w", encoding="utf-8") as f:
        json.dump(feedback_log, f, indent=2, ensure_ascii=False)

    # 추천 모델 반영
    model = {}
    if os.path.exists(model_path):
        with open(model_path, encoding="utf-8") as f:
            model = json.load(f)

    entry = model.get(loop, {
        "executed": 0,
        "matched": 0,
        "last_feedback": "",
        "updated_at": ""
    })

    entry["executed"] += 1
    if feedback["matched"]:
        entry["matched"] += 1
    entry["last_feedback"] = feedback["feedback"]
    entry["updated_at"] = feedback["timestamp"]

    model[loop] = entry

    with open(model_path, "w", encoding="utf-8") as f:
        json.dump(model, f, indent=2, ensure_ascii=False)

    print(f"✅ 피드백 + 추천 학습 모델 저장 완료 → {feedback_log_path}, {model_path}")

if __name__ == "__main__":
    collect_feedback()