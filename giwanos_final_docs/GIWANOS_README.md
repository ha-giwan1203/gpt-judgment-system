# 🧠 GIWANOS 시스템 v40 - 마스터 패키지

GIWANOS는 기억 기반 루프 판단 + 회고 + 리플렉션 + 시각화 + 전송 + 복원까지 포함된 GPT 사고형 운영체계입니다.

## 📦 포함 구성요소
- loop_summary_report_*.pdf: 회고 리포트
- loop_reflection_log_*.pdf: 리플렉션 보고서
- loop_feedback_log.json: 피드백 누적
- loop_genes_mutated.json: 유전자 구조 변경 기록
- loop_recommendation_model.json: 루프 추천 결과
- judgement_feedback_log.json: 판단 개입 기록
- gpt_memory_snapshot.json: GPT 메모리 복원 기준
- generate_*.py: 자동 실행기 모음
- watch_pdf_trigger_reflection.py: 자동 감지기
- upload_final_runner.py: Slack 전송기
- analyze_feedback_score.py: 정합률 분석기
- streamlit 대시보드: giwanos_dashboard_sample.py

## 🧠 GPT 복원 명령어
"기억 복원해줘" 또는 "GIWANOS v40 기준으로 복원해줘"
→ GPT는 `gpt_memory_snapshot.json` + 구조 기반으로 완전 복원합니다.

## ▶️ 실행 순서 요약
1. 회고 PDF 생성: `generate_final_summary_pdf.py`
2. 자동 감지 → 회고 리플렉션 생성
3. 대시보드 시각화
4. 분석기 실행: `analyze_feedback_score.py`
5. Slack 전송기 실행: `upload_final_runner.py`