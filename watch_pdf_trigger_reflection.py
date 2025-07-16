import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

# 절대 경로로 지정 (실제 폴더에 맞게)
WATCH_FOLDER = os.path.abspath("./reports/summary_pdfs")

class PDFTriggerHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith(".pdf") and "loop_summary_report" in event.src_path:
            print(f"🧠 새 회고 PDF 감지됨: {event.src_path}")
            subprocess.run(["python", "generate_reflection_pdf.py"], check=True)

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(PDFTriggerHandler(), path=WATCH_FOLDER, recursive=False)
    observer.start()
    print(f"👀 감지기 실행 중... 감시 폴더: {WATCH_FOLDER} (Ctrl+C로 중지)")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("🛑 감지기 중단됨.")
        observer.stop()
    observer.join()