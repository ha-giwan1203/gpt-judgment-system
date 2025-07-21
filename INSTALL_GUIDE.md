# 🛠️ GIWANOS 설치 가이드 (v2025_07_19)

## ✅ 설치 전 준비사항
1. Python 3.10 이상 설치
2. 필수 패키지 설치:
```bash
pip install -r requirements.txt
```

---

## 🚀 설치 방법

### 1. 설치 스크립트 실행
```bash
python setup_giwanos.py
```
- `.env` 자동 생성됨 (`config/.env.template` 기반)
- 폴더 자동 생성됨 (`reflections`, `logs`, `_보존`, ...)

---

## 🧠 주요 실행 파일

| 실행기 | 설명 |
|--------|------|
| `loop_main_ui.py` | 루프 선택 실행 메뉴 |
| `auto_loop_discovery_runner.py` | 전체 루프 자동 실행기 |
| `upload_final_runner.py` | 회고 결과 전송기 (Slack/Notion) |
| `generate_reflection_pdf.py` | 회고 PDF 생성기 |
| `zip_backup_generator.py` | ZIP 백업 루프 |
| `file_sort_for_지완OS_v2.py` | 정리기 루프 실행기 |
| `loop_webhook_server.py` | Webhook 기반 외부 호출 루프 |

---

## 📁 폴더 구조

- `logs/` → 실행 로그, 오류 기록
- `loop_backups/` → 회고 및 정리 ZIP 백업
- `reflections/` → 회고 결과물 PDF/MD 저장
- `_보존`, `_정리_후보`, `_검토_필요`, `_분류불가` → 정리 루프 대상 분류

---

## 🔐 환경 설정 (.env)
- `.env`는 설치 시 자동 생성됨
- 수동 설정 시 참조: `config/.env.template`

