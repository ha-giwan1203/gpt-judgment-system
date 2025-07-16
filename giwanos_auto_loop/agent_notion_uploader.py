
import os
import json
from datetime import datetime

# 환경 변수 기반 설정
notion_token = os.getenv("NOTION_TOKEN", "mock-token")
notion_db = os.getenv("NOTION_DATABASE_ID", "mock-db-id")
reflection_path = "./giwanos_auto_loop/reflection_result.json"

# 회고 결과 로드
if not os.path.exists(reflection_path):
    print("[Agent_Notion] 회고 결과 없음")
    exit()

with open(reflection_path, "r", encoding="utf-8") as f:
    reflection = json.load(f)

# 업로드 데이터 구성
title = f"실행기: {reflection['last_action']}"
status = reflection['last_result']
description = reflection.get("last_reason", "사유 없음")
date = datetime.now().isoformat()

payload = {
    "parent": { "database_id": notion_db },
    "properties": {
        "제목": { "title": [{ "text": { "content": title } }] },
        "상태": { "status": { "name": status } },
        "설명": { "rich_text": [{ "text": { "content": description } }] },
        "날짜": { "date": { "start": date } }
    }
}

# 실제 호출 또는 시뮬레이션
try:
    import requests
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {notion_token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200 or response.status_code == 201:
        print("[Agent_Notion] 전송 성공")
    else:
        print(f"[Agent_Notion] 실패: {response.status_code} - {response.text}")
except Exception as e:
    print(f"[Agent_Notion] 오류: {e}")
