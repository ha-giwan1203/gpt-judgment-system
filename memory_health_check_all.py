#!/usr/bin/env python
import sys
import io
# ─── 윈도우 콘솔을 UTF-8로 재설정 ──────────────────────────────────
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
# ────────────────────────────────────────────────────────────────

import os
import subprocess
from datetime import datetime

BASE = os.getcwd()
LOG_PATH = os.path.join(BASE, "memory_diagnosis_log.md")
errors = []

def run_and_log(script, log_file):
    try:
        out = subprocess.check_output(
            [sys.executable, script],
            stderr=subprocess.STDOUT,
            text=True, encoding="utf-8", errors="replace"
        )
        with open(log_file, "a", encoding="utf-8") as lf:
            lf.write(f"## [{datetime.now():%Y-%m-%d %H:%M:%S}] {script}\n\n")
            lf.write(out + "\n")
    except subprocess.CalledProcessError as e:
        errors.append(f"{script} failed: {e.output.strip()}")

if __name__ == "__main__":
    # 기존 로그 파일 초기화
    with open(LOG_PATH, "w", encoding="utf-8") as lf:
        lf.write(f"# Memory Health Check Log ({datetime.now():%Y-%m-%d %H:%M:%S})\n\n")

    # 1) memory_loader
    run_and_log("memory_loader.py", LOG_PATH)
    # 2) memory_compressor
    run_and_log("memory_compressor.py", LOG_PATH)
    # 3) memory_guard
    run_and_log("memory_guard.py", LOG_PATH)
    # 4) memory_updater
    run_and_log("memory_updater.py", LOG_PATH)

    # 완료 메시지 (이모지도 OK)
    print(f"📄 진단 결과가 {LOG_PATH}에 저장되었습니다.")