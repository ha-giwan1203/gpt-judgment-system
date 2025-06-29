import streamlit as st
import os

st.set_page_config(page_title="GPT 판단 시스템", layout="wide")

st.title("🧠 GPT 판단 시스템")
st.markdown("""
이 시스템은 GPT 기반으로 파일을 판단하고, 자동 보고서를 생성하는 Web UI입니다.

---
""")

# 업로드
uploaded_file = st.file_uploader("판단할 파일을 업로드하세요", type=["txt", "pdf", "docx", "csv"])

if uploaded_file:
    st.success(f"파일 업로드 완료: {uploaded_file.name}")

    # 파일 저장
    save_path = os.path.join("reports", uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info("GPT 판단 중...")

    # 판단 결과 예시 출력 (임시)
    st.markdown("""
    ### 📝 판단 결과
    - 분류: 예시_카테고리
    - 판단 이유: 이 판단은 파일 내용에 기반하여 예시로 생성되었습니다.
    """)

    # 자동 저장 완료
    st.success("판단 결과 자동 저장 완료 ✅")

else:
    st.warning("파일을 업로드하면 판단이 시작됩니다.")
