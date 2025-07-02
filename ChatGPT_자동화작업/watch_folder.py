
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os

WATCH_PATH = "C:/구글지완/ChatGPT_자동화작업"

class ChangeHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"🟡 새 파일 감지됨: {event.src_path}")
            run_sort()

    def on_modified(self, event):
        if not event.is_directory:
            print(f"🔵 파일 수정 감지됨: {event.src_path}")
            run_sort()

def run_sort():
    print("🔁 file_sort.py 실행 중...")
    subprocess.run(["python", "C:/구글지완/ChatGPT_자동화작업/file_sort.py"], check=False)
    print("✅ 정리 완료.")

if __name__ == "__main__":
    print(f"👁 감시 시작: {WATCH_PATH}")
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_PATH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
