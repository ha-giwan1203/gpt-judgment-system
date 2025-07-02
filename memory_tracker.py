import os
import json
from datetime import datetime
from difflib import unified_diff

RESTORE_FILE = "restore_prompt.txt"
SNAPSHOT_FILE = ".last_restore_snapshot.txt"
BACKUP_DIR = "memory_backup"
LOG_FILE = "memory_change_log.json"

def load_text(path):
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def save_text(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def track_changes():
    current = load_text(RESTORE_FILE)
    previous = load_text(SNAPSHOT_FILE)

    if current is None:
        print("⚠️ restore_prompt.txt가 없습니다.")
        return

    if current == previous:
        print("✅ 변화 없음: 복원 프롬프트가 동일합니다.")
        return

    # 변화 감지
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    ensure_dir(BACKUP_DIR)
    backup_path = os.path.join(BACKUP_DIR, f"restore_backup_{now}.txt")
    save_text(backup_path, current)
    save_text(SNAPSHOT_FILE, current)

    # diff 생성
    diff_lines = list(unified_diff(
        previous.splitlines() if previous else [],
        current.splitlines(),
        fromfile="이전",
        tofile="현재",
        lineterm=""
    ))

    print("🔄 변화 감지됨! 백업 및 기록 완료.")
    print("\n".join(diff_lines[-10:]))  # 최근 변경 요약 출력

    # 로그 기록
    log_entry = {
        "timestamp": now,
        "diff": diff_lines
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    track_changes()
