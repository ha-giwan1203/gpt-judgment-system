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

    run_git([
        "git add .",
        f'git commit -m "{message}"',
        "git push origin main",
        f"git tag {version_tag}",
        f"git push origin {version_tag}"
    ])

    print(f"✅ Release pushed: {version_tag}")

if __name__ == "__main__":
    main()
