import json
from datetime import datetime, timedelta
from pathlib import Path

RETIRE_PATH = Path("logs/loop_retirement_list.json")
EXEC_MEM_PATH = Path("logs/loop_execution_memory.json")
REACTIVATED_PATH = Path("logs/loop_reactivation_log.json")

REACTIVATE_DAYS = 5  # 최근 5일 이내 성공 시 복귀
MIN_SUCCESS_RATE = 0.6

def reactivate_loops():
    if not RETIRE_PATH.exists() or not EXEC_MEM_PATH.exists():
        print("❌ 휴면 루프 또는 실행 로그 없음")
        return []

    retired = json.load(open(RETIRE_PATH, encoding="utf-8"))
    exec_data = json.load(open(EXEC_MEM_PATH, encoding="utf-8"))

    reactivated = []
    now = datetime.now()

    for loop in retired:
        recent_execs = [
            e for e in exec_data if e["loop"] == loop and e["result"] == "success"
            and (now - datetime.fromisoformat(e["executed_at"])) <= timedelta(days=REACTIVATE_DAYS)
        ]
        total = len([e for e in exec_data if e["loop"] == loop])
        success_rate = len(recent_execs) / total if total > 0 else 0

        if success_rate >= MIN_SUCCESS_RATE and recent_execs:
            reactivated.append({
                "loop": loop,
                "reactivated_at": now.isoformat(),
                "success_rate": round(success_rate, 2),
                "reason": "최근 성공률 회복"
            })

    if reactivated:
        with open(REACTIVATED_PATH, "w", encoding="utf-8") as f:
            json.dump(reactivated, f, indent=2, ensure_ascii=False)
        print(f"✅ 복귀 루프: {[r['loop'] for r in reactivated]}")
    else:
        print("📭 복귀 조건을 충족한 루프 없음")

if __name__ == "__main__":
    reactivate_loops()