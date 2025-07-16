import json
import os
import requests
from datetime import datetime

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

def load_latest_recommendation(log_path="loop_recommendation_log.json"):
    try:
        data = json.load(open(log_path, encoding="utf-8"))
        return data[-1] if data else None
    except:
        return None

def send_to_notion(recommendation):
    if not NOTION_TOKEN or not NOTION_DATABASE_ID:
        print("❌ .env에 NOTION_TOKEN 또는 DATABASE_ID 설정 필요")
        return

    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    ts = recommendation.get("timestamp", "")
    date_str = ts.split("T")[0]
    recs = recommendation.get("recommendations", [])

    for rec in recs:
        payload = {
            "parent": { "database_id": NOTION_DATABASE_ID },
            "properties": {
                "제목": {
                    "title": [{
                        "text": {
                            "content": f"추천 루프: {rec['loop']}"
                        }
                    }]
                },
                "날짜": {
                    "date": { "start": date_str }
                },
                "설명": {
                    "rich_text": [{
                        "text": { "content": rec["reason"] }
                    }]
                },
                "우선순위": {
                    "number": rec["priority"]
                },
                "태그": {
                    "multi_select": [
                        {"name": "추천"},
                        {"name": rec["loop"]}
                    ]
                }
            }
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            print(f"✅ Notion 전송 완료: {rec['loop']}")
        else:
            print(f"⚠️ 전송 실패({rec['loop']}): {response.status_code}")

if __name__ == "__main__":
    latest = load_latest_recommendation()
    send_to_notion(latest)