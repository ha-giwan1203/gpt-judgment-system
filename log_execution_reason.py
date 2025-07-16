
import json
import os
from datetime import datetime

TRIGGER_FILE = "gpt_trigger.json"
LOG_FILE = "logs/loop_execution_reason.json"

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if os.path.exists(TRIGGER_FILE):
    with open(TRIGGER_FILE, "r", encoding="utf-8") as f:
        trigger = json.load(f)
    reason = {
        "time": now,
        "action": trigger.get("action", "알 수 없음"),
        "reason": "gpt_trigger.json 변경 감지"
    }
else:
    reason = {
        "time": now,
        "action": "알 수 없음",
        "reason": "트리거 파일 없음 (수동 실행 또는 기타 이유)"
    }

logs = []
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        try:
            logs = json.load(f)
        except:
            logs = []

logs.append(reason)

with open(LOG_FILE, "w", encoding="utf-8") as f:
    json.dump(logs, f, ensure_ascii=False, indent=2)

print(f"[✅ 루프 실행 사유 기록 완료] → {LOG_FILE}")
