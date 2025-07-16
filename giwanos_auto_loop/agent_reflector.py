
import json
import os
from datetime import datetime

base_path = "./giwanos_auto_loop"
manifest_path = os.path.join(base_path, "memory_manifest.json")
reflection_path = os.path.join(base_path, "loop_reflection_log.md")

# 회고 내용 구성
now = datetime.now().isoformat()
reflection = f"""## 🧠 루프 실행 회고 - {now}
- 상태: 실행기 호출 완료 여부 확인 필요
- 메모리 기록: {manifest_path}
- 회고 요약: 실행기 호출 시 파일 존재하지 않음 (경로 점검 필요)
"""

# 회고 로그 저장
with open(reflection_path, "a", encoding="utf-8") as f:
    f.write(reflection + "\n")

print("[Agent_Reflector] 회고 내용 저장 완료")
