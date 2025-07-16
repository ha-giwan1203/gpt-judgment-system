from fpdf import FPDF
from fpdf.enums import XPos, YPos
from datetime import datetime
import os
import textwrap

pdf_path = "loop_test_results_report.pdf"
log_path = "logs/loop_test_results_log.txt"
font_path = "C:/giwanos/Nanum_Gothic/NanumGothic.ttf"

class PDF(FPDF):
    def header(self):
        self.set_font("Nanum", '', 14)
        self.cell(0, 10, "GIWANOS 루프 테스트 결과 보고서", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Nanum", '', 8)
        self.cell(0, 10, f"페이지 {self.page_no()}", align="C")

pdf = PDF()
pdf.add_font("Nanum", "", font_path, uni=True)
pdf.set_font("Nanum", '', 11)
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

pdf.set_text_color(50, 50, 50)
pdf.cell(0, 10, f"생성일: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(5)

if os.path.exists(log_path):
    with open(log_path, encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        content = line.strip().replace("─", "-").replace("│", "|")
        short = content[:300]
        wrapped = textwrap.wrap(short, width=100, break_long_words=True, break_on_hyphens=False)
        if "[테스트 일시:" in content:
            pdf.set_text_color(0, 0, 120)
        elif "[OK]" in content:
            pdf.set_text_color(0, 120, 0)
        elif "[X]" in content:
            pdf.set_text_color(200, 0, 0)
        else:
            pdf.set_text_color(0, 0, 0)
        for wline in wrapped:
            pdf.multi_cell(100, 8, wline)

else:
    pdf.set_text_color(180, 0, 0)
    pdf.cell(0, 10, "⚠ 테스트 결과 로그 파일이 존재하지 않습니다.")

pdf.output(pdf_path)
print(f"✅ PDF 저장 완료 → {pdf_path}")