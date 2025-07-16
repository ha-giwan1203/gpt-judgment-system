
# ✅ 회고 요약 정리 루프
import json, os, datetime
from dotenv import load_dotenv
load_dotenv()

def write_summary():
    fpath = "logs/loop_feedback_log.json"
    if not os.path.exists(fpath): return

    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    latest = data[-1] if data else {}

    summary = {
        "timestamp": datetime.datetime.now().isoformat(),
        "loop": latest.get("loop", "unknown"),
        "score": latest.get("score", None),
        "note": latest.get("note", ""),
        "executed_by": os.getenv("GIWANOS_MODE", "unknown"),
        "pdf_generated": os.path.exists("loop_reflection_with_memory.pdf")
    }

    os.makedirs("logs", exist_ok=True)
    log_path = "logs/loop_summary_log.json"
    try:
        if os.path.exists(log_path):
            with open(log_path, "r", encoding="utf-8") as f:
                all_data = json.load(f)
        else:
            all_data = []
        all_data.append(summary)
        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        print("✅ 회고 요약 기록 완료")
    except Exception as e:
        print("🚫 기록 실패:", e)

if __name__ == "__main__":
    write_summary()