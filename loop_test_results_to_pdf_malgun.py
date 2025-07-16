from fpdf import FPDF, XPos, YPos
from datetime import datetime
import os

class PDF(FPDF):
    def header(self):
        font_path = "C:/Windows/Fonts/malgun.ttf"
        self.add_font("Malgun", "", font_path)
        self.set_font("Malgun", "", 16)
        self.cell(0, 10, "GIWANOS 루프 테스트 결과 보고서", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Malgun", "", 10)
        self.cell(0, 10, f"페이지 {self.page_no()}", align="C")

pdf = PDF()
pdf.add_page()
pdf.set_font("Malgun", "", 12)
pdf.cell(0, 10, f"생성일: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

log_path = "logs/loop_test_results_log.txt"
if os.path.exists(log_path):
    with open(log_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line.strip():
                pdf.multi_cell(0, 8, line.strip())
else:
    pdf.cell(0, 10, "로그 파일이 존재하지 않습니다.", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.output("loop_test_results_report.pdf")
print("✅ PDF 저장 완료 → loop_test_results_report.pdf")
