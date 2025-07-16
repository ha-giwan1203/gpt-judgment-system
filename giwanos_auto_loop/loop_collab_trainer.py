import json
from pathlib import Path
from operator import itemgetter

COLLAB_SCORE_PATH = Path("logs/loop_collaboration_score.json")
TOP_COMBOS_PATH = Path("logs/loop_top_collab_pairs.json")

def train_collab_priority(top_n=5):
    if not COLLAB_SCORE_PATH.exists():
        print("❌ 협업 점수 파일 없음")
        return

    collabs = json.load(open(COLLAB_SCORE_PATH, encoding="utf-8"))
    sorted_pairs = sorted(collabs.items(), key=itemgetter(1), reverse=True)
    top_pairs = sorted_pairs[:top_n]

    with open(TOP_COMBOS_PATH, "w", encoding="utf-8") as f:
        json.dump({k: v for k, v in top_pairs}, f, indent=2, ensure_ascii=False)

    print(f"✅ 협업 우선 진화 조합 저장 완료 → {TOP_COMBOS_PATH.name}")
    return top_pairs

if __name__ == "__main__":
    train_collab_priority()