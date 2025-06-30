# ✅ tools/create_clean_zip.py - 민감 정보 제외된 배포용 zip 생성기
import os
import zipfile
from datetime import datetime

ZIP_NAME = f"GPT_Upload_System_CLEAN_{datetime.now().strftime('%Y%m%d')}.zip"
EXCLUDE = [
    "token.json",
    "client_secrets.json",
    "README_구글연동_기록.txt",
    ".git",
    "__pycache__",
    ".log"
]

with zipfile.ZipFile(ZIP_NAME, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for foldername, subfolders, filenames in os.walk("."):
        if any(ex in foldername for ex in EXCLUDE):
            continue
        for filename in filenames:
            if any(filename.endswith(ext) for ext in [".pyc", ".log"]):
                continue
            if filename in EXCLUDE:
                continue
            filepath = os.path.join(foldername, filename)
            arcname = os.path.relpath(filepath, start=".")
            zipf.write(filepath, arcname)

print(f"[✓] 민감 정보 제외된 CLEAN 버전 압축 완료 → {ZIP_NAME}")
