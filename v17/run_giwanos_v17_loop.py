from dotenv import load_dotenv
load_dotenv("C:/giwanos/giwanos_auto_loop/.env")

# run_giwanos_v17_loop.py (Terminal UI)
from giwanos_self_design.loop_generator import load_loop_scores, generate_loop_blueprint, save_blueprint
from datetime import datetime

def log(msg):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"{timestamp} {msg}")

def main():
    log("🚀 GIWANOS v17 루프 자율 설계기 시작")

    user_input = input("🧠 수행 목적을 입력하세요: ").strip()
    loop_scores = load_loop_scores()
    blueprint = generate_loop_blueprint(user_input, loop_scores)
    save_blueprint(blueprint)

    log("✅ 루프 설계 완료 → loop_blueprint.json 저장됨")
    log("🔁 설계된 루프 순서:")
    for loop in blueprint["loop_order"]:
        print(f"→ {loop}")

    log("🏁 설계기 종료")

if __name__ == "__main__":
    main()
