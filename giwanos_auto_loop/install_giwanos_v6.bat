@echo off
echo [GIWANOS v6 설치 시작]

REM 1. 작업 디렉토리 생성
mkdir C:\giwanos

REM 2. 파일 복사 (압축 해제된 디렉토리에서 C:\giwanos로)
xcopy /E /I /Y "%~dp0giwanos_main_loop_v6.py" "C:\giwanos\"
xcopy /E /I /Y "%~dp0smart_judge.py" "C:\giwanos\"
xcopy /E /I /Y "%~dp0tree_thought_simulator.py" "C:\giwanos\"
xcopy /E /I /Y "%~dp0failure_reason_extractor.py" "C:\giwanos\"
xcopy /E /I /Y "%~dp0judgement_feedback_log.json" "C:\giwanos\"
xcopy /E /I /Y "%~dp0GIWANOS_v6_FINAL_INFO.txt" "C:\giwanos\"

xcopy /E /I /Y "%~dp0giwanos_auto_loop" "C:\giwanos\giwanos_auto_loop\"
xcopy /E /I /Y "%~dp0giwanos_memory" "C:\giwanos\giwanos_memory\"

REM 3. 완료 메시지
echo [GIWANOS v6 설치 완료: C:\giwanos]
pause
