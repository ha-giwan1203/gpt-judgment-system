
# ✅ 회고 점수 통계 요약 루프
import json, os, datetime
from dotenv import load_dotenv
load_dotenv()
from collections import defaultdict

def aggregate():
    path = "logs/loop_feedback_log.json"
    if not os.path.exists(path): return

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    loop_scores = defaultdict(list)
    scores = []

    for d in data:
        if "loop" in d and "score" in d:
            loop_scores[d["loop"]].append(d["score"])
            scores.append(d["score"])

    loop_stats = {
        k: {
            "count": len(v),
            "avg": round(sum(v)/len(v), 2)
        } for k, v in loop_scores.items()
    }

    summary = {
        "total_count": len(scores),
        "average_score": round(sum(scores)/len(scores), 2) if scores else 0,
        "max_score": max(scores) if scores else None,
        "min_score": min(scores) if scores else None,
        "most_used_loop": max(loop_scores, key=lambda x: len(loop_scores[x]), default=None),
        "loop_stats": loop_stats,
        "last_updated": datetime.datetime.now().isoformat()
    }

    with open("logs/feedback_aggregate_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print("✅ 점수 통계 요약 완료")

if __name__ == "__main__":
    aggregate()