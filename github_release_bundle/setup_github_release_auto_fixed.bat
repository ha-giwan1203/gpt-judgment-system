@echo off
chcp 65001 >nul

SET TARGET_DIR=C:\giwanos\github_release_bundle

IF NOT EXIST "%TARGET_DIR%" (
    echo ?? [�ڵ� ����] %TARGET_DIR%
    mkdir "%TARGET_DIR%"
)

cd /d "%TARGET_DIR%"

IF EXIST ".git\index.lock" (
    echo ?? Git lock ���� ������. �ڵ� ���� ��...
    del /f /q ".git\index.lock"
)

IF NOT EXIST ".git" (
    echo ?? Git ����� �ʱ�ȭ ��...
    git init
)

git remote remove origin 2>nul
git remote add origin https://github.com/YOUR_ID/YOUR_REPO.git

REM ������ ����
python push_github_release.py

pause
