import json
from datetime import datetime
from pathlib import Path

def summarize_recommendations(log_path="loop_recommendation_log.json", output="loop_recommendation_summary.txt"):
    try:
        data = json.load(open(log_path, encoding="utf-8"))
    except:
        print("❌ 추천 로그 파일이 없습니다.")
        return

    summary_lines = []
    summary_lines.append("# 📊 추천 루프 요약 리포트")
    summary_lines.append(f"총 추천 기록 수: {len(data)}")
    summary_lines.append("")

    loop_count = {}
    for entry in data:
        for rec in entry.get("recommendations", []):
            loop = rec["loop"]
            loop_count[loop] = loop_count.get(loop, 0) + 1

    summary_lines.append("## 🔁 루프별 추천 횟수")
    for loop, count in sorted(loop_count.items(), key=lambda x: -x[1]):
        summary_lines.append(f"- {loop}: {count}회")

    summary_lines.append("")
    summary_lines.append("## 📅 최근 추천 기록")
    for entry in data[-5:]:
        summary_lines.append(f"📌 {entry['timestamp']}")
        for rec in entry.get("recommendations", []):
            summary_lines.append(f"  - {rec['loop']} (이유: {rec['reason']}, 우선순위: {rec['priority']})")
        summary_lines.append("")

    # 저장
    with open(output, "w", encoding="utf-8") as f:
        f.write("\n".join(summary_lines))

    print(f"✅ 요약 리포트 생성 완료 → {output}")

if __name__ == "__main__":
    summarize_recommendations()