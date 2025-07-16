
import os
import json
from datetime import datetime
from notion_client import Client
from dotenv import load_dotenv
from giwanos_env import load_giwanos_env

# Load .env
load_giwanos_env(verbose=True)

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

def upload_file(filepath, notion, config):
    filename = os.path.basename(filepath)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    ftype = "PDF" if filename.endswith(".pdf") else "JSON" if filename.endswith(".json") else "MD"
    tags = [{"name": "자동 업로드"}, {"name": config.get("version", "v41")}]

    props = {
        "Name": {"title": [{"text": {"content": filename}}]},
        "Date": {"date": {"start": now}},
        "Status": {"status": {"name": "완료"}},
        "Path": {"rich_text": [{"text": {"content": filepath}}]},
        "Type": {"select": {"name": ftype}},
        "Tags": {"multi_select": tags},
        "Description": {"rich_text": [{"text": {"content": f"{ftype} 자동 업로드"}}]}
    }

    try:
        notion.pages.create(
            parent={"database_id": NOTION_DATABASE_ID},
            properties=props
        )
        print(f"✅ {filename} 업로드 성공")
    except Exception as e:
        print(f"❌ {filename} 업로드 실패:", e)

def main():
    if not NOTION_TOKEN or not NOTION_DATABASE_ID:
        print("❌ Notion API 정보 누락")
        return

    notion = Client(auth=NOTION_TOKEN)
    config = load_config(CONFIG_PATH)
    files = detect_files(config)

    if not files:
        print("⚠️ 업로드할 파일이 없습니다.")
        return

    for f in files:
        upload_file(f, notion, config)

if __name__ == "__main__":
    main()
