
import os
import json
import subprocess
from datetime import datetime

base_path = "./giwanos_auto_loop"
trigger_path = os.path.join(base_path, "gpt_trigger.json")
manifest_path = os.path.join(base_path, "memory_manifest.json")
log_path = os.path.join(base_path, "loop_reflection_log.md")

# 1. 트리거 감지
if not os.path.exists(trigger_path):
    print("🚫 트리거 파일이 없습니다.")
    exit()

with open(trigger_path, "r", encoding="utf-8") as f:
    trigger = json.load(f)

trigger_id = trigger.get("trigger_id")
action = trigger.get("requested_action")
notes = trigger.get("notes")

# 2. 판단 로그 작성
now = datetime.now().isoformat()
reflection = f"""## 🧠 루프 실행 - {now}
- Trigger ID: {trigger_id}
- 요청 작업: {action}
- 메모: {notes}
"""

# 3. 실행기 호출
try:
    reflection += f"- 실행 시작: `{action}`\n"
    if action.endswith('.py') and os.path.exists(action):
        result = subprocess.run(["python", action], capture_output=True, text=True, check=True)
        reflection += f"- 실행 출력:\n{result.stdout}\n"
    elif action.endswith('.bat') and os.path.exists(action):
        subprocess.run([action], shell=True, check=True)
    else:
        reflection += f"- ⚠️ 실행기 파일 `{action}`이 존재하지 않음.\n"
except Exception as e:
    reflection += f"- ❌ 실행 중 오류 발생: {e}\n"
else:
    reflection += "- ✅ 실행 완료\n"

# 4. 회고 로그 저장
with open(log_path, "a", encoding="utf-8") as log_file:
    log_file.write(reflection + "\n")

# 5. memory_manifest.json에 기록 추가
if os.path.exists(manifest_path):
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
else:
    manifest = {"version": "1.0", "executions": []}

manifest["executions"].append({
    "timestamp": now,
    "trigger_id": trigger_id,
    "action": action,
    "result": "success" if "✅" in reflection else "fail",
    "notes": notes
})
manifest["last_updated"] = now

with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=4, ensure_ascii=False)

# 6. 트리거 제거
os.remove(trigger_path)

print("✅ 루프 실행 완료 및 기록 저장됨.")
