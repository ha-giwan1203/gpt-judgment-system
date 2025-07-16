
# ✅ 실행 감시 및 철학 기준 로그 기록기
import json
import datetime
import os

def log_philosophy_guard(status: str, reason: str):
    log = {
        "timestamp": datetime.datetime.now().isoformat(),
        "status": status,
        "reason": reason
    }

    log_path = "logs/loop_philosophy_guard_log.json"
    os.makedirs("logs", exist_ok=True)

    try:
        if os.path.exists(log_path):
            with open(log_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = []

        data.append(log)

        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"🧠 철학 감시 로그 기록됨: {status} - {reason}")
    except Exception as e:
        print("🚫 로그 기록 실패:", e)

if __name__ == "__main__":
    log_philosophy_guard("pass", "실행 통과 테스트용")
