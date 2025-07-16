import json
from pathlib import Path
from datetime import datetime

FEEDBACK_USER_LOG = Path("logs/loop_user_feedback.json")

def collect_feedback(loop_name, feedback: str):
    entry = {
        "loop": loop_name,
        "timestamp": datetime.now().isoformat(),
        "feedback": feedback  # "👍" or "👎"
    }

    if FEEDBACK_USER_LOG.exists():
        data = json.load(open(FEEDBACK_USER_LOG, encoding="utf-8"))
    else:
        data = []

    data.append(entry)
    with open(FEEDBACK_USER_LOG, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ 사용자 피드백 수집 완료: {loop_name} → {feedback}")

if __name__ == "__main__":
    collect_feedback("loop_recommender.py", "👍")