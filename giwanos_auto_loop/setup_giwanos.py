
import os
import json
import platform
import getpass
import socket
import psutil

base_path = "./giwanos_auto_loop"
os.makedirs(base_path, exist_ok=True)

# 기본 파일들
status = {
    "hostname": socket.gethostname(),
    "user": getpass.getuser(),
    "os": platform.system(),
    "disk_usage_percent": psutil.disk_usage('/').percent
}
context = {
    "hour": 12,
    "weekday": 1,
    "time_slot": "오전",
    "file_count": 10
}
roles = {
    "devices": {
        socket.gethostname(): {
            "type": "자동등록",
            "allowed_actions": [
                "file_sort_for_지완OS_v2.py",
                "zip_backup_generator.py"
            ],
            "policy": {
                "max_disk_usage": 95,
                "allow_night": True
            }
        }
    }
}

files = {
    "pc_status.json": status,
    "giwanos_context.json": context,
    "device_roles.json": roles,
    "memory_manifest.json": {"version": "1.0", "executions": []}
}

for name, content in files.items():
    with open(os.path.join(base_path, name), "w", encoding="utf-8") as f:
        json.dump(content, f, indent=4, ensure_ascii=False)

print("[Setup_GIWANOS] 기본 구조 및 파일 생성 완료.")
