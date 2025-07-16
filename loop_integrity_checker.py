import os
import json
from datetime import datetime

def check_file(path, desc):
    if os.path.exists(path):
        size = os.path.getsize(path)
        updated = datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y-%m-%d %H:%M:%S')
        print(f"[✅] {desc} 존재함 ({size} bytes, 마지막 수정: {updated})")
    else:
        print(f"[❌] {desc} 없음 → 점검 필요!")

def check_json_key(path, desc, keys):
    if not os.path.exists(path):
        print(f"[❌] {desc} 없음 → 점검 필요!")
        return
    try:
        data = json.load(open(path, encoding="utf-8"))
        if all(k in data for k in keys):
            print(f"[✅] {desc} 내용 정상")
        else:
            print(f"[⚠️] {desc} 일부 항목 누락됨: {keys}")
    except Exception as e:
        print(f"[❌] {desc} 파싱 실패: {e}")

if __name__ == "__main__":
    print("🧠 GIWANOS 루프 실행 결과 + 로컬 동기화 점검 시작")

    check_file("loop_summary_report.pdf", "회고 루프 PDF")
    check_json_key("logs/loop_genes_mutated.json", "진화 루프 결과", ["genes", "mutated_at"])
    check_file("logs/loop_feedback_log.json", "피드백 루프 로그")
    check_file("logs/loop_recommendation_model.json", "추천 학습 모델")
    check_file("logs/loop_local_sync_log.json", "로컬 감시 동기화 로그")

    print("\n✅ 루프 전체 점검 완료")