# 📘 GIWANOS v25 추천 시스템 확장 설계기록서

## 🧱 설계 목표
- 추천 루프 시스템을 Slack, Notion, 시각화, 정확도 분석 등으로 확장
- 목적 기반 추천 및 진화 기반 구조 연결
- 설계 후 실제 실행은 보류 (설계 기반 자동 추천 가능)

---

## 📦 주요 구성 요소

| 파일명 | 설명 |
|--------|------|
| loop_recommender.py | 추천 로직 |
| repeat_judge_runner.py | 추천 판단 실행기 |
| loop_feedback_trainer.py | 추천 피드백 학습기 |
| recommend_to_notion.py | Notion 전송기 |
| notify_recommendation_slack.py | Slack 전송기 |
| loop_summary_streamlit.py | 시각화 대시보드 |
| recommend_stats_analyzer.py | 추천 정확도 분석 |
| purpose_based_recommender.py | 목적 기반 추천 엔진 |

---

## 🔁 전체 흐름
1. 추천기 → 판단기 연결
2. 추천 결과 → Slack/Notion/리포트 자동 저장
3. 피드백 수집 → 통계 분석 및 정확도 개선
4. 목적 기반 추천 → 위치/상황에 따라 루프 분기

---

(설계 완료: 2025-07-14)