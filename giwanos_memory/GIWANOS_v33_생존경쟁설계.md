# 🔥 GIWANOS v33 루프 생존 경쟁 진화 설계기록서

## 🎯 목표
- 루프들이 시뮬레이션을 통해 스스로 테스트 받고
- 생존 기준에 따라 선발되며
- 실험 환경에서 조건부 평가를 받는 루프 경쟁 생태계 구성

---

## 📦 핵심 구성 요소

| 모듈 | 기능 |
|------|------|
| `loop_simulator.py` | 루프 유전자 기반 시뮬레이션 실행 (성공률, 시간, 점수 평가) |
| `loop_natural_selector.py` | 시뮬레이션 점수 기반 생존 루프 선발 |
| `loop_scoreboard.json` | 루프 점수 저장소 |
| `loop_survivors.json` | 생존한 루프 이름 목록 |
| `loop_lab_manager.py` | 루프 그룹별 실험 실행 및 기록 |
| `loop_lab_experiments.json` | 실험 세션 기록 저장소 |

---

## 🔁 실행 흐름

1. 루프 시뮬레이션 실행 (`loop_simulator.py`)
2. 평가 점수 계산 및 저장 (`loop_scoreboard.json`)
3. 생존 기준 이상 루프만 선발 (`loop_natural_selector.py`)
4. 실험 그룹 구성하여 테스트 (`loop_lab_manager.py`)
5. 향후 진화 루프 대상 선정에 사용

---

## 🔮 향후 확장 (v34~)

- 루프 실험 반복 기반 평균 정확도 측정
- 루프 생존률 로그 시각화 대시보드
- 루프 진화 트리 그리기 (루프 계보 시각화)

(작성일: 2025-07-14 by GIWANOS v33 생존 진화 시스템)