# giwanos_launcher_all.py (Fixed display version)
import subprocess
from datetime import datetime

loop_map = {
    "14": "v14/run_giwanos_v14_loop.py",
    "15": "v15/run_giwanos_v15_loop.py",
    "16": "v16/run_giwanos_v16_loop.py",
    "17": "v17/run_giwanos_v17_loop.py",
    "18": "v18/run_giwanos_v18_loop.py",
    "19": "v19/run_giwanos_v19_loop.py",
    "20": "v20/run_giwanos_v20_loop.py",
    "21": "v21/run_giwanos_v21_loop.py",
    "22": "v22/run_giwanos_v22_loop.py",
    "23": "v23/run_giwanos_v23_loop.py"
}

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def main():
    log("GIWANOS 통합 실행기 시작")
    print("=== 실행 가능한 루프 목록 ===")
    for key, path in loop_map.items():
        print(f"[{key}] {path.split('/')[-1]}")
    print("[0] 종료")

    choice = input("→ 실행할 루프 번호를 입력하세요: ").strip()
    if choice == "0":
        print("종료합니다.")
        return
    if choice in loop_map:
        target = loop_map[choice]
        log(f"{target} 실행 중...")
        subprocess.run(["python", target])
    else:
        print("❌ 잘못된 입력입니다.")

if __name__ == "__main__":
    main()
