
import os
import json
from datetime import datetime
from notion_client import Client
from dotenv import load_dotenv

# Load environment and config
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

def upload_to_notion():
    if not NOTION_TOKEN or not NOTION_DATABASE_ID:
        print("❌ Notion API 정보가 누락되었습니다.")
        return

    config = load_config(CONFIG_PATH)
    summary_path = get_reflection_pdf_path(config)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    if not summary_path:
        print("⚠️ 회고 PDF 파일을 찾을 수 없습니다.")
        return

    notion = Client(auth=NOTION_TOKEN)

    props = {
        "이름": {"title": [{"text": {"content": f"회고 리포트 {now}"}}]},
        "날짜": {"date": {"start": now}},
        "상태": {"select": {"name": "완료"}},
        "경로": {"rich_text": [{"text": {"content": summary_path}}]},
        "설명": {"rich_text": [{"text": {"content": "자동 회고 업로드 (config 기반)"}}]},
        "유형": {"select": {"name": "PDF"}},
        "태그": {"multi_select": [{"name": "회고"}, {"name": config.get("version", "vXX")}]},
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
