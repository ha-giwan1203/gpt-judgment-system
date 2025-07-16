# route_feedback_analyzer.py

import json
from collections import defaultdict

def analyze_routes(route_log_path="giwanos_feedback_loop/route_log.json"):
    try:
        with open(route_log_path, "r", encoding="utf-8") as f:
            logs = json.load(f)
    except:
        print("❌ route_log.json 파일을 찾을 수 없습니다.")
        return {}

    loop_count = defaultdict(int)
    for entry in logs:
        for loop in entry.get("route", []):
            loop_count[loop] += 1

    total = sum(loop_count.values())
    loop_scores = {loop: round(count / total, 3) for loop, count in loop_count.items()}
    return loop_scores

def save_scores(scores, output_path="giwanos_feedback_loop/loop_effect_score.json"):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=2, ensure_ascii=False)
    print("✅ 루프 효과성 점수 저장 완료:", output_path)

if __name__ == "__main__":
    scores = analyze_routes()
    if scores:
        save_scores(scores)
