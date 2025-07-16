from fpdf import FPDF
from fpdf.enums import XPos, YPos
import os
from datetime import datetime

def generate_summary():
    pdf = FPDF()
    pdf.add_page()

    font_path = "C:\\Windows\\Fonts\\malgun.ttf"
    if not os.path.exists(font_path):
        print("❌ Malgun Gothic 폰트가 시스템에 없습니다.")
        return

    pdf.add_font("Malgun", "", font_path)
    pdf.set_font("Malgun", "", 14)

    pdf.cell(200, 10, "GIWANOS 루프 실행 요약 보고서", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Malgun", "", 11)
    pdf.cell(200, 10, f"생성일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)

    pdf.multi_cell(0, 8, "- 회고 루프 테스트 성공\n- 전체 자동 실행 루프 정상 동작\n- Slack 전송 루프 통합 예정")

    output_path = "loop_summary_report.pdf"
    pdf.output(output_path)
    print(f"✅ PDF 생성 완료 → {output_path}")

if __name__ == "__main__":
    print("[루프 시작] 실행 목적: 회고")
    generate_summary()