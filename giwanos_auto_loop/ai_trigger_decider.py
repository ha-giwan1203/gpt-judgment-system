import json
import os
from datetime import datetime

# KPI 기반 자동 트리거 판단기
def load_kpi(path):
    if not os.path.exists(path):
        print("❌ KPI 파일이 존재하지 않습니다.")
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def decide_trigger(kpi):
    # 조건: 실패율이 30% 이상이면 재실행 트리거 생성
    if kpi["총 실행"] == 0:
        return None
    실패율 = (kpi["실패"] / kpi["총 실행"]) * 100
    if 실패율 >= 30:
        return {
            "loop": "정리루프_v2",
            "command": "재실행",
            "status": "대기",
            "parameters": {
                "retry": True,
                "reason": f"실패율 {실패율:.1f}% (기준 초과)"
            },
            "description": "자동 판단: 실패율 높아 재실행 권고",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    return None

def export_trigger(trigger, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(trigger, f, ensure_ascii=False, indent=2)
    print(f"✅ 자동 트리거 생성됨: {path}")

def main():
    kpi_path = ".memory/feedback_kpi_latest.json"
    trigger_path = "gpt_trigger_정리루프_v2.json"

    print("🧠 KPI 기반 트리거 판단 시작...")
    kpi = load_kpi(kpi_path)
    if not kpi:
        return

    trigger = decide_trigger(kpi)
    if trigger:
        export_trigger(trigger, trigger_path)
    else:
        print("👌 조건을 만족하는 자동 트리거 없음 (정상 범위)")

if __name__ == "__main__":
    main()