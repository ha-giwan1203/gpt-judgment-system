from dotenv import load_dotenv
load_dotenv("C:/giwanos/giwanos_auto_loop/.env")

# run_giwanos_v23_loop.py (Terminal UI)
from giwanos_self_creator.realtime_judge_generator import snapshot_context, generate_loop
from datetime import datetime

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def main():
    log("🚀 GIWANOS v23 실시간 루프 생성기 시작")

    user_input = input("🧠 지금 무엇을 하고 싶으신가요? ").strip()
    context = snapshot_context(user_input)
    loop_id, loop_data = generate_loop(context)

    log("✅ 생성된 루프 정보:")
    print(f"→ ID: {loop_id}")
    print(f"→ 이름: {loop_data['name']}")
    print(f"→ 중요도: {loop_data['importance']}")
    print(f"→ 이유: {loop_data['reason']}")

    log("🏁 루프 생성 완료")

if __name__ == "__main__":
    main()
