import os
import time
import json
from datetime import datetime

WATCH_PATH = "./trigger_input"
TRIGGER_FILE = "gpt_trigger.json"
LOG_FILE = "trigger_execution.log"

def load_trigger_state():
    path = os.path.join(WATCH_PATH, TRIGGER_FILE)
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def log_execution(trigger_content):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] Trigger executed:\n")
        f.write(json.dumps(trigger_content, ensure_ascii=False, indent=2))
        f.write("\n\n")

def main():
    print("👀 Watching for trigger file changes...")
    before = {}
    while True:
        try:
            time.sleep(2)
            path = os.path.join(WATCH_PATH, TRIGGER_FILE)
            if not os.path.exists(path):
                continue
            stat = os.stat(path)
            after = {TRIGGER_FILE: stat.st_mtime}
            modified = {f for f in before if (f in after and before[f] != after[f])}
            if modified:
                trigger = load_trigger_state()
                log_execution(trigger)
                print(f"✅ Trigger detected and logged at {datetime.now()}")
            before = after
        except KeyboardInterrupt:
            print("👋 Watcher stopped by user.")
            break
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()