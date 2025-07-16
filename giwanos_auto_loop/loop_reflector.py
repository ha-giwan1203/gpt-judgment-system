import json
import os
from datetime import datetime

KPI_PATH = ".memory/feedback_kpi_latest.json"
ERROR_LOG = ".memory/loop_error_explanation.txt"
REPORT_OUT = ".memory/loop_reflection_summary.md"

os.makedirs(".memory", exist_ok=True)

def load_kpi():
    if not os.path.exists(KPI_PATH):
        return None
    with open(KPI_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def load_errors():
    if not os.path.exists(ERROR_LOG):
        return []
    with open(ERROR_LOG, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def generate_summary(kpi, errors):
    lines = []
    lines.append("# 🧠 루프 회고 판단 요약")
    lines.append("")
    lines.append(f"생성일: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("## KPI 분석")
    lines.append(f"- 총 실행: {kpi['총 실행']}")
    lines.append(f"- 성공: {kpi['성공']}")
    lines.append(f"- 실패: {kpi['실패']}")
    lines.append(f"- 성공률: {kpi['성공률']}%")
    lines.append("")
    if errors:
        lines.append("## 오류 요약 및 GPT 회고")
        for err in errors:
            lines.append(f"- {err}")
            if "파일 없음" in err or "No such file" in err:
                lines.append("  → 🧠 판단: 출력 경로 누락 또는 파일 생성 실패로 예상됩니다.")
            elif "Permission denied" in err:
                lines.append("  → 🧠 판단: 실행 권한이 없거나 관리자 권한이 필요합니다.")
            else:
                lines.append("  → 🧠 판단: 일반적 실행 실패, 루프별 구성 검토 필요.")
    else:
        lines.append("✅ 오류 없이 정상 실행됨. 시스템 상태 양호.")
    return "\n".join(lines)

def main():
    kpi = load_kpi()
    errors = load_errors()
    if not kpi:
        print("❌ KPI 데이터를 불러올 수 없습니다.")
        return
    summary = generate_summary(kpi, errors)
    with open(REPORT_OUT, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"✅ 회고 판단 요약 저장됨 → {REPORT_OUT}")

if __name__ == "__main__":
    main()