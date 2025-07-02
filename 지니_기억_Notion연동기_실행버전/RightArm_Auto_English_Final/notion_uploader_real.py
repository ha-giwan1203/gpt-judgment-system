
import os
import json
import requests

def upload_to_notion(summary, config_path):
    # Load config
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    database_id = config['notion_database_id']
    notion_token = os.getenv(config['notion_token_env'])

    if not notion_token or not database_id:
        print("❌ Notion token or database ID missing.")
        return "failed"

    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {notion_token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    # Example summary structure
    # summary = {
    #   "title": "Memory Summary Title",
    #   "content": "Full summary content...",
    #   "tags": ["자동", "기억"],
    #   "status": "진행 중",
    #   "result_id": "auto-1234"
    # }

    new_page = {
        "parent": { "database_id": database_id },
        "properties": {
            "이름": {
                "title": [
                    { "text": { "content": summary.get("title", "제목 없음") } }
                ]
            },
            "설명": {
                "rich_text": [
                    { "text": { "content": summary.get("content", "") } }
                ]
            },
            "상태": {
                "status": {
                    "name": summary.get("status", "진행 중")
                }
            },
            "결과 ID": {
                "rich_text": [
                    { "text": { "content": summary.get("result_id", "") } }
                ]
            },
            "태그": {
                "multi_select": [{"name": tag} for tag in summary.get("tags", [])]
            }
        }
    }

    response = requests.post(url, headers=headers, json=new_page)

    if response.status_code == 200:
        print("✅ Notion 업로드 성공")
        return "success"
    else:
        print(f"❌ Notion 업로드 실패: {response.status_code} - {response.text}")
        return "failed"
