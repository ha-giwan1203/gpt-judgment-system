
import json
import os
from datetime import datetime

base_path = "./giwanos_auto_loop"
status_path = os.path.join(base_path, "pc_status.json")
guard_result_path = os.path.join(base_path, "local_guard_result.json")

if not os.path.exists(status_path):
    print("[Agent_LocalGuard] pc_status.json 없음")
    exit()

with open(status_path, "r", encoding="utf-8") as f:
    status = json.load(f)

# 완화된 정책: User 또는 DESKTOP-MH0F8GQ 허용
hostname = status.get("hostname", "")
user = status.get("user", "").lower()

host_ok = hostname in ["GPC-DAEWON01", "GPC-HOME", "DESKTOP-MH0F8GQ"]
user_ok = user in ["jhajiwan", "user"]

disk_ok = status["disk_usage_percent"] < 95

reason = []
if not host_ok:
    reason.append("🚫 허용되지 않은 hostname")
if not user_ok:
    reason.append("🚫 허용되지 않은 사용자")
if not disk_ok:
    reason.append("🚫 디스크 사용량 초과")

result = {
    "timestamp": datetime.now().isoformat(),
    "hostname": hostname,
    "user": user,
    "disk_usage_percent": status["disk_usage_percent"],
    "host_ok": host_ok,
    "user_ok": user_ok,
    "disk_ok": disk_ok,
    "allow_loop": host_ok and user_ok and disk_ok,
    "block_reason": reason
}

with open(guard_result_path, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

if result["allow_loop"]:
    print("[Agent_LocalGuard] ✅ 루프 실행 허용")
else:
    print(f"[Agent_LocalGuard] 루프 실행 차단 → {' | '.join(reason)}")
