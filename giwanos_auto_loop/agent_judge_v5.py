
import json
import os
from datetime import datetime
from collections import Counter

base_path = "./giwanos_auto_loop"
manifest_path = os.path.join(base_path, "memory_manifest.json")
summary_path = os.path.join(base_path, "reflection_summary.json")
trigger_path = os.path.join(base_path, "gpt_trigger.json")

# 최근 실행 기록 불러오기
executions = []
if os.path.exists(manifest_path):
    with open(manifest_path, "r", encoding="utf-8") as f:
        executions = json.load(f).get("executions", [])[-10:]

# 회고 요약 분석
excluded = []
if os.path.exists(summary_path):
    with open(summary_path, "r", encoding="utf-8") as f:
        summary = json.load(f)
        if "실행 실패" in summary["summary"]:
            excluded.append(summary["action"])

# 실패율 계산
fail_counts = Counter()
total_counts = Counter()
for e in executions:
    a = e["action"]
    total_counts[a] += 1
    if "fail" in e["result"]:
        fail_counts[a] += 1

fail_rate = {a: fail_counts[a] / total_counts[a] for a in total_counts}
excluded += [a for a, r in fail_rate.items() if r >= 0.6]

# 실행기 후보
candidates = ["file_sort_for_지완OS_v2.py", "upload_final_runner.py", "zip_backup_generator.py"]
candidates = [c for c in candidates if c not in excluded]

# 기본 순환 판단
executed = [e["action"] for e in executions]
last = executed[-1] if executed else None
if last in candidates:
    idx = candidates.index(last)
    next_action = candidates[(idx + 1) % len(candidates)]
else:
    next_action = candidates[0] if candidates else "file_sort_for_지완OS_v2.py"

# 트리거 생성
trigger = {
    "trigger_id": f"agent_judge_v5_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
    "timestamp": datetime.now().isoformat(),
    "requested_action": next_action,
    "notes": f"[Agent_Judge_v5] 회고 분석 기반 판단. 제외된 실행기: {excluded}"
}

with open(trigger_path, "w", encoding="utf-8") as f:
    json.dump(trigger, f, indent=4, ensure_ascii=False)

print(f"[Agent_Judge_v5] 판단 완료 → 다음 실행기: {next_action} (제외: {excluded})")
