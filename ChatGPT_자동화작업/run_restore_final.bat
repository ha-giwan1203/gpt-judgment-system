@echo off
setlocal

:: ? ���� zip ��� (�� ������ �����ϴ� ��� Ȯ�� �ʼ�!)
set "ZIPPATH=G:\�� ����̺�\ChatGPT_�ڵ�ȭ�۾�\�ý��ۼ���\GPT_Judgment_System_v12_Clean.zip"

:: ? ���� ��� ����
set "DEST=C:\GPT_Judgment_System_CLEAN"

echo.
echo ?? ���� ��� Ȯ��:
echo ZIP ���: [%ZIPPATH%]
echo ��� ����: [%DEST%]
echo.

:: zip ���� ���� Ȯ��
if not exist "%ZIPPATH%" (
    echo ? [ERROR] ZIP ������ ã�� �� �����ϴ�!
    pause
    exit /b
)

echo ??? ���� ���� ���� ��...
rd /s /q "%DEST%" >nul 2>nul

echo ?? ���� ���� ��...
powershell -Command "Expand-Archive -Path '%ZIPPATH%' -DestinationPath '%DEST%' -Force"
if errorlevel 1 (
    echo ? [ERROR] ���� ���� �� ���� �߻�!
    pause
    exit /b
)

echo ? ���� �Ϸ�! ������ �ʱ�ȭ�Ǿ����ϴ�.
pause
