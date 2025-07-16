from datetime import datetime
import os
import requests
import json

pdf_file = "loop_test_results_report.pdf"
notion_token = os.getenv("NOTION_TOKEN")
notion_db = os.getenv("NOTION_DATABASE_ID")
slack_webhook = os.getenv("SLACK_WEBHOOK")

def send_to_slack():
    if not slack_webhook or not os.path.exists(pdf_file):
        return False
    with open(pdf_file, "rb") as f:
        res = requests.post(
            slack_webhook,
            files={"file": (pdf_file, f, "application/pdf")},
            data={"filename": pdf_file, "channels": "#general", "initial_comment": f"[자동보고] 루프 테스트 결과 보고서 ({datetime.now().date()})"}
        )
    return res.status_code == 200

def send_to_notion():
    if not notion_token or not notion_db or not os.path.exists(pdf_file):
        return False
    headers = {
        "Authorization": f"Bearer {notion_token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    payload = {
        "parent": { "database_id": notion_db },
        "properties": {
            "제목": { "title": [{ "text": { "content": os.path.basename(pdf_file) } }] },
            "날짜": { "date": { "start": datetime.now().isoformat() } },
            "상태": { "status": { "name": "완료" } },
            "유형": { "select": { "name": "테스트" } },
            "태그": { "multi_select": [{ "name": "루프" }, { "name": "보고서" }] },
            "설명": { "rich_text": [{ "text": { "content": "루프 테스트 결과 자동 보고서 업로드됨." } }] }
        }
    }
    res = requests.post("https://api.notion.com/v1/pages", headers=headers, data=json.dumps(payload))
    return res.status_code == 200

status = {
    "slack": send_to_slack(),
    "notion": send_to_notion(),
    "saved_at": datetime.now().isoformat()
}

with open("logs/loop_test_upload_log.json", "w", encoding="utf-8") as f:
    json.dump(status, f, ensure_ascii=False, indent=2)
print("✅ 전송 루프 완료")