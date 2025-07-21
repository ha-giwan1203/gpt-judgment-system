import sys
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except AttributeError:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace', line_buffering=True)


import os

ROOT = "C:/giwanos"

print("🚀 GIWANOS 마스터 실행 시작")

# 1. 회고 PDF 생성
print("▶ 회고 PDF 생성:", os.path.join(ROOT, "generate_reflection_pdf.py"))
os.system(f"python {ROOT}/generate_reflection_pdf.py")

# 2. 회고 요약 .md 전송
md_reflector = os.path.join(ROOT, "send_reflection_md.py")
if os.path.exists(md_reflector):
    print("▶ 회고 .md 전송:", md_reflector)
    os.system(f"python {md_reflector}")
else:
    print("⚠️ 스킵: 회고 md 전송 (파일 없음)")

# 3. Notion 전송기 (PDF 메모 방식)
print("▶ Notion 전송기:", os.path.join(ROOT, "upload_final_runner.py"))
os.system(f"python {ROOT}/upload_final_runner.py")

# 4. GitHub 전송 루프
upload_hub = os.path.join(ROOT, "GIWANOS_upload.py")
if os.path.exists(upload_hub):
    print("▶ GitHub 전송 루프:", upload_hub)
    os.system(f"python {upload_hub}")
else:
    print("⚠️ 스킵: GitHub 업로드 루프 없음")

# 5. ZIP 백업 생성
print("▶ ZIP 백업 생성:", os.path.join(ROOT, "zip_backup_generator.py"))
os.system(f"python {ROOT}/zip_backup_generator.py")

# 6. 사고 판단 기록
print("▶ 사고 판단 루프:", os.path.join(ROOT, "repeat_judge_runner.py"))
os.system(f"python {ROOT}/repeat_judge_runner.py")

print("🎯 GIWANOS 마스터 루프 실행 완료")
