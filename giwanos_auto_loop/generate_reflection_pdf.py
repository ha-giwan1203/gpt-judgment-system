from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

# 경로 설정
md_path = "loop_reflection_log.md"
pdf_path = "loop_reflection_log.pdf"
font_name = "NanumGothic"
fallback_font = "Helvetica"

# 폰트 등록 (시스템에 설치된 Nanum Gothic이 있는 경우)
try:
    pdfmetrics.registerFont(TTFont(font_name, "NanumGothic.ttf"))
    font_to_use = font_name
except:
    font_to_use = fallback_font

# 회고 로그 읽기
if not os.path.exists(md_path):
    print("[❌ 회고 로그 파일이 존재하지 않습니다]")
    exit()

with open(md_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# PDF 생성
c = canvas.Canvas(pdf_path, pagesize=A4)
width, height = A4
c.setFont(font_to_use, 12)

y = height - 40
for line in lines:
    line = line.strip()
    if y < 40:
        c.showPage()
        c.setFont(font_to_use, 12)
        y = height - 40
    c.drawString(40, y, line)
    y -= 18

c.save()
print(f"[✅ 회고 PDF 생성 완료] → {pdf_path}")
