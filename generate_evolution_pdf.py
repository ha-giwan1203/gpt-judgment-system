
import os
import json
from datetime import datetime
import matplotlib.pyplot as plt
from fpdf import FPDF

# ✅ 경로 설정
genes_path = "logs/loop_genes_mutated.json"
font_path = "Nanum_Gothic/NanumGothic-Regular.ttf"
output_path = f"evolution_summary_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

# ✅ 데이터 로딩
if not os.path.exists(genes_path):
    print("❌ 진화 결과 파일이 없습니다.")
    exit()

with open(genes_path, "r", encoding="utf-8") as f:
    data = json.load(f)
    mutated = data.get("mutated_genes", [])
    improvements = data.get("improvements", [])

# ✅ 폰트 확인
if not os.path.exists(font_path):
    print("❌ NanumGothic-Regular.ttf 파일이 없습니다. 'Nanum_Gothic' 폴더에 넣어주세요.")
    exit()

# ✅ PDF 생성
pdf = FPDF()
pdf.add_page()
pdf.add_font("Nanum", "", font_path)
pdf.set_font("Nanum", size=16)
pdf.cell(0, 10, "GIWANOS 진화 루프 보고서", ln=True)
pdf.ln(10)

pdf.set_font("Nanum", size=12)
pdf.multi_cell(0, 10, f"변경된 유전자 수: {len(mutated)}개")
pdf.ln(5)

if improvements:
    pdf.multi_cell(0, 10, "개선사항 Top 5:")
    for imp in improvements[:5]:
        pdf.cell(0, 10, f"- {imp}", ln=True)
    pdf.ln(5)

    # ✅ 개선사항 그래프
    plt.figure(figsize=(6, 4))
    plt.barh(improvements[:5], [1]*len(improvements[:5]))
    plt.title("개선 포인트 Top 5")
    plt.tight_layout()
    chart_path = "evolution_chart.png"
    plt.savefig(chart_path)
    pdf.image(chart_path, w=160)
    os.remove(chart_path)

# ✅ 저장
pdf.output(output_path)
print(f"[✅ 진화 PDF 생성 완료] → {output_path}")
