# 🧠 GIWANOS 시스템 전체 구조 요약

## ✅ 구성 개요
GIWANOS는 트리거 기반 자동 실행 → 회고/진화 루프 → 보고/전송/백업 → 실행 기록까지 완비된 자동화 운영체계입니다.

---

## 📂 핵심 구성 요소

### 🔍 트리거 감지기
- `watch_trigger_fixed.py`: `gpt_trigger.json` 감지 → action 분기 실행
- `gpt_trigger.json`: { "action": "회고" }, "진화", "대시보드" 등 지정

### 📄 보고 루프
- `generate_reflection_pdf.py`: 회고 PDF 생성 (정합률 + 오류 그래프)
- `run_report_bundle.py`: 회고 전체 자동 실행기 (PDF → Slack/Notion/ZIP/Email)

### 🧬 진화 루프
- `generate_evolution_pdf.py`: 진화 결과 PDF 보고서 자동 생성
- `evolution_loop.py`: 진화 조건 기반 루프 실행기 (외부 연동 가능)

### 📤 전송 및 보고
- `upload_final_runner.py`: Slack + Notion 전송
- `send_loop_report_email.py`: 이메일로 회고 보고서 발송
- `loop_feedback_result_slack.py`: 요약 Slack 메시지 전송

### 📊 대시보드
- `loop_dashboard.py`: Streamlit 기반 루프 상태 시각화

### 🧠 기록기
- `log_execution_reason.py`: 실행 이유를 자동 기록 (`loop_execution_reason.json`)

### 📦 백업
- `loop_zip_backup_generator.py`: ZIP 압축으로 로그/보고서 보존

---

## 🔄 자동 실행 흐름

1. `gpt_trigger.json` 수정
2. `watch_trigger_fixed.py`가 감지
3. 회고 루프 또는 진화 루프 자동 실행
4. 보고서 생성 → Slack/Notion/Email 전송
5. 실행 사유 기록 → ZIP 백업
6. 대시보드 실시간 상태 시각화

---

## ✅ 확장 예정 항목 (v14~)
- `schedule_giwanos.py`: 시간 기반 자동 실행
- `watch_folder_trigger.py`: 실적 파일 감지 자동 루프
- `ai_loop_judger.py`: 루프 실행 여부 AI 판단기