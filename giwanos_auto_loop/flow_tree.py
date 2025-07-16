import json
import os
from datetime import datetime

KPI_PATH = ".memory/feedback_kpi_latest.json"
BRANCH_OUT = ".memory/flow_tree_decision.json"

def load_kpi():
    if not os.path.exists(KPI_PATH):
        return None
    with open(KPI_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def decide_branch(kpi):
    if not kpi:
        return {"decision": "unknown", "reason": "KPI 없음"}

    if kpi["성공률"] >= 90:
        return {
            "decision": "진행",
            "next_loop": "진화루프_v3",
            "reason": "성공률 양호 → 루프 정상 진행"
        }
    elif 60 <= kpi["성공률"] < 90:
        return {
            "decision": "재실행",
            "next_loop": "보고루프_v2",
            "reason": f"성공률 {kpi['성공률']}% → 보조 루프 재실행 추천"
        }
    else:
        return {
            "decision": "중단",
            "next_loop": None,
            "reason": f"성공률 낮음 → 루프 일시 중지 필요"
        }

def main():
    kpi = load_kpi()
    result = decide_branch(kpi)
    result["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(BRANCH_OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"📊 조건 분기 결정 저장됨 → {BRANCH_OUT}")
    print(f"결정: {result['decision']} / 사유: {result['reason']}")

if __name__ == "__main__":
    main()