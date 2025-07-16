# 🧠 GIWANOS v26 진화 루프 설계기록서

## 🎯 목적
- 추천 루프에서 얻은 피드백, 정확도, 회고 데이터를 기반으로
- 루프 간 진화 판단, 자동 조정, 개선 루프 실행을 설계

---

## 📂 핵심 구성 요소

| 파일명 | 위치 | 설명 |
|--------|------|------|
| evolution_loop.py | giwanos_auto_loop/ | 진화 트리거 감지 → 정확도 분석 → 진화 계획 생성 |
| loop_thought_trigger.json | giwanos_auto_loop/ | 회고 또는 외부 판단으로 생성된 트리거 |
| loop_feedback_log.json | logs/ | 추천 결과 피드백 로그 |
| evolution_plan_log.json | logs/ | 진화 계획 결과 저장 로그 |
| GIWANOS_v26_진화루프_설계기록서.md | giwanos_memory/ | 본 설계 문서 |

---

## 🔁 흐름 요약

1. 회고 결과 → 진화 트리거 생성
2. 진화 루프 실행 → 정확도 기반 조정
3. 루프별 가중치/추천 우선순위 조절 가능성 반영
4. Slack/Notion 통합 가능 구조 설계

---

## 🔜 확장 계획

- 진화 계획 Slack 알림 (`notify_evolution_slack.py`)
- 진화 상태 Notion 기록 (`evolution_to_notion.py`)
- 추천 시스템 자체 weight 학습 구조 반영

(작성일: 2025-07-14, by GIWANOS 시스템 자동 회고기)