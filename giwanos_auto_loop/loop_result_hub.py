import json
from pathlib import Path
from datetime import datetime

RESULT_HUB = Path("logs/loop_result_hub.json")

def push_result(loop_name, result_data):
    entry = {
        "loop": loop_name,
        "timestamp": datetime.now().isoformat(),
        "result": result_data
    }

    if RESULT_HUB.exists():
        log = json.load(open(RESULT_HUB, encoding="utf-8"))
    else:
        log = []

    log.append(entry)
    with open(RESULT_HUB, "w", encoding="utf-8") as f:
        json.dump(log, f, indent=2, ensure_ascii=False)

    print(f"📡 결과 기록 완료: {loop_name} → loop_result_hub.json")

if __name__ == "__main__":
    push_result("loop_recommender.py", {"executed": True, "score": 0.82})