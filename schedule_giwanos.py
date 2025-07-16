import schedule
import subprocess
import time
from datetime import datetime

def run_loop():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"⏰ [{now}] 자동 루프 실행 시작")
    subprocess.run(["python", "run_report_bundle.py"])
    print(f"✅ [{now}] 자동 루프 실행 완료")

# ✅ 매일 17:00에 실행 (원하면 시간 변경 가능)
schedule.every().day.at("17:00").do(run_loop)

print("🕒 GIWANOS 스케줄러가 시작되었습니다. 매일 17:00에 루프가 실행됩니다.")
while True:
    schedule.run_pending()
    time.sleep(10)