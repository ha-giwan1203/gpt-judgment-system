from dotenv import load_dotenv
load_dotenv("C:/giwanos/giwanos_auto_loop/.env")

# run_giwanos_v19_loop.py (Terminal UI)
from giwanos_loop_evolution.loop_survival_analyzer import load_logs, save_fitness
from datetime import datetime

def log(msg):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"{timestamp} {msg}")

def main():
    log("🚀 GIWANOS v19 루프 생존 평가 시작")

    sources = [
        "giwanos_path_loop/loop_effect_score.json",
        "giwanos_self_design/loop_blueprint.json",
        "giwanos_loop_ecosystem/loop_ecosystem_state.json"
    ]
    fitness = load_logs(sources)
    save_fitness(fitness)

    log("📊 생존 점수:")
    for k, v in fitness.items():
        print(f"→ {k}: {v}")

    log("🏁 평가 종료")

if __name__ == "__main__":
    main()
