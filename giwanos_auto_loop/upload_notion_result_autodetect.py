
import os
import json
from datetime import datetime
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()
CONFIG_PATH = "giwanos_config.json"
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

def load_config(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def detect_files(config):
    folder = config.get("final_reflection_dir", "")
    files = []
    if os.path.exists(folder):
        for fname in os.listdir(folder):
            if fname.endswith((".pdf", ".json", ".md")):
                files.append(os.path.join(folder, fname))
    return files

def detect_fields(notion, database_id):
    try:
        db = notion.databases.retrieve(database_id=database_id)
        return db.get("properties", {})
    except Exception as e:
        print("❌ Notion 필드 감지 실패:", e)
        return {}

def get_field_by_type(fields, field_type):
    for k, v in fields.items():
        if v.get("type") == field_type:
            return k
    return None

def upload_file(filepath, notion, config, fields):
    filename = os.path.basename(filepath)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    ftype = "PDF" if filename.endswith(".pdf") else "JSON" if filename.endswith(".json") else "MD"
    tags = [{"name": "자동 업로드"}, {"name": config.get("version", "vXX")}]

    props = {
        get_field_by_type(fields, "title"): {"title": [{"text": {"content": filename}}]},
        get_field_by_type(fields, "date"): {"date": {"start": now}},
        get_field_by_type(fields, "status") or get_field_by_type(fields, "select"): {"status": {"name": "완료"}},
        get_field_by_type(fields, "rich_text"): {"rich_text": [{"text": {"content": filepath}}]},
        get_field_by_type(fields, "multi_select"): {"multi_select": tags},
        get_field_by_type(fields, "select"): {"select": {"name": ftype}},
    }

    props = {k: v for k, v in props.items() if k}

    try:
        notion.pages.create(
            parent={"database_id": NOTION_DATABASE_ID},
            properties=props
        )
        print(f"✅ {filename} 업로드 성공")
    except Exception as e:
        print(f"❌ {filename} 업로드 실패: {e}")

def main():
    if not NOTION_TOKEN or not NOTION_DATABASE_ID:
        print("❌ Notion API 환경변수 누락")
        return

    notion = Client(auth=NOTION_TOKEN)
    config = load_config(CONFIG_PATH)
    files = detect_files(config)
    fields = detect_fields(notion, NOTION_DATABASE_ID)

    if not files or not fields:
        print("⚠️ 업로드할 파일 또는 필드 없음")
        return

    for f in files:
        upload_file(f, notion, config, fields)

if __name__ == "__main__":
    main()
