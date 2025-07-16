
import streamlit as st
import os
import json
from datetime import datetime
import subprocess

st.set_page_config(page_title="GIWANOS 루프 추천 및 실행 UI", layout="wide")
st.title("🧠 GIWANOS 루프 추천 · 회고 정리 · 자동 실행 대시보드")

# -----------------------------
# 추천 로직
def recommend_loops():
    recommendations = []

    # 조건 1: 최근 기억 수정
    try:
        with open(".memory/manifest.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            for entry in data.get("entries", []):
                updated = entry.get("updated_at", "")
                if " " in updated:
                    updated_dt = datetime.strptime(updated, "%Y-%m-%d %H:%M")
                    if (datetime.now() - updated_dt).total_seconds() < 86400:
                        recommendations.append(("진화 루프", "최근 기억 수정 → 진화 필요"))
                        break
    except:
        pass

    # 조건 2: 회고 PDF 없음
    if not os.path.exists("loop_reflection_with_memory.pdf"):
        recommendations.append(("회고 PDF 생성 루프", "회고 PDF 없음 → 정리 필요"))

    # 조건 3: Notion 업로드 누락 (가정)
    recommendations.append(("Notion 전송 루프", "전송 여부 미확인 → 점검 필요"))

    return recommendations

# -----------------------------
# 회고 PDF 정리
def list_reflection_pdfs():
    pdfs = []
    for fname in os.listdir():
        if fname.startswith("loop_reflection") and fname.endswith(".pdf"):
            try:
                timestamp = os.path.getmtime(fname)
                pdfs.append((fname, datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M")))
            except:
                continue
    pdfs.sort(reverse=True, key=lambda x: x[1])
    return pdfs

# -----------------------------
# UI 구성
st.subheader("📌 추천 루프")
recommendations = recommend_loops()
if recommendations:
    for r in recommendations:
        st.success(f"🔹 {r[0]} — {r[1]}")

    top_loop = recommendations[0][0]
    st.markdown(f"### ✅ 가장 우선 실행 추천 루프: **{top_loop}**")
    if st.button(f"🚀 '{top_loop}' 지금 실행하기"):
        # 실행 매핑
        exec_map = {
            "진화 루프": "python evolution_loop.py",
            "회고 PDF 생성 루프": "python generate_reflection_with_memory.py",
            "Notion 전송 루프": "python upload_notion_with_memory.py"
        }
        command = exec_map.get(top_loop)
        if command:
            st.info(f"실행 명령: `{command}`")
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            st.code(result.stdout + result.stderr)
        else:
            st.warning("❌ 해당 루프 실행 명령이 정의되어 있지 않습니다.")
else:
    st.info("모든 루프 상태가 안정적입니다. 추천 루프 없음.")

st.divider()
st.subheader("📄 회고 PDF 정리")
pdf_list = list_reflection_pdfs()
if pdf_list:
    for fname, mod_time in pdf_list:
        st.write(f"🗂️ `{fname}` - 마지막 수정: {mod_time}")
else:
    st.warning("📂 회고 PDF 파일이 존재하지 않습니다.")
