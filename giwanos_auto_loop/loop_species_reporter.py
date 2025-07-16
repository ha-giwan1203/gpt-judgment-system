import json
from pathlib import Path
from fpdf import FPDF
from datetime import datetime

LEADER_PATH = Path("logs/loop_species_leaders.json")
REPORT_PATH = Path("C_giwanos/loop_species_leader_report.pdf")

def generate_leader_report():
    if not LEADER_PATH.exists():
        print("❌ 리더 루프 파일 없음")
        return

    leaders = json.load(open(LEADER_PATH, encoding="utf-8"))

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "👑 루프 종 리더 자동 보고서", ln=True, align="C")
    pdf.set_font("Arial", "", 11)
    pdf.cell(200, 8, f"작성일: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    pdf.ln(5)

    for i, l in enumerate(leaders, 1):
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 8, f"{i}. {l['loop']}", ln=True)
        pdf.set_font("Arial", "", 11)
        pdf.cell(200, 8, f"  평균 성능 점수: {l['score']}", ln=True)
        pdf.ln(4)

    pdf.output(str(REPORT_PATH))
    print(f"📄 리더 루프 PDF 보고서 생성 완료 → {REPORT_PATH.name}")

if __name__ == "__main__":
    generate_leader_report()