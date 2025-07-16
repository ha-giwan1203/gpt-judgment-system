import streamlit as st
import json
from collections import Counter
from datetime import datetime

st.set_page_config(page_title="GIWANOS 추천 루프 대시보드", layout="wide")

st.title("📊 GIWANOS 추천 루프 대시보드")

# 추천 로그 로드
def load_data():
    try:
        with open("loop_recommendation_log.json", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

data = load_data()
if not data:
    st.warning("추천 로그 데이터가 없습니다.")
    st.stop()

# 추천 횟수 카운트
loop_counts = Counter()
for entry in data:
    for r in entry.get("recommendations", []):
        loop_counts[r["loop"]] += 1

# 📈 추천 횟수 시각화
st.subheader("루프별 추천 횟수")
st.bar_chart(loop_counts)

# 📅 최근 추천 내역
st.subheader("최근 추천 기록 (최신 5개)")
for entry in data[-5:][::-1]:
    ts = entry.get("timestamp", "N/A")
    st.markdown(f"### {ts}")
    for r in entry.get("recommendations", []):
        st.markdown(f"- `{r['loop']}`: {r['reason']} (우선순위 {r['priority']})")
    st.markdown("---")