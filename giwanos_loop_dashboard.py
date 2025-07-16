
import streamlit as st
import json
import os

st.set_page_config(page_title="GIWANOS 루프 대시보드", layout="wide")
st.title("🧠 GIWANOS 루프 실행 결과 대시보드")

st.header("📌 최근 추천 루프 기록")
route_log_path = "C:/giwanos/v15/giwanos_path_loop/route_log.json"
if os.path.exists(route_log_path):
    with open(route_log_path, "r", encoding="utf-8") as f:
        route_logs = json.load(f)
        for log in reversed(route_logs[-5:]):
            st.markdown(f"**🕒 {log['timestamp']}**")
            st.write(f"입력: {log['input']}")
            st.write("추천 루프:", " → ".join(log['route']))
            st.markdown("---")
else:
    st.warning("route_log.json 파일이 없습니다.")

st.header("🧬 복제된 루프")
replicated_path = "C:/giwanos/v21/giwanos_self_evolution/replicated_loops.json"
if os.path.exists(replicated_path):
    with open(replicated_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        for name, loop in data.items():
            st.markdown(f"**{name}** (from: {loop.get('mutated_from')})")
            st.write(f"중요도: {loop.get('importance')}, 생성: {loop.get('created_at')}")
            st.write(f"사유: {loop.get('reason', '-')}")
            st.markdown("---")
else:
    st.warning("복제 루프 데이터가 없습니다.")

st.header("⚡ 실시간 생성 루프")
live_path = "C:/giwanos/v23/self_created_loops.json"
if os.path.exists(live_path):
    with open(live_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        for id, loop in data.items():
            st.markdown(f"**🆔 {id}**")
            st.write(f"이름: {loop.get('name')}, 중요도: {loop.get('importance')}")
            st.write(f"사유: {loop.get('reason')}")
            st.markdown("---")
else:
    st.warning("실시간 생성 루프 데이터가 없습니다.")
