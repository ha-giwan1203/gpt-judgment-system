import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RUNNABLES = [
    "loop_recommender.py",
    "loop_summary_writer.py",
    "loop_explainer.py",
    "loop_mutator.py"
]

def run_loop_script(filename):
    path = Path("giwanos_auto_loop") / filename
    if path.exists():
        print(f"🚀 실행 시작: {filename}")
        subprocess.run(["python", str(path)])
        print(f"✅ 실행 완료: {filename}")
    else:
        print(f"❌ 파일 없음: {filename}")

def run_all_parallel():
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(run_loop_script, RUNNABLES)

if __name__ == "__main__":
    run_all_parallel()