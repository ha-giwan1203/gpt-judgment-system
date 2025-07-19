import os
import subprocess
import datetime
import json

ZIP_TARGET = "GIWANOS_FINAL_INSTALL_COMPLETE.zip"
TAG_PREFIX = "v"

def run_git(commands):
    for cmd in commands:
        print(f"💻 {cmd}")
        subprocess.run(cmd, shell=True, check=True)

def main():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    version_tag = TAG_PREFIX + datetime.datetime.now().strftime("%Y%m%d%H%M")
    message = f"Release {version_tag} - Automated GIWANOS Release"

    # Dummy 파일로 커밋 유도
    with open("release_dummy.txt", "w", encoding="utf-8") as f:
        f.write(f"Release executed: {message}\n")

    # Git add
    run_git(["git add ."])

    # 변경사항 유무 판단
    status = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    if not status.stdout.strip():
        print("⚠️ 변경된 파일이 없어 커밋을 건너뜁니다.")
    else:
        run_git([f'git commit -m "{message} (자동 커밋)"'])

    # pull 전에 커밋 처리 후 rebase
    run_git(["git pull origin main --rebase"])

    # push 및 tag
    run_git([
        "git push origin main",
        f"git tag {version_tag}",
        f"git push origin {version_tag}"
    ])

    print(f"✅ Release pushed: {version_tag}")

if __name__ == "__main__":
    main()
