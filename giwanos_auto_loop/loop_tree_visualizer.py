import json
import graphviz
from pathlib import Path

LINEAGE_PATH = Path("logs/loop_gene_lineage.json")

def draw_loop_tree(output_file="loop_tree"):
    if not LINEAGE_PATH.exists():
        print("❌ 계보 파일 없음")
        return

    lineage = json.load(open(LINEAGE_PATH, encoding="utf-8"))
    dot = graphviz.Digraph(format="png")
    dot.attr(rankdir="LR")

    for child, entries in lineage.items():
        for e in entries:
            if "parents" in e:
                for parent in e["parents"]:
                    dot.edge(parent, child)
            else:
                dot.node(child)

    dot.render(output_file, cleanup=True)
    print(f"✅ 루프 트리 시각화 완료 → {output_file}.png")

if __name__ == "__main__":
    draw_loop_tree()