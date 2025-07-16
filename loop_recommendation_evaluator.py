
# ✅ 추천 루프 판단기
import json, os, datetime
from dotenv import load_dotenv
load_dotenv()
from collections import defaultdict

def evaluate():
    try:
        with open("logs/loop_feedback_log.json", "r", encoding="utf-8") as f:
            feedback = json.load(f)
        with open("logs/trigger_execution_log.json", "r", encoding="utf-8") as f:
            trigger = json.load(f)
    except Exception as e:
        print("🚫 파일 불러오기 실패:", e)
        return

    usage = defaultdict(int)
    score_map = defaultdict(list)

    for t in trigger:
        if "loop" in t:
            usage[t["loop"]] += 1
    for f in feedback:
        if "loop" in f and "score" in f:
            score_map[f["loop"]].append(f["score"])

    top_score = max(score_map.items(), key=lambda x: sum(x[1])/len(x[1]), default=(None, []))[0]
    most_used = max(usage, key=usage.get, default=None)
    least_effective = None

    for loop, scores in score_map.items():
        if usage[loop] >= 3:
            avg = sum(scores)/len(scores)
            if not least_effective or avg < least_effective["avg_score"]:
                least_effective = {"name": loop, "usage": usage[loop], "avg_score": round(avg, 2)}

    out = {
        "top_scored_loop": top_score,
        "most_frequent_loop": most_used,
        "least_effective_loop": least_effective,
        "last_updated": datetime.datetime.now().isoformat()
    }

    with open("logs/loop_recommendation_score.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ 추천 평가 결과 기록 완료")

if __name__ == "__main__":
    evaluate()