import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))  # giwanos_auto_loop를 직접 경로에 추가

import json
from agent_memory import AgentMemory
from smart_judge import smart_tree_judge

def save_failure(context, reason):
    log = {"context": context, "reason": reason}
    filepath = "judgement_feedback_log.json"
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            existing = json.load(f)
    else:
        existing = []
    existing.append(log)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
    print(f"[❌ 테스트 실패 판단 기록됨] → {filepath}")

def run_main():
    memory = AgentMemory()
    memory.load_memory()

    if "--test-fail" in sys.argv:
        print("🚧 [테스트 모드] 실패 판단 강제 생성 중...")
        test_context = "테스트 실패 케이스: 이전 판단에서 오류 발생"
        test_reason = "조건 분기 잘못 처리됨"
        save_failure(test_context, test_reason)
        return

    print("✅ GIWANOS 루프 시작 - agent_memory 로드됨")

if __name__ == "__main__":
    run_main()
