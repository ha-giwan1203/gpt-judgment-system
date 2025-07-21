# 🧰 GIWANOS 설치 가이드 (최종 버전 기준)

이 문서는 `GIWANOS_FINAL_VALIDATED_COMPLETE.zip` 기준으로  
지완 시스템을 설치, 실행, 확장하는 전체 순서를 안내합니다.

---

## 📦 압축 해제

1. zip 파일을 원하는 폴더에 압축 해제
2. 아래 디렉토리 구조가 있는지 확인
   - run/
   - loop_modules/
   - config/
   - README, loop_memory_state.json, .env 등

---

## 🛠️ 설치 단계

1. `.env` 설정 확인  
   - `.env` 파일이 존재하지 않으면 → `setup_config.py` 실행
   - 기본값으로 설정되어 있음

2. 패키지 설치

```bash
python setup_giwanos.py
```

---

## ▶️ 실행 방법

### CLI 방식

```bash
python run/loop_main.py
```

### UI 방식 (Streamlit)

```bash
streamlit run loop_main_ui.py
```

---

## 💡 추천 루프 흐름

1. 회고 루프 실행 → `loop_reflection_gpt_agent.py`
2. 회고 PDF 생성 → `generate_reflection_pdf.py`
3. 연동 루프 실행 → `upload_final_runner.py`
4. Slack/Notion/ZIP/Drive 전송
5. 루프 추천 실행 → `loop_recommender.py`
6. 진단 실행 → `loop_diagnostics.py`

---

## 🔁 외부 트리거 사용 시

- 이메일 트리거: `loop_email_trigger.py`
- Webhook 트리거: `loop_webhook_server.py`

---

## 🧠 재정합된 구성 요소 요약

- `.env`, `token.json` → 설정 완료됨
- Slack / Notion / Gmail / Drive 연동 가능
- 루프: 회고, 전송, 추천, 진단, 자동화 루프 포함
- 백업 및 ZIP 구조 완비
- 시각화: Plotly + Streamlit 기반
- 실행기 `.bat` / `.spec` 구성 포함

---

지금 구조는 실제 설치/전달/운영/백업까지 가능한  
**최종 GIWANOS 루프 운영체계 기준 구조**입니다.
