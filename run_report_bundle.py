
import os

print("\n🚀 GIWANOS 보고서 자동 루프 시작")

# 1️⃣ 회고 PDF 생성
if os.path.exists("generate_reflection_pdf.py"):
    print("\n📄 [1/4] 회고 PDF 생성 중...")
    os.system("python generate_reflection_pdf.py")
else:
    print("❌ generate_reflection_pdf.py 파일이 없습니다.")

# 2️⃣ 전송 (Slack + Notion)
if os.path.exists("upload_final_runner.py"):
    print("\n📤 [2/4] Slack + Notion 전송 중...")
    os.system("python upload_final_runner.py")
else:
    print("❌ upload_final_runner.py 파일이 없습니다.")

# 3️⃣ ZIP 백업
if os.path.exists("loop_zip_backup_generator.py"):
    print("\n📦 [3/4] ZIP 백업 생성 중...")
    os.system("python loop_zip_backup_generator.py")
else:
    print("❌ loop_zip_backup_generator.py 파일이 없습니다.")

# 4️⃣ 요약 Slack 전송
if os.path.exists("loop_feedback_result_slack.py"):
    print("\n💬 [4/4] 회고 요약 Slack 전송 중...")
    os.system("python loop_feedback_result_slack.py")
else:
    print("❌ loop_feedback_result_slack.py 파일이 없습니다.")

print("\n✅ 전체 자동 루프 완료! 🎉")
