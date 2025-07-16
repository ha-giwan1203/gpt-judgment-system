import json
import os
import requests
from dotenv import dotenv_values

env = dotenv_values(".env")

SLACK_URL = env.get("SLACK_WEBHOOK_URL", "")

if not SLACK_URL:
    print("❌ SLACK_WEBHOOK_URL 없음 (.env 확인 필요)")
    exit()

# 최근 KPI 로드
kpi_path = ".memory/feedback_kpi_latest.json"
trigger_path = "gpt_trigger_진화루프_v3.json"

def send_message(text):
    res = requests.post(SLACK_URL, json={"text": text})
    if res.status_code == 200:
        print("✅ Slack 전송 성공")
    else:
        print(f"❌ Slack 전송 실패: {res.status_code} - {res.text}")

if os.path.exists(kpi_path):
    with open(kpi_path, "r", encoding="utf-8") as f:
        kpi = json.load(f)
    message = f"""📊 GIWANOS 루프 실행 요약
- 총 실행: {kpi['총 실행']}
- 성공: {kpi['성공']}
- 실패: {kpi['실패']}
- 성공률: {kpi['성공률']}%
"""
    send_message(message)

if os.path.exists(trigger_path):
    with open(trigger_path, "r", encoding="utf-8") as f:
        trig = json.load(f)
    tmsg = f"""🚨 트리거 생성됨: {trig['loop']}
→ 명령: {trig['command']}
→ 사유: {trig['parameters']['reason']}
"""
    send_message(tmsg)