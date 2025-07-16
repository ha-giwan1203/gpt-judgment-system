import json
from pathlib import Path
from datetime import datetime

LOG_PATH = Path("logs/loop_conversation_log.json")

def log_conversation(user, message, action=None):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "user": user,
        "message": message,
        "loop_action": action
    }

    if LOG_PATH.exists():
        data = json.load(open(LOG_PATH, encoding="utf-8"))
    else:
        data = []

    data.append(entry)
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"🗣 대화 로그 기록 완료: {user} → {message}")

if __name__ == "__main__":
    log_conversation("지완", "회고기 실행해줘", action="loop_summary_writer.py 실행")