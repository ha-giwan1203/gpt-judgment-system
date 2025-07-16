# philosophy_checker.py

import json
from datetime import datetime

def load_philosophy(path="giwanos_self_awareness/loop_philosophy.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def evaluate_execution(loop_name, min_threshold=0.6):
    data = load_philosophy()
    loop = data.get(loop_name, {})
    decision = {
        "loop": loop_name,
        "importance": loop.get("importance", 0),
        "reason": loop.get("reason", ""),
        "mandatory": loop.get("mandatory", False),
        "execute": loop.get("mandatory", False) or loop.get("importance", 0) >= min_threshold,
        "timestamp": datetime.now().isoformat()
    }
    return decision

def save_log(entry, log_path="giwanos_self_awareness/meta_conscience_log.json"):
    try:
        with open(log_path, "r", encoding="utf-8") as f:
            logs = json.load(f)
    except:
        logs = []
    logs.append(entry)
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    loop = input("🔍 실행할 루프 이름을 입력하세요: ").strip()
    result = evaluate_execution(loop)
    save_log(result)
    print("✅ 판단 결과:", result)
