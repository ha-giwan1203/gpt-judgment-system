import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="루프 실험 결과 뷰어", layout="wide")
st.title("🧪 GIWANOS 루프 실험 로그 뷰어")

EXPERIMENT_LOG = Path("logs/loop_lab_experiments.json")

if not EXPERIMENT_LOG.exists():
    st.warning("실험 기록 파일이 없습니다.")
    st.stop()

experiments = json.load(open(EXPERIMENT_LOG, encoding="utf-8"))

st.markdown(f"총 실험 세션 수: **{len(experiments)}**")

for exp in experiments[::-1]:
    st.subheader(f"🔬 그룹: {exp['group']}")
    st.markdown(f"- 실행 시각: `{exp['executed_at']}`")
    st.markdown(f"- 테스트 루프: {', '.join(exp['tested_loops'])}")
    st.markdown(f"- 노트: {exp.get('notes', '-')}")
    st.markdown("---")