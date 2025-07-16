# 🧠 GIWANOS 기억 구조 요약

## ✅ 주요 기억 요소

### 1. gpt_trigger.json
- 루프 실행 목적을 정의함
- 예: { "action": "회고" }, "진화", "대시보드"

### 2. .env
- Slack, Notion, Email, GDrive, OpenAI 연동 정보 포함
- 시스템 실행에 필요한 모든 환경 설정

### 3. logs/loop_execution_reason.json
- 루프 실행 시점, 목적, 이유를 기록
- 회고/진화/정리 등의 실행 판단 근거로 사용

### 4. loop_feedback_log.json, loop_genes_mutated.json
- 회고 및 진화 결과 데이터 기록
- PDF 리포트, Slack 메시지 생성에 사용됨

### 5. loop_dashboard.py
- 기억 데이터 기반 시각화 UI (Streamlit)
- 회고 요약, 오류율, 유전자 개선 내역 등 확인 가능

### 6. ZIP 백업
- loop_summary_backup_*.zip
- PDF, JSON 로그, 리포트 파일 통합 백업 구조

---

## 🔄 기억 흐름 요약

```
[입력 or 트리거]
→ gpt_trigger.json 변경
→ watch_trigger_fixed.py 감지
→ 해당 루프 실행(run_report_bundle.py 등)
→ PDF 생성, 전송, 백업
→ 실행 사유 기록 + 기억 파일 갱신
→ Streamlit으로 확인 가능
```