
import subprocess
from recommend_loop_from_memory import recommend_loops

# 간단한 실행 맵
LOOP_EXEC_MAP = {
    "진화 루프": "python evolution_loop.py",
    "회고 PDF 생성 루프": "python generate_reflection_with_memory.py",
    "Notion 전송 루프": "python upload_notion_with_memory.py"
}

def run_recommended_loop():
    # 추천 루프 얻기
    from recommend_loop_from_memory import RECOMMENDATION_RULES
    recommendations = []
    if __name__ == "__main__":
        recommendations = RECOMMENDATION_RULES

    print("🧠 추천 루프 판단 중...")
    from recommend_loop_from_memory import recommend_loops as run_rules
    result = run_rules()

    if not result:
        print("✅ 모든 루프 상태 안정적 → 실행할 루프 없음")
        return

    top_loop = result[0]["recommend"]
    command = LOOP_EXEC_MAP.get(top_loop)

    if command:
        print(f"🚀 실행 시작: {top_loop}")
        subprocess.run(command, shell=True)
    else:
        print(f"❌ 실행 명령 없음: {top_loop}")

if __name__ == "__main__":
    run_recommended_loop()
