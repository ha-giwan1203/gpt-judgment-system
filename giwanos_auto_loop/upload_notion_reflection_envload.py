
import os
import json
from datetime import datetime
from notion_client import Client
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# 환경 설정
CONFIG_PATH = "giwanos_config.json"
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

def load_config(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def load_summary():
    path = "loop_backups/FINAL_REFLECTION/loop_summary_report.pdf"
    if os.path.exists(path):
        return path
    return None

def upload_to_notion():
    if not NOTION_TOKEN or not NOTION_DATABASE_ID:
        print("❌ Notion API 정보가 누락되었습니다. .env 파일 또는 환경변수 확인 필요.")
        return

    notion = Client(auth=NOTION_TOKEN)
    config = load_config(CONFIG_PATH)
    summary_path = load_summary()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    if not summary_path:
        print("⚠️ 회고 PDF 파일이 존재하지 않습니다.")
        return

    props = {
        "이름": {"title": [{"text": {"content": f"회고 리포트 {now}"}}]},
        "날짜": {"date": {"start": now}},
        "상태": {"select": {"name": "완료"}},
        "경로": {"rich_text": [{"text": {"content": summary_path}}]},
        "설명": {"rich_text": [{"text": {"content": "자동 회고 업로드"}}]},
        "유형": {"select": {"name": "PDF"}},
        "태그": {"multi_select": [{"name": "회고"}, {"name": "v40"}]},
    }

    try:
        notion.pages.create(
            parent={"database_id": NOTION_DATABASE_ID},
            properties=props
        )
        print("✅ Notion 업로드 성공")
    except Exception as e:
        print("❌ Notion 업로드 실패:", e)

if __name__ == "__main__":
    upload_to_notion()
