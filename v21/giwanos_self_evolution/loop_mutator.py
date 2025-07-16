# loop_mutator.py (patched for v21)
import json
from datetime import datetime
import random
import copy
import os

def mutate_loop(loop_name, base_philosophy_path="giwanos_self_awareness/loop_philosophy.json", output_path="giwanos_self_evolution/replicated_loops.json"):
    try:
        with open(base_philosophy_path, "r", encoding="utf-8") as f:
            base_data = json.load(f)
    except:
        print("❌ 철학 파일을 불러올 수 없습니다.")
        return {}

    if loop_name not in base_data:
        print(f"❌ 루프 '{loop_name}' 의 철학이 존재하지 않습니다.")
        return {}

    origin = base_data[loop_name]
    replica = copy.deepcopy(origin)

    variation = round(random.uniform(-0.1, 0.2), 3)
    replica["importance"] = max(0.0, min(1.0, origin["importance"] + variation))
    replica_name = f"{loop_name}_v{random.randint(2, 9)}"
    replica["mutated_from"] = loop_name
    replica["created_at"] = datetime.now().isoformat()

    try:
        with open(output_path, "r", encoding="utf-8") as f:
            existing = json.load(f)
    except:
        existing = {}

    existing[replica_name] = replica
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

    print(f"✅ 루프 '{loop_name}' 변이 → '{replica_name}' 생성 완료")
    return {replica_name: replica}

if __name__ == "__main__":
    loop = input("🔁 복제/진화할 루프 이름을 입력하세요: ").strip()
    mutate_loop(loop)
