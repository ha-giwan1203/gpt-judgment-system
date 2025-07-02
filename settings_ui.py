import os

def load_env(file_path=".env"):
    if not os.path.exists(file_path):
        print("⚠️ .env 파일이 없어 새로 생성합니다.")
        return {}
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    env = {}
    for line in lines:
        if "=" in line and not line.startswith("#"):
            key, value = line.strip().split("=", 1)
            env[key] = value
    return env

def save_env(env, file_path=".env"):
    with open(file_path, "w", encoding="utf-8") as f:
        for key, value in env.items():
            f.write(f"{key}={value}\n")
    print(f"✅ 저장 완료: {file_path}")

def edit_env():
    env = load_env()
    keys = [
        "NOTION_TOKEN",
        "NOTION_DATABASE_ID",
        "GDRIVE_FOLDER_ID",
        "GITHUB_TOKEN"
    ]
    for key in keys:
        current = env.get(key, "")
        new = input(f"{key} [{current}]: ").strip()
        if new:
            env[key] = new
    save_env(env)

if __name__ == "__main__":
    edit_env()
