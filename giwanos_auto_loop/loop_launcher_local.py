import subprocess
import os

os.makedirs("logs", exist_ok=True)

loops = {
    "정리루프_v2": "./file_sort_for_지완OS_v2.py",
    "보고루프_v2": "./generate_pdf.py",
    "진화루프_v3": "./evolution_loop.py"
}

def log(message):
    with open("logs/loop_launcher.log", "a", encoding="utf-8") as f:
        f.write(message + "\n")

print("🔁 giwanos 루프 자동 실행 시작")
log("=== 루프 실행 시작 ===")

for name, script in loops.items():
    try:
        print(f"▶️ {name} 실행 중...")
        log(f"[실행] {name} - {script}")
        subprocess.run(["python", script], check=True)
        log(f"[완료] {name} 실행 완료")
    except Exception as e:
        log(f"[오류] {name}: {e}")
        print(f"❌ {name} 실행 중 오류 발생: {e}")

log("=== 루프 실행 종료 ===")
print("✅ 루프 자동 실행 완료")