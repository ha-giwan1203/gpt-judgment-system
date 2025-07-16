# loop_generator.py

import json
from datetime import datetime

def load_loop_scores(path="loop_effect_score.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def generate_loop_blueprint(user_input, loop_scores):
    user_input = user_input.lower()
    blueprint = {
        "purpose": user_input,
        "designed_at": datetime.now().isoformat(),
        "loop_order": []
    }

    if "정산" in user_input or "판단" in user_input:
        blueprint["loop_order"].append("judgement_loop")
    if "회고" in user_input:
        blueprint["loop_order"].append("reflection_loop")
    if "보고" in user_input or "전송" in user_input:
        blueprint["loop_order"].append("report_loop")
    if "정리" in user_input:
        blueprint["loop_order"].append("sort_loop")

    # Optional: sort by loop_scores
    blueprint["loop_order"].sort(key=lambda x: -loop_scores.get(x, 0))

    return blueprint

def save_blueprint(bp, path="loop_blueprint.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(bp, f, indent=2, ensure_ascii=False)

def main():
    user_input = input("🧠 수행 목적을 입력하세요: ").strip()
    loop_scores = load_loop_scores()
    blueprint = generate_loop_blueprint(user_input, loop_scores)
    save_blueprint(blueprint)
    print("✅ 루프 설계 완료 → loop_blueprint.json 저장됨")
    print("🔁 설계된 루프 순서:", " → ".join(blueprint['loop_order']))

if __name__ == "__main__":
    main()
