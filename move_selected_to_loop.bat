@echo off
echo [GIWANOS 설치 파일 정리 시작]
cd /d C:\giwanos
move run_giwanos_full_loop.py giwanos_auto_loop\
move setup_giwanos.py giwanos_auto_loop\
move upload_final_runner.py giwanos_auto_loop\
echo [완료] 지정된 파일이 giwanos_auto_loop로 이동되었습니다.
pause