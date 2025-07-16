import json
from pathlib import Path

SIM_RESULT_PATH = Path("logs/loop_simulation_result.json")
SCOREBOARD_PATH = Path("logs/loop_scoreboard.json")
SURVIVORS_PATH = Path("logs/loop_survivors.json")

SURVIVAL_THRESHOLD = 0.6

def select_survivors():
    if not SIM_RESULT_PATH.exists():
        print("❌ 시뮬레이션 결과 없음")
        return

    results = json.load(open(SIM_RESULT_PATH, encoding="utf-8"))
    scoreboard = {}
    survivors = []
    for r in results:
        loop = r["loop"]
        score = r["score"]
        scoreboard[loop] = {
            "score": score,
            "success": r["success"],
            "estimated_time": r["estimated_time"]
        }
        if score >= SURVIVAL_THRESHOLD:
            survivors.append(loop)

    # 저장
    json.dump(scoreboard, open(SCOREBOARD_PATH, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    json.dump(survivors, open(SURVIVORS_PATH, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    print(f"✅ 생존 루프 선정 완료 → {len(survivors)}개 생존")
    return survivors

if __name__ == "__main__":
    select_survivors()