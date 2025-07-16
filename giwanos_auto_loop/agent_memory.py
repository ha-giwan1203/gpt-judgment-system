class AgentMemory:
    def __init__(self):
        self.memory = []

    def load_memory(self):
        # 실제로는 JSON 또는 DB에서 불러올 수 있음
        self.memory = [
            {"context": "불량품 판정 기준", "response": "기준 외 수치는 불량으로 처리"},
            {"context": "작업자 피드백", "response": "휴먼에러가 자주 발생함"}
        ]

    def query(self, context):
        # 간단한 유사 검색 (샘플)
        for item in self.memory:
            if item["context"] in context:
                return item["response"]
        return "이전에 기록된 정보 없음"
