
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

def upload_file_to_notion(filepath, notion, config):
    filename = os.path.basename(filepath)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    tags = [{"name": "자동 업로드"}, {"name": config.get("version", "vXX")}]
    ftype = "PDF" if filename.endswith(".pdf") else "JSON" if filename.endswith(".json") else "MD"

    props = {
        "Name": {"title": [{"text": {"content": filename}}]},
        "Date": {"date": {"start": now}},
        "Status": {"status": {"name": "완료"}},
        "Path": {"rich_text": [{"text": {"content": filepath}}]},
        "Type": {"select": {"name": ftype}},
        "Tags": {"multi_select": tags},
        "Description": {"rich_text": [{"text": {"content": f"자동 업로드된 {ftype} 파일"}}]}
    }

    try:
        notion.pages.create(
            parent={"database_id": NOTION_DATABASE_ID},
            properties=props
        )
        print(f"✅ {filename} 업로드 완료")
    except Exception as e:
        print(f"❌ {filename} 업로드 실패: {e}")

def main():
    if not NOTION_TOKEN or not NOTION_DATABASE_ID:
        print("❌ Notion API 정보가 누락됨")
        return

    notion = Client(auth=NOTION_TOKEN)
    config = load_config(CONFIG_PATH)
    files = detect_files(config)

    if not files:
        print("⚠️ 업로드할 파일이 없습니다.")
        return

    for f in files:
        upload_file_to_notion(f, notion, config)

if __name__ == "__main__":
    main()
