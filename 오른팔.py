
# 🧠 오른팔: 자동 정리 + Notion 로그 시스템 (Main Script)

import requests
from datetime import datetime
import os
import random

# ✅ 환경 설정
NOTION_TOKEN = "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"
DATABASE_ID = "223fee67-0be8-803c-afbc-dd27aec799f4"

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# ✅ 오른팔 기록 함수
def 오른팔_기록(
    파일명,
    경로,
    상태,
    설명=None,
    크기=None,
    유형=None,
    태그=None,
    결과ID=None
):
    url = "https://api.notion.com/v1/pages"
    today = datetime.now().strftime("%Y-%m-%d")

    properties = {
        "이름": {"title": [{"text": {"content": 파일명}}]},
        "날짜": {"date": {"start": today}},
        "경로": {"rich_text": [{"text": {"content": 경로}}]},
        "상태": {"status": {"name": 상태}},
    }

    if 설명:
        properties["설명"] = {"rich_text": [{"text": {"content": 설명}}]}
    if 크기 is not None:
        properties["크기"] = {"number": 크기}
    if 유형:
        properties["유형"] = {"select": {"name": 유형}}
    if 태그:
        properties["태그"] = {"multi_select": [{"name": t} for t in 태그]}
    if 결과ID:
        properties["결과 ID"] = {"rich_text": [{"text": {"content": 결과ID}}]}

    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": properties
    }

    response = requests.post(url, headers=HEADERS, json=payload)

    if response.status_code == 200:
        print(f"✅ 기록 완료: {파일명}")
    else:
        print(f"❌ 실패: {response.status_code} | {response.text}")

# ✅ 예제 테스트 실행
if __name__ == "__main__":
    오른팔_기록(
        파일명="오른팔_시작_로그.txt",
        경로="/오토로그/테스트",
        상태="완료",
        설명="시스템 최초 실행 로그",
        크기=1,
        유형="문서",
        태그=["시작", "테스트"],
        결과ID=f"start-{random.randint(1000,9999)}"
    )
