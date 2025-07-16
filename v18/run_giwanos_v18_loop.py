from dotenv import load_dotenv
load_dotenv("C:/giwanos/giwanos_auto_loop/.env")

# run_giwanos_v18_loop.py (Terminal UI)
from giwanos_loop_ecosystem.ecosystem_manager import load_loop_config, simulate_interaction, save_state
from datetime import datetime

def log(msg):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"{timestamp} {msg}")

def main():
    log("🚀 GIWANOS v18 루프 생태계 시뮬레이션 시작")

    config = load_loop_config()
    results = simulate_interaction(config)
    save_state(results)

    log("📊 루프 상호작용 결과:")
    for entry in results:
        print(f"→ {entry['loop']}: {entry['decision']}")

    log("🏁 시뮬레이션 종료")

if __name__ == "__main__":
    main()
