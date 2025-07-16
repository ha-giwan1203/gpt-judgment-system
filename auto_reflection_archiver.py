
import os
import shutil
from datetime import datetime

def backup_pdf(source_file="loop_reflection_with_memory.pdf", backup_dir="loop_backups"):
    if not os.path.exists(source_file):
        print(f"❌ 회고 PDF 없음: {source_file}")
        return

    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    target_name = f"loop_reflection_backup_{timestamp}.pdf"
    target_path = os.path.join(backup_dir, target_name)

    shutil.copyfile(source_file, target_path)
    print(f"✅ 회고 PDF 자동 백업 완료: {target_path}")

if __name__ == "__main__":
    backup_pdf()
