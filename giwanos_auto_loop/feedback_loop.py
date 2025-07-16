import json
import os
from datetime import datetime

# 로그 파일 로딩
def load_log(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

# 요약 생성
def summarize(log_lines):
    summary = {
        "총 실행": 0,
        "성공": 0,
        "실패": 0,
        "실패내역": [],
        "실행기록": log_lines
    }
    for line in log_lines:
        if "[실행]" in line:
            summary["총 실행"] += 1
        elif "[완료]" in line:
            summary["성공"] += 1
        elif "[오류]" in line:
            summary["실패"] += 1
            summary["실패내역"].append(line)
    return summary

# KPI JSON 저장
def export_kpi(summary, kpi_path):
    kpi = {
        "kpi_id": "feedback_" + datetime.now().strftime("%Y%m%d_%H%M%S"),
        "날짜": datetime.now().isoformat(),
        "총 실행": summary["총 실행"],
        "성공": summary["성공"],
        "실패": summary["실패"],
        "성공률": round((summary["성공"] / summary["총 실행"]) * 100, 2) if summary["총 실행"] > 0 else 0,
        "실패내역": summary["실패내역"]
    }
    with open(kpi_path, "w", encoding="utf-8") as f:
        json.dump(kpi, f, ensure_ascii=False, indent=2)
    return kpi

def main():
    log_path = "logs/loop_launcher.log"
    kpi_output_path = ".memory/feedback_kpi_latest.json"

    print("🧠 루프 실행 회고 시작")
    lines = load_log(log_path)
    if not lines:
        print("⚠️ 로그가 없습니다.")
        return

    summary = summarize(lines)
    kpi = export_kpi(summary, kpi_output_path)

    print("=== 실행 회고 요약 ===")
    print(f"총 실행: {kpi['총 실행']}")
    print(f"성공: {kpi['성공']}")
    print(f"실패: {kpi['실패']}")
    print(f"성공률: {kpi['성공률']}%")
    if kpi["실패"] > 0:
        print("❌ 실패 내역:")
        for fail in kpi["실패내역"]:
            print("  -", fail)
    print(f"📁 KPI 저장 완료 → {kpi_output_path}")

if __name__ == "__main__":
    main()