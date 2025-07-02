import os

def load_restore_prompt(file_path="restore_prompt.txt"):
    if not os.path.exists(file_path):
        print("❌ restore_prompt.txt 파일이 존재하지 않습니다.")
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    print("✅ 복원 프롬프트가 성공적으로 로드되었습니다.")
    return content

if __name__ == "__main__":
    prompt = load_restore_prompt()
    if prompt:
        print("\n--- 복원 프롬프트 내용 ---\n")
        print(prompt.strip())
        print("\n--- (끝) ---\n")
