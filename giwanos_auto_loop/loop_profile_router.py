import json
from pathlib import Path

PROFILE_PATH = Path("logs/user_profile.json")
ROUTE_CONFIG_PATH = Path("logs/loop_profile_routes.json")

def route_loop_by_profile():
    if not PROFILE_PATH.exists():
        print("❌ 사용자 프로파일 없음")
        return

    profile = json.load(open(PROFILE_PATH, encoding="utf-8"))
    role = profile.get("role", "default")
    location = profile.get("location", "모바일")

    # 사용자 역할 + 위치 기반 루프 추천
    routes = json.load(open(ROUTE_CONFIG_PATH, encoding="utf-8")) if ROUTE_CONFIG_PATH.exists() else {}

    matched_route = routes.get(role, {}).get(location, [])
    if matched_route:
        print(f"✅ 사용자 '{role}' @ {location} → 추천 루프: {matched_route}")
    else:
        print(f"📭 설정된 루프 없음 for {role} @ {location}")

if __name__ == "__main__":
    route_loop_by_profile()