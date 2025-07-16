
import json
import os

try:
    import loop_change_diff_checker
except ImportError:
    print("❌ loop_change_diff_checker 모듈을 불러올 수 없습니다.")

try:
    import loop_feedback_analyzer
except ImportError:
    print("❌ loop_feedback_analyzer 모듈을 불러올 수 없습니다.")

LOG_DIR = "logs"

def run_evolution():
    print("🧬 [진화 루프 시작] GIWANOS 구조 분석 및 피드백 기반 개선")

    # 1. 구조 변경 비교
    print("🔍 [1/2] 루프 변경 비교 실행 중...")
    if hasattr(loop_change_diff_checker, "run_diff_check"):
        loop_change_diff_checker.run_diff_check()
    elif hasattr(loop_change_diff_checker, "main"):
        loop_change_diff_checker.main()
    else:
        print("⚠️ run_diff_check 또는 main 함수 없음 → 변경 비교 생략")

    # 2. 피드백 분석 및 유전자 진화 판단
    print("🧠 [2/2] 피드백 기반 유전자 분석 실행 중...")
    if hasattr(loop_feedback_analyzer, "analyze_feedback"):
        result = loop_feedback_analyzer.analyze_feedback()
    else:
        print("❌ analyze_feedback 함수 없음 → 진화 생략")
        return

    os.makedirs(LOG_DIR, exist_ok=True)
    out_path = os.path.join(LOG_DIR, "loop_genes_mutated.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"✅ 진화 완료 → {out_path}")

if __name__ == "__main__":
    run_evolution()
