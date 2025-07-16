import json
from datetime import datetime
from pathlib import Path
from random import uniform

GENES_PATH = Path("logs/loop_genes.json")
RESULT_HUB_PATH = Path("logs/loop_result_hub.json")
FUSION_TREE_PATH = Path("logs/loop_fusion_tree.json")
NEW_GENES_PATH = Path("logs/loop_genes_fused.json")

def fuse_loops(parent1, parent2, new_loop_name):
    if not GENES_PATH.exists() or not RESULT_HUB_PATH.exists():
        print("❌ 유전자 또는 실행 결과 없음")
        return

    genes = json.load(open(GENES_PATH, encoding="utf-8"))
    results = json.load(open(RESULT_HUB_PATH, encoding="utf-8"))
    fusion_tree = json.load(open(FUSION_TREE_PATH, encoding="utf-8")) if FUSION_TREE_PATH.exists() else {}

    g1 = genes.get(parent1)
    g2 = genes.get(parent2)

    if not g1 or not g2:
        print("❌ 부모 루프 유전자 없음")
        return

    # 유전자 평균 + 약간의 변이
    fused = {
        k: round((g1[k] + g2[k]) / 2 + uniform(-0.05, 0.05), 3)
        if k != "mutation_rate" else round(uniform(0.05, 0.15), 3)
        for k in g1
    }

    # 유전자 저장
    with open(NEW_GENES_PATH, "w", encoding="utf-8") as f:
        json.dump({new_loop_name: fused}, f, indent=2, ensure_ascii=False)

    # 계보 트리 저장
    fusion_tree[new_loop_name] = {
        "parents": [parent1, parent2],
        "created_at": datetime.now().isoformat(),
        "fused_traits": fused
    }
    with open(FUSION_TREE_PATH, "w", encoding="utf-8") as f:
        json.dump(fusion_tree, f, indent=2, ensure_ascii=False)

    print(f"🧬 새로운 합성 루프 생성됨: {new_loop_name}")
    return fused

if __name__ == "__main__":
    fuse_loops("loop_recommender.py", "loop_explainer.py", "loop_rec_explainer_fused.py")