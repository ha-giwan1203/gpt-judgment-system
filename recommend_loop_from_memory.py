
import json
import os
from datetime import datetime

# 기본 추천 규칙 (간단한 조건 기반 로직)
RECOMMENDATION_RULES = [
    {
        "condition": "memory_updated_within_24h",
        "recommend": "진화 루프",
        "reason": "최근 기억이 수정됨 → 진화 필요"
    },
    {
        "condition": "no_recent_pdf",
        "recommend": "회고 PDF 생성 루프",
        "reason": "최근 회고 보고서가 없음 → 정리 필요"
    },
    {
        "condition": "no_notion_upload_detected",
        "recommend": "Notion 전송 루프",
        "reason": "최근 결과물이 Notion에 전송되지 않음"
    }
]

def memory_updated_within_24h(manifest_path=".memory/manifest.json"):
    if not os.path.exists(manifest_path):
        return False
    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        for entry in data.get("entries", []):
            updated = entry.get("updated_at", "")
            if " " in updated:
                updated_dt = datetime.strptime(updated, "%Y-%m-%d %H:%M")
                if (datetime.now() - updated_dt).total_seconds() < 86400:
                    return True
    except:
        pass
    return False

def no_recent_pdf(pdf_path="loop_reflection_with_memory.pdf"):
    return not os.path.exists(pdf_path)

def no_notion_upload_detected():
    # 간단한 구현: Notion 업로드 기록 파일 없거나 오래된 경우
    return True  # 실제 사용 시 로그 기반 판단 필요

def recommend_loops():
    recommendations = []
    if memory_updated_within_24h():
        recommendations.append(RECOMMENDATION_RULES[0])
    if no_recent_pdf():
        recommendations.append(RECOMMENDATION_RULES[1])
    if no_notion_upload_detected():
        recommendations.append(RECOMMENDATION_RULES[2])

    print("✅ 실행 추천 결과:")
    for rec in recommendations:
        print(f"🔹 추천 루프: {rec['recommend']} — {rec['reason']}")
    if not recommendations:
        print("🔸 특별히 추천할 루프 없음 — 모든 흐름이 안정적입니다.")

if __name__ == "__main__":
    recommend_loops()
