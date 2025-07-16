import os
import json
import datetime
import requests

def send_summary():
    slack_webhook = os.environ.get("SLACK_WEBHOOK")
    if not slack_webhook:
        print("❌ SLACK_WEBHOOK 환경변수가 설정되지 않았습니다.")
        return

    score_path = os.path.join("logs", "loop_recommendation_score.json")

    try:
        with open(score_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ 추천 점수 파일을 찾을 수 없습니다: {score_path}")
        return

    top = data.get("top_scored_loop")
    most = data.get("most_frequent_loop")
    least = data.get("least_effective_loop")

    if not (top and most and least):
        print("⚠️ 최고 추천 결과가 비어 있습니다. 메시지를 전송하지 않습니다.")
        return

    message = f"""*GIWANOS 루프 추천 요약 결과*
🏆 최고 점수 루프: `{top.get('name')}` (평균 점수: {top.get('avg_score')})
📈 가장 자주 실행된 루프: `{most.get('name')}` (실행 횟수: {most.get('count')})
📉 가장 비효율적인 루프: `{least.get('name')}` (사용도: {least.get('usage')})
⏱️ 기준 시각: {data.get('last_updated')}"""

    payload = {"text": message}
    response = requests.post(slack_webhook, json=payload)

    if response.status_code == 200:
        print("✅ Slack 메시지 전송 완료")
    else:
        print(f"❌ Slack 전송 실패: {response.status_code} - {response.text}")


if __name__ == "__main__":
    send_summary()