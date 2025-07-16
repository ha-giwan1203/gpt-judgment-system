
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from dotenv import load_dotenv

SCOPES = ['https://www.googleapis.com/auth/drive.file']

def authenticate():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def upload_file(filename, folder_id):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {'name': os.path.basename(filename), 'parents': [folder_id]}
    media = MediaFileUpload(filename, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    file_id = file.get('id')
    print(f"✅ 업로드 성공! 링크: https://drive.google.com/file/d/{file_id}/view?usp=sharing")
    return file_id

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    folder_id = os.getenv("GDRIVE_PARENT_FOLDER_ID")
    upload_file("GIWANOS_회고_v14_v23.pdf", folder_id)
