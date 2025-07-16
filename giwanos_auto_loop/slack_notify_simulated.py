
import os

webhook_url = os.getenv("SLACK_WEBHOOK_URL", "https://hooks.slack.com/services/test/mock-url")
message = {
    "text": "📣 [GPT 사고 루프 보고] 판단 → 실행 → 회고 루프가 성공적으로 작동 중입니다."
}

try:
    import requests
    response = requests.post(webhook_url, json=message)
    if response.status_code == 200:
        print("✅ Slack 메시지 전송 성공")
    else:
        print(f"❌ Slack 전송 실패: {response.status_code}")
except Exception as e:
    print(f"❌ Slack 전송 중 오류 발생: {e}")
