import subprocess
from datetime import datetime

print(f"🧬 [GIWANOS 진화 루프 v2.0 시작] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def run(name, script):
    print(f"▶️ {name} 실행 중...")
    try:
        subprocess.run(["python", script], check=True)
    except Exception as e:
        print(f"❌ {name} 오류 발생: {e}")

steps = [
    ("루프 실행", "./loop_launcher_local.py"),
    ("회고 분석", "./feedback_loop.py"),
    ("오류 분석", "./loop_error_explainer.py"),
    ("GPT 회고 판단", "./loop_reflector.py"),
    ("구조 수정 제안", "./auto_mutator.py"),
    ("조건 분기 판단", "./flow_tree.py"),
    ("회고 자동 전송 (Notion)", "./notion_auto_reporter_fixed_v2.py")
]

for name, script in steps:
    run(name, script)

print(f"✅ GIWANOS 진화 루프 v2.0 완료")