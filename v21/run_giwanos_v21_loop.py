# run_giwanos_v21_loop.py
from giwanos_self_evolution.loop_mutator import mutate_loop
from datetime import datetime

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def main():
    log("🧬 GIWANOS v21 루프 진화기 시작")
    loop = input("🧠 복제/진화할 루프 이름을 입력하세요: ").strip()
    result = mutate_loop(loop)
    if result:
        for name, data in result.items():
            log(f"✅ 생성된 루프: {name}")
            log(f"→ 중요도: {data['importance']}, 변이 원본: {data['mutated_from']}")
    else:
        log("❌ 루프 생성 실패 또는 철학 없음")
    log("🏁 진화기 종료")

if __name__ == "__main__":
    main()
