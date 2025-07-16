import os
import shutil
import json
from datetime import datetime

SOURCE_DIR = "pending_to_sync"
TARGET_DIR = "C:/giwanos"
LOG_PATH = "logs/loop_auto_apply_log.json"

def scan_pending_files():
    files = []
    for dirpath, _, filenames in os.walk(SOURCE_DIR):
        for name in filenames:
            src_path = os.path.join(dirpath, name)
            rel = os.path.relpath(src_path, SOURCE_DIR)
            tgt_path = os.path.join(TARGET_DIR, rel)
            files.append((src_path, tgt_path, rel))
    return files

def copy_and_log(files):
    log_entries = []
    for src, tgt, rel in files:
        os.makedirs(os.path.dirname(tgt), exist_ok=True)
        try:
            shutil.copy2(src, tgt)
            entry = {
                "path": rel,
                "status": "✅ 복사됨",
                "time": datetime.now().isoformat()
            }
            log_entries.append(entry)
            print(f"📥 적용됨: {rel}")
        except Exception as e:
            entry = {
                "path": rel,
                "status": f"❌ 오류: {e}",
                "time": datetime.now().isoformat()
            }
            log_entries.append(entry)
            print(f"❌ 실패: {rel}")

    if log_entries:
        os.makedirs("logs", exist_ok=True)
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            for entry in log_entries:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    print("📦 지니 → 로컬 자동 반영기 시작")
    if not os.path.exists(SOURCE_DIR):
        print(f"❗ {SOURCE_DIR} 폴더가 없습니다.")
    else:
        files = scan_pending_files()
        if files:
            copy_and_log(files)
        else:
            print("✅ 적용할 파일이 없습니다.")