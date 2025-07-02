import os

def find_google_drive():
    candidates = [
        os.path.expanduser("~\\내 드라이브"),
        "G:\\내 드라이브",
        "D:\\GoogleDrive",
        "C:\\GoogleDrive",
    ]
    for path in candidates:
        if os.path.exists(path):
            print(f"✅ Google Drive 폴더 발견: {path}")
            return path
    print("❌ Google Drive 폴더를 찾을 수 없습니다. 설정을 확인해주세요.")
    return None

# 예시 실행:
# drive_path = find_google_drive()
