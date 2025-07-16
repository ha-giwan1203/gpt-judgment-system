
import json
import os
from datetime import datetime

TRIGGER_PATH = "gpt_trigger.json"

def run_sync_check():
    if not os.path.exists(TRIGGER_PATH):
        print("⚠️ 트리거 없음 - 변경 없음")
        return
    with open(TRIGGER_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    print("✅ 트리거 감지됨 → GPT 동기화 시작")
    print(f"🗂 변경 경로: {data.get('path')}")
    print(f"⏱ 시간: {datetime.fromtimestamp(data.get('timestamp'))}")
    # 여기에 GPT 연동 또는 회고 자동화 코드 삽입 가능

if __name__ == "__main__":
    run_sync_check()
