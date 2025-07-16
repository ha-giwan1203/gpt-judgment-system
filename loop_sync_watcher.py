import os
import json
import time
from datetime import datetime

WATCH_DIR = "C:/giwanos"
LOG_PATH = "logs/loop_local_sync_log.json"
EXTENSIONS = [".py", ".json", ".pdf", ".zip"]

def scan_directory(root):
    synced = []
    for root_dir, _, files in os.walk(root):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in EXTENSIONS:
                full_path = os.path.join(root_dir, f)
                try:
                    stats = os.stat(full_path)
                    synced.append({
                        "filename": f,
                        "path": os.path.relpath(full_path, WATCH_DIR),
                        "size": stats.st_size,
                        "last_modified": datetime.fromtimestamp(stats.st_mtime).isoformat()
                    })
                except Exception as e:
                    continue
    return synced

def save_log(synced_list):
    os.makedirs("logs", exist_ok=True)
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(synced_list, f, indent=2, ensure_ascii=False)
    print(f"✅ 로컬 상태 동기화 완료 → {LOG_PATH}")

if __name__ == "__main__":
    print(f"🧠 로컬 감시 시작: {WATCH_DIR}")
    synced_data = scan_directory(WATCH_DIR)
    save_log(synced_data)