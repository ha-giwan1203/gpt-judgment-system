
import os
import socket
import getpass
import json
import platform
import psutil
from datetime import datetime

base_path = "./giwanos_auto_loop"
status_path = os.path.join(base_path, "pc_status.json")

status = {
    "timestamp": datetime.now().isoformat(),
    "hostname": socket.gethostname(),
    "user": getpass.getuser(),
    "os": platform.system(),
    "platform": platform.platform(),
    "cpu_count": psutil.cpu_count(),
    "ram_total_gb": round(psutil.virtual_memory().total / (1024 ** 3), 2),
    "disk_usage_percent": psutil.disk_usage('/').percent,
    "ip": socket.gethostbyname(socket.gethostname())
}

with open(status_path, "w", encoding="utf-8") as f:
    json.dump(status, f, indent=4, ensure_ascii=False)

print(f"[Agent_PC_Status] 로컬 상태 저장 완료 → Host: {status['hostname']}, User: {status['user']}, Disk: {status['disk_usage_percent']}%")
