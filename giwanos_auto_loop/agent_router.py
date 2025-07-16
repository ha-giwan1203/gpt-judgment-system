
import json
import os
from datetime import datetime

base_path = "./giwanos_auto_loop"
status_path = os.path.join(base_path, "pc_status.json")
roles_path = os.path.join(base_path, "device_roles.json")
trigger_path = os.path.join(base_path, "gpt_trigger.json")

if not os.path.exists(status_path) or not os.path.exists(roles_path):
    print("[Agent_Router] 필수 정보 없음")
    exit()

with open(status_path, "r", encoding="utf-8") as f:
    pc = json.load(f)

with open(roles_path, "r", encoding="utf-8") as f:
    roles = json.load(f)["devices"]

hostname = pc.get("hostname")
role = roles.get(hostname)

if not role:
    print(f"[Agent_Router] 🚫 디바이스({hostname})는 등록되지 않음")
    exit()

# 정책 확인
allowed = role.get("allowed_actions", [])
policy = role.get("policy", {})
disk_ok = pc.get("disk_usage_percent", 100) < policy.get("max_disk_usage", 100)
night_ok = True
if not policy.get("allow_night", True):
    hour = pc.get("timestamp", "").split("T")[1][:2]
    night_ok = not (int(hour) < 6 or int(hour) >= 20)

if not disk_ok or not night_ok:
    print(f"[Agent_Router] 🚫 정책 조건 위배: Disk OK = {disk_ok}, Night OK = {night_ok}")
    exit()

if not allowed:
    print(f"[Agent_Router] 🚫 실행기 없음: {hostname}")
    exit()

# 기본 실행기 선택
selected = allowed[0]

trigger = {
    "trigger_id": f"agent_router_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
    "timestamp": datetime.now().isoformat(),
    "requested_action": selected,
    "notes": f"[Agent_Router] 정책 기반 실행기 결정"
}

with open(trigger_path, "w", encoding="utf-8") as f:
    json.dump(trigger, f, indent=4, ensure_ascii=False)

print(f"[Agent_Router] ✅ 루프 실행 결정 → {selected} (호스트: {hostname})")
