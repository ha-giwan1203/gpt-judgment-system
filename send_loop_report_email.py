
import os
import smtplib
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_TO = "s250ppp@gmail.com"
EMAIL_USER = os.getenv("EMAIL_USER")  # 발신자 이메일 주소
EMAIL_PASS = os.getenv("EMAIL_PASS")  # 앱 비밀번호 또는 계정 비번

# 최근 PDF 찾기
pdf_files = sorted([f for f in os.listdir() if f.startswith("loop_reflection_log_") and f.endswith(".pdf")], reverse=True)
if not pdf_files:
    print("❌ 보낼 PDF 파일이 없습니다.")
    exit()
pdf_file = pdf_files[0]

# 메일 메시지 생성
msg = EmailMessage()
msg["Subject"] = "GIWANOS 회고 보고서 자동 발송"
msg["From"] = EMAIL_USER
msg["To"] = EMAIL_TO
msg.set_content(f"자동 생성된 회고 보고서를 첨부합니다.\n\n파일명: {pdf_file}")

# 첨부
with open(pdf_file, "rb") as f:
    file_data = f.read()
    msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=pdf_file)

# 발송
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)
    print(f"✅ 이메일 발송 완료 → {EMAIL_TO}")
except Exception as e:
    print("❌ 이메일 발송 실패:", e)
