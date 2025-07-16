import os
import time
import json
from datetime import datetime

# 감지 대상 폴더와 조건
WATCH_FOLDER = "input_data"
TRIGGER_FILE = "gpt_trigger.json"
LOG_FILE = "logs/folder_trigger_log.txt"
FILENAME_KEYWORDS = ["입력", "실적", "GERP"]

# 이전 상태 저장
seen_files = set()

def log(msg):
    now = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{now} {msg}\n")
    print(f"{now} {msg}")

def trigger_loop():
    # 회고 트리거 자동 갱신
    trigger = { "action": "회고" }
    with open(TRIGGER_FILE, "w", encoding="utf-8") as f:
        json.dump(trigger, f, ensure_ascii=False, indent=2)
    log("✅ 트리거 업데이트됨 → 회고 루프 실행 예정")

def watch_folder():
    log(f"📁 폴더 감지기 시작: {WATCH_FOLDER}")
    os.makedirs(WATCH_FOLDER, exist_ok=True)
    global seen_files
    while True:
        try:
            current_files = set(os.listdir(WATCH_FOLDER))
            new_files = [f for f in current_files - seen_files if any(k in f for k in FILENAME_KEYWORDS)]
            if new_files:
                log(f"📂 새로운 실적 파일 감지됨: {new_files}")
                trigger_loop()
            seen_files = current_files
            time.sleep(5)
        except KeyboardInterrupt:
            log("🛑 폴더 감지기 종료됨")
            break
        except Exception as e:
            log(f"❌ 오류 발생: {e}")
            time.sleep(10)

if __name__ == "__main__":
    watch_folder()