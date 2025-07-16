import os
import re

log_path = "logs/loop_launcher.log"
output_path = ".memory/loop_error_explanation.txt"

os.makedirs(".memory", exist_ok=True)

def extract_errors(lines):
    return [line for line in lines if "[오류]" in line]

def explain_error(error_line):
    if "파일 없음" in error_line or "No such file" in error_line:
        return "📂 파일이 존재하지 않음 → 경로 또는 파일 생성 여부 확인 필요"
    if "ImportError" in error_line:
        return "📦 모듈 누락 → requirements.txt 확인 또는 pip install 필요"
    if "Permission denied" in error_line:
        return "🔐 권한 문제 → 실행 권한 또는 관리자 권한 확인"
    if "KeyError" in error_line:
        return "🔑 .env 또는 설정 파일 내 키 누락 → 환경 설정 확인"
    return "❓ 일반 오류 → 로그 문장 직접 검토 필요"

def generate_report(errors):
    report = ["# ❌ 루프 오류 요약 리포트", ""]
    for e in errors:
        explanation = explain_error(e)
        report.append(f"- {e}")
        report.append(f"  → {explanation}")
        report.append("")
    return "\n".join(report)

def main():
    if not os.path.exists(log_path):
        print("⚠️ 로그 파일이 없습니다.")
        return
    with open(log_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]
    errors = extract_errors(lines)
    if not errors:
        print("✅ 오류 없음")
        return
    report = generate_report(errors)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"📄 오류 분석 리포트 저장됨: {output_path}")

if __name__ == "__main__":
    main()