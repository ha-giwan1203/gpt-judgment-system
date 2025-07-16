import os
import json
from datetime import datetime
import requests
from dotenv import dotenv_values

env = dotenv_values(os.path.join(os.getcwd(), ".env"))

notion_token = env.get("NOTION_TOKEN")
db_id = env.get("NOTION_DATABASE_ID")
REFLECTION_PATH = ".memory/loop_reflection_summary.md"

if not notion_token or not db_id:
    print("❌ Notion 설정 누락 (.env)")
    exit()

if not os.path.exists(REFLECTION_PATH):
    print("⚠️ 회고 문서가 없습니다.")
    exit()

with open(REFLECTION_PATH, "r", encoding="utf-8") as f:
    reflection = f.read()

url = "https://api.notion.com/v1/pages"
headers = {
    "Authorization": f"Bearer {notion_token}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

data = {
    "parent": {"database_id": db_id},
    "properties": {
        "제목": {
            "title": [
                {"text": {"content": f"GPT 자동 회고 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"}
            }]
        },
        "상태": {
            "status": {
                "name": "보관"
            }
        },
        "설명": {
            "rich_text": [
                {"text": {"content": "자동 회고 설명입니다."}}
            ]
        }
    },
    "children": [
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"text": {"content": reflection[:1900]}}]
            }
        }
    ]
}

res = requests.post(url, headers=headers, json=data)
if res.status_code == 200:
    print("✅ Notion 회고 업로드 성공")
else:
    print(f"❌ Notion 전송 실패: {res.status_code} - {res.text}")