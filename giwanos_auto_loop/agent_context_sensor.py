
import os
import json
from datetime import datetime
import random

base_path = "./giwanos_auto_loop"
context_path = os.path.join(base_path, "giwanos_context.json")

# 상황 감지: 시간대, 요일, 파일 수 시뮬레이션
now = datetime.now()
hour = now.hour
weekday = now.weekday()  # 0=월, 6=일
time_slot = "야간" if hour < 6 or hour >= 20 else "오전" if hour < 12 else "오후"

# 파일 수 시뮬레이션 (정리 대상 파일 수)
file_count = random.randint(0, 150)

context = {
    "timestamp": now.isoformat(),
    "hour": hour,
    "weekday": weekday,
    "time_slot": time_slot,
    "file_count": file_count
}

with open(context_path, "w", encoding="utf-8") as f:
    json.dump(context, f, indent=4, ensure_ascii=False)

print(f"[Agent_Context] 상황 기록 완료 → 시간대: {time_slot}, 파일 수: {file_count}")
