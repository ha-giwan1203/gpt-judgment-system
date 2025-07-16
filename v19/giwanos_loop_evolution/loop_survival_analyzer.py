# loop_survival_analyzer.py

import json
from collections import defaultdict

def load_logs(score_paths):
    merged_scores = defaultdict(float)
    counts = defaultdict(int)

    for path in score_paths:
        try:
            with open(path, "r", encoding="utf-8") as f:
                scores = json.load(f)
            for loop, score in scores.items():
                merged_scores[loop] += score
                counts[loop] += 1
        except:
            continue

    avg_scores = {loop: round(merged_scores[loop]/counts[loop], 3) for loop in merged_scores}
    return avg_scores

def save_fitness(scores, path="giwanos_loop_evolution/loop_fitness_score.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=2, ensure_ascii=False)
    print("✅ 루프 생존 점수 저장 완료:", path)

if __name__ == "__main__":
    sources = [
        "giwanos_path_loop/loop_effect_score.json",     # from v16
        "giwanos_self_design/loop_blueprint.json",      # from v17
        "giwanos_loop_ecosystem/loop_ecosystem_state.json"  # from v18
    ]
    fitness = load_logs(sources)
    save_fitness(fitness)
    print("📊 생존 점수:")
    for k, v in fitness.items():
        print(f"→ {k}: {v}")
