
# memory_search_injection.py

from search_memory_with_prompt import search_memory_for_context

def get_memory_context_for_evolution(topic: str = "이번 진화에서 참고할 회고는?"):
    try:
        print(f"🔍 기억 검색 중: '{topic}'")
        return search_memory_for_context(topic)
    except Exception as e:
        print("❌ 기억 검색 실패:", e)
        return "기억 검색 실패: 오류 발생"

# 진화 루프 내 사용 예:
if __name__ == "__main__":
    context = get_memory_context_for_evolution("정산 루프 과거 오류는?")
    print("🧠 기억 기반 회고 컨텍스트:")
    print(context)
