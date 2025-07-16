import os
import shutil
from datetime import datetime

# 백업 대상 파일 목록
backup_targets = [
    "loop_config_giwanos.json",
    "memory_manifest_정리루프.json",
    "memory_manifest_보고루프.json",
    "memory_manifest_진화루프.json",
    ".env_giwanos_template"
]

def make_backup():
    backup_root = ".backup"
    date_folder = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    full_path = os.path.join(backup_root, date_folder)
    os.makedirs(full_path, exist_ok=True)

    print(f"🛡️ 메모리 백업 시작 → {full_path}")
    for file in backup_targets:
        if os.path.exists(file):
            shutil.copy(file, os.path.join(full_path, file))
            print(f"✅ 백업됨: {file}")
        else:
            print(f"⚠️ 파일 없음 (건너뜀): {file}")
    print("📦 백업 완료")

if __name__ == "__main__":
    make_backup()