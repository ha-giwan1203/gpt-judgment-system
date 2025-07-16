import json
import graphviz
from pathlib import Path

FUSION_TREE_PATH = Path("logs/loop_fusion_tree.json")

def visualize_fusion_tree(output_file="loop_fusion_tree"):
    if not FUSION_TREE_PATH.exists():
        print("❌ 계보 파일이 없습니다.")
        return

    tree = json.load(open(FUSION_TREE_PATH, encoding="utf-8"))
    dot = graphviz.Digraph(format="png")
    dot.attr(rankdir="LR")

    for child, data in tree.items():
        parents = data.get("parents", [])
        for p in parents:
            dot.edge(p, child)
        dot.node(child, shape="box", style="filled", color="lightblue")

    dot.render(output_file, cleanup=True)
    print(f"🌳 루프 합성 계보 트리 시각화 완료 → {output_file}.png")

if __name__ == "__main__":
    visualize_fusion_tree()