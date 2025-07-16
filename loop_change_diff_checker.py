import os
import json
from datetime import datetime

SYNC_LOG = "logs/loop_local_sync_log.json"
SNAPSHOT_PATH = "logs/loop_local_sync_snapshot.json"

def load_json(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def build_index(entries):
    return {entry["path"]: entry for entry in entries}

def compare_snapshots(prev, curr):
    added, removed, modified = [], [], []

    for path in curr:
        if path not in prev:
            added.append(curr[path])
        elif curr[path]["last_modified"] != prev[path]["last_modified"]:
            modified.append(curr[path])

    for path in prev:
        if path not in curr:
            removed.append(prev[path])

    return added, removed, modified

def print_summary(added, removed, modified):
    if added:
        print(f"📥 추가된 파일 ({len(added)}):")
        for f in added:
            print(f"   + {f['path']} ({f['last_modified']})")
    if removed:
        print(f"🗑️ 삭제된 파일 ({len(removed)}):")
        for f in removed:
            print(f"   - {f['path']}")
    if modified:
        print(f"✏️ 수정된 파일 ({len(modified)}):")
        for f in modified:
            print(f"   * {f['path']} → {f['last_modified']}")

if __name__ == "__main__":
    print("🔍 로컬 동기화 변경 비교 시작")

    curr_log = load_json(SYNC_LOG)
    prev_snapshot = load_json(SNAPSHOT_PATH)

    curr_index = build_index(curr_log)
    prev_index = build_index(prev_snapshot)

    added, removed, modified = compare_snapshots(prev_index, curr_index)
    print_summary(added, removed, modified)

    # 최신 상태를 snapshot으로 저장
    with open(SNAPSHOT_PATH, "w", encoding="utf-8") as f:
        json.dump(curr_log, f, indent=2, ensure_ascii=False)

    print("\n✅ 변경 비교 완료 → 최신 상태 스냅샷 저장됨")