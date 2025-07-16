
import requests
from datetime import datetime

# ✅ 지완님이 사용 중이던 기존 정상 작동 Webhook 주소
slack_webhook_url = "https://hooks.slack.com/services/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"

def upload_to_slack(file_path="loop_reflection_with_memory.pdf"):
    import os
    if not os.path.exists(file_path):
        print("❌ 회고 PDF 파일이 존재하지 않습니다.")
        return

    file_name = os.path.basename(file_path)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = {
        "text": f"📄 *GIWANOS 회고 PDF 자동 업로드*\n• `{file_name}`\n• 생성 시각: {now}"
    }

    response = requests.post(slack_webhook_url, json=message)
    if response.status_code == 200:
        print("✅ Slack 메시지 전송 완료")
    else:
        print(f"❌ Slack 전송 실패: {response.status_code} - {response.text}")

if __name__ == "__main__":
    upload_to_slack()
