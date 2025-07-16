
import json
from datetime import datetime
import os

base_path = "./giwanos_auto_loop"
trigger_path = os.path.join(base_path, "gpt_trigger.json")

trigger = {
    "trigger_id": f"auto_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
    "timestamp": datetime.now().isoformat(),
    "requested_action": "file_sort_for_지완OS_v2.py",
    "notes": "자동 트리거 테스트"
}

with open(trigger_path, "w", encoding="utf-8") as f:
    json.dump(trigger, f, indent=4, ensure_ascii=False)

print(f"✅ 트리거 자동 생성됨: {trigger['trigger_id']}")
