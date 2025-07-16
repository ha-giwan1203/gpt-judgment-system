import json
import random
from pathlib import Path
from datetime import datetime

GENE_PATH = Path("logs/loop_genes.json")
LINEAGE_PATH = Path("logs/loop_gene_lineage.json")
OUTPUT_PATH = Path("logs/loop_genes_crossover.json")

def crossover_genes(loop1, loop2, new_loop_name):
    if not GENE_PATH.exists():
        print("❌ 유전자 파일 없음")
        return

    genes = json.load(open(GENE_PATH, encoding="utf-8"))
    g1 = genes.get(loop1)
    g2 = genes.get(loop2)

    if not g1 or not g2:
        print("❌ 부모 루프 유전자 누락")
        return

    # 유전자 평균 조합
    new_gene = {
        k: round((g1[k] + g2[k]) / 2, 3) if k != "mutation_rate" else round(random.uniform(0.05, 0.2), 3)
        for k in g1
    }

    # 결과 저장
    result = {new_loop_name: new_gene}
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    # 계보 업데이트
    lineage = json.load(open(LINEAGE_PATH, encoding="utf-8")) if LINEAGE_PATH.exists() else {}
    lineage[new_loop_name] = [{
        "created_at": datetime.now().isoformat(),
        "parents": [loop1, loop2],
        "merged_traits": new_gene
    }]
    with open(LINEAGE_PATH, "w", encoding="utf-8") as f:
        json.dump(lineage, f, indent=2, ensure_ascii=False)

    print(f"✅ 새로운 루프 유전자 생성: {new_loop_name}")
    return new_gene

if __name__ == "__main__":
    crossover_genes("loop_recommender.py", "loop_feedback_trainer.py", "loop_feedback_recommender.py")