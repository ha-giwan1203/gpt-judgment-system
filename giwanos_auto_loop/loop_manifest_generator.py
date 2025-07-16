
import json
from datetime import datetime

manifest = {
    "manifest_generated_at": datetime.now().isoformat(),
    "active_genes": {},
    "active_loops": [
        "repeat_judge_runner.py",
        "generate_reflection_pdf.py",
        "evolution_loop.py",
        "upload_final_runner.py",
        "zip_backup_generator.py"
    ],
    "recommended_next": "backup_zip",
    "stability_flag": True
}

try:
    with open("logs/loop_genes_mutated.json", "r", encoding="utf-8") as f:
        gene_data = json.load(f)
        manifest["active_genes"] = gene_data.get("genes", {})
except FileNotFoundError:
    manifest["active_genes"] = {"note": "loop_genes_mutated.json not found"}

with open("loop_manifest.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print("✅ loop_manifest.json 생성 완료")
