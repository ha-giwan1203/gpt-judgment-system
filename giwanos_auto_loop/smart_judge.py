from giwanos_auto_loop.agent_memory import AgentMemory

def smart_tree_judge(context, memory: AgentMemory):
    # 트리 기반 판단 시뮬레이터
    # 실패 원인을 분석하고 가지별 판단을 비교 (샘플 구현)
    reason = memory.query(context)
    if "잘못" in reason or "오류" in reason:
        return {
            "status": "improved",
            "reason": reason,
            "suggestion": "개선된 판단 수행됨"
        }
    return {
        "status": "same",
        "reason": reason
    }
