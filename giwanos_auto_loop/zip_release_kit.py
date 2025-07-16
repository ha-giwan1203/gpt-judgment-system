
import zipfile
import os

base_path = "./giwanos_auto_loop"
release_path = "./giwanos_auto_loop/GIWANOS_사고루프_FULL.zip"

include_files = [
    "loop_launcher.py",
    "file_sort_for_지완OS_v2.py",
    "zip_backup_generator.py",
    "upload_final_runner.py",
    "trigger_generator.py",
    "memory_manifest.json",
    "loop_reflection_log.md",
    "loop_reflection_summary.md"
]

with zipfile.ZipFile(release_path, "w") as zipf:
    for file in include_files:
        path = os.path.join(base_path, file)
        if os.path.exists(path):
            zipf.write(path, arcname=file)

print(f"✅ 배포용 ZIP 생성 완료: GIWANOS_사고루프_FULL.zip")
