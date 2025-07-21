import sys
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except AttributeError:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace', line_buffering=True)

import os
from datetime import datetime

base = os.path.dirname(os.path.abspath(__file__))
reflections_dir = os.path.join(base, "..", "..", "reflections")
os.makedirs(reflections_dir, exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
output_file = os.path.join(reflections_dir, "loop_reflection_log.md")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("# GIWANOS 회고 리포트\n")
    f.write(f"생성 시각: {timestamp}\n\n")
    f.write("- 루프: 정리기, PDF 생성기, 전송기, 백업기\n")
    f.write("- 결과: 회고 테스트 완료.\n")

print(f"✅ 회고 리포트 생성 완료: {output_file}")
