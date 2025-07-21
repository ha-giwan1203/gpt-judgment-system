import sys
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except AttributeError:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace', line_buffering=True)

import os
import sys

# 루트 기준 상대경로로 상위 3단계까지 올려서 sys.path 등록
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if BASE not in sys.path:
    sys.path.insert(0, BASE)

from send_slack_report import send_slack_message
from upload_notion_safe import upload_to_notion

print("📤 전송기 시작")

# Slack 메시지 전송
send_slack_message("✅ GIWANOS Slack 전송 테스트 완료")

# 회고 리포트 경로 (루트 기준)
reflection_path = os.path.join(BASE, "reflections", "loop_reflection_log.md")

if os.path.exists(reflection_path):
    print(f"📄 회고 파일 발견: {reflection_path}")
    upload_to_notion(reflection_path, page_title="GIWANOS 회고 리포트")
else:
    print(f"❌ 회고 파일 없음: {reflection_path}")

print("✅ 전송기 완료")
