@echo off
set DEST=G:\내 드라이브\ChatGPT_자동화작업\시스템설계
if not exist "%DEST%" (
    echo [경고] Google Drive 폴더가 존재하지 않습니다!
    echo 경로를 다시 설정하거나 Drive 동기화 설정을 확인해주세요.
    pause
    exit /b
)
set ZIPNAME=GPT_Judgment_System_v12_Clean
set SRCDIR=%~dp0
powershell Compress-Archive -Path "%SRCDIR%\*" -DestinationPath "%DEST%\%ZIPNAME%.zip"
echo 백업 완료!
pause
