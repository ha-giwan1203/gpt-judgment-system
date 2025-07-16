
import subprocess
from smart_loop_recommender import smart_recommend, score_loop

def get_top_loop():
    candidates = ["evolution_loop", "generate_reflection", "upload_to_notion"]
    scored = [(loop, score_loop(loop)) for loop in candidates]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[0][0] if scored else None

def run_loop(loop_name):
    command_map = {
        "evolution_loop": "python evolution_loop.py",
        "generate_reflection": "python generate_reflection_with_memory.py",
        "upload_to_notion": "python upload_notion_with_memory.py"
    }
    command = command_map.get(loop_name)
    if command:
        print(f"🚀 실행 중: {loop_name} → `{command}`")
        subprocess.run(command, shell=True)
    else:
        print(f"❌ 실행 명령 없음: {loop_name}")

def main():
    print("🧠 우선순위 기반 루프 추천 → 자동 실행 시작")
    top_loop = get_top_loop()
    if top_loop:
        print(f"✅ 추천된 루프: {top_loop}")
        run_loop(top_loop)
    else:
        print("⚠️ 추천 루프 없음")

if __name__ == "__main__":
    main()
