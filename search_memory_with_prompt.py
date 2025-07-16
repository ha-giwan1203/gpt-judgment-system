
import os
from sentence_transformers import SentenceTransformer, util

# ✅ 지완 로컬 모델 경로
MODEL_PATH = "C:/giwanos/models/all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_PATH)

def search_memory_for_context(query: str = "이번 회고에 참고할 기억은?"):
    memory_texts = []
    memory_vectors = []
    memory_sources = []

    MEMORY_DB = "giwanos_memory/vector_index/"

    for fname in os.listdir(MEMORY_DB):
        if fname.endswith(".json"):
            with open(os.path.join(MEMORY_DB, fname), "r", encoding="utf-8") as f:
                import json
                data = json.load(f)
                memory_texts.append(data["text"])
                memory_vectors.append(data["embedding"])
                memory_sources.append(data["source"])

    if not memory_vectors:
        return "📂 기억 데이터가 없습니다."

    query_embedding = model.encode(query, convert_to_tensor=True)
    results = util.semantic_search(query_embedding, memory_vectors, top_k=3)[0]

    result_lines = ["📚 유사 기억 검색 결과:"]
    for r in results:
        idx = r["corpus_id"]
        score = r["score"]
        snippet = memory_texts[idx][:150].replace("\n", " ")
        result_lines.append(f"- ({score:.3f}) [{memory_sources[idx]}] {snippet}...")

    return "\n".join(result_lines)

if __name__ == "__main__":
    print(search_memory_for_context("정산 루프 오류 기억"))
