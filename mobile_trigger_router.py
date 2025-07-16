
# ✅ 모바일 명령 전용 루프 감지 라우터
import os
import json

def detect_trigger_and_route():
    try:
        with open("gpt_trigger.json", "r", encoding="utf-8") as f:
            trigger = json.load(f)
        cmd = trigger.get("command")
        if cmd:
            print(f"📥 감지된 명령: {cmd}")
            os.system(cmd)
        else:
            print("❗ 명령이 비어 있음")
    except Exception as e:
        print("🚫 트리거 감지 실패:", e)

if __name__ == "__main__":
    detect_trigger_and_route()
