
import json
import os
from datetime import datetime

base_path = "./giwanos_auto_loop"
manifest_path = os.path.join(base_path, "memory_manifest.json")
trigger_path = os.path.join(base_path, "gpt_trigger.json")

# 최근 실행 내역 로드
with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

executions = manifest.get("executions", [])[-5:]
actions = [e["action"] for e in executions]

# 단순 규칙 예시:
# - 같은 실행기 3회 이상 반복 → 다른 실행기로 분기
# - 마지막 실패 → 백업 루프 실행
last_action = executions[-1]["action"] if executions else None
last_result = executions[-1]["result"] if executions else None

# 판단 결과 → 다음 실행기 결정
if actions.count(last_action) >= 3:
    next_action = "upload_final_runner.py"
elif last_result == "fail":
    next_action = "zip_backup_generator.py"
else:
    next_action = "file_sort_for_지완OS_v2.py"

# 트리거 생성
trigger = {
    "trigger_id": f"judge_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
    "timestamp": datetime.now().isoformat(),
    "requested_action": next_action,
    "notes": "판단기 자동 트리거"
}

with open(trigger_path, "w", encoding="utf-8") as f:
    json.dump(trigger, f, indent=4, ensure_ascii=False)

print(f"✅ 판단 완료: 다음 실행기 → {next_action}")
