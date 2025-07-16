
import json
import os
from datetime import datetime

base_path = "./giwanos_auto_loop"
goals_path = os.path.join(base_path, "giwanos_goals.json")
context_path = os.path.join(base_path, "giwanos_context.json")
status_path = os.path.join(base_path, "pc_status.json")
trigger_path = os.path.join(base_path, "gpt_trigger.json")

# 로딩
with open(goals_path, "r", encoding="utf-8") as f:
    goals = json.load(f)["goals"]

with open(context_path, "r", encoding="utf-8") as f:
    context = json.load(f)

with open(status_path, "r", encoding="utf-8") as f:
    status = json.load(f)

# 통합된 현재 상황
env = {**context, **status}

# 조건 평가 함수
def eval_conditions(conds, env):
    try:
        return all(eval(cond, {}, env) for cond in conds)
    except:
        return False

# 우선순위 판단
selected = None
for goal, spec in goals.items():
    if eval_conditions(spec["conditions"], env):
        selected = spec["preferred_action"]
        break

if not selected:
    selected = "file_sort_for_지완OS_v2.py"

# 트리거 생성
trigger = {
    "trigger_id": f"agent_judge_goals_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
    "timestamp": datetime.now().isoformat(),
    "requested_action": selected,
    "notes": f"[Agent_Judge_Goals] 목적 기반 판단 실행"
}

with open(trigger_path, "w", encoding="utf-8") as f:
    json.dump(trigger, f, indent=4, ensure_ascii=False)

print(f"[Agent_Judge_Goals] 판단 완료 → 다음 실행기: {selected}")
