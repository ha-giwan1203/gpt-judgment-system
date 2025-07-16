# run_giwanos_master_loop.py (Final Fixed)
import subprocess
from datetime import datetime

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def run_base_loops():
    base_path = "C:/giwanos/giwanos_auto_loop"
    steps = [
        "repeat_judge_runner.py",
        "generate_reflection_pdf.py",
        "upload_final_runner.py",
        "zip_backup_generator.py"
    ]
    for step in steps:
        log(f"📦 기반 루프 실행: {base_path}/{step}")
        subprocess.run(["python", step], cwd=base_path, check=True)

def run_extension_loops():
    extension_loops = {
        "14": "run_giwanos_v14_loop.py",
        "15": "run_giwanos_v15_loop.py",
        "16": "run_giwanos_v16_loop.py",
        "17": "run_giwanos_v17_loop.py",
        "18": "run_giwanos_v18_loop.py",
        "19": "run_giwanos_v19_loop.py",
        "20": "run_giwanos_v20_loop.py",
        "21": "run_giwanos_v21_loop.py",
        "22": "run_giwanos_v22_loop.py",
        "23": "run_giwanos_v23_loop.py"
    }
    for ver, filename in extension_loops.items():
        path = f"C:/giwanos/v{ver}"
        log(f"🧪 확장 루프 실행: {path}/{filename}")
        subprocess.run(["python", filename], cwd=path, check=True)

def main():
    log("🚀 GIWANOS MASTER LOOP 시작")
    run_base_loops()
    run_extension_loops()
    log("✅ GIWANOS MASTER LOOP 전체 실행 완료")

if __name__ == "__main__":
    main()
