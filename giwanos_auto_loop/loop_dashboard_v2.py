import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="GIWANOS 루프 종합 대시보드", layout="wide")
st.title("📊 GIWANOS 루프 운영 대시보드 v2")

# Load data files
paths = {
    "genes": Path("logs/loop_genes.json"),
    "scores": Path("logs/loop_score_tracker.json"),
    "survivors": Path("logs/loop_survivors.json"),
    "lineage": Path("logs/loop_gene_lineage.json")
}

data = {}
for key, path in paths.items():
    if path.exists():
        data[key] = json.load(open(path, encoding="utf-8"))
    else:
        data[key] = None
        st.warning(f"{key} 파일 없음: {path}")

# 생존 루프 표시
if data["survivors"]:
    st.subheader("✅ 생존 루프 목록")
    for loop in data["survivors"]:
        st.markdown(f"- **{loop}**")

# 루프 평균 점수 표시
if data["scores"]:
    st.subheader("📈 루프 평균 점수 (벤치마크 기반)")
    chart_data = {loop: info["average_score"] for loop, info in data["scores"].items()}
    st.bar_chart(chart_data)

# 루프 유전자 트리 요약
if data["lineage"]:
    st.subheader("🌳 루프 계보 요약")
    for child, entries in data["lineage"].items():
        for e in entries:
            parents = ", ".join(e.get("parents", []))
            st.markdown(f"- `{child}` ← {parents} @ {e.get('created_at', 'N/A')}")