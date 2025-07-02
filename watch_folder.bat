
@echo off
title GPT 문서 자동 정리 감시기
cd /d "C:\구글지완\ChatGPT_자동화작업"
echo [START] 실시간 감시 시작 중...
python watch_folder.py
pause
