import os
import json
from datetime import datetime

def mutate_genes():
    # 샘플 유전자 데이터 생성
    genes = {
        "collaboration": 0.88,
        "risk_tolerance": 0.61,
        "stability": 0.93
    }
    mutated = {
        "genes": genes,
        "mutated_at": datetime.now().isoformat()
    }

    # logs 경로에 파일 저장
    os.makedirs("logs", exist_ok=True)
    path = os.path.join("logs", "loop_genes_mutated.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(mutated, f, indent=2, ensure_ascii=False)

    print(f"✅ 루프 유전자 돌연변이 완료 → {path}")

if __name__ == "__main__":
    print("[루프 시작] 실행 목적: 진화")
    mutate_genes()