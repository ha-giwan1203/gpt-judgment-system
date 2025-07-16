
# ✅ 루프 트리거 상태 점검기
import json
import os

def check_trigger_status():
    path = "trigger_execution_log.json"
    if not os.path.exists(path):
        print("❗ 실행 기록 없음")
        return

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        if not data:
            print("❗ 기록 없음")
        else:
            print(f"✅ 최근 실행: {data[-1].get('timestamp')} / 루프: {data[-1].get('loop')}")

if __name__ == "__main__":
    check_trigger_status()
