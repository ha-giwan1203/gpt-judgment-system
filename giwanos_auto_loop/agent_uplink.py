
import os
import json
from datetime import datetime

# 슬랙 Webhook 주소 (환경변수 또는 기본값 사용)
webhook_url = os.getenv("SLACK_WEBHOOK_URL", "https://hooks.slack.com/services/test/mock-url")
message = {
    "text": f"📤 [Agent_Uplink] 판단 루프 실행됨 — {datetime.now().isoformat()}\n"
            f"- 역할: 판단 → 실행 → 회고 → 기록 완료\n"
            f"- 대상: file_sort_for_지완OS_v2.py (실행 실패 기록됨)"
}

try:
    import requests
    response = requests.post(webhook_url, json=message)
    if response.status_code == 200:
        print("[Agent_Uplink] Slack 전송 성공")
    else:
        print(f"[Agent_Uplink] Slack 전송 실패: {response.status_code}")
except Exception as e:
    print(f"[Agent_Uplink] Slack 전송 오류: {e}")
