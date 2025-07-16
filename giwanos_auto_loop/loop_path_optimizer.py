import json
from itertools import permutations
from statistics import mean
from pathlib import Path

SCORE_PATH = Path("logs/loop_score_tracker.json")
OPTIMAL_PATH = Path("logs/loop_optimal_path.json")

def path_score(path, scores):
    # 단순 평균 성능 점수 + 순서 영향 보정
    total = 0
    for i, loop in enumerate(path):
        loop_score = scores.get(loop, {}).get("average_score", 0.5)
        weight = 1.0 - (i * 0.1)  # 앞쪽 루프에 가중치 부여
        total += loop_score * weight
    return round(total / len(path), 4) if path else 0.0

def optimize_path():
    if not SCORE_PATH.exists():
        print("❌ 점수 파일 없음")
        return

    scores = json.load(open(SCORE_PATH, encoding="utf-8"))
    loop_names = list(scores.keys())
    best_path = []
    best_score = 0

    for perm in permutations(loop_names, min(3, len(loop_names))):
        score = path_score(perm, scores)
        if score > best_score:
            best_score = score
            best_path = perm

    result = {
        "best_path": list(best_path),
        "path_score": best_score
    }

    with open(OPTIMAL_PATH, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"✅ 최적 루프 경로 계산 완료 → {OPTIMAL_PATH.name}")
    print(f"▶️ {result['best_path']} (점수: {result['path_score']})")

if __name__ == "__main__":
    optimize_path()