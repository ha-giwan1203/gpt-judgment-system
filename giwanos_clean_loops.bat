
@echo off
echo 🧹 GIWANOS 실행기 정리 중...

:: create archive directory if not exists
if not exist archive mkdir archive

:: move test files
move /Y giwanos_auto_loop\test_giwanos_v41.py archive\
move /Y giwanos_auto_loop\run_giwanos_v41.py archive\
move /Y giwanos_auto_loop\upload_notion_result_*.py archive\

:: move duplicate recommendation UI
move /Y streamlit_ui\loop_recommendation_ui.py archive\

:: optional: move all v14~v22 experimental folders to archive
for %%V in (v14 v15 v16 v17 v18 v19 v20 v21 v22) do (
    if exist %%V move /Y %%V archive\
)

echo ✅ 정리 완료: 중복 실행기, 테스트 파일, 이전 UI가 archive\로 이동되었습니다.
pause
