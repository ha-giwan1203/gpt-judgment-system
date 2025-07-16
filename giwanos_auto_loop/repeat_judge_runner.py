import json
from loop_recommender import recommend_loops

def run_recommended_loop():
    recommendations = recommend_loops()
    if not recommendations:
        print("❌ 추천 루프 없음")
        return

    # 우선순위 가장 높은 루프 선택
    sorted_loops = sorted(recommendations, key=lambda x: x["priority"])
    top_loop = sorted_loops[0]
    loop_name = top_loop["loop"]
    reason = top_loop["reason"]
    print(f"🚀 실행할 루프: {loop_name} (이유: {reason})")

    # 실행 흐름 예시 (이름 기준 분기)
    if loop_name == "정리기":
        print("📦 정리 루프 실행 중... (예시)")
    elif loop_name == "회고기":
        print("🧠 회고 루프 실행 중... (예시)")
    elif loop_name == "정산 루프":
        print("📊 정산 루프 실행 중... (예시)")
    elif loop_name == "휴식 루프":
        print("😌 휴식 권장 - 실행 없음")
    else:
        print(f"⚠️ 알 수 없는 루프: {loop_name}")

if __name__ == "__main__":
    run_recommended_loop()