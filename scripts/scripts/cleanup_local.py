
import os
import shutil

# 현재 실행 중인 폴더 기준
target_dir = os.path.abspath(os.path.dirname(__file__))

# 정리용 하위 폴더 생성
backup_dir = os.path.join(target_dir, "backup")
script_dir = os.path.join(target_dir, "scripts")
docs_dir = os.path.join(target_dir, "docs")
zip_dir = os.path.join(target_dir, "zips")
os.makedirs(backup_dir, exist_ok=True)
os.makedirs(script_dir, exist_ok=True)
os.makedirs(docs_dir, exist_ok=True)
os.makedirs(zip_dir, exist_ok=True)

# 정리 기준 확장자별 매핑
ext_map = {
    ".zip": zip_dir,
    ".py": script_dir,
    ".bat": script_dir,
    ".md": docs_dir,
    ".txt": docs_dir
}

# 파일 정리
for file in os.listdir(target_dir):
    src = os.path.join(target_dir, file)
    if os.path.isfile(src):
        ext = os.path.splitext(file)[1].lower()
        dest_folder = ext_map.get(ext)
        if dest_folder:
            dest = os.path.join(dest_folder, file)
            shutil.move(src, dest)

print("✅ Folder cleanup complete: files sorted into zips / docs / scripts / backup.")
