import os
import requests
from pathlib import Path

PDF_REPORT = Path("C_giwanos/loop_reflection_report_v25.pdf")
TREE_IMAGE = Path("loop_tree.png")
WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_file_to_slack(file_path: Path, title="루프 보고서"):
    if not WEBHOOK_URL:
        print("❌ SLACK_WEBHOOK_URL 환경변수 없음")
        return
    if not file_path.exists():
        print(f"❌ 파일 없음: {file_path}")
        return

    with open(file_path, "rb") as f:
        response = requests.post(
            url="https://slack.com/api/files.upload",
            headers={"Authorization": f"Bearer {WEBHOOK_URL}"},
            files={"file": f},
            data={"filename": file_path.name, "title": title, "channels": "#general"}
        )

    if response.status_code == 200 and response.json().get("ok"):
        print(f"✅ 전송 완료: {file_path.name}")
    else:
        print(f"⚠️ 전송 실패: {file_path.name} → {response.text}")

if __name__ == "__main__":
    send_file_to_slack(PDF_REPORT, title="🧾 회고 PDF 보고서")
    send_file_to_slack(TREE_IMAGE, title="🌳 루프 진화 트리")