# run_giwanos_v16_loop.py (patched with route_log from v15 path)
import json
from datetime import datetime

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def main():
    log("🚀 GIWANOS v16 루프 피드백 분석기 시작")
    path = "C:/giwanos/v15/giwanos_path_loop/route_log.json"
    try:
        with open(path, "r", encoding="utf-8") as f:
            logs = json.load(f)
        if not logs:
            log("⚠️ route_log.json은 비어 있음")
            return
        log("📊 최근 추천 경로 분석 결과:")
        latest = logs[-1]
        print(f"🕒 입력 시간: {latest['timestamp']}")
        print(f"🧠 입력 내용: {latest['input']}")
        print("🧭 추천 경로:")
        for r in latest["route"]:
            print(f"→ {r}")
    except FileNotFoundError:
        log("❌ route_log.json 파일을 찾을 수 없습니다.")
    except Exception as e:
        log(f"❌ 분석 실패: {e}")

if __name__ == "__main__":
    main()
