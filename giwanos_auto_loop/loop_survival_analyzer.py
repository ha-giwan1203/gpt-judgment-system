import json
from pathlib import Path
from statistics import mean

SURVIVOR_LOG = Path("logs/loop_survivors.json")
SCOREBOARD = Path("logs/loop_scoreboard.json")

def analyze_survival():
    if not SURVIVOR_LOG.exists() or not SCOREBOARD.exists():
        print("❌ 생존 목록 또는 점수판 없음")
        return

    survivors = set(json.load(open(SURVIVOR_LOG, encoding="utf-8")))
    scores = json.load(open(SCOREBOARD, encoding="utf-8"))

    all_loops = list(scores.keys())
    survival_scores = {loop: scores[loop]["score"] for loop in survivors if loop in scores}
    dead_loops = [loop for loop in all_loops if loop not in survivors]

    avg_survival_score = round(mean(survival_scores.values()), 3) if survival_scores else 0.0
    survival_rate = round(len(survivors) / len(all_loops) * 100, 1) if all_loops else 0.0

    print("📊 생존률 분석 결과:")
    print(f"- 총 루프 수: {len(all_loops)}")
    print(f"- 생존 루프 수: {len(survivors)}")
    print(f"- 생존률: {survival_rate}%")
    print(f"- 생존 루프 평균 점수: {avg_survival_score}")
    print(f"- 제거된 루프: {dead_loops}")
    return survival_rate, avg_survival_score

if __name__ == "__main__":
    analyze_survival()