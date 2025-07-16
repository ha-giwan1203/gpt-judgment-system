import time

LOOP_CHAIN = [
    "loop_recommender.py",
    "repeat_judge_runner.py",
    "loop_feedback_trainer.py",
    "evolution_loop.py",
    "loop_summary_reporter.py"
]

def execute_chain():
    print("🔁 루프 자동 연결 흐름 시작")
    for script in LOOP_CHAIN:
        print(f"🚀 실행: {script}")
        time.sleep(1)  # 실제 실행 대신 대기 시뮬레이션
    print("✅ 루프 체인 실행 완료")

if __name__ == "__main__":
    execute_chain()