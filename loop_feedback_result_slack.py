
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

log_path = "logs/loop_feedback_log.json"
pdf_path = sorted([f for f in os.listdir() if f.startswith("loop_reflection_log_") and f.endswith(".pdf")], reverse=True)
latest_pdf = pdf_path[0] if pdf_path else None

summary = "회고 요약: 주요 항목 없음"
if os.path.exists(log_path):
    with open(log_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        if isinstance(data, list):
            first = data[0] if data else {}
            result = first.get("summary", "")
        elif isinstance(data, dict):
            result = data.get("summary", "")
        else:
            result = ""
        if result:
            summary = f"회고 요약: {result}"

message = {"text": summary}
if latest_pdf:
    message["text"] += f"\n📎 PDF 파일: {latest_pdf}"

if SLACK_WEBHOOK:
    r = requests.post(SLACK_WEBHOOK, json=message)
    if r.status_code == 200:
        print("✅ 회고 요약 Slack 전송 완료")
    else:
        print("❌ 전송 실패:", r.text)
else:
    print("❌ Slack Webhook 설정 누락")
