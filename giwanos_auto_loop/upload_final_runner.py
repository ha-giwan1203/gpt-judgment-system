import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

PDF_PATH = "loop_reflection_log.pdf"
DESC = f"📄 GIWANOS 회고 PDF 자동 업로드 ({datetime.now().strftime('%Y-%m-%d')})"

def send_to_slack():
    if not SLACK_WEBHOOK:
        print("[⚠️ SLACK_WEBHOOK 미설정 - .env 확인 필요]")
        return
    payload = {
        "text": DESC
    }
    response = requests.post(SLACK_WEBHOOK, json=payload)
    print("[✅ Slack 전송 완료]" if response.status_code == 200 else "[❌ Slack 전송 실패]", response.text)

def send_to_notion():
    if not NOTION_TOKEN or not NOTION_DATABASE_ID:
        print("[⚠️ Notion 설정 미완 - .env 확인 필요]")
        return

    notion_url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    today = datetime.now().strftime("%Y-%m-%d")
    payload = {
        "parent": { "database_id": NOTION_DATABASE_ID },
        "properties": {
            "제목": {
                "title": [
                    {
                        "text": {
                            "content": f"회고 루프 - {today}"
                        }
                    }
                ]
            },
            "설명": {
                "rich_text": [
                    {
                        "text": {
                            "content": "GIWANOS 루프 회고 자동 전송됨"
                        }
                    }
                ]
            },
            "상태": {
                "status": {
                    "name": "완료"
                }
            },
            "날짜": {
                "date": {
                    "start": today
                }
            },
            "경로": {
                "rich_text": [
                    {
                        "text": {
                            "content": PDF_PATH
                        }
                    }
                ]
            }
        }
    }

    response = requests.post(notion_url, headers=headers, json=payload)
    if response.status_code == 200:
        print("[✅ Notion 전송 완료]")
    else:
        print("[❌ Notion 전송 실패]", response.text)

if __name__ == "__main__":
    print("🚀 회고 PDF 자동 전송 루프 시작")
    if os.path.exists(PDF_PATH):
        send_to_slack()
        send_to_notion()
    else:
        print("[❌ PDF 파일이 존재하지 않습니다]")
