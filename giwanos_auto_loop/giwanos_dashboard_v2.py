
import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(page_title="GIWANOS 대시보드 v2", layout="wide")

st.title("🧠 GIWANOS 상태 대시보드 v2")

# 공통 로더
def load_json(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# 레이아웃: 탭 구성
tab1, tab2, tab3 = st.tabs(["🧬 유전자", "🧾 회고 로그", "🤖 추천 루프"])

# 탭 1: 유전자
with tab1:
    st.subheader("현재 유전자 상태")
    genes = load_json("logs/loop_genes_mutated.json").get("genes", {})
    if genes:
        st.bar_chart(genes)
        for k, v in genes.items():
            st.metric(label=k, value=v)
    else:
        st.warning("유전자 정보가 없습니다.")

# 탭 2: 회고 로그
with tab2:
    st.subheader("회고 피드백 로그")
    feedback = load_json("logs/loop_feedback_log.json")
    if isinstance(feedback, list) and feedback:
        st.write(f"총 회고 로그 수: {len(feedback)}")
        st.json(feedback[-1])  # 최신 항목
    else:
        st.info("회고 피드백 로그가 비어있습니다.")

# 탭 3: 추천 루프
with tab3:
    st.subheader("추천 루프 상태")
    model = load_json("logs/loop_recommendation_model.json")
    if model:
        next_loop = model.get("recommended_next", "없음")
        st.success(f"다음 추천 루프: {next_loop}")
        st.json(model)
    else:
        st.warning("추천 모델 정보가 없습니다.")
