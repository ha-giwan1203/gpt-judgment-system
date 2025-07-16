import json
from pathlib import Path

PROFILE_PATH = Path("logs/user_profiles.json")
ACCESS_PATH = Path("logs/loop_access_control.json")

def get_user_routes(user_id):
    profiles = json.load(open(PROFILE_PATH, encoding="utf-8")) if PROFILE_PATH.exists() else {}
    access = json.load(open(ACCESS_PATH, encoding="utf-8")) if ACCESS_PATH.exists() else {}

    profile = profiles.get(user_id)
    if not profile:
        return f"❌ 사용자 '{user_id}' 프로필 없음"

    role = profile.get("role", "guest")
    allowed = access.get(role, [])
    return {
        "user": user_id,
        "role": role,
        "location": profile.get("location", "N/A"),
        "allowed_loops": allowed
    }

if __name__ == "__main__":
    result = get_user_routes("지완")
    print(result)