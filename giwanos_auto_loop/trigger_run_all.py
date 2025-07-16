
import os
import json
import subprocess
from giwanos_env import load_giwanos_env

# Load environment
load_giwanos_env(verbose=True)

TRIGGER_PATH = "gpt_trigger.json"

def check_trigger():
    return os.path.exists(TRIGGER_PATH)

def run_step(name, command):
    print(f"\n▶️ [{name}] 실행 중...")
    try:
        subprocess.run(command, check=True)
        print(f"✅ [{name}] 완료")
    except subprocess.CalledProcessError as e:
        print(f"❌ [{name}] 오류 발생:", e)

def main():
    if not check_trigger():
        print("⚠️ 트리거 파일이 없습니다. 실행 종료.")
        return

    run_step("회고 조건 판단", ["python", "loop_condition_checker.py"])
    run_step("회고 루프", ["python", "generate_reflection_pdf.py"])
    run_step("진화 루프", ["python", "evolution_loop.py"])
    run_step("자동 백업", ["python", "auto_save_to_final_reflection.py"])
    run_step("Notion 업로드", ["python", "upload_notion_result_autodetect.py"])
    run_step("ZIP 백업 생성", ["python", "zip_backup_generator.py"])

if __name__ == "__main__":
    main()
