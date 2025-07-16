
@echo off
echo 🧼 Streamlit UI 정리 중...

:: archive 폴더 확인
if not exist archive mkdir archive

:: 이동 대상
move /Y loop_dashboard_v2.py archive\
move /Y loop_collab_dashboard.py archive\
move /Y loop_summary_streamlit.py archive\
move /Y loop_monitor_dashboard.py archive\
move /Y loop_state_dashboard.py archive\
move /Y streamlit_ui\loop_recommendation_ui.py archive\

echo ✅ UI 정리 완료: 사용하지 않는 Streamlit 파일이 archive\로 이동되었습니다.
pause
