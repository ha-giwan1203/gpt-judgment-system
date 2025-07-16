import streamlit as st

# 설치 상태 표시 텍스트
try:
    with open("dashboard_install_status.txt", "r", encoding="utf-8") as f:
        status = f.read()
    st.markdown("### 🚀 GIWANOS 설치 상태")
    st.code(status)
except FileNotFoundError:
    st.warning("⚠️ 설치 상태 텍스트 파일이 없습니다.")

st.markdown("---")
st.markdown("🧠 여기에 루프 실행 결과, 회고 로그, 추천 흐름 등을 붙일 수 있습니다.")