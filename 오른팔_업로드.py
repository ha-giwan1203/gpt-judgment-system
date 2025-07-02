
# ☁️ 오른팔 → Google Drive 업로드 자동화 코드

import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# 📁 구글 서비스 계정 키 파일 경로
SERVICE_ACCOUNT_FILE = "festive-vim-464414-n4-06083c964269.json"
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

# 📂 업로드할 파일 경로
FILE_PATH = "오른팔_시스템_전체패키지.zip"
# 📁 구글 드라이브 상의 폴더 ID (루트면 None)
FOLDER_ID = None  # 필요 시 입력

def upload_to_drive():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build("drive", "v3", credentials=creds)

    file_metadata = {
        "name": os.path.basename(FILE_PATH),
    }
    if FOLDER_ID:
        file_metadata["parents"] = [FOLDER_ID]

    media = MediaFileUpload(FILE_PATH, resumable=True)
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id, name"
    ).execute()

    print(f"✅ 업로드 완료: {file.get('name')} (ID: {file.get('id')})")

if __name__ == "__main__":
    upload_to_drive()
