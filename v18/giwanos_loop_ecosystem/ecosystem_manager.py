# ecosystem_manager.py

import json
from datetime import datetime

def load_loop_config(path="giwanos_loop_ecosystem/loop_agent_config.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def simulate_interaction(loop_config):
    logs = []
    for loop, info in loop_config.items():
        if info["status"] == "conflict":
            decision = "보류"
        elif info["priority"] >= 0.7:
            decision = "우선 실행"
        else:
            decision = "협의 필요"

        logs.append({
            "loop": loop,
            "decision": decision,
            "timestamp": datetime.now().isoformat()
        })
    return logs

def save_state(logs, state_path="giwanos_loop_ecosystem/loop_ecosystem_state.json",
               log_path="giwanos_loop_ecosystem/loop_ecosystem_log.json"):
    with open(state_path, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)

    try:
        with open(log_path, "r", encoding="utf-8") as f:
            existing = json.load(f)
    except:
        existing = []
    existing.extend(logs)
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

def main():
    loop_config = load_loop_config()
    results = simulate_interaction(loop_config)
    save_state(results)
    print("✅ 루프 생태계 상호작용 시뮬레이션 완료")
    for log in results:
        print(f"→ {log['loop']}: {log['decision']}")

if __name__ == "__main__":
    main()
