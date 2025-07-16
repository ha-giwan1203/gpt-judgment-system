import os
from datetime import datetime
from fpdf import FPDF

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = "./reports/summary_pdfs"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, f"loop_reflection_log_{timestamp}.pdf")

reflection_text = """
[GIWANOS REFLECTION]

- 이 회고는 루프 사고 흐름을 요약합니다.
- 최근 판단은 안정적으로 작동하였으며,
- 다음 루프 설계에 반영할 전략이 도출되었습니다.
"""

pdf = FPDF()
pdf.add_page()
pdf.add_font("Nanum", "", os.path.join("Nanum_Gothic", "NanumGothic-Regular.ttf"))
pdf.set_font("Nanum", size=11)

for line in reflection_text.strip().split('\n'):
    pdf.cell(200, 10, txt=line.strip(), ln=1)

pdf.output(output_path)
print(f"✅ 회고 리플렉션 PDF 저장 완료 → {output_path}")