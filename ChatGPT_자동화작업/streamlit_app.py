import streamlit as st
import os
import datetime

# 페이지 제목
st.set_page_config(page_title="GPT 판단 시스템", layout="centered")
st.title("📂 GPT 판단 시스템 Web UI")

# 파일 업로드
uploaded_file = st.file_uploader("📄 판단할 파일 업로드", type=["txt", "md", "json"])

if uploaded_file is not None:
    # 업로드한 파일 내용 읽기
    content = uploaded_file.read().decode("utf-8")

    # 간단한 판단 예시 (길이 판단)
    length = len(content)
    if length < 100:
        judgment = "📘 간단한 문서입니다."
    elif length < 1000:
        judgment = "📙 중간 길이의 문서입니다."
    else:
        judgment = "📕 긴 문서입니다."

    # 판단 결과 출력
    st.subheader("🧠 판단 결과")
    st.markdown(judgment)

    # 보고서 저장
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = os.path.join(reports_dir, f"report_{now}.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"# 판단 결과\n\n{judgment}\n\n---\n\n원본 내용:\n\n{content}")

    st.success(f"✅ 보고서 저장 완료: `{report_path}`")