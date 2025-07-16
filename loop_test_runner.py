import os
import subprocess
from datetime import datetime

LOOP_DIR = "giwanos_auto_loop"
TARGETS = [
    "loop_summary_writer.py",
    "loop_mutator.py",
    "loop_feedback_trainer.py",
    "upload_final_runner.py"
]

LOG_PATH = "logs/loop_test_results_log.txt"

def run_test(script):
    path = os.path.join(LOOP_DIR, script)
    if not os.path.exists(path):
        return (script, "❌ 파일 없음", "")
    try:
        result = subprocess.run(["python", path], capture_output=True, text=True, timeout=20)
        if result.returncode == 0:
            return (script, "✅ 정상 실행", result.stdout.strip())
        else:
            return (script, "❌ 실행 실패", result.stderr.strip())
    except Exception as e:
        return (script, "❌ 예외 발생", str(e))

if __name__ == "__main__":
    print("🧪 루프 테스트 자동 실행기 시작")
    results = []
    for target in TARGETS:
        r = run_test(target)
        results.append(r)
        print(f"{r[1]} → {r[0]}")

    # 로그 저장
    os.makedirs("logs", exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"
[테스트 일시: {datetime.now().isoformat()}]
")
        for r in results:
            f.write(f"{r[1]}: {r[0]}
{r[2]}
")
        f.write("-" * 40 + "\n")

    print(f"✅ 테스트 완료 → {LOG_PATH}")