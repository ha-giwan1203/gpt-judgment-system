
import zipfile
import os

base_path = "./giwanos_auto_loop"
output_file = os.path.join(base_path, "GIWANOS_v5_FULL.zip")

include_extensions = [".py", ".json", ".md"]
exclude_files = ["GIWANOS_v5_FULL.zip"]

with zipfile.ZipFile(output_file, "w") as zipf:
    for root, _, files in os.walk(base_path):
        for file in files:
            if any(file.endswith(ext) for ext in include_extensions) and file not in exclude_files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, base_path)
                zipf.write(full_path, arcname)

print(f"[Packager] ✅ GIWANOS_v5_FULL.zip 생성 완료")
