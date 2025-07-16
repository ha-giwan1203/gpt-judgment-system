
import os
import shutil

def main():
    ROOT = "C:/giwanos"
    os.makedirs(ROOT, exist_ok=True)
    folders = ["auto_modules", "giwanos_memory", "giwanos_auto_loop", "설계", "reports", "logs", "zip"]
    for f in folders:
        os.makedirs(os.path.join(ROOT, f), exist_ok=True)
        shutil.copytree(f, os.path.join(ROOT, f), dirs_exist_ok=True)
    for f in [".env", "credentials.json"]:
        shutil.copy(f, os.path.join(ROOT, f))
    print("✅ GIWANOS 시스템 설치 완료 → C:/giwanos")

if __name__ == "__main__":
    main()
