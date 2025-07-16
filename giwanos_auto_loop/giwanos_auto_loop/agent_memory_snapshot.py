
import os
import zipfile
from datetime import datetime

memory_dir = "giwanos_memory"
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
snapshot_path = f"memory_snapshot_{timestamp}.zip"

if os.path.exists(memory_dir):
    with zipfile.ZipFile(snapshot_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for foldername, _, filenames in os.walk(memory_dir):
            for filename in filenames:
                path = os.path.join(foldername, filename)
                arcname = os.path.relpath(path, memory_dir)
                zipf.write(path, arcname)
    print(f"[Snapshot] 기억 백업 완료 → {snapshot_path}")
else:
    print("❌ giwanos_memory 디렉토리가 없습니다.")
