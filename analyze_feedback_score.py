import json
import os
from datetime import datetime

LOG_PATH = "./giwanos_memory/loop_feedback_log.json"
REPORT_PATH = "./reports/summary_pdfs/loop_feedback_analysis_report.txt"

if not os.path.exists(LOG_PATH):
    print("❌ loop_feedback_log.json 파일이 존재하지 않습니다.")
    exit()

with open(LOG_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

scores = []
comments = []

for date, entry in data.items():
    scores.append(entry.get("score", 0))
    comments.append(f"{date}: {entry.get('comment', '')}")

if not scores:
    print("❌ 피드백 데이터가 없습니다.")
    exit()

avg_score = sum(scores) / len(scores)
min_score = min(scores)
max_score = max(scores)

# 보고서 생성
with open(REPORT_PATH, "w", encoding="utf-8") as f:
    f.write("📊 GIWANOS 회고 루프 피드백 분석 보고서\n")
    f.write(f"총 회고 횟수: {len(scores)}\n")
    f.write(f"평균 점수: {avg_score:.2f}\n")
    f.write(f"최고 점수: {max_score} / 최저 점수: {min_score}\n\n")
    f.write("📝 코멘트 기록:\n")
    for c in comments:
        f.write(f"- {c}\n")

print(f"✅ 정합률 분석 보고서 생성 완료 → {REPORT_PATH}")