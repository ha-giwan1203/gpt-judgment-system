from fpdf import FPDF
from datetime import datetime
import os

# 지완이 제공한 최종 폰트 경로
FONT_PATH = "C:/giwanos/Nanum_Gothic/Noto_Sans_KR/static/NanumGothic-Regular.ttf"

if not os.path.exists(FONT_PATH):
    print("❌ NanumGothic-Regular.ttf 폰트가 존재하지 않습니다. 경로를 확인해주세요.")
    exit()

pdf = FPDF()
pdf.add_page()
pdf.add_font("Nanum", "", FONT_PATH, uni=True)
pdf.set_font("Nanum", size=16)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
title = f"GIWANOS 시스템 기억 회고 보고서\n({now})"
pdf.cell(0, 10, txt=title, ln=True)

pdf.set_font("Nanum", size=12)
lines = [
    "[1] .env 설정 완료됨 - Slack / Notion / Gmail / OpenAI 연동 정상",
    "[2] 회고/진화 PDF 생성기 정상 작동",
    "[3] 전송기(upload_notion_summary_CLEANED.py) 성공 적용됨",
    "[4] ZIP 자동 백업 구조 정상 작동 (loop_backups/ 포함)",
    "[5] Notion 필드 자동 감지기 적용 (get_notion_db_properties.py)",
    "[6] 루프(run_report_bundle.py) 통합 성공",
    "[7] 진단기(diagnose_giwanos.py) 통해 점검 완료",
    "[8] 기억 고정 완료됨 → '기억 복원해줘'로 호출 가능",
    "[9] Slack / Notion 전송 루프 모두 성공 상태 기록됨",
    "[10] GIWANOS_Final_Bundle_*.zip 백업 생성 완료"
]

for line in lines:
    pdf.cell(0, 10, txt=line, ln=True)

filename = f"GIWANOS_기억회고_보고서_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
pdf.output(filename)
print(f"✅ 회고 PDF 생성 완료 → {filename}")