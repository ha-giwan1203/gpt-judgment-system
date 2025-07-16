
import os
import json
from sentence_transformers import SentenceTransformer
import hashlib

# 설정
MEMORY_PATH = ".memory/"
OUTPUT_PATH = "giwanos_memory/vector_index/"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

os.makedirs(OUTPUT_PATH, exist_ok=True)
model = SentenceTransformer(EMBEDDING_MODEL)

def embed_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    if not text.strip():
        return None
    embedding = model.encode(text)
    return {
        "source": os.path.basename(filepath),
        "text": text[:1000],
        "embedding": embedding.tolist()
    }

def save_embedding(data, filename):
    hash_key = hashlib.sha256(filename.encode()).hexdigest()[:12]
    out_path = os.path.join(OUTPUT_PATH, f"{hash_key}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ 저장됨: {out_path}")

def main():
    print("🔍 .memory/ 폴더 내 기억 파일 임베딩 중...")
    for fname in os.listdir(MEMORY_PATH):
        if fname.endswith((".md", ".json", ".txt")):
            fpath = os.path.join(MEMORY_PATH, fname)
            try:
                result = embed_file(fpath)
                if result:
                    save_embedding(result, fname)
            except Exception as e:
                print(f"❌ 오류 ({fname}):", e)

if __name__ == "__main__":
    main()
