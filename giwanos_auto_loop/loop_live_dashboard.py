import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="GIWANOS 실시간 루프 대시보드", layout="wide")
st.title("📡 GIWANOS Live 루프 대시보드")

LOGS = {
    "피드백": "logs/loop_user_feedback.json",
    "실험 기록": "logs/loop_lab_experiments.json",
    "추천 결과": "logs/loop_recommendation_model.json",
    "생존 루프": "logs/loop_survivors.json",
    "우선순위": "logs/loop_priority_model.json"
}

for name, path in LOGS.items():
    log_path = Path(path)
    st.subheader(f"📁 {name}")
    if log_path.exists():
        data = json.load(open(log_path, encoding="utf-8"))
        st.json(data)
    else:
        st.warning(f"{name} 로그 없음")

st.info("데이터는 실시간으로 로드되며 새로고침 시 갱신됩니다.")