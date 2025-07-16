
import zipfile
import os
from datetime import datetime

base_path = "./giwanos_auto_loop"
backup_dir = "./giwanos_auto_loop/backups"
os.makedirs(backup_dir, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_name = f"loop_backup_{timestamp}.zip"
backup_path = os.path.join(backup_dir, backup_name)

with zipfile.ZipFile(backup_path, 'w') as zipf:
    for folder, _, files in os.walk(base_path):
        for file in files:
            if not file.endswith(".zip"):
                file_path = os.path.join(folder, file)
                zipf.write(file_path, os.path.relpath(file_path, base_path))

print(f"✅ 백업 생성 완료: {backup_name}")
