
# 🧠 오른팔 + Google Drive 연동 감시 시스템

import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from 오른팔 import 오른팔_기록
import random

# 감시 대상 폴더 (로컬 드라이브에 Google Drive가 동기화된 폴더)
WATCH_FOLDER = "C:/구글지완"  # 필요 시 경로 수정

# 키워드 분류 기준 (예시)
KEYWORDS = {
    "급여": "/01_문서자료/급여",
    "보고서": "/02_보고서",
    "계약": "/03_계약서",
}

def 분류_경로_결정(파일명):
    for 키워드, 경로 in KEYWORDS.items():
        if 키워드 in 파일명:
            return 경로, "완료"
    return "/99_분류불가", "예외"

class 감시핸들러(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        파일경로 = event.src_path
        파일명 = os.path.basename(파일경로)
        확장자 = os.path.splitext(파일명)[-1].lower()
        크기 = os.path.getsize(파일경로) // 1024  # KB 단위

        분류경로, 상태 = 분류_경로_결정(파일명)

        try:
            오른팔_기록(
                파일명=파일명,
                경로=분류경로,
                상태=상태,
                설명="자동 감시 기록",
                크기=크기,
                유형="기타" if 상태 != "완료" else "문서",
                태그=["감시", "자동"],
                결과ID=f"watch-{random.randint(1000,9999)}"
            )
            print(f"📦 정리됨: {파일명}")
        except Exception as e:
            print(f"❌ 기록 실패: {파일명} | 오류: {e}")

if __name__ == "__main__":
    print(f"👀 감시 시작: {WATCH_FOLDER}")
    event_handler = 감시핸들러()
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("🛑 감시 중단됨.")

    observer.join()
