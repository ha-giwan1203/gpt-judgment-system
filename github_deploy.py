import os
import requests
import subprocess

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = "your-github-username"  # 본인 GitHub 사용자명
REPO_NAME = "rightarm-system"

def create_github_repo():
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": REPO_NAME,
        "private": False,
        "description": "RightArm 기억 기반 자동화 시스템 저장소"
    }
    r = requests.post(url, headers=headers, json=data)
    if r.status_code == 201:
        print("✅ GitHub 저장소 생성 완료")
    elif r.status_code == 422:
        print("⚠️ 이미 같은 이름의 저장소가 존재함")
    else:
        print(f"❌ 저장소 생성 실패: {r.status_code} | {r.text}")

def push_code():
    repo_url = f"https://{USERNAME}:{GITHUB_TOKEN}@github.com/{USERNAME}/{REPO_NAME}.git"
    subprocess.run("git init", shell=True)
    subprocess.run("git add .", shell=True)
    subprocess.run('git commit -m "RightArm 초기 커밋"', shell=True)
    subprocess.run(f"git remote add origin {repo_url}", shell=True)
    subprocess.run("git branch -M main", shell=True)
    subprocess.run("git push -u origin main", shell=True)

if __name__ == "__main__":
    create_github_repo()
    push_code()
