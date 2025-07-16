from dotenv import load_dotenv
import os
print('[TEST] TEST_ENV_VAR:', os.getenv('TEST_ENV_VAR'))
load_dotenv("C:/giwanos/giwanos_auto_loop/.env")

# run_giwanos_v20_loop.py (Terminal UI)
from giwanos_self_awareness.philosophy_checker import evaluate_execution, save_log
from datetime import datetime

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def main():
    log("🧠 GIWANOS v20 철학 기반 실행 판단기 시작")
    loop = input("🗂 판단할 루프 이름을 입력하세요: ").strip()
    result = evaluate_execution(loop)
    save_log(result)

    log("📌 판단 결과:")
    print(f"→ 루프: {result['loop']}")
    print(f"→ 실행 여부: {'✅ 실행함' if result['execute'] else '❌ 실행 안 함'}")
    print(f"→ 이유: {result['reason']}")
    print(f"→ 중요도: {result['importance']} / 필수 여부: {result['mandatory']}")

    log("🏁 판단 종료")

if __name__ == "__main__":
    main()
