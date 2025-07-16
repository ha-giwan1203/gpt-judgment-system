
import os
from datetime import datetime
from zipfile import ZipFile

# ✅ 포함할 파일 목록
files_to_zip = [
    "loop_summary_report.pdf",
    "logs/loop_feedback_log.json",
    "logs/loop_recommendation_model.json",
    "logs/loop_genes_mutated.json"
]

# ✅ ZIP 이름 설정
today = datetime.today().strftime("%Y%m%d")
zip_name = f"loop_backups/loop_summary_backup_{today}.zip"

# ✅ 압축 실행
with ZipFile(zip_name, "w") as zipf:
    for file in files_to_zip:
        if os.path.exists(file):
            zipf.write(file)
            print(f"📦 포함됨: {file}")
        else:
            print(f"⚠️ 없음 (건너뜀): {file}")

print(f"✅ ZIP 생성 완료 → {zip_name}")
