import sys
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except AttributeError:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace', line_buffering=True)


from fpdf import FPDF
import os

FONT_PATH = os.path.join(os.getcwd(), "Nanum_Gothic", "NanumGothic-Regular.ttf")

pdf = FPDF()
pdf.add_page()
pdf.add_font("Nanum", "", FONT_PATH)
pdf.set_font("Nanum", size=12)

lines = [
    "🧠 GIWANOS 회고 PDF 테스트입니다.",
    "한글이 정상 출력되어야 합니다.",
    "이 파일은 자동으로 NanumGothic 폰트를 사용합니다."
]

for line in lines:
    safe_line = line.replace("\n", " ").strip()
    pdf.cell(0, 10, txt=safe_line, ln=True)

output_path = "loop_reflection_log.pdf"
pdf.output(output_path)
print(f"✅ 회고 PDF 생성 완료: {output_path}")
