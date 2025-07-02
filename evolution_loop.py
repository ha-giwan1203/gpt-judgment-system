import os
import json
from datetime import datetime
from evolution_planner import extract_state, suggest_plan

EXEC_LOG = "evolution_status.json"
RESTORE_FILE = "restore_prompt.txt"

def load_restore():
    if not os.path.exists(RESTORE_FILE):
        return ""
    with open(RESTORE_FILE, "r", encoding="utf-8") as f:
        return f.read()

def load_status():
    if not os.path.exists(EXEC_LOG):
        return {}
    with open(EXEC_LOG, "r", encoding="utf-8") as f:
        return json.load(f)

def save_status(status):
    with open(EXEC_LOG, "w", encoding="utf-8") as f:
        json.dump(status, f, ensure_ascii=False, indent=2)

def run_loop():
    print("🔁 EvolutionGPT 루프 시작")
    prompt = load_restore()
    modules = extract_state(prompt)
    goals = suggest_plan(modules)

    status = load_status()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for i, goal in enumerate(goals, 1):
        if goal in status and status[goal]["status"] == "완료":
            print(f"{i}. ✅ 완료됨 – {goal}")
        else:
            print(f"{i}. ⏳ 미실행 – {goal}")
            # 실행은 자동이 아니라 추천만 (혼자 쓰는 구조이므로)
            status[goal] = {
                "status": "미실행",
                "last_suggested": now
            }

    save_status(status)
    print("\n📁 상태 기록: evolution_status.json")

if __name__ == "__main__":
    run_loop()
