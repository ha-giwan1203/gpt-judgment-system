
import streamlit as st
import json
import os

st.set_page_config(page_title="GIWANOS 상태 대시보드", layout="wide")
st.title("🧠 GIWANOS 사고 루프 대시보드")

base_path = "./giwanos_auto_loop"

def show_json(title, path):
    st.subheader(title)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            st.json(json.load(f))
    else:
        st.warning(f"{os.path.basename(path)} 파일 없음")

show_json("📊 루프 메모리 기록 (memory_manifest.json)", os.path.join(base_path, "memory_manifest.json"))
show_json("📋 회고 로그 요약 (reflection_summary.json)", os.path.join(base_path, "reflection_summary.json"))
show_json("🖥 현재 디바이스 정보 (pc_status.json)", os.path.join(base_path, "pc_status.json"))
show_json("🔒 디바이스 역할 및 정책 (device_roles.json)", os.path.join(base_path, "device_roles.json"))
show_json("🧭 상황 정보 (giwanos_context.json)", os.path.join(base_path, "giwanos_context.json"))
show_json("🚦 실행 트리거 상태 (gpt_trigger.json)", os.path.join(base_path, "gpt_trigger.json"))
