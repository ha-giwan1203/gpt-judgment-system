import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

SURVIVAL_LOG = Path("logs/loop_survivors_species.json")
TREND_LOG = Path("logs/loop_survival_trend.json")

def update_trend():
    if not SURVIVAL_LOG.exists():
        print("❌ 생존자 기록 없음")
        return

    trend_data = json.load(open(TREND_LOG, encoding="utf-8")) if TREND_LOG.exists() else []
    latest = json.load(open(SURVIVAL_LOG, encoding="utf-8"))

    trend_data.append({
        "timestamp": latest.get("evaluated_at", datetime.now().isoformat()),
        "survivors": latest.get("survivors", [])
    })

    with open(TREND_LOG, "w", encoding="utf-8") as f:
        json.dump(trend_data, f, indent=2, ensure_ascii=False)

    print(f"📈 생존률 트렌드 기록 업데이트 완료 → {TREND_LOG.name}")
    return trend_data

if __name__ == "__main__":
    update_trend()