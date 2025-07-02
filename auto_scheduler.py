import schedule
import time
import os
from datetime import datetime

def run_restore_and_dispatch():
    print(f"⏰ [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 자동 복원 및 보고 실행 중...")
    os.system("python memory_restorer.py")
    os.system("python report_auto_dispatcher.py")

# 매일 오전 08:00에 실행 (원하면 시간 수정 가능)
schedule.every().day.at("08:00").do(run_restore_and_dispatch)

print("✅ 자동 복원 + 보고 스케줄러가 시작되었습니다. (매일 08:00 실행)")

while True:
    schedule.run_pending()
    time.sleep(10)
