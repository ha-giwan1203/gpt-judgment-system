# 🧠 GIWANOS - GPT 기반 루프 사고 시스템

> 기억 기반 루프 판단, 회고 리포트, 진화 실행, Slack 전송, 피드백 자동 분석까지 통합된 AI 사고 시스템입니다.

---

## 🚀 구성 요소

| 파일명 | 설명 |
|--------|------|
| `generate_final_summary_pdf.py` | 회고 리포트 PDF 생성 |
| `generate_reflection_pdf.py` | 리플렉션 기반 PDF 생성 |
| `upload_final_runner.py` | Slack/Notion 보고서 전송 |
| `analyze_feedback_score.py` | 피드백 정합률 분석기 |
| `giwanos_dashboard_sample.py` | Streamlit 대시보드 |
| `giwanos_memory/` | 기억 구조 벡터/요약 파일 |
| `giwanos_final_docs/` | README, 복원 안내서 등 포함 |

---

## 🧭 실행 흐름

1. `run_giwanos_full_loop.py` 실행 → 목적 판단
2. 루프 선택 → 회고/진화 실행
3. 결과 PDF 자동 생성 → Slack/Notion 전송
4. 피드백 → 자동 분석 및 리플렉션 생성
5. 루프 진화 → 다음 루프 설계로 연결

---

## 📌 사용 위치

- 로컬 경로: `C:/giwanos/`
- 저장소: [https://github.com/ha-giwan1203/gpt-judgment-system](https://github.com/ha-giwan1203/gpt-judgment-system)

> 이 페이지는 GitHub Pages를 통해 자동 배포되었습니다.
