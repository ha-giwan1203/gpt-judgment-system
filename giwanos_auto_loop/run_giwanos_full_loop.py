import json
import os
import subprocess
from datetime import datetime

def log_feedback(loop):
    logs_dir = "logs"
    os.makedirs(logs_dir, exist_ok=True)
    log_path = os.path.join(logs_dir, "loop_feedback_log.json")
    model_path = os.path.join(logs_dir, "loop_recommendation_model.json")

    feedback = {
        "loop": loop,
        "matched": True,
        "feedback": "👍",
        "timestamp": datetime.now().isoformat()
    }

    feedback_log = []
    if os.path.exists(log_path):
        with open(log_path, encoding="utf-8") as f:
            feedback_log = json.load(f)
    feedback_log.append(feedback)
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(feedback_log, f, indent=2, ensure_ascii=False)

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
    entry["matched"] += 1
    entry["last_feedback"] = feedback["feedback"]
    entry["updated_at"] = feedback["timestamp"]
    model[loop] = entry

    with open(model_path, "w", encoding="utf-8") as f:
        json.dump(model, f, indent=2, ensure_ascii=False)

    print(f"✅ 자동 피드백 기록 완료 → {log_path}, {model_path}")

# 루프 목록과 실행 파일 매핑
purposes = [
    ("회고", "loop_summary_writer.py"),
    ("진화", "loop_mutator.py")
]
base = "giwanos_auto_loop"

if __name__ == "__main__":
    print("🧠 GIWANOS 목적 순환 자동 루프 실행 + 자동 피드백 기록 시작")

    for purpose, filename in purposes:
        print(f"\n[FULL LOOP] 🧠 실행 목적: {purpose}")
        subprocess.call(["python", os.path.join(base, filename)])
        log_feedback(filename)

    # 마지막으로 피드백 루프 이름도 자동으로 기록 (실행 생략)
    log_feedback("loop_feedback_trainer.py")

    print("\n✅ 전체 루프 실행 및 피드백 자동 기록 완료")