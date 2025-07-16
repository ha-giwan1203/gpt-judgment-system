
import time
import json
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

TRIGGER_PATH = "gpt_trigger.json"
WATCH_PATH = "C:/giwanos/"

class TriggerHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            data = {
                "path": event.src_path,
                "event": "modified",
                "timestamp": time.time()
            }
            with open(TRIGGER_PATH, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            print(f"[🟡 Trigger] 변경 감지: {event.src_path}")

if __name__ == "__main__":
    event_handler = TriggerHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_PATH, recursive=True)
    observer.start()
    print(f"🔄 감시 시작: {WATCH_PATH}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
