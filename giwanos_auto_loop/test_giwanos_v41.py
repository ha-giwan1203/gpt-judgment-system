
import subprocess
import os

def run_test(name, command):
    print(f"\n🧪 [테스트] {name}")
    try:
        subprocess.run(command, check=True)
        print(f"✅ [{name}] 성공")
    except subprocess.CalledProcessError as e:
        print(f"❌ [{name}] 실패:", e)

if __name__ == "__main__":
    run_test("전체 루프 실행", ["python", "run_giwanos_v41.py"])
    run_test("회고 보고서 PDF 변환", ["python", "markdown_to_pdf_fixed.py"])
    run_test("Notion 업로드 (지완 필드)", ["python", "upload_notion_result_giwanos.py"])
