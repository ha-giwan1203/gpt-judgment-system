
import os
import socket
import getpass
import json
import platform
import psutil

base_path = "./giwanos_auto_loop"
roles_path = os.path.join(base_path, "device_roles.json")
status_path = os.path.join(base_path, "pc_status.json")

# 현재 디바이스 정보 수집
hostname = socket.gethostname()
user = getpass.getuser()
disk_usage = psutil.disk_usage('/').percent

new_device = {
    "type": "자동등록",
    "allowed_actions": [
        "file_sort_for_지완OS_v2.py",
        "zip_backup_generator.py"
    ],
    "policy": {
        "max_disk_usage": 90,
        "allow_night": True
    }
}

# 기존 roles 불러오기
if os.path.exists(roles_path):
    with open(roles_path, "r", encoding="utf-8") as f:
        roles = json.load(f)
else:
    roles = {"devices": {}}

# 등록
roles["devices"][hostname] = new_device

with open(roles_path, "w", encoding="utf-8") as f:
    json.dump(roles, f, indent=4, ensure_ascii=False)

print(f"[Agent_Register_Device] 등록 완료 → Host: {hostname}, User: {user}, Disk: {disk_usage}%")
