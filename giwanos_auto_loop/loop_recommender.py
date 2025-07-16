
import json
import datetime
from pathlib import Path

def recommend_loops(context_path=".memory/context_state.json"):
    try:
        context = json.load(open(context_path, encoding="utf-8"))
    except:
        context = {}

    # 예시 입력값
    location = context.get("location", "회사")
    last_run = context.get("last_loop_run", {})
    file_change = context.get("file_change_detected", False)

    recommendations = []

    if file_change:
        recommendations.append({
            "loop": "정리기",
            "reason": "파일 변화 감지됨",
            "priority": 1
        })

    if last_run.get("회고기", 9999) > 7:
        recommendations.append({
            "loop": "회고기",
            "reason": "최근 회고 없음",
            "priority": 2
        })

    if location == "회사":
        recommendations.append({
            "loop": "정산 루프",
            "reason": "회사 위치에서만 실행 가능",
            "priority": 3
        })

    if not recommendations:
        recommendations.append({
            "loop": "휴식 루프",
            "reason": "특이사항 없음",
            "priority": 99
        })

    # 로그 저장
    save_path = Path("loop_recommendation_log.json")
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "recommendations": recommendations
    }
    if save_path.exists():
        data = json.load(open(save_path, encoding="utf-8"))
    else:
        data = []
    data.append(log_entry)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return recommendations

if __name__ == "__main__":
    results = recommend_loops()
    for rec in results:
        print(f"✅ {rec['loop']} 추천됨 - 이유: {rec['reason']} (우선순위 {rec['priority']})")
