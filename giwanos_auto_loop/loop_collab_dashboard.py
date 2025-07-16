import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="루프 협업 시각화", layout="wide")
st.title("🤝 GIWANOS 루프 협업 시너지 대시보드")

COLLAB_PATH = Path("logs/loop_collaboration_score.json")

if not COLLAB_PATH.exists():
    st.warning("협업 점수 파일이 없습니다.")
    st.stop()

scores = json.load(open(COLLAB_PATH, encoding="utf-8"))
sorted_scores = sorted(scores.items(), key=lambda x: -x[1])

st.subheader("📈 상위 협업 루프 조합")
for pair, score in sorted_scores[:10]:
    st.markdown(f"- `{pair}` → 시너지 점수: **{score}**")

chart_data = {pair: score for pair, score in sorted_scores[:20]}
st.bar_chart(chart_data)