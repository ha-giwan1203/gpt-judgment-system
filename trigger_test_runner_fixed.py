import time
from pathlib import Path

# 현재 실행 중인 디렉토리 기준
WATCH_DIR = Path(".").resolve()
LOG_FILE = WATCH_DIR / "trigger_execution.log"
TEST_FILE = WATCH_DIR / "test_trigger_check.txt"

# 테스트 파일 생성
with open(TEST_FILE, "w", encoding="utf-8") as f:
    f.write("감지기 테스트 실행됨")

# 로그 기록
with open(LOG_FILE, "a", encoding="utf-8") as f:
    f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ✅ 감지기 테스트: test_trigger_check.txt 생성됨\n")

print("✅ 테스트 트리거 실행 완료 →", TEST_FILE.name)