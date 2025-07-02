@echo off
setlocal

:: ? 복원 zip 경로 (※ 실제로 존재하는 경로 확인 필수!)
set "ZIPPATH=G:\내 드라이브\ChatGPT_자동화작업\시스템설계\GPT_Judgment_System_v12_Clean.zip"

:: ? 복원 대상 폴더
set "DEST=C:\GPT_Judgment_System_CLEAN"

echo.
echo ?? 복원 경로 확인:
echo ZIP 경로: [%ZIPPATH%]
echo 대상 폴더: [%DEST%]
echo.

:: zip 파일 존재 확인
if not exist "%ZIPPATH%" (
    echo ? [ERROR] ZIP 파일을 찾을 수 없습니다!
    pause
    exit /b
)

echo ??? 기존 폴더 삭제 중...
rd /s /q "%DEST%" >nul 2>nul

echo ?? 압축 해제 중...
powershell -Command "Expand-Archive -Path '%ZIPPATH%' -DestinationPath '%DEST%' -Force"
if errorlevel 1 (
    echo ? [ERROR] 압축 해제 중 오류 발생!
    pause
    exit /b
)

echo ? 복원 완료! 폴더가 초기화되었습니다.
pause
