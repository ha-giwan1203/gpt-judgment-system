# 🔀 GIWANOS v27 멀티 목적 루프 / 루프 스케줄러 설계기록서

## 🎯 설계 목표
- 목적 기반 추천을 넘어서 복수 루프를 병렬 평가
- 시간, 위치, 목적, 정확도, 피드백을 모두 고려한 루프 실행 우선순위 결정
- 루프 스케줄러 또는 루프 플래너와 통합 설계 기반 마련

---

## 🔧 예정 구조

| 구성 요소 | 설명 |
|-----------|------|
| `loop_scheduler.py` | 루프 우선순위 계산 + 시간 기반 스케줄링 |
| `loop_priority_model.json` | 추천 정확도, 사용빈도, 피드백 기반 weight 계산 기록 |
| `user_goal_router.py` | 사용자 목적에 따라 루프 분기 처리 |
| `scheduled_loop_log.json` | 루프 실행 계획 기록 및 다음 루프 자동 지정 |

---

## 🧠 설계 기반

- 추천 루프 (`loop_recommender.py`)
- 진화 루프 (`evolution_loop.py`)
- 트리거 기반 판단기 (`loop_thought_trigger.json`)
- 정확도 통계 분석기 (`recommend_stats_analyzer.py`)

---

## 🔜 확장 방향

- 멀티 사용자 지원 (user_profile.json 기반 루프 분기)
- 목적 기반 루프 트리거 자동 생성기
- 루프 상태 Streamlit UI 통합 → 일정/우선순위/진행률 시각화

(작성일: 2025-07-14 by GIWANOS 시스템)