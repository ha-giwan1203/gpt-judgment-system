
@echo off
echo [1] 🧠 철학 기준 검사 시작
python design_integrity_checker.py

echo [2] 🛡 철학 감시 로그 기록
python loop_philosophy_guard.py

echo [3] 📤 회고 결과 Slack 전송
python upload_feedback_result_slack.py

echo [4] 📦 회고 PDF ZIP 백업
python loop_zip_backup_rotator.py

echo [5] 🔎 트리거 상태 확인
python loop_trigger_status_checker.py

echo ✅ GIWANOS 루프 전체 실행 완료.
pause
