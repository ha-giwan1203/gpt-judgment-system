# ✅ tools/create_final_zip.py - 시스템 전체 최종 압축 패키지 생성기
import os
import zipfile
from datetime import datetime

ZIP_NAME = f"GPT_Upload_System_vFinal_{datetime.now().strftime('%Y%m%d')}.zip"
EXCLUDE_EXT = [".pyc", ".log"]
EXCLUDE_DIR = ["__pycache__", ".git"]

with zipfile.ZipFile(ZIP_NAME, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for foldername, subfolders, filenames in os.walk("."):
        foldername = foldername.replace("./", "")
        if any(ex in foldername for ex in EXCLUDE_DIR):
            continue
        for filename in filenames:
            if any(filename.endswith(ext) for ext in EXCLUDE_EXT):
                continue
            filepath = os.path.join(foldername, filename)
            arcname = os.path.relpath(filepath, start=".")
            zipf.write(filepath, arcname)

print(f"[✓] 최종 시스템 압축 완료 → {ZIP_NAME}")
