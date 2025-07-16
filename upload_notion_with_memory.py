
import os
import json
from datetime import datetime

# 가정: 노션 연동은 token과 database_id가 .env에서 불러옴
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()
notion = Client(auth=os.getenv("NOTION_TOKEN"))
database_id = os.getenv("NOTION_DATABASE_ID")

def load_manifest_metadata(manifest_path=".memory/manifest.json"):
    if not os.path.exists(manifest_path):
        return "메모리 메타정보 없음"
    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            summaries = []
            for entry in data.get("entries", []):
                line = f"• {entry.get('filename')}: {entry.get('description', '')}"
                summaries.append(line)
            return "\n".join(summaries)
    except Exception as e:
        return f"메모리 로딩 실패: {e}"

def upload_summary_to_notion(title, file_path, memory_summary):
    today = datetime.today().strftime("%Y-%m-%d")
    notion.pages.create(
        parent={"database_id": database_id},
        properties={
            "제목": {"title": [{"text": {"content": title}}]},
            "날짜": {"date": {"start": today}},
            "경로": {"rich_text": [{"text": {"content": file_path}}]},
            "설명": {"rich_text": [{"text": {"content": memory_summary}}]},
            "상태": {"select": {"name": "완료"}},
            "유형": {"select": {"name": "회고"}},
            "태그": {"multi_select": [{"name": "기억연동"}]}
        }
    )
    print("✅ Notion 업로드 완료")

if __name__ == "__main__":
    file_path = "loop_reflection_with_memory.pdf"
    memory_summary = load_manifest_metadata()
    upload_summary_to_notion("GIWANOS 회고 보고서 (기억 반영)", file_path, memory_summary)
