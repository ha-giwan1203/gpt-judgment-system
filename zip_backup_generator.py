# zip_backup_generator.py (timestamped version)
import zipfile
import os
from datetime import datetime

def generate_zip_backup():
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"loop_backup_{now}.zip"
    base_dir = "C:/giwanos"
    zip_path = os.path.join(base_dir, "loop_backups", zip_name)

    os.makedirs(os.path.dirname(zip_path), exist_ok=True)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in os.listdir(base_dir):
            if file.lower().endswith((".pdf", ".json", ".txt")) and "loop" in file.lower():
                zipf.write(os.path.join(base_dir, file), arcname=file)

    print(f"✅ 백업 생성 완료: {zip_name}")

if __name__ == "__main__":
    generate_zip_backup()
