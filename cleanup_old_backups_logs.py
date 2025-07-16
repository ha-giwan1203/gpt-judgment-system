
import os
import shutil
from datetime import datetime, timedelta

def move_old_files(base_dir, days_old, extensions, archive_dir="archive"):
    now = datetime.now()
    moved_files = []

    for root, _, files in os.walk(base_dir):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                full_path = os.path.join(root, file)
                modified_time = datetime.fromtimestamp(os.path.getmtime(full_path))
                if (now - modified_time).days >= days_old:
                    os.makedirs(archive_dir, exist_ok=True)
                    target_path = os.path.join(archive_dir, file)
                    shutil.move(full_path, target_path)
                    moved_files.append((full_path, target_path))

    return moved_files

def main():
    print("🧼 loop_backups/ 및 logs/ 정리 시작...")

    backups_moved = move_old_files("loop_backups", 7, [".pdf"])
    logs_moved = move_old_files("logs", 10, [".json", ".txt"])

    print(f"✅ 백업 파일 이동 완료: {len(backups_moved)}개")
    print(f"✅ 로그 파일 이동 완료: {len(logs_moved)}개")

    if backups_moved or logs_moved:
        print("\n📦 이동된 파일 목록:")
        for src, dst in backups_moved + logs_moved:
            print(f"→ {os.path.basename(src)} → {dst}")
    else:
        print("📂 이동할 파일이 없습니다.")

if __name__ == "__main__":
    main()
