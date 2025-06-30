# ✅ tools/drive_upload.py - Google Drive 자동 업로드 최종판
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
from datetime import datetime
import zipfile

# 폴더 준비
os.makedirs("tools", exist_ok=True)
os.makedirs("backup", exist_ok=True)

CLIENT_SECRET_FILE = "client_secrets.json"
UPLOAD_FOLDER = "backup"
TEST_ZIP_NAME = "latest_test.zip"
TOKEN_FILE = "token.json"

def authenticate_drive():
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile(CLIENT_SECRET_FILE)    # ✅ 기존 토큰이 있다면 불러오기
    if os.path.exists(TOKEN_FILE):
        gauth.LoadCredentialsFile(TOKEN_FILE)

    # ✅ 토큰이 없거나 만료되었으면 인증 시도
    if gauth.credentials is None or gauth.credentials.invalid:
        gauth.LocalWebserverAuth()
        gauth.SaveCredentialsFile(TOKEN_FILE)

    return GoogleDrive(gauth)

def ensure_drive_folder(drive, parent_id, folder_name):
    query = f"'{parent_id}' in parents and title = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder' and trashed=false"
    file_list = drive.ListFile({'q': query}).GetList()
    if file_list:
        return file_list[0]['id']
    folder = drive.CreateFile({'title': folder_name, 'mimeType': 'application/vnd.google-apps.folder', 'parents': [{'id': parent_id}]})
    folder.Upload()
    return folder['id']

def upload_file_to_drive(filepath, root_folder_name="GPT_Backups"):
    drive = authenticate_drive()
    file_name = os.path.basename(filepath)
    today = datetime.now()

    file_list = drive.ListFile({'q': f"title='{root_folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    if file_list:
        root_id = file_list[0]['id']
    else:
        root = drive.CreateFile({'title': root_folder_name, 'mimeType': 'application/vnd.google-apps.folder'})
        root.Upload()
        root_id = root['id']

    year_id = ensure_drive_folder(drive, root_id, str(today.year))
    month_id = ensure_drive_folder(drive, year_id, f"{today.month:02d}")
    day_id = ensure_drive_folder(drive, month_id, f"{today.day:02d}")

    upload_file = drive.CreateFile({"title": file_name, 'parents': [{'id': day_id}]})
    upload_file.SetContentFile(filepath)
    upload_file.Upload()
    print(f"[✓] 업로드 완료: {file_name} → Google Drive /{root_folder_name}/{today.year}/{today.month:02d}/{today.day:02d}/")

def create_test_zip():
    test_file_path = os.path.join(UPLOAD_FOLDER, "test.txt")
    with open(test_file_path, "w", encoding="utf-8") as f:
        f.write("This is a test file for upload.\n")
    zip_path = os.path.join(UPLOAD_FOLDER, TEST_ZIP_NAME)
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(test_file_path, arcname="test.txt")
    os.remove(test_file_path)
    print(f"[✓] 테스트 zip 생성 완료: {zip_path}")

def main():
    create_test_zip()
    zip_path = os.path.join(UPLOAD_FOLDER, TEST_ZIP_NAME)
    if os.path.exists(zip_path):
        upload_file_to_drive(zip_path)
    else:
        print("[!] 테스트용 zip 파일이 없습니다.")

if __name__ == '__main__':
    main()


