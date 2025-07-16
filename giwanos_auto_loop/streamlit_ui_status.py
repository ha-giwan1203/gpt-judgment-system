
import streamlit as st
import json
import os

st.set_page_config(page_title="GPT 사고 루프 상태", layout="wide")

st.title("🧠 지완 사고 루프 상태 대시보드")

base_path = "./giwanos_auto_loop"
manifest_path = os.path.join(base_path, "memory_manifest.json")
log_path = os.path.join(base_path, "loop_reflection_log.md")

st.subheader("📦 루프 실행 기록 (memory_manifest.json)")
if os.path.exists(manifest_path):
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
        st.json(manifest)
else:
    st.warning("memory_manifest.json 파일이 없습니다.")

st.subheader("📝 회고 로그 (loop_reflection_log.md)")
if os.path.exists(log_path):
    with open(log_path, "r", encoding="utf-8") as f:
        st.text(f.read())
else:
    st.warning("loop_reflection_log.md 파일이 없습니다.")
