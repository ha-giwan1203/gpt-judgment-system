
import shutil
import os

# 자동 저장 디렉토리
FINAL_DIR = os.path.join("loop_backups", "FINAL_REFLECTION")
os.makedirs(FINAL_DIR, exist_ok=True)

# 자동 백업할 파일 목록
backup_targets = {
    "loop_summary_report.pdf": "loop_summary_report.pdf",
    "logs/loop_feedback_log.json": "loop_feedback_log.json",
    "logs/loop_genes_mutated.json": "loop_genes_mutated.json",
    "logs/loop_recommendation_model.json": "loop_recommendation_model.json",
    "giwanos_auto_loop/loop_manifest.json": "loop_manifest.json",
}

for src, name in backup_targets.items():
    if os.path.exists(src):
        dst = os.path.join(FINAL_DIR, name)
        shutil.copy(src, dst)
        print(f"📁 자동 백업됨 → {dst}")
