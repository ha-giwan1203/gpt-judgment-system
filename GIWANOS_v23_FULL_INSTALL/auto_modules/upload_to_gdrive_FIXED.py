
import os
import io
import mimetypes
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from dotenv import dotenv_values

# 설정
SCOPES = ['https://www.googleapis.com/auth/drive.file']
TOKEN_PATH = './secrets/token_gdrive.json'
CREDS_PATH = './credentials.json'

# .env에서 GDRIVE_FOLDER_ID 읽기
env = dotenv_values(".env")
GDRIVE_FOLDER_ID = env.get("GDRIVE_FOLDER_ID")

def authenticate():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        os.makedirs(os.path.dirname(TOKEN_PATH), exist_ok=True)
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
    return creds

def upload_to_drive(filepath):
    if not os.path.exists(filepath):
        print(f"❌ 파일이 존재하지 않습니다: {filepath}")
        return

    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': os.path.basename(filepath),
        'parents': [GDRIVE_FOLDER_ID] if GDRIVE_FOLDER_ID else []
    }
    media = MediaFileUpload(filepath, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id, webViewLink').execute()

    print(f"✅ 업로드 완료: {file.get('webViewLink')}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="업로드할 파일 경로")
    args = parser.parse_args()
    upload_to_drive(args.file)
