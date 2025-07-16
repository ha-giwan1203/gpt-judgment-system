
import streamlit as st
import json
import os

st.set_page_config(page_title="GIWANOS 대시보드", layout="wide")

st.title("🧠 GIWANOS 상태 대시보드")

# 파일 로딩 함수
def load_json(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# 유전자 상태 시각화
st.header("🧬 유전자 상태")
genes = load_json("logs/loop_genes_mutated.json").get("genes", {})
if genes:
    st.bar_chart(genes)
else:
    st.info("유전자 정보가 없습니다.")

# 회고 피드백 로그 요약
st.header("🧾 회고 피드백 로그")
feedback_log = load_json("logs/loop_feedback_log.json")
if isinstance(feedback_log, list) and feedback_log:
    st.write(f"총 회고 로그 수: {len(feedback_log)}")
    st.json(feedback_log[-1])
else:
    st.warning("회고 피드백 로그가 비어있습니다.")

# 추천 루프
st.header("🤖 추천 루프")
recommend = load_json("logs/loop_recommendation_model.json")
if recommend:
    st.success(f"다음 추천 루프: {recommend.get('recommended_next')}")
    st.json(recommend)
else:
    st.info("추천 모델 정보가 없습니다.")
