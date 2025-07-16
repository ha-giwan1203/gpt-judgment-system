import os
print("▶ 루프 테스트 PDF 생성 중...")
os.system("python loop_test_results_to_pdf_malgun.py")
print("▶ 전송 루프 실행 중...")
os.system("python loop_upload_test_report.py")
print("✅ 전체 루프 실행 완료")