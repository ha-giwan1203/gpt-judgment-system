
import json
import os

def load_json(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def should_run_reflection():
    feedback = load_json("logs/loop_feedback_log.json")
    last_genes = load_json("logs/loop_genes_mutated.json")
    recommend = load_json("logs/loop_recommendation_model.json")

    reflection_flag = False
    reasons = []

    # 조건 1: 추천 루프가 회고 루프일 경우
    if recommend.get("recommended_next") == "reflection":
        reflection_flag = True
        reasons.append("추천 루프가 reflection임")

    # 조건 2: 유전자 변화량이 임계값을 넘은 경우
    if "genes" in last_genes:
        if any(float(v) > 0.9 or float(v) < 0.1 for v in last_genes["genes"].values()):
            reflection_flag = True
            reasons.append("유전자 변화량이 기준치 초과")

    # 조건 3: 피드백 로그가 일정량 이상 누적됨
    if isinstance(feedback, list) and len(feedback) >= 3:
        reflection_flag = True
        reasons.append("피드백 로그 누적 3건 이상")

    return reflection_flag, reasons

if __name__ == "__main__":
    flag, reasons = should_run_reflection()
    print(f"회고 실행 필요 여부: {flag}")
    if reasons:
        print("실행 사유:")
        for r in reasons:
            print(f" - {r}")
    else:
        print("※ 특별한 실행 조건 없음.")
