import os
import requests

# PDF 파일 경로 (가장 최근 파일 기준)
from glob import glob
latest_pdf = sorted(glob("./reports/summary_pdfs/loop_summary_report_*.pdf"))[-1]

# Slack Webhook URL (환경변수에서 불러오기)
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK_URL")

if SLACK_WEBHOOK:
    with open(latest_pdf, "rb") as f:
        filename = os.path.basename(latest_pdf)
        files = {'file': (filename, f, 'application/pdf')}
        payload = {
            "filename": filename,
            "title": f"📎 자동 회고 전송: {filename}",
            "initial_comment": "새로운 회고 PDF가 생성되었습니다.",
            "channels": "#general"
        }
        print(f"📤 Slack으로 전송 시도 중: {filename}")
        response = requests.post(
            url="https://slack.com/api/files.upload",
            params={"token": os.getenv("SLACK_TOKEN")},
            data=payload,
            files=files
        )
        print("✅ Slack 전송 완료" if response.ok else f"❌ 실패: {response.text}")
else:
    print("⚠️ SLACK_WEBHOOK_URL 환경변수가 설정되지 않았습니다.")