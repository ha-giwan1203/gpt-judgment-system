import json
from pathlib import Path

GENE_PATH = Path("logs/loop_genes.json")
SCORE_PATH = Path("logs/loop_score_tracker.json")

def explain_loop(loop_name):
    gene_data = json.load(open(GENE_PATH, encoding="utf-8")) if GENE_PATH.exists() else {}
    score_data = json.load(open(SCORE_PATH, encoding="utf-8")) if SCORE_PATH.exists() else {}

    gene = gene_data.get(loop_name)
    score_info = score_data.get(loop_name)

    if not gene:
        return f"❌ 유전자 정보 없음 for {loop_name}"

    explanation = f"🧠 루프 `{loop_name}` 설명:\n"
    explanation += f"- 공격성: {gene['aggressiveness']} → 빠른 실행 가능하지만 실패 가능성 있음\n"
    explanation += f"- 협업성: {gene['collaboration']} → 다른 루프와 연결에 유리함\n"
    explanation += f"- 안정성: {gene['stability']} → 성공률 높일 수 있음\n"
    explanation += f"- 돌연변이율: {gene['mutation_rate']}\n"

    if score_info:
        explanation += f"- 평균 성능 점수: {score_info['average_score']} (±{score_info['stdev']}) based on {score_info['runs']} runs\n"

    return explanation

if __name__ == "__main__":
    print(explain_loop("loop_recommender.py"))