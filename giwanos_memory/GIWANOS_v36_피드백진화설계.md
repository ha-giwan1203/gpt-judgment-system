# 🔁 GIWANOS v36 피드백 기반 추천 진화 설계기록서

## 🎯 목표
- 루프 추천 시스템이 사용자의 피드백과 실행 결과를 기반으로 학습하고
- 추천 정확도와 신뢰도를 스스로 개선하는 구조 구축
- 추천 결과를 자연어로 설명하고, 피드백 결과를 시각화하는 운영체계 구성

---

## 📦 핵심 구성 요소

| 모듈 | 기능 |
|------|------|
| `loop_rl_trainer.py` | 피드백 기반 강화 학습 추천 weight 계산 |
| `loop_feedback_collector.py` | 사용자 👍/👎 피드백 수집기 |
| `loop_weight_adjuster.py` | 기존 weight + 학습 weight 기반 추천 우선순위 조정 |
| `loop_feedback_dashboard.py` | 피드백 결과 시각화 Streamlit 대시보드 |
| `loop_user_feedback.json` | 사용자 피드백 로그 저장소 |
| `loop_rl_trained_weights.json` | 강화 학습 결과 저장소 |
| `loop_priority_model_adjusted.json` | 추천 우선순위 조정 모델 저장소 |

---

## 🧠 추천 진화 흐름 요약

1. 추천 → 실행 → 피드백 수집
2. 강화 학습 → 추천 정확도 향상
3. 자연어 설명 및 신뢰성 기반 추천
4. 피드백 대시보드로 투명한 운영

---

## 🔮 향후 v37 제안

- 실시간 Slack/Streamlit 추천 피드백 버튼  
- 추천 정확도 추세 시각화 (시간 기반)
- 사용자 기반 추천 모델 분기 (지완 vs 민수 등)

(작성일: 2025-07-14 by GIWANOS 피드백 진화 시스템)