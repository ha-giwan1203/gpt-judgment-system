import streamlit as st
import json
from pathlib import Path
from collections import Counter

st.set_page_config(page_title="루프 피드백 대시보드", layout="wide")
st.title("👍 GIWANOS 사용자 피드백 대시보드")

FEEDBACK_LOG = Path("logs/loop_user_feedback.json")

if not FEEDBACK_LOG.exists():
    st.warning("피드백 로그 파일이 없습니다.")
    st.stop()

data = json.load(open(FEEDBACK_LOG, encoding="utf-8"))

loop_feedback = Counter()
for entry in data:
    symbol = entry["feedback"]
    key = f"{entry['loop']} ({symbol})"
    loop_feedback[key] += 1

st.subheader("📊 루프별 사용자 피드백 요약")
for key, count in loop_feedback.items():
    st.markdown(f"- `{key}`: {count}회")

st.bar_chart(dict(loop_feedback))