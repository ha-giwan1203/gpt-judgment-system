@echo off
title RightArm 자동 실행

echo [1] GPT 기억 복원 시작...
python memory_restorer.py

echo [2] 진화 루프 실행...
python evolution_loop.py

echo [3] 필요시 Notion 자동 전송 실행...
:: 예: python upload_final_runner.py 또는 notion_logger_final.py

echo.
echo === 실행 완료 ===
pause
