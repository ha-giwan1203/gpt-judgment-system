import zipfile
import os
from datetime import datetime

target = "C:/giwanos"
backup_name = f"GIWANOS_Backup_v23_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
with zipfile.ZipFile(backup_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for foldername, _, filenames in os.walk(target):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            arcname = os.path.relpath(filepath, start=target)
            zipf.write(filepath, arcname)
print(f"✅ 백업 완료: {backup_name}")