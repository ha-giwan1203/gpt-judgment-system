import json
from datetime import datetime, timedelta
from pathlib import Path

MEMORY_FILE = Path("logs/loop_execution_memory.json")
FAIL_THRESHOLD = 2  # 최근 2회 연속 실패 시 재시도 추천

def detect_unhealthy_loops():
    if not MEMORY_FILE.exists():
        print("❌ 실행 기록 없음")
        return []

    data = json.load(open(MEMORY_FILE, encoding="utf-8"))
    recent = {}
    for entry in reversed(data):
        loop = entry["loop"]
        result = entry["result"]
        if loop not in recent:
            recent[loop] = []
        recent[loop].append(result)
        if len(recent[loop]) >= FAIL_THRESHOLD:
            continue

    unhealthy = []
    for loop, results in recent.items():
        if results[:FAIL_THRESHOLD] == ["fail"] * FAIL_THRESHOLD:
            unhealthy.append(loop)

    return unhealthy

def auto_recovery_action():
    failures = detect_unhealthy_loops()
    if not failures:
        print("✅ 모든 루프 정상 또는 실패 임계 미달")
        return

    print("⚠️ 다음 루프 재시도 권장:")
    for loop in failures:
        print(f"- {loop} → 최근 {FAIL_THRESHOLD}회 연속 실패")

if __name__ == "__main__":
    auto_recovery_action()