import os
from dotenv import load_dotenv

load_dotenv()

def check(key):
    val = os.getenv(key)
    if val and "여기에" not in val:
        print(f"✅ {key} 설정됨")
    else:
        print(f"❌ {key} 누락 또는 기본값 상태")

if __name__ == "__main__":
    print("🧪 .env 설정값 점검 중...")
    keys = ["NOTION_TOKEN", "NOTION_DATABASE_ID", "GDRIVE_FOLDER_ID", "GITHUB_TOKEN"]
    for k in keys:
        check(k)
