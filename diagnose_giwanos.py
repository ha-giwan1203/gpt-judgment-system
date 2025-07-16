import os
import json
from pathlib import Path

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

print("🔍 GIWANOS 시스템 종합 점검 시작")

# 파일 존재 확인
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

# PDF/ZIP 확인
pdf_files = list(Path().glob("loop_reflection_log_*.pdf"))
zip_files = list(Path("loop_backups").glob("*.zip")) if Path("loop_backups").exists() else []
print(f"📄 회고 PDF 파일 수: {len(pdf_files)}")
print(f"📦 ZIP 백업 파일 수: {len(zip_files)}")

# 트리거 상태 확인
check_trigger()

# .env 키 확인
from dotenv import load_dotenv
load_dotenv()
for key in ["SLACK_WEBHOOK", "NOTION_TOKEN", "EMAIL_USER"]:
    check_env_key(key)

# 실행 기록 확인
check_recent_loop_reason()

print("✅ GIWANOS 점검 완료")