import os
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OWNER = "your-github-username"  # 여기를 수정
REPO = "rightarm-system"        # 여기를 수정
TAG = "v1.2"
ZIP_FILE = "RightArm_AutoFlow_v1.2.zip"

def create_release():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/releases"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "tag_name": TAG,
        "name": "RightArm AutoFlow v1.2",
        "body": "기억 기반 자동화 시스템 RightArm v1.2 릴리즈",
        "draft": False,
        "prerelease": False
    }
    r = requests.post(url, headers=headers, json=data)
    if r.status_code == 201:
        print("✅ 릴리즈 생성 완료")
        return r.json()["upload_url"].split("{")[0]
    else:
        print(f"❌ 릴리즈 실패: {r.status_code} | {r.text}")
        return None

def upload_asset(upload_url):
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Content-Type": "application/zip"
    }
    params = {"name": ZIP_FILE}
    with open(ZIP_FILE, "rb") as f:
        r = requests.post(upload_url, headers=headers, params=params, data=f)
    if r.status_code == 201:
        print("✅ zip 업로드 완료")
    else:
        print(f"❌ zip 업로드 실패: {r.status_code} | {r.text}")

if __name__ == "__main__":
    url = create_release()
    if url:
        upload_asset(url)
