from fpdf import FPDF
import json
import os
from datetime import datetime

FONT_PATH = "C:/giwanos/Nanum_Gothic/NanumGothic-Regular.ttf"
STATE_FILE = "giwanos_state.json"

if not os.path.exists(FONT_PATH):
    print(f"❌ 폰트 파일을 찾을 수 없습니다: {FONT_PATH}")
    exit(1)

if not os.path.exists(STATE_FILE):
    print(f"❌ 설치 정보 파일이 없습니다: {STATE_FILE}")
    exit(1)

with open(STATE_FILE, "r", encoding="utf-8") as f:
    state = json.load(f)

pdf = FPDF()
pdf.add_page()
pdf.add_font("NanumGothic", "", FONT_PATH, uni=True)
pdf.set_font("NanumGothic", size=12)

pdf.cell(200, 10, txt="GIWANOS 설치 회고 보고서", ln=True, align="C")
pdf.ln(10)

for k, v in state.items():
    pdf.cell(200, 10, txt=f"{k}: {v}", ln=True)

filename = f"GIWANOS_설치_회고_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
pdf.output(filename)
print(f"✅ 회고 PDF 생성됨: {filename}")