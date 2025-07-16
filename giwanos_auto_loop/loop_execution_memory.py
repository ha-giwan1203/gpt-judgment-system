import json
from datetime import datetime
from pathlib import Path

MEMORY_FILE = Path("logs/loop_execution_memory.json")

def record_loop_execution(loop_name, result="success", notes=""):
    now = datetime.now().isoformat()
    entry = {
        "loop": loop_name,
        "executed_at": now,
        "result": result,
        "notes": notes
    }

    if MEMORY_FILE.exists():
        data = json.load(open(MEMORY_FILE, encoding="utf-8"))
    else:
        data = []

    data.append(entry)
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ 루프 실행 기록 저장됨: {loop_name} → {result}")

if __name__ == "__main__":
    record_loop_execution("정리기", result="success", notes="v29 테스트 실행")