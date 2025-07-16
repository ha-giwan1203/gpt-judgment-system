
import os
import json
import subprocess
from loop_condition_checker import should_run_reflection

TRIGGER_PATH = "gpt_trigger.json"
CONFIG_PATH = "giwanos_config.json"

def load_config(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def run_reflection_if_needed():
    config = load_config(CONFIG_PATH)
    trigger_enabled = config.get("use_trigger_for_reflection", False)
    if not trigger_enabled:
        print("🚫 트리거 기반 회고 실행은 설정에서 비활성화되어 있음.")
        return

    if not os.path.exists(TRIGGER_PATH):
        print("⚠️ 트리거 파일 없음. 실행 중단.")
        return

    print("🔍 트리거 감지됨 → 조건 확인 중...")
    should_run, reasons = should_run_reflection()
    if should_run:
        print("✅ 회고 루프 실행 조건 충족 → generate_reflection_pdf.py 실행")
        subprocess.call(["python", "generate_reflection_pdf.py"])
    else:
        print("❎ 회고 실행 조건 불충분")
        if reasons:
            print("🔹 판단 근거:")
            for r in reasons:
                print(f" - {r}")
        else:
            print(" - 조건 없음")

if __name__ == "__main__":
    run_reflection_if_needed()
