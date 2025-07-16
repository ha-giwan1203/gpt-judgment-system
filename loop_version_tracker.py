
# ✅ 루프 변경 감지 기록기
import os, hashlib, json, datetime
from dotenv import load_dotenv
load_dotenv()

def md5(file):
    with open(file, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def track():
    target_files = [f for f in os.listdir() if f.endswith(".py") or f.endswith(".bat")]
    log_path = "logs/loop_genes_lineage.json"
    os.makedirs("logs", exist_ok=True)

    lineage = []
    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8") as f:
            lineage = json.load(f)

    known = {item["filename"]: item["checksum"] for item in lineage}

    for f in target_files:
        now_checksum = md5(f)
        if f not in known or known[f] != now_checksum:
            lineage.append({
                "filename": f,
                "checksum": now_checksum,
                "change_type": "modified" if f in known else "new",
                "changed_at": datetime.datetime.now().isoformat(),
                "comment": ""
            })

    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(lineage, f, indent=2, ensure_ascii=False)
    print("✅ 루프 변경 기록 완료")

if __name__ == "__main__":
    track()