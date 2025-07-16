
@echo off
echo 🧼 백업 및 로그 정리 중...

:: 백업 폴더 생성 확인
if not exist archive mkdir archive

:: 오래된 백업 정리
forfiles /p loop_backups /s /m *.pdf /d -7 /c "cmd /c move @file archive\"

:: 오래된 로그 정리
forfiles /p logs /s /m *.json /d -10 /c "cmd /c move @file archive\"
forfiles /p logs /s /m *.txt /d -10 /c "cmd /c move @file archive\"

echo ✅ loop_backups 및 logs 정리 완료: 7~10일 이전 파일은 archive\로 이동되었습니다.
pause
