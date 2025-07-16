
import os
import json
from datetime import datetime
from notion_client import Client
from dotenv import load_dotenv

# Load .env and config
load_dotenv()
CONFIG_PATH = "giwanos_config.json"
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

def load_config(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def get_reflection_pdf_path(config):
    folder = config.get("final_reflection_dir", "")
    filename = config.get("default_reflection_pdf", "")
    path = os.path.join(folder, filename)
    return path if os.path.exists(path) else None

def detect_fields(notion, database_id):
    try:
        db = notion.databases.retrieve(database_id=database_id)
        return db.get("properties", {})
    except Exception as e:
        print("❌ Notion 데이터베이스 필드 감지 실패:", e)
        return {}

def upload_to_notion():
    if not NOTION_TOKEN or not NOTION_DATABASE_ID:
        print("❌ Notion API 토큰 또는 DB ID 누락")
        return

    notion = Client(auth=NOTION_TOKEN)
    config = load_config(CONFIG_PATH)
    summary_path = get_reflection_pdf_path(config)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    if not summary_path:
        print("⚠️ 회고 PDF 파일 없음")
        return

    fields = detect_fields(notion, NOTION_DATABASE_ID)
    if not fields:
        return

    def get_field(name, field_type):
        for key, val in fields.items():
            if val.get("type") == field_type:
                return key
        return None

    props = {
        get_field("title", "title"): {"title": [{"text": {"content": f"회고 리포트 {now}"}}]},
        get_field("date", "date"): {"date": {"start": now}},
        get_field("status", "status") or get_field("select", "select"): {"status": {"name": "완료"}},
        get_field("rich_text", "rich_text"): {"rich_text": [{"text": {"content": summary_path}}]},
        get_field("multi_select", "multi_select"): {"multi_select": [{"name": "회고"}, {"name": config.get("version", "vXX")}]}
    }

    props = {k: v for k, v in props.items() if k}  # remove None keys

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
