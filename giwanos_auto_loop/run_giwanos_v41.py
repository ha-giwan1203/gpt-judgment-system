
import subprocess

def run_step(name, command):
    print(f"\n🟢 [{name}] 실행 시작")
    try:
        subprocess.run(command, check=True)
        print(f"✅ [{name}] 실행 완료")
    except subprocess.CalledProcessError as e:
        print(f"❌ [{name}] 오류 발생:", e)

if __name__ == "__main__":
    run_step("회고 조건 판단", ["python", "loop_condition_checker.py"])
    run_step("회고 루프 실행", ["python", "generate_reflection_pdf.py"])
    run_step("진화 루프 실행", ["python", "evolution_loop.py"])
    run_step("회고 자동 저장", ["python", "auto_save_to_final_reflection.py"])
    run_step("Notion 결과 업로드", ["python", "upload_notion_result_autodetect.py"])
    run_step("ZIP 백업 생성", ["python", "zip_backup_generator.py"])
