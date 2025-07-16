from dotenv import load_dotenv
load_dotenv("C:/giwanos/giwanos_auto_loop/.env")

# run_giwanos_v22_loop.py (Terminal UI)
from giwanos_meta_designer.philosophy_evaluator import load_philosophies, evaluate_philosophy, save_evaluation
from datetime import datetime

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def main():
    log("🧠 GIWANOS v22 철학 평가 및 메타 설계 시작")

    paths = [
        "giwanos_self_awareness/loop_philosophy.json",
        "giwanos_self_evolution/replicated_loops.json"
    ]
    philosophies = load_philosophies(*paths)
    results = evaluate_philosophy(philosophies)
    save_evaluation(results)

    log("📊 평가 결과:")
    for name, info in results.items():
        print(f"→ {name}: {'✅ 승인' if info['approved'] else '❌ 기각'} (점수: {info['score']})")

    log("🏁 v22 메타 설계기 종료")

if __name__ == "__main__":
    main()
