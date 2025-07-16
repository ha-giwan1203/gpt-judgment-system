import json
from pathlib import Path
from statistics import mean

SCOREBOARD = Path("logs/loop_score_tracker.json")
SURVIVORS = Path("logs/loop_survivors_species.json")
LEADER_OUTPUT = Path("logs/loop_species_leaders.json")

def select_leaders(top_n=2):
    if not SCOREBOARD.exists() or not SURVIVORS.exists():
        print("❌ 점수판 또는 생존자 파일 없음")
        return

    scores = json.load(open(SCOREBOARD, encoding="utf-8"))
    survivors = json.load(open(SURVIVORS, encoding="utf-8")).get("survivors", [])

    candidates = [(loop, scores[loop]["average_score"]) for loop in survivors if loop in scores]
    ranked = sorted(candidates, key=lambda x: -x[1])[:top_n]

    leaders = [{"loop": loop, "score": score} for loop, score in ranked]
    with open(LEADER_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(leaders, f, indent=2, ensure_ascii=False)

    print(f"👑 리더 루프 선정 완료 → {LEADER_OUTPUT.name}")
    for l in leaders:
        print(f"⭐️ {l['loop']} (평균 점수: {l['score']})")
    return leaders

if __name__ == "__main__":
    select_leaders()