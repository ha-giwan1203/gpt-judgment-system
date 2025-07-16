import json
import requests
from pathlib import Path

def load_latest_recommendation(log_path="loop_recommendation_log.json"):
    try:
        data = json.load(open(log_path, encoding="utf-8"))
        return data[-1] if data else None
    except:
        return None

def notify_slack(webhook_url, recommendation):
    if not recommendation:
        print("❌ 최근 추천 없음")
        return

    ts = recommendation.get("timestamp", "")
    recs = recommendation.get("recommendations", [])
    if not recs:
        text = f"❌ [{ts}] 추천 루프 없음"
    else:
        text = f"📣 *GIWANOS 추천 루프 알림* ({ts})\n"
        for r in recs:
            text += f"- `{r['loop']}`: {r['reason']} (우선순위 {r['priority']})\n"

    payload = {
        "text": text
    }

    response = requests.post(webhook_url, json=payload)
    if response.status_code == 200:
        print("✅ Slack 전송 성공")
    else:
        print(f"⚠️ Slack 전송 실패: {response.status_code}")

if __name__ == "__main__":
    # TODO: 실제 Webhook URL로 바꿔야 함
    webhook = "<YOUR_SLACK_WEBHOOK_URL>"
    latest = load_latest_recommendation()
    notify_slack(webhook, latest)