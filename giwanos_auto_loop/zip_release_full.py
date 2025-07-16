
import zipfile
import os

base_path = "./giwanos_auto_loop"
release_file = os.path.join(base_path, "GIWANOS_사고루프_FULL.zip")

with zipfile.ZipFile(release_file, "w") as zipf:
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if not file.endswith(".zip"):
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, base_path)
                zipf.write(full_path, arcname=arcname)

print(f"✅ 전체 시스템 ZIP 생성 완료: {release_file}")
