
import os
import json
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="GIWANOS 대시보드", layout="wide")
st.title("📊 GIWANOS 루프 대시보드")

# ✅ 트리거 상태 보기
st.header("🔍 트리거 상태")
if os.path.exists("gpt_trigger.json"):
    with open("gpt_trigger.json", "r", encoding="utf-8") as f:
        trigger = json.load(f)
    st.json(trigger)
else:
    st.warning("트리거 파일이 없습니다.")

# ✅ 정합률 + 오류 비율 시각화
st.header("📈 회고 정합률 및 오류 비율")
feedback_file = "logs/loop_feedback_log.json"
if os.path.exists(feedback_file):
    with open(feedback_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        if isinstance(data, list):
            data = data[0]
        summary = data.get("summary", "")
        errors = data.get("errors", [])
        st.text(f"요약: {summary}")

        error_types = {}
        for e in errors:
            et = e.get("type", "기타")
            error_types[et] = error_types.get(et, 0) + 1
        if error_types:
            st.subheader("오류 유형 분포")
            df = pd.DataFrame(error_types.items(), columns=["오류 유형", "건수"])
            st.bar_chart(df.set_index("오류 유형"))
else:
    st.info("회고 로그 파일이 없습니다.")

# ✅ 진화 요약 시각화
st.header("🧬 진화 루프 결과")
genes_file = "logs/loop_genes_mutated.json"
if os.path.exists(genes_file):
    with open(genes_file, "r", encoding="utf-8") as f:
        gdata = json.load(f)
        mutated = gdata.get("mutated_genes", [])
        improvements = gdata.get("improvements", [])
        st.write(f"변경된 유전자 수: {len(mutated)}개")
        if improvements:
            st.subheader("개선사항 Top 5")
            st.write(improvements[:5])
            imp_df = pd.DataFrame({"개선 항목": improvements[:5], "개수": [1]*len(improvements[:5])})
            st.bar_chart(imp_df.set_index("개선 항목"))
else:
    st.info("진화 로그 파일이 없습니다.")

# ✅ 최근 ZIP 백업 보기
st.header("📦 ZIP 백업 리스트")
backup_dir = "loop_backups"
if os.path.exists(backup_dir):
    files = sorted([f for f in os.listdir(backup_dir) if f.endswith(".zip")], reverse=True)
    for f in files[:5]:
        st.write(f"🗂️ {f}")
else:
    st.warning("백업 폴더가 없습니다.")

# ✅ 회고 PDF 링크
st.header("📄 최근 회고 PDF")
pdfs = sorted([f for f in os.listdir() if f.startswith("loop_reflection_log_") and f.endswith(".pdf")], reverse=True)
if pdfs:
    latest = pdfs[0]
    st.write(f"[{latest} 보기](./{latest})")
else:
    st.info("회고 PDF가 없습니다.")
