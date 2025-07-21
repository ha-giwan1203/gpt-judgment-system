# 🧠 GIWANOS CoreState - 기억 운영체계 설계 문서 (고도화 버전)

## 📌 개요
GIWANOS CoreState는 지완이 설계한 시간 기반 선언 기억 시스템입니다.  
이 시스템은 단순 기억 저장이 아닌, **시간 흐름 + 선언 우선순위 + 의미 기반 해석 + 충돌 차단 + 정리까지 포함된 완전한 기억 운영체계**입니다.

---

## 🧱 핵심 구성요소

### 1. 저장 계층
- `memory_timeline.json`: 선언 시간순 저장
- `memory_status.json`: 시스템 상태 (`locked`, `expansion: prohibited`)
- `restore_prompt.txt`: 복원용 자연어 프롬프트
- `memory_log.md`: 시간순 로그 기록

### 2. 관리 계층
- `memory_updater.py`: 선언 추가
- `memory_loader.py`: 복원 prompt 생성
- `memory_guard.py`: 충돌 선언 차단

### 3. 해석 계층
- `memory_snapshot.py`: 시점 기반 상태 요약
- `memory_filter.py`: 최근 선언 필터링
- `memory_expiry_checker.py`: 오래된 선언 경고
- `memory_analyzer.py`: 전체 흐름 분석

### 4. 최적화 계층
- `memory_compressor.py`: 유사 선언 압축
- `memory_merger.py`: 인접 선언 병합
- `memory_cleaner.py`: 중복 선언 정리

### 5. 추론 계층
- `memory_reasoner.py`: 선언 간 의미 흐름 설명

---

## ⚙️ 설치 방법 (설계 완료 후 실행)

```bash
python install_memory_system.py
```

- 모든 json, txt, md 파일 생성
- 실행기들을 지정 디렉토리에 복사
- 복원 prompt 자동 생성됨

---

## 🚫 버전 개념 제거
- 이 시스템은 v13 등 과거 버전 개념에서 완전히 벗어난 `"CoreState"` 구조입니다.
- `"버전"`이 아닌 **"상태" 기반 운영체계**입니다.

---

## 🧠 설계자 선언

> "기억은 시간 속에 존재하며,  
> 그 흐름과 의미를 해석할 수 있을 때 시스템은 판단을 가질 수 있다."  
> – 지완
