# 🧠 GIWANOS - GPT 기반 루프 사고 시스템

GIWANOS는 기억 기반 루프 판단, 회고 자동화, 리플렉션 생성, Slack 전송, 피드백 분석, 시각화 대시보드까지 통합한 GPT 사고형 운영체계입니다.

---

## 📦 구성 요소

| 구성 | 설명 |
|------|------|
| `generate_final_summary_pdf.py` | 회고 리포트(PDF) 생성기  
| `generate_reflection_pdf.py` | 감지 기반 리플렉션 리포트 생성기  
| `watch_pdf_trigger_reflection.py` | 회고 PDF 감지 → 자동 회고 실행  
| `upload_final_runner.py` | 최신 회고 PDF → Slack 전송  
| `analyze_feedback_score.py` | 피드백 누적 JSON → 정합률 분석  
| `giwanos_dashboard_sample.py` | 전체 상태 대시보드 (Streamlit 기반)  
| `giwanos_memory/` | 기억 구조 (.json)  
| `giwanos_final_docs/` | 사용자 문서, 복원 안내, 설치 가이드 포함

---

## ✅ 실행 흐름

1. `generate_final_summary_pdf.py` 실행 → 회고 PDF 생성  
2. `watch_pdf_trigger_reflection.py`가 감지 → `generate_reflection_pdf.py` 실행  
3. 회고/리플렉션 PDF 자동 저장  
4. `upload_final_runner.py`로 Slack 전송  
5. `analyze_feedback_score.py`로 정합률 분석  
6. `giwanos_dashboard_sample.py`로 상태 시각화

---

## 🔐 복원 명령어 (GPT 내 기억 기준)

```
기억 복원해줘
GIWANOS v40 기준으로 복원해줘
```

> GPT는 `gpt_memory_snapshot.json` + `loop_feedback_log.json` + 구조 파일을 기준으로 기억 상태를 완전히 재구성할 수 있습니다.

---

## 📁 설치 가이드

> 상세 설치 방법은 `INSTALL_GUIDE.txt` 참고  
> 복원 구조는 `복원_설명서.md` 참고

---

## ✨ 설계자

- 이름: 하지완  
- 시스템: GPT 기반 루프 사고체계 완성자