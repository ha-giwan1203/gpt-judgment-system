import os
import json
from datetime import datetime
import traceback

ERROR_LOG = "logs/loop_error_log.json"

def log_error(loop_name, exception):
    os.makedirs("logs", exist_ok=True)
    now = datetime.now().isoformat()

    error_entry = {
        "loop": loop_name,
        "time": now,
        "error": str(exception),
        "trace": traceback.format_exc()
    }

    existing = []
    if os.path.exists(ERROR_LOG):
        with open(ERROR_LOG, encoding="utf-8") as f:
            try:
                existing = json.load(f)
            except:
                existing = []

    existing.append(error_entry)

    with open(ERROR_LOG, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

    print(f"❌ 루프 실행 실패 기록됨 → {ERROR_LOG}")