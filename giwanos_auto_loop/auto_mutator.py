import json
import os
from datetime import datetime

KPI_PATH = ".memory/feedback_kpi_latest.json"
MUTATION_OUT = ".memory/manifest_mutation_suggestion.md"

os.makedirs(".memory", exist_ok=True)

def load_kpi():
    if not os.path.exists(KPI_PATH):
        return None
    with open(KPI_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_mutation(kpi):
    if not kpi or kpi["총 실행"] == 0:
        return "# ⚠️ 구조 제안 불가 - KPI 데이터 없음"

    실패율 = 100 - kpi["성공률"]
    lines = [f"# 🛠️ 구조 개선 제안 (기준 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')})", ""]
    lines.append(f"- 총 실행: {kpi['총 실행']}")
    lines.append(f"- 실패: {kpi['실패']}")
    lines.append(f"- 실패율: {실패율:.1f}%")
    lines.append("")

    if 실패율 >= 40:
        lines.append("🧠 GPT 제안:")
        lines.append("- memory_manifest_진화루프.json에서 'summary_info.json' 파일 생성을 검증하거나 파일명을 명시적으로 지정")
        lines.append("- 실행기 내부에 예외처리 추가: 파일 경로 확인, 실패 시 메시지 로그")
        lines.append("- KPI 분석 루프에 재시도 옵션 추가")
    elif 실패율 >= 20:
        lines.append("🧠 GPT 제안:")
        lines.append("- Slack 전송 루틴에서 실패 로그가 포함되도록 수정")
        lines.append("- memory_guard를 통한 자동 백업 주기 2배 증가")
    else:
        lines.append("✅ 실패율 낮음 → 구조 수정 불필요")

    return "\n".join(lines)

def main():
    kpi = load_kpi()
    report = generate_mutation(kpi)
    with open(MUTATION_OUT, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"✅ 구조 수정 제안 저장됨 → {MUTATION_OUT}")

if __name__ == "__main__":
    main()