#!/usr/bin/env python
import sys
import io
# 윈도우 콘솔을 UTF-8로 재설정
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import os
import json

def run_self_check():
    """
    시스템의 메모리 구성요소 및 진단 로그 파일들이 모두 올바르게 존재하고 유효한지 검사합니다.
    """
    errors = []
    base_dir = os.getcwd()

    # 검사 대상 파일 목록
    expected_files = [
        'memory_timeline.json',
        'restore_prompt.txt',
        'memory_loader.py',
        'install_memory_system.py',
        'memory_health_check_all.py',
        'memory_dashboard.md',
        'README.md',
        'memory_compressed.json',
        'memory_diagnosis_log.md'
    ]

    for fname in expected_files:
        fpath = os.path.join(base_dir, fname)
        if not os.path.exists(fpath):
            errors.append(f"Missing file: {fname}")

    # JSON 파일 유효성 검사
    for jfile in ['memory_timeline.json', 'memory_compressed.json']:
        jpath = os.path.join(base_dir, jfile)
        if os.path.exists(jpath):
            try:
                with open(jpath, 'r', encoding='utf-8') as jf:
                    json.load(jf)
            except Exception as e:
                errors.append(f"Invalid JSON in {jfile}: {e}")

    # 결과 출력
    if errors:
        print("🚨 Self-check detected issues:")
        for err in errors:
            print(f"- {err}")
        sys.exit(1)

if __name__ == "__main__":
    run_self_check()
    # SELF CHECK 완료 메시지 출력
    print("✅ memory_self_check.py: SELF CHECK OK")
