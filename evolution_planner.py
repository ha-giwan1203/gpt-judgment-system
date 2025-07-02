import os

def extract_state(prompt):
    modules = []
    lines = prompt.lower()

    if "memory_restorer" in lines: modules.append("memory_restorer")
    if "memory_tracker" in lines: modules.append("memory_tracker")
    if "memory_dashboard" in lines: modules.append("memory_dashboard")
    if "auto_scheduler" in lines: modules.append("auto_scheduler")
    if "actiongpt" in lines: modules.append("actiongpt")
    if "report_auto_dispatcher" in lines: modules.append("report_auto_dispatcher")
    if "notion" in lines: modules.append("notion_integration")

    return modules

def suggest_plan(modules):
    goals = []
    if "memory_dashboard" in modules:
        goals.append("기억 시각화 UI에 최근 diff 자동 반영")

    if "memory_tracker" in modules:
        goals.append("restore_prompt.txt 변경 시 Slack/이메일 알림 기능 추가")

    if "actiongpt" in modules:
        goals.append("설명형 명령 기반 자동 실행 루틴 강화")

    if "auto_scheduler" in modules:
        goals.append("정기 스케줄 + 조건 기반 복원/실행 자동화")

    if "notion_integration" in modules:
        goals.append("보고서 전송 전 AI 자동 요약 필터 적용")

    if not goals:
        goals.append("모듈 기반 자동 목표 설정을 위해 구성 요소를 확장하세요.")

    return goals

def run_planner():
    path = "restore_prompt.txt"
    if not os.path.exists(path):
        print("⚠️ restore_prompt.txt 없음")
        return

    with open(path, "r", encoding="utf-8") as f:
        prompt = f.read()

    modules = extract_state(prompt)
    goals = suggest_plan(modules)

    print("🧠 복원 상태 기반 시스템 분석")
    print(f"✅ 감지된 구성 요소: {', '.join(modules)}\n")
    print("🎯 자동 생성된 실행 목표:")
    for i, goal in enumerate(goals, 1):
        print(f"{i}. {goal}")

if __name__ == "__main__":
    run_planner()
