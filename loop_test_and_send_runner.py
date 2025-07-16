import os
import subprocess

print("▶ 루프 테스트 + 전송 자동 실행 시작")

# 1. 테스트 PDF 생성
print("🧪 loop_test_results_to_pdf_malgun.py 실행 중...")
subprocess.run(["python", "loop_test_results_to_pdf_malgun.py"], check=True)

# 2. 전송 루프 실행
print("📤 upload_final_runner.py 실행 중...")
subprocess.run(["python", "upload_final_runner.py"], check=True)

print("✅ 테스트 + 전송 루프 완료")