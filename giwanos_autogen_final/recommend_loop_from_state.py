import json

STATE_FILE = "giwanos_state.json"

try:
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        state = json.load(f)
except FileNotFoundError:
    print("❌ 설치 정보 파일이 없습니다.")
    exit(1)

print("🧠 설치 기준 추천 루프 구성")
print("설치 상태:", state.get("status"))
print("설치 위치:", state.get("installed_path"))
print("추천 루프: judgement_loop → reflection_loop → report_loop → sort_loop")