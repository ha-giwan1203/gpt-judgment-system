
import os
import json

def extract_failures(log_path="giwanos_memory/reflection_log.json"):
    if not os.path.exists(log_path):
        print("❌ 회고 로그 파일이 존재하지 않습니다.")
        return []

    with open(log_path, "r", encoding="utf-8") as f:
        logs = json.load(f)

    failures = []
    for entry in logs:
        if entry.get("result") == "fail":
            failures.append({
                "action": entry.get("action"),
                "reason": entry.get("reason"),
                "timestamp": entry.get("timestamp")
            })

    print(f"🔍 실패 판단 {len(failures)}건 추출됨:")
    for f in failures:
        print(f"- [{f['timestamp']}] {f['action']} → 이유: {f['reason']}")
    return failures

if __name__ == "__main__":
    extract_failures()
