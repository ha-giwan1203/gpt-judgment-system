# realtime_judge_generator.py

import json
from datetime import datetime
import random

def snapshot_context(user_input, snapshot_path="giwanos_self_creator/context_snapshot.json"):
    now = datetime.now()
    context = {
        "timestamp": now.isoformat(),
        "hour": now.hour,
        "user_input": user_input,
        "recent_loops": ["judgement_loop", "reflection_loop"],  # example
        "daypart": "late" if now.hour >= 22 else "normal"
    }
    with open(snapshot_path, "w", encoding="utf-8") as f:
        json.dump(context, f, indent=2, ensure_ascii=False)
    return context

def generate_loop(context, output_path="giwanos_self_creator/self_created_loops.json"):
    base_name = "loop"
    if "정리" in context["user_input"] and "보고" in context["user_input"]:
        base_name = "combo_report_sort_loop"
    elif "정리" in context["user_input"]:
        base_name = "auto_sort_loop"
    elif "보고" in context["user_input"]:
        base_name = "rapid_report_loop"

    loop = {
        "name": base_name,
        "generated_at": context["timestamp"],
        "importance": round(random.uniform(0.65, 0.95), 3),
        "reason": "사용자 요청 및 시간대, 최근 루프 기준으로 자동 생성됨"
    }

    try:
        with open(output_path, "r", encoding="utf-8") as f:
            existing = json.load(f)
    except:
        existing = {}

    unique_name = f"{base_name}_{random.randint(1000,9999)}"
    existing[unique_name] = loop

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

    return unique_name, loop

if __name__ == "__main__":
    user_input = input("🧠 지금 무엇을 하고 싶으신가요? ").strip()
    context = snapshot_context(user_input)
    loop_id, loop_data = generate_loop(context)
    print(f"✅ 루프 생성됨: {loop_id}")
    print(loop_data)
