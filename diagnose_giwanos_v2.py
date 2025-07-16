import os
import json
from pathlib import Path
from datetime import datetime

def check_file(path, label):
    if Path(path).exists():
        print(f"✅ {label}: 존재함")
    else:
        print(f"❌ {label}: 없음")

def check_env_key(key):
    value = os.getenv(key)
    if value:
        print(f"✅ .env 설정 - {key}: OK")
    else:
        print(f"⚠️ .env 설정 - {key}: 누락됨")

def check_trigger():
    try:
        with open("gpt_trigger.json", "r", encoding="utf-8") as f:
            trigger = json.load(f)
        action = trigger.get("action", "")
        if action:
            print(f"✅ gpt_trigger.json: action = '{action}'")
        else:
            print("❌ gpt_trigger.json: action 없음")
    except Exception as e:
        print(f"❌ gpt_trigger.json 오류: {e}")

def check_recent_loop_reason():
    path = Path("logs/loop_execution_reason.json")
    if not path.exists():
        print("⚠️ 실행 기록 없음")
        return
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list) and data:
            latest = data[-1]
            print(f"🧠 최근 루프 실행: {latest.get('time')} / {latest.get('action')} / {latest.get('reason')}")
        else:
            print("⚠️ 실행 기록 데이터 없음")
    except Exception as e:
        print(f"❌ 실행 기록 읽기 오류: {e}")

def check_pdf_validity():
    pdfs = list(Path().glob("loop_reflection_log_*.pdf"))
    if pdfs:
        print(f"📄 회고 PDF 파일 수: {len(pdfs)} → 최신: {pdfs[-1].name}")
    else:
        print("❌ 회고 PDF 없음")

def check_zip_validity():
    zips = list(Path("loop_backups").glob("*.zip")) if Path("loop_backups").exists() else []
    if zips:
        print(f"📦 ZIP 백업 파일 수: {len(zips)} → 최신: {zips[-1].name}")
    else:
        print("❌ ZIP 백업 없음")

def check_font_file():
    font_path = Path("Nanum_Gothic/NanumGothic-Regular.ttf")
    if font_path.exists():
        print("✅ 한글 폰트 (NanumGothic) 설치됨")
    else:
        print("⚠️ NanumGothic-Regular.ttf 없음 → PDF 한글 깨질 수 있음")

def check_loop_logs():
    log_files = list(Path("logs").glob("*.log")) if Path("logs").exists() else []
    issues = []
    for log in log_files:
        text = log.read_text(encoding="utf-8", errors="ignore")
        if "Traceback" in text or "오류" in text or "❌" in text:
            issues.append(log.name)
    if issues:
        print(f"❌ 로그 오류 감지됨 → {issues}")
    else:
        print("✅ 로그 파일 내 오류 없음")

print("🔍 GIWANOS 시스템 종합 점검 [v2]")

# 기본 구성 체크
check_file(".env", ".env 설정 파일")
check_file("gpt_trigger.json", "gpt_trigger.json")
check_file("run_report_bundle.py", "회고 실행기")
check_file("generate_reflection_pdf.py", "회고 PDF 생성기")
check_file("generate_evolution_pdf.py", "진화 PDF 생성기")
check_file("loop_feedback_result_slack.py", "Slack 요약 전송기")
check_file("send_loop_report_email.py", "이메일 전송기")
check_file("loop_dashboard.py", "Streamlit 대시보드")
check_file("logs", "logs 폴더")
check_file("loop_backups", "loop_backups 폴더")

# 상태 점검
check_pdf_validity()
check_zip_validity()
check_trigger()
from dotenv import load_dotenv
load_dotenv()
for key in ["SLACK_WEBHOOK", "NOTION_TOKEN", "EMAIL_USER"]:
    check_env_key(key)
check_recent_loop_reason()
check_font_file()
check_loop_logs()

print("✅ GIWANOS v2 점검 완료")