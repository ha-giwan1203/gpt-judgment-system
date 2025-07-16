
from fpdf import FPDF
import os

log_path = "C:/giwanos/giwanos_memory/loop_reflection_log.md"
pdf_path = "C:/giwanos/giwanos_memory/loop_reflection_log.pdf"

if not os.path.exists(log_path):
    print("❌ 회고 로그 파일이 없습니다.")
    exit()

with open(log_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_font("ArialUnicode", "", fname="C:/Windows/Fonts/malgun.ttf", uni=True)
pdf.set_font("ArialUnicode", size=12)

for line in lines:
    pdf.multi_cell(0, 8, txt=line.strip())

pdf.output(pdf_path)
print(f"✅ PDF 생성 완료 → {pdf_path}")
