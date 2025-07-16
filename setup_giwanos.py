
import os
import shutil

BASE_PATH = os.getcwd()

folders = [
    "giwanos_auto_loop",
    "giwanos_memory",
    "loop_backups",
    "logs",
    "install",
    "archive",
    "streamlit_ui"
]

def create_folder_structure():
    for folder in folders:
        full_path = os.path.join(BASE_PATH, folder)
        os.makedirs(full_path, exist_ok=True)
        print(f"✅ 폴더 생성됨: {folder}")

def copy_template_env():
    template_path = os.path.join(BASE_PATH, ".env.template")
    env_path = os.path.join(BASE_PATH, ".env")
    if os.path.exists(template_path):
        shutil.copyfile(template_path, env_path)
        print("✅ .env 파일이 템플릿 기준으로 생성됨")
    else:
        print("⚠️ .env.template 파일이 존재하지 않아 .env 생성 생략됨")

def main():
    print("📦 GIWANOS 설치 시작...")
    create_folder_structure()
    copy_template_env()
    print("🏁 GIWANOS 설치 완료!")

if __name__ == "__main__":
    main()
