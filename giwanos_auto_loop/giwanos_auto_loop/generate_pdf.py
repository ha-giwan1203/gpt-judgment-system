
from fpdf import FPDF
import os

md_path = "giwanos_memory/loop_reflection_log.md"
pdf_path = "giwanos_memory/loop_reflection_log.pdf"

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

if os.path.exists(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        clean_line = line.encode("latin-1", errors="ignore").decode("latin-1")
        pdf.multi_cell(0, 10, clean_line.strip())
    pdf.output(pdf_path)
    print(f"[PDF] 회고 PDF 생성 완료 → {pdf_path}")
else:
    print("❌ 회고 로그 파일이 없습니다.")
