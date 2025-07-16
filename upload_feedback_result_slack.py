
# ✅ 회고 결과를 Slack으로 전송하는 스크립트 (dotenv 포함)
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

def send_slack_message(text):
    webhook_url = os.getenv("SLACK_WEBHOOK")
    if not webhook_url:
        print("🚫 SLACK_WEBHOOK 환경변수가 설정되지 않았습니다.")
        return
    payload = {"text": text}
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            print("✅ Slack 메시지 전송 완료")
        else:
            print(f"🚫 Slack 전송 실패: {response.status_code} - {response.text}")
    except Exception as e:
        print("🚫 Slack 전송 예외 발생:", e)

def summarize_feedback():
    try:
        with open("logs/loop_feedback_log.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            if not data:
                return "❗ 최근 피드백 데이터 없음"
            latest = data[-1]
            return f"📄 회고 요약 (점수: {latest.get('score')})\n{latest.get('note')}"
    except Exception:
        return "❗ 회고 피드백 불러오기 실패"

if __name__ == "__main__":
    summary = summarize_feedback()
    send_slack_message(summary)
