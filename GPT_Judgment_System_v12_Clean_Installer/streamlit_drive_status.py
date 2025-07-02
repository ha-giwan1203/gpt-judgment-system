import streamlit as st
import os

drive_path = "G:/내 드라이브"
if os.path.exists(drive_path):
    st.success(f"✅ Google Drive 연동됨: {drive_path}")
else:
    st.error("❌ Google Drive 경로를 찾을 수 없습니다. 설정을 확인해주세요.")

if st.button("📦 백업하기"):
    os.system("run_backup.bat")
if st.button("🔄 복원하기"):
    os.system("run_restore.bat")
