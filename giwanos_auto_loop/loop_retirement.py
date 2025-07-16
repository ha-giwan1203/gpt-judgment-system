import json
from pathlib import Path

EVAL_PATH = Path("logs/loop_evaluation_score.json")
RETIRE_PATH = Path("logs/loop_retirement_list.json")

RETIRE_THRESHOLD = 0.5  # 평가점수 기준치

def retire_loops():
    if not EVAL_PATH.exists():
        print("❌ 평가 점수 없음")
        return

    evals = json.load(open(EVAL_PATH, encoding="utf-8"))
    retired = {}
    for loop, info in evals.items():
        if info["score"] < RETIRE_THRESHOLD:
            retired[loop] = info

    if retired:
        with open(RETIRE_PATH, "w", encoding="utf-8") as f:
            json.dump(retired, f, indent=2, ensure_ascii=False)
        print(f"📦 휴면/제거 대상 루프: {list(retired.keys())}")
    else:
        print("✅ 모든 루프 유지됨")

if __name__ == "__main__":
    retire_loops()