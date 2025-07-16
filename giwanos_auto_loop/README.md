# GIWANOS v1.0

GIWANOS는 GPT 기반 자동 루프 시스템입니다.  
이 패키지는 정리, 보고, 진화 루프를 포함하며, 판단-회고-실행-보고 루프가 연결된 운영체제 구조입니다.

## 포함 항목
- loop_config + memory_manifest 3종
- 실행기: loop_launcher, feedback_loop, ai_trigger_decider
- 트리거 샘플 + KPI 자동 생성기
- 대시보드 (Streamlit)
- 사용자 매뉴얼 + 기억 회고 리포트
- 환경 설정 템플릿 (.env)
- 기억 보호기 (memory_guard.py)

## 실행 방법
1. .env 복사 후 Slack/Notion 연동 정보 입력
2. Python 3.x 환경에서 `python loop_launcher.py` 실행
3. 실행 결과는 `/logs`, `/memory`, `/outputs`에 저장됩니다
4. 회고는 `feedback_loop.py`, 판단은 `ai_trigger_decider.py`
5. 상태는 `streamlit run loop_dashboard.py`로 시각화

모든 구조는 memory_manifest 기반 복원 가능하며,  
이 ZIP 자체가 루프 시스템의 복원 지시문입니다.