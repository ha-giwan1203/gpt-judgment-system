@echo off
echo [1] 회고 루프 테스트
powershell -Command "Set-Content -Path .\logs\loop_config.json -Value '{\"execution_purpose\": \"회고\"}'"
python run_giwanos_full_loop.py

echo [2] 진화 루프 테스트
powershell -Command "Set-Content -Path .\logs\loop_config.json -Value '{\"execution_purpose\": \"진화\"}'"
python run_giwanos_full_loop.py

echo [3] 피드백 루프 테스트
powershell -Command "Set-Content -Path .\logs\loop_config.json -Value '{\"execution_purpose\": \"피드백\"}'"
python run_giwanos_full_loop.py

echo.
echo ✅ GIWANOS 루프 자동 목적 실행 테스트 완료!
pause