import time
import os
from pathlib import Path

WATCH_DIR = Path(".").resolve()
LOG_FILE = WATCH_DIR / "trigger_execution.log"

def snapshot(dir_path):
    return {f: os.path.getmtime(f) for f in dir_path.glob("*") if f.is_file()}

def write_log(msg):
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")
    print(f"📍 감지됨: {msg}")

print(f"👀 감시 시작: {WATCH_DIR}")
before = snapshot(WATCH_DIR)

while True:
    time.sleep(1)
    after = snapshot(WATCH_DIR)
    added = set(after.keys()) - set(before.keys())
    removed = set(before.keys()) - set(after.keys())
    modified = {f for f in before if f in after and before[f] != after[f]]

    for f in added:
        write_log(f"🆕 추가됨: {f.name}")
    for f in removed:
        write_log(f"❌ 삭제됨: {f.name}")
    for f in modified:
        write_log(f"✏️ 수정됨: {f.name}")

    before = after