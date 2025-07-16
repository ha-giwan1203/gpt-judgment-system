from fpdf import FPDF
import os
from datetime import datetime

class PDF(FPDF):
    def header(self):
        font_path = "C:/giwanos/Nanum_Gothic/NanumGothic-Regular.ttf"
        self.add_font("Nanum", "", font_path, uni=True)
        self.set_font("Nanum", "", 16)
        self.cell(0, 10, "📘 GIWANOS 회고 결과 요약", align="C", new_x="LMARGIN", new_y="NEXT")

    def footer(self):
        self.set_y(-15)
        self.set_font("Nanum", "", 10)
        self.cell(0, 10, f"페이지 {self.page_no()}", align="C")

pdf = PDF()
pdf.add_page()

font_path = "C:/giwanos/Nanum_Gothic/NanumGothic-Regular.ttf"
pdf.add_font("Nanum", "", font_path, uni=True)
pdf.set_font("Nanum", "", 12)

log_file = "logs/loop_reflection_log.txt"
if os.path.exists(log_file):
    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    pdf.multi_cell(0, 8, line)
                except:
                    pdf.cell(0, 8, f"⚠️ 렌더 불가한 줄 건너뜀", new_x="LMARGIN", new_y="NEXT")
else:
    pdf.cell(0, 10, "❌ 회고 로그 파일을 찾을 수 없습니다.", new_x="LMARGIN", new_y="NEXT")

output_path = "loop_summary_report.pdf"
pdf.output(output_path)
print(f"✅ PDF 저장 완료 → {output_path}")
