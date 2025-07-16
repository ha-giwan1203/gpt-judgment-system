import os
import json
from datetime import datetime

KPI_PATH = ".memory/feedback_kpi_latest.json"
ERROR_LOG_PATH = ".memory/loop_error_explanation.txt"
OUTPUT_SUMMARY = ".memory/self_reflection_summary.md"
ACTION_PLAN = ".memory/self_action_recommendation.json"
LOG_PATH = "logs/self_reflect.log"

os.makedirs(".memory", exist_ok=True)
os.makedirs("logs", exist_ok=True)

def load_kpi():
    if not os.path.exists(KPI_PATH):
        return None
    with open(KPI_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def load_errors():
    if not os.path.exists(ERROR_LOG_PATH):
        return []
    with open(ERROR_LOG_PATH, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def reflect(kpi, errors):
    summary = []
    decision = {
        "action": "continue",
        "reason": "성공률 양호",
        "modifications": []
    }

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    summary.append(f"# 🧠 Self Reflection Summary ({now})\n")
    summary.append(f"총 실행: {kpi['총 실행']}")
    summary.append(f"성공: {kpi['성공']}")
    summary.append(f"실패: {kpi['실패']}")
    summary.append(f"성공률: {kpi['성공률']}%\n")

    if errors:
        summary.append("## 주요 오류:")
        for err in errors[-3:]:
            summary.append(f"- {err}")
        summary.append("")

    if kpi["성공률"] < 80:
        decision["action"] = "modify"
        decision["reason"] = "성공률 저하"
        decision["modifications"].append({
            "target": "loop_launcher.py",
            "suggest": "실패 루프 제거 또는 재정렬"
        })

    if any("Permission denied" in e for e in errors):
        decision["action"] = "alert"
        decision["reason"] = "실행 권한 오류"
        decision["modifications"].append({
            "target": "execution_env",
            "suggest": "파일 실행 권한 확인 필요"
        })

    return "\n".join(summary), decision

def write_logs(text, action):
    with open(OUTPUT_SUMMARY, "w", encoding="utf-8") as f:
        f.write(text)
    with open(ACTION_PLAN, "w", encoding="utf-8") as f:
        json.dump(action, f, ensure_ascii=False, indent=2)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] Self-reflect executed\n")

def main():
    kpi = load_kpi()
    errors = load_errors()
    if not kpi:
        print("❌ KPI 정보 없음")
        return
    summary_text, decision = reflect(kpi, errors)
    write_logs(summary_text, decision)
    print("✅ Self Reflect 루프 완료")

if __name__ == "__main__":
    main()