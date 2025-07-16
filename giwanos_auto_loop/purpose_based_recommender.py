import json
from datetime import datetime

def recommend_by_purpose(purpose="정산", context_path=".memory/context_state.json"):
    try:
        context = json.load(open(context_path, encoding="utf-8"))
    except:
        context = {}

    location = context.get("location", "회사")
    file_change = context.get("file_change_detected", False)
    day = datetime.now().weekday()

    recommendations = []

    if purpose == "정산":
        if location == "회사":
            recommendations.append({"loop": "정산 루프", "reason": "정산 목적 + 회사 위치", "priority": 1})
        else:
            recommendations.append({"loop": "회고기", "reason": "정산 목적이지만 회사 아님", "priority": 2})

    elif purpose == "정리":
        if file_change:
            recommendations.append({"loop": "정리기", "reason": "파일 변경 감지됨", "priority": 1})
        else:
            recommendations.append({"loop": "회고기", "reason": "정리 목적이지만 변화 없음", "priority": 3})

    elif purpose == "휴식":
        if day >= 5:
            recommendations.append({"loop": "회고기", "reason": "주말 회고 추천", "priority": 1})
        else:
            recommendations.append({"loop": "휴식 루프", "reason": "업무일이지만 휴식 지정됨", "priority": 2})

    else:
        recommendations.append({"loop": "회고기", "reason": f"기본 회고 처리 for '{purpose}'", "priority": 3})

    return recommendations

if __name__ == "__main__":
    print("📌 목적 기반 추천 예시")
    for p in ["정산", "정리", "휴식", "테스트"]:
        recs = recommend_by_purpose(p)
        print(f"▶ 목적: {p}")
        for r in recs:
            print(f"  - {r['loop']}: {r['reason']} (우선순위 {r['priority']})")