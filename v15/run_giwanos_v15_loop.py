# run_giwanos_v15_loop.py (final route_log save fix)
from giwanos_path_loop.path_planner import plan_execution_path
from datetime import datetime
import json
import os

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def main():
    log("🚀 GIWANOS v15 루프 경로 설계기 시작")
    user_input = input("🧠 실행 목적을 입력하세요: ").strip()
    route, readable = plan_execution_path(user_input)

    if not route:
        log("❌ 실행할 루프가 없습니다.")
        return

    log("📌 추천된 루프 실행 경로:")
    for step in readable:
        print("→", step)

    # ✅ route_log 저장: route가 있을 때만
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "input": user_input,
        "route": route
    }
    log_path = os.path.join("giwanos_path_loop", "route_log.json")
    try:
        with open(log_path, "r", encoding="utf-8") as f:
            logs = json.load(f)
    except:
        logs = []
    logs.append(log_entry)
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
