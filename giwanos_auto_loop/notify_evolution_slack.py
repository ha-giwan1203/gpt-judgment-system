import json
import requests
from pathlib import Path

def notify_evolution_plan(webhook_url="https://hooks.slack.com/services/YOUR/WEBHOOK/URL"):
    plan_path = Path("logs/evolution_plan_log.json")
    if not plan_path.exists():
        print("❌ 진화 계획 로그 없음")
        return

    plan = json.load(open(plan_path, encoding="utf-8"))
    text = f"📈 *GIWANOS 진화 계획 알림*\n"
    text += f"- Trigger: {plan.get('trigger_reason')}\n"
    text += f"- Action: {plan.get('action')}\n"
    text += "*조정 루프 정확도:*\n"

    for loop, detail in plan.get("adjustments", {}).items():
        acc = detail["accuracy"]
        weight = detail["adjust_weight"]
        text += f"• `{loop}` → {acc:.1f}% 정확도 / weight {weight}\n"

    payload = { "text": text }
    r = requests.post(webhook_url, json=payload)
    print("✅ Slack 전송 완료" if r.status_code == 200 else f"⚠️ 실패: {r.status_code}")

if __name__ == "__main__":
    notify_evolution_plan()