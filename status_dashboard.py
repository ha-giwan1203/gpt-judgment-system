import sys
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except AttributeError:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace', line_buffering=True)

import json
from pathlib import Path

base_path = Path(__file__).resolve().parent
state_file = base_path / "loop_memory_state.json"
log_file = base_path / "loop_result_log.json"

def show_state():
    print("\n🧠 [GIWANOS 상태 요약]")
    if state_file.exists():
        state = json.loads(state_file.read_text(encoding="utf-8"))
        for k, v in state.items():
            print(f"{k}: {v}")
    else:
        print("loop_memory_state.json 없음")

def show_log():
    print("\n📋 [루프 실행 결과 로그]")
    if log_file.exists():
        logs = json.loads(log_file.read_text(encoding="utf-8"))
        for entry in logs.get("results", [])[-5:]:
            print(f"- [{entry.get('timestamp')}] {entry.get('loop')} ▶ {entry.get('status')}")

if __name__ == "__main__":
    show_state()
    show_log()
