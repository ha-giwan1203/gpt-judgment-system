import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(page_title="GIWANOS 루프 대시보드", layout="wide")
st.title("📊 GIWANOS 시스템 상태 대시보드")

# KPI 시각화
st.header("🧠 루프 실행 KPI 요약")

kpi_path = ".memory/feedback_kpi_latest.json"
if os.path.exists(kpi_path):
    with open(kpi_path, "r", encoding="utf-8") as f:
        kpi = json.load(f)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("총 실행", kpi["총 실행"])
    col2.metric("성공", kpi["성공"])
    col3.metric("실패", kpi["실패"])
    col4.metric("성공률", f"{kpi['성공률']}%")

    if kpi["실패"] > 0:
        st.subheader("❌ 실패 내역")
        for fail in kpi["실패내역"]:
            st.text(fail)
else:
    st.warning("KPI 파일이 아직 생성되지 않았습니다.")

# 로그 미리보기
st.header("📄 루프 실행 로그")
log_path = "logs/loop_launcher.log"
if os.path.exists(log_path):
    with open(log_path, "r", encoding="utf-8") as f:
        lines = f.readlines()[-15:]
    for line in lines:
        st.code(line.strip(), language="log")
else:
    st.info("로그 파일 없음")