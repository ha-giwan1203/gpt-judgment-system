import sys
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except AttributeError:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace', line_buffering=True)

import zipfile
import os
from pathlib import Path
from datetime import datetime

base_path = Path(__file__).resolve().parent
folders = ["_보존", "_정리_후보", "_검토_필요", "_분류불가"]
output_dir = base_path / "loop_backups"
output_dir.mkdir(parents=True, exist_ok=True)

def create_backup():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"giwanos_backup_{timestamp}.zip"
    zip_path = output_dir / zip_name

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for folder in folders:
            folder_path = base_path / folder
            if not folder_path.exists():
                continue
            for file in folder_path.glob("*"):
                arcname = f"{folder}/{file.name}"
                zipf.write(file, arcname)
    print("✅ 백업 완료:", zip_path)

if __name__ == "__main__":
    create_backup()
