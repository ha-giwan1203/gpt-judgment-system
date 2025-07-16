
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def convert_md_to_pdf(md_path, output_pdf):
    if not os.path.exists(md_path):
        print("❌ .md 파일이 존재하지 않습니다.")
        return

    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4
    x, y = 50, height - 50
    c.setFont("Helvetica", 10)

    for line in lines:
        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 10)
            y = height - 50
        c.drawString(x, y, line.strip())
        y -= 15

    c.save()
    print(f"✅ PDF 저장 완료: {output_pdf}")

if __name__ == "__main__":
    md_path = "loop_backups/FINAL_REFLECTION/GIWANOS_v40_회고요약.md"
    output_pdf = "loop_backups/FINAL_REFLECTION/GIWANOS_v40_회고요약.pdf"
    convert_md_to_pdf(md_path, output_pdf)
