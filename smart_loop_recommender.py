
import json
import os
from datetime import datetime

# Configurable model (can be loaded from external json in the future)
priority_model = {
    "evolution_loop": {
        "base_score": 1.0,
        "memory_link_boost": 0.5,
        "recent_failure_boost": 0.3,
        "consecutive_penalty": -0.4
    },
    "generate_reflection": {
        "base_score": 0.8,
        "no_recent_pdf": 0.7,
        "linked_loop": 0.2
    },
    "upload_to_notion": {
        "base_score": 0.6,
        "not_uploaded_flag": 0.9
    }
}

# Simulated data inputs (would be loaded from real files)
memory_recently_updated = True
loop_last_failed = ["evolution_loop"]
last_loop_run = "evolution_loop"
recent_pdf_exists = False
not_uploaded_flag = True

def score_loop(loop):
    score = priority_model[loop]["base_score"]

    if loop == "evolution_loop":
        if memory_recently_updated:
            score += priority_model[loop]["memory_link_boost"]
        if loop in loop_last_failed:
            score += priority_model[loop]["recent_failure_boost"]
        if loop == last_loop_run:
            score += priority_model[loop]["consecutive_penalty"]

    if loop == "generate_reflection":
        if not recent_pdf_exists:
            score += priority_model[loop]["no_recent_pdf"]
        if last_loop_run == "evolution_loop":
            score += priority_model[loop]["linked_loop"]

    if loop == "upload_to_notion":
        if not_uploaded_flag:
            score += priority_model[loop]["not_uploaded_flag"]

    return round(score, 3)

def smart_recommend():
    candidates = ["evolution_loop", "generate_reflection", "upload_to_notion"]
    scored = [(loop, score_loop(loop)) for loop in candidates]
    scored.sort(key=lambda x: x[1], reverse=True)

    print("🧠 스마트 루프 추천 결과:")
    for loop, score in scored:
        print(f"🔹 {loop} → score: {score}")

if __name__ == "__main__":
    smart_recommend()
