import json
import os

def load_manifest(manifest_path):
    if not os.path.exists(manifest_path):
        return None
    with open(manifest_path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_env(env_path):
    if not os.path.exists(env_path):
        return {}
    with open(env_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    env_vars = {}
    for line in lines:
        if "=" in line and not line.strip().startswith("#"):
            key, value = line.strip().split("=", 1)
            env_vars[key.strip()] = value.strip()
    return env_vars

def check_manifest(manifest, base_path="/mnt/data"):
    results = []
    for key in ["실행기", "트리거", "감지기", "전송기", "진화기", "판단기", "요약기"]:
        if key in manifest:
            path = os.path.join(base_path, manifest[key])
            status = "✅ 존재" if os.path.exists(path) else "❌ 없음"
            results.append((key, manifest[key], status))
    return results

def check_env_vars(required_keys, env_dict):
    results = []
    for key in required_keys:
        status = "✅ 있음" if key in env_dict else "❌ 없음"
        results.append((key, status))
    return results

def main():
    base_path = "/mnt/data"
    manifest_files = [
        "memory_manifest_정리루프.json",
        "memory_manifest_보고루프.json",
        "memory_manifest_진화루프.json"
    ]
    env_file = os.path.join(base_path, ".env_giwanos_template")
    print("🔍 GIWANOS 시스템 메모리 상태 점검")

    env_data = load_env(env_file)
    for mfile in manifest_files:
        mpath = os.path.join(base_path, mfile)
        manifest = load_manifest(mpath)
        if manifest:
            print(f"--- {manifest['루프이름']} ---")
            for label, target, status in check_manifest(manifest, base_path):
                print(f"[{status}] {label}: {target}")
            print("환경변수 체크:")
            for key, status in check_env_vars(manifest.get("환경변수", {}).get("필수", []), env_data):
                print(f"[{status}] {key}")
            print()

if __name__ == "__main__":
    main()