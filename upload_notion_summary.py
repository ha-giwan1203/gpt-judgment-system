import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path

# ✅ .env 로딩
load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

if not NOTION_TOKEN or not NOTION_DATABASE_ID:
    print("❌ .env에서 Notion 설정을 찾을 수 없습니다.")
    exit()

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# ✅ 최신 회고 PDF 감지
pdf_files = sorted(Path(".").glob("GIWANOS_기억회고_보고서_*.pdf"), key=os.path.getmtime, reverse=True)
if not pdf_files:
    print("❌ 회고 PDF 파일이 존재하지 않습니다.")
    exit()

latest_pdf = pdf_files[0]
pdf_name = latest_pdf.name

# ✅ 확정 필드 구조 기준
data = {
    "parent": { "database_id": NOTION_DATABASE_ID },
    "properties": {
        "제목": {
            "title": [{ "text": { "content": pdf_name } }]
        },
        "상태": {
            "status": { "name": "업로드 완료" }
        },
        "설명": {
            "rich_text": [{ "text": { "content": "GPT 기억 회고 보고서 자동 등록" } }]
        },
        "유형": {
            "select": { "name": "PDF" }
        },
        "경로": {
            "rich_text": [{ "text": { "content": str(latest_pdf.resolve()) } }]
        },
        "날짜": {
            "date": { "start": datetime.now().isoformat() }
        }
    }
}

res = requests.post("https://api.notion.com/v1/pages", headers=headers, json=data)

if res.status_code == 200:
    print(f"✅ Notion 카드 생성 완료 → {pdf_name}")
else:
    print(f"❌ 전송 실패: {res.status_code} - {res.text}")