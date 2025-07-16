from dotenv import load_dotenv
load_dotenv("C:/giwanos/giwanos_auto_loop/.env")

# run_giwanos_v14_loop.py
import subprocess
import json
from datetime import datetime
def log(msg):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"{timestamp} {msg}")
def run_module(path):
    log(f"⏯ 실행: {path}")
    subprocess.run(["python", path])
def load_meta():
    with open("giwanos_meta_loop/meta_loop_state.json", "r", encoding="utf-8") as f:
        return json.load(f)
def main():
    log("🚀 GIWANOS v14 협업 루프 실행 시작")
    run_module("giwanos_meta_loop/loop_cross_referencer.py")
    log("🧠 추천 루프 확인 중...")
    result = subprocess.run(["python", "giwanos_meta_loop/meta_collab_planner.py"],
                            capture_output=True, text=True)
    print(result.stdout)
    meta = load_meta()
    ready_loops = [k for k, v in meta.items() if v["status"] == "ready"]
    if not ready_loops:
        log("❌ 실행할 루프 없음 (모두 대기 또는 종료)")
    else:
        log(f"✅ 실행 가능 루프: {', '.join(ready_loops)}")
        log("🔔 루프별 실행은 수동 실행 또는 자동 트리거 설정 필요")
    log("🏁 v14 루프 실행기 종료")
if __name__ == "__main__":
    main()