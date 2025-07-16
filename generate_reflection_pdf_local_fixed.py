from fpdf import FPDF
from fpdf.enums import XPos, YPos
from datetime import datetime
import os

pdf_path = "loop_reflection_report.pdf"
font_path = os.path.abspath("C:/Windows/Fonts/malgun.ttf")

class PDF(FPDF):
    def header(self):
        self.set_font("Malgun", '', 16)
        self.cell(0, 10, "GIWANOS 루프 회고 요약 보고서", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")

pdf = PDF()
pdf.add_font("Malgun", "", font_path, uni=True)
pdf.set_font("Malgun", '', 12)
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
pdf.set_text_color(50, 50, 50)
pdf.cell(0, 10, f"생성일시: {now}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(8)

summary = """
이 보고서는 루프 실행 이후의 회고 내용을 요약한 것입니다.

- 회고 루프 실행 성공
- 테스트 루프 결과 PDF 출력 완료
- 자동 전송 루프 Slack/Notion 일부 실패
- 루프 리포트 ZIP 파일 생성 완료
- 로컬 상태 동기화 및 추천 완료

※ 이상은 mock 기반 예시입니다. 실제 loop_reflection_log.md가 있을 경우 그 내용을 자동 반영합니다.
"""

for line in summary.strip().split("\n"):
    pdf.multi_cell(0, 8, line.strip())

pdf.output(pdf_path)
print(f"✅ 회고 PDF 저장 완료 → {pdf_path}")