# meta_collab_planner.py
import json
from datetime import datetime
def load_meta_state(path="giwanos_meta_loop/meta_loop_state.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}
def recommend_next_loop(meta_state):
    scores = {}
    for loop_name, info in meta_state.items():
        if info.get("status") == "ready":
            score = info.get("confidence", 0.5)
            score += 0.1 if info.get("shared_at") else 0
            scores[loop_name] = score
    sorted_loops = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [loop for loop, _ in sorted_loops]
def main():
    meta_state = load_meta_state()
    next_loops = recommend_next_loop(meta_state)
    if not next_loops:
        print("⚠️ 실행할 협업 루프가 없습니다.")
    else:
        print("✅ 추천 협업 루프:", " → ".join(next_loops))
if __name__ == "__main__":
    main()