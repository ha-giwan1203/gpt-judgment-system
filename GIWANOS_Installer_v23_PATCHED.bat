@echo off
setlocal
echo ==========================================
echo  GIWANOS SYSTEM INSTALLER (v14 ~ v23) - PATCHED
echo ==========================================

set BASE=C:\giwanos

for %%Z in (
  GIWANOS_v14_PATCHED.zip
  GIWANOS_v15_PATCHED.zip
  GIWANOS_v16_PATCHED.zip
  GIWANOS_v17_PATCHED.zip
  GIWANOS_v18_PATCHED.zip
  GIWANOS_v19_PATCHED.zip
  GIWANOS_v20_PATCHED.zip
  GIWANOS_v21_PATCHED.zip
  GIWANOS_v22_PATCHED.zip
  GIWANOS_v23_PATCHED.zip
) do (
    set ZIP=%%Z

    if "%%Z"=="GIWANOS_v14_PATCHED.zip" set DIR=v14
    if "%%Z"=="GIWANOS_v15_PATCHED.zip" set DIR=v15
    if "%%Z"=="GIWANOS_v16_PATCHED.zip" set DIR=v16
    if "%%Z"=="GIWANOS_v17_PATCHED.zip" set DIR=v17
    if "%%Z"=="GIWANOS_v18_PATCHED.zip" set DIR=v18
    if "%%Z"=="GIWANOS_v19_PATCHED.zip" set DIR=v19
    if "%%Z"=="GIWANOS_v20_PATCHED.zip" set DIR=v20
    if "%%Z"=="GIWANOS_v21_PATCHED.zip" set DIR=v21
    if "%%Z"=="GIWANOS_v22_PATCHED.zip" set DIR=v22
    if "%%Z"=="GIWANOS_v23_PATCHED.zip" set DIR=v23

    echo Installing %%Z ...
    powershell -Command "Expand-Archive -Force '%%Z' '%BASE%\%DIR%'"
    echo ✓ %%Z 설치 완료 → %BASE%\%DIR%
)

echo ------------------------------------------
echo GIWANOS v14~v23 패치 설치 완료.
echo 각 루프 실행기는 C:\giwanos\vXX\ 에서 사용 가능합니다.
pause
endlocal
