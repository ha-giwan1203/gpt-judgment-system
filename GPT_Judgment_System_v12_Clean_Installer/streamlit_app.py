import streamlit as st
import os
from dotenv import load_dotenv

# 환경변수 로드
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
notion_token = os.getenv("NOTION_API_TOKEN")

drive_path = "G:/내 드라이브"

st.set_page_config(page_title="GPT 판단 시스템", layout="centered")
st.title("📄 GPT 판단 자동화 시스템 v12")

# API 키 상태 확인
if not api_key:
    st.warning("⚠️ 현재 OpenAI API 키가 설정되어 있지 않습니다. 판단 기능은 비활성화됩니다.")
else:
    st.success("✅ OpenAI API 키가 정상적으로 설정되어 있습니다.")

# Google Drive 상태 확인
if os.path.exists(drive_path):
    st.info(f"📂 Google Drive 연동 경로 확인됨: {drive_path}")
else:
    st.error("❌ Google Drive 경로를 찾을 수 없습니다. 설정을 확인해주세요.")

# 파일 업로드
uploaded_file = st.file_uploader("📎 판단할 파일 업로드", type=["txt", "pdf", "docx"])

if uploaded_file:
    st.success(f"✅ 업로드 완료: {uploaded_file.name}")
    st.markdown("(※ 키가 연동되면 자동 판단 + 리포트 + Notion 저장까지 실행됩니다)")
else:
    st.caption("파일을 업로드하면 판단이 시작됩니다.")

# 수동 실행 버튼들
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📦 백업 실행"):
        os.system("run_backup.bat")
        st.success("백업 실행 완료!")

with col2:
    if st.button("🔄 복원 실행"):
        os.system("run_restore.bat")
        st.success("복원 완료. 시스템 초기화됨")

with col3:
    if st.button("⏫ 버전 확인"):
        os.system("python version_check.py")
