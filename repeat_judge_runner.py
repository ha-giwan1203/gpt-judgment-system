
import time
import subprocess
import os
import json

base_path = "./giwanos_auto_loop"
judge_script = os.path.join(base_path, "agent_judge.py")
executor_script = os.path.join(base_path, "agent_executor.py")
guard_script = os.path.join(base_path, "agent_local_guard.py")
lock_path = os.path.join(base_path, "loop.lock")
guard_result_path = os.path.join(base_path, "local_guard_result.json")

print("🧠 판단 루프 반복 실행 시작 (Ctrl+C로 종료)")

try:
    while True:
        if os.path.exists(lock_path):
            print("⛔ 루프 실행 중복 감지: 이전 루프 실행 중")
            time.sleep(30)
            continue

        # 1. 락 파일 생성
        with open(lock_path, "w") as f:
            f.write("locked")

        try:
            # 2. 로컬 상태 판단
            print("\n🧭 로컬 상태 점검 중...")
            subprocess.run(["python", guard_script])

            if not os.path.exists(guard_result_path):
                print("❌ 로컬 판단 결과 없음 → 루프 중단")
                break

            with open(guard_result_path, "r", encoding="utf-8") as f:
                guard = json.load(f)

            if not guard.get("allow_loop", False):
                print(f"🛑 루프 차단됨: {' | '.join(guard.get('block_reason', []))}")
                time.sleep(60)
                continue

            # 3. 판단기 실행
            print("🔄 판단기 실행 중...")
            subprocess.run(["python", judge_script])

            # 4. 트리거 감지 후 실행기 호출
            trigger_path = os.path.join(base_path, "gpt_trigger.json")
            if os.path.exists(trigger_path):
                print("🚀 트리거 발견 → 실행기 호출")
                subprocess.run(["python", executor_script])
            else:
                print("⏭️ 트리거 없음")
        finally:
            if os.path.exists(lock_path):
                os.remove(lock_path)

        time.sleep(60)
except KeyboardInterrupt:
    print("\n🛑 판단 루프 반복 종료됨")
