import os
import json
from datetime import datetime
from modules.memory_parser import generate_summary
from modules.notion_uploader import upload_to_notion

# 직접 지정한 Notion 정보 (더 이상 .env_en 사용 안 함)
NOTION_TOKEN = "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"
DATABASE_ID = "223fee67-0be8-803c-afbc-dd27aec799f4"

# 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKUP_PATH = os.path.join(BASE_DIR, 'data', 'memory_backup_en.json')
LOG_PATH = os.path.join(BASE_DIR, 'logs', 'upload_log_en.txt')

# 폴더 생성
os.makedirs(os.path.dirname(BACKUP_PATH), exist_ok=True)
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

# 요약 생성
summary = {
    "title": "기억 요약 전송",
    "content": generate_summary().get("content", ""),
    "tags": ["자동", "기억"],
    "status": "진행 중",
    "result_id": f"auto-{datetime.now().strftime('%H%M%S')}"
}

# 백업 저장
with open(BACKUP_PATH, 'w', encoding='utf-8') as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

# Notion 업로드
upload_result = upload_to_notion(summary, NOTION_TOKEN, DATABASE_ID)

# 로그 저장
with open(LOG_PATH, 'a', encoding='utf-8') as log_file:
    log_file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Upload status: {upload_result}\n")

print("✅ English memory summary uploaded successfully.")
