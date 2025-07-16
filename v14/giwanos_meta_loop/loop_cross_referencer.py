# loop_cross_referencer.py
import json
from datetime import datetime
def cross_reference(meta_state):
    references = []
    loops = list(meta_state.keys())
    for i in range(len(loops)):
        for j in range(i+1, len(loops)):
            a, b = loops[i], loops[j]
            if meta_state[a]["result"] == meta_state[b]["result"]:
                relation = "동일 판단"
            else:
                relation = "충돌 판단"
            references.append({
                "loop_a": a,
                "loop_b": b,
                "relation": relation,
                "timestamp": datetime.now().isoformat()
            })
    return references
def save_relations(relations, path="loop_relation_log.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            existing = json.load(f)
    except:
        existing = []
    existing.extend(relations)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
def main():
    with open("giwanos_meta_loop/meta_loop_state.json", "r", encoding="utf-8") as f:
        meta_state = json.load(f)
    refs = cross_reference(meta_state)
    save_relations(refs)
    print(f"✅ {len(refs)}개 루프 관계 기록됨.")
if __name__ == "__main__":
    main()