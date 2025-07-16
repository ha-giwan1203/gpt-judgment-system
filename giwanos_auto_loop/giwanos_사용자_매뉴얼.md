# 🧠 GIWANOS 시스템 사용자 매뉴얼

---

## 📦 시스템 개요

GIWANOS는 GPT 기반 자동화 루프 시스템입니다.  
정리, 보고, 진화 루프를 기억 기반으로 설계하고 실행하며, Slack/Notion 연동을 통해 결과를 자동 보고합니다.

---

## 🧩 시스템 구성 요소

| 구성 요소 | 설명 |
|-----------|------|
| `loop_config_giwanos.json` | 전체 루프 정의 및 활성 설정 |
| `memory_manifest_*.json` | 루프별 메타 정보, 실행기, 로그, 출력 경로 정의 |
| `loop_launcher.py` | 모든 루프를 순차 실행하는 메인 실행기 |
| `feedback_loop.py` | 실행 결과 회고 및 KPI 저장 |
| `ai_trigger_decider.py` | KPI 기반 조건 판단 후 트리거 자동 생성 |
| `loop_dashboard.py` | KPI 시각화 대시보드 (Streamlit) |
| `.env` | Slack/Notion 연동용 환경 변수 설정 |
| `gpt_trigger_*.json` | 루프 실행 트리거 파일 |

---

## 🧠 실행 흐름

1. `loop_launcher.py` 실행 → 루프 순차 실행  
2. 실행 로그 → `logs/loop_launcher.log` 저장  
3. 회고 실행: `feedback_loop.py` → KPI 자동 생성  
4. 판단 실행: `ai_trigger_decider.py` → 트리거 자동 생성  
5. `loop_dashboard.py` 실행 시 상태 대시보드 확인 가능

---

## ⚙️ 환경 설정 (.env 예시)

```bash
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/XXX
NOTION_TOKEN=secret_xxxx
NOTION_DATABASE_ID=xxxxxxxxx
EXECUTION_MODE=company
```

---

## 📤 Slack/Notion 전송 여부

- memory_manifest에 따라 자동 연동
- GDrive는 현재 제외됨 (추후 연동 가능)

---

## 🛠️ 설치 및 실행

1. 폴더에 ZIP 압축 해제
2. `.env` 설정
3. Python 실행: `python loop_launcher.py`
4. KPI 분석: `python feedback_loop.py`
5. 대시보드 실행: `streamlit run loop_dashboard.py`

---

## 📁 기타

- 모든 결과는 `.memory/`, `logs/`, `outputs/` 폴더에 저장됩니다.
- 복원 가능 구조로 설계되어 있으며, ZIP + 지시문으로 언제든지 이식 가능합니다.