import json
from collections import Counter

def analyze_feedback(feedback_log="loop_feedback_log.json"):
    try:
        data = json.load(open(feedback_log, encoding="utf-8"))
    except:
        print("❌ 피드백 로그 없음")
        return

    if not data:
        print("⚠️ 피드백 데이터가 없습니다.")
        return

    matched = [d for d in data if d["matched"]]
    unmatched = [d for d in data if not d["matched"]]

    print(f"총 피드백 수: {len(data)}")
    print(f"✅ 일치: {len(matched)}회 ({len(matched)/len(data)*100:.1f}%)")
    print(f"❌ 불일치: {len(unmatched)}회 ({len(unmatched)/len(data)*100:.1f}%)")
    print("")

    # 루프별 정확도
    loop_stats = {}
    for d in data:
        loop = d["executed_loop"]
        if loop not in loop_stats:
            loop_stats[loop] = {"match": 0, "total": 0}
        loop_stats[loop]["total"] += 1
        if d["matched"]:
            loop_stats[loop]["match"] += 1

    print("📈 루프별 추천 정확도")
    for loop, stat in loop_stats.items():
        accuracy = stat["match"] / stat["total"] * 100
        print(f"- {loop}: {stat['match']} / {stat['total']} 일치 ({accuracy:.1f}%)")

if __name__ == "__main__":
    analyze_feedback()