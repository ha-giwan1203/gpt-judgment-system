
# ✅ GIWANOS 철학 위배 방지용 실행 전 검사기
import json
import os
import sys
from dotenv import load_dotenv

load_dotenv()

def check_design_integrity():
    try:
        with open("GIWANOS_PHILOSOPHY.json", "r", encoding="utf-8") as f:
            philosophy = json.load(f)
    except Exception as e:
        print("🚫 철학 기준 파일을 불러올 수 없습니다:", e)
        sys.exit(1)

    if philosophy.get("enforce_mobile_command_only") and os.getenv("GIWANOS_MODE") == "desktop":
        print("🚫 데스크탑에서 직접 실행이 차단되었습니다. 모바일 명령만 허용됩니다.")
        sys.exit(1)

    print("✅ 철학 기준 통과")

if __name__ == "__main__":
    check_design_integrity()
