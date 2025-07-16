import os
from datetime import datetime
from fpdf import FPDF

# 경로 설정
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = "./reports/summary_pdfs"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, f"loop_summary_report_{timestamp}.pdf")

# 폰트 경로
font_path = os.path.join("Nanum_Gothic", "NanumGothic-Regular.ttf")


pdf = FPDF()
pdf.add_page()
pdf.add_font("Nanum", "", font_path)
pdf.set_font("Nanum", size=12)
pdf.cell(200, 10, txt="GIWANOS 회고 리포트 (최종 요약)", ln=1, align='C')
pdf.output(output_path)
print(f"✅ 회고 PDF 생성 완료 → {output_path}")