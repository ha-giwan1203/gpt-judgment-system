import os
import datetime

os.makedirs(".memory", exist_ok=True)
pdf_path = ".memory/정산_보고서_테스트.pdf"

with open(pdf_path, "w", encoding="utf-8") as f:
    f.write("테스트용 PDF 콘텐츠 (가상)")

print("✅ 보고루프 테스트 실행 완료 - PDF 생성됨")