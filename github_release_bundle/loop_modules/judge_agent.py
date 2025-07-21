import sys
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except AttributeError:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace', line_buffering=True)

def run_judgement():
    print("🧠 GIWANOS 판단기 실행 중...")
    # 간단한 판단 흐름 예시
    from datetime import datetime
    now = datetime.now()
    if now.hour < 12:
        result = "오전 루프 추천: 리더보드 생성"
    else:
        result = "오후 루프 추천: 회고 실행"
    print(f"[판단 결과] {result}")

if __name__ == "__main__":
    run_judgement()
