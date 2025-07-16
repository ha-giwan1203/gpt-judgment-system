import streamlit as st
import json
import os
import glob

st.set_page_config(page_title="GIWANOS 시스템 대시보드", layout="wide")
st.title("🧠 GIWANOS 시스템 대시보드")

# 경로 고정
base_path = "./giwanos_memory"
pdf_path = "./reports/summary_pdfs"

files = {
    "📄 GPT 기억 스냅샷": "gpt_memory_snapshot.json",
    "📄 기억 요약 설명": "gpt_memory_summary.md",
    "📊 피드백 로그": "loop_feedback_log.json",
    "🧬 유전자 로그": "loop_genes_mutated.json",
    "📊 루프 추천 결과": "loop_recommendation_model.json",
    "🧠 판단 로그": "judgement_feedback_log.json"
}

# 메타 파일들 표시
for label, filename in files.items():
    st.markdown("---")
    st.subheader(label)
    full_path = os.path.join(base_path, filename)
    if os.path.exists(full_path):
        if filename.endswith(".json"):
            with open(full_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                st.json(data)
        elif filename.endswith(".md") or filename.endswith(".txt"):
            with open(full_path, "r", encoding="utf-8") as f:
                st.code(f.read(), language="markdown")
        else:
            st.write("✅ 파일 존재함")
    else:
        st.error(f"❌ 파일 없음: {filename}")

# 회고 PDF 탐색
st.markdown("---")
st.subheader("📄 회고 요약 PDF (loop_summary_report_*)")
summary_pdfs = sorted(glob.glob(os.path.join(pdf_path, "loop_summary_report_*.pdf")))
if summary_pdfs:
    for pdf_file in summary_pdfs:
        filename = os.path.basename(pdf_file)
        st.markdown(f"📎 [{filename}]({pdf_file})")
else:
    st.warning("요약 회고 PDF가 없습니다.")

# 리플렉션 PDF 탐색
st.markdown("---")
st.subheader("📄 회고 리플렉션 PDF (loop_reflection_log_*)")
reflection_pdfs = sorted(glob.glob(os.path.join(pdf_path, "loop_reflection_log_*.pdf")))
if reflection_pdfs:
    for pdf_file in reflection_pdfs:
        filename = os.path.basename(pdf_file)
        st.markdown(f"📎 [{filename}]({pdf_file})")
else:
    st.warning("리플렉션 회고 PDF가 없습니다.")