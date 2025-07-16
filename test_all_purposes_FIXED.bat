@echo off
echo [1] 회고 테스트 시작...
powershell -Command "Set-Content -Path .\logs\loop_config.json -Value '{\"execution_purpose\": \"회고\"}'"
python giwanos_auto_loop/loop_summary_writer.py

echo [2] 진화 테스트 시작...
powershell -Command "Set-Content -Path .\logs\loop_config.json -Value '{\"execution_purpose\": \"진화\"}'"
python giwanos_auto_loop/loop_mutator.py

echo [3] 피드백 테스트 시작...
powershell -Command "Set-Content -Path .\logs\loop_config.json -Value '{\"execution_purpose\": \"피드백\"}'"
python giwanos_auto_loop/loop_feedback_trainer.py

echo.
echo ✅ 전체 자동 목적 루프 테스트 완료!
pause