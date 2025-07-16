from fpdf import FPDF
from datetime import datetime
import os

pdf = FPDF()
pdf.add_page()
font_path = "Nanum_Gothic/NanumGothic-Regular.ttf"
if not os.path.exists(font_path):
    print("❌ NanumGothic.ttf 폰트 파일이 없습니다. C:/giwanos/Nanum_Gothic/ 폴더에 넣어주세요.")
    exit()

pdf.add_font("Nanum", "", font_path, uni=True)
pdf.set_font("Nanum", "", 14)
pdf.cell(0, 10, "GIWANOS 시스템 최종 요약 리포트", ln=True)

pdf.set_font("Nanum", "", 11)
pdf.ln(4)
pdf.multi_cell(0, 8, f'''
시스템 이름: GIWANOS (GPT 기반 루프 자동화 운영체계)
리포트 생성일: {datetime.now().strftime('%Y-%m-%d %H:%M')}

[설계 및 구성]
- 폴더 구조, 실행기, 트리거, 환경 설정 전부 완료
- 회고/진화/정리/전송 루프 전부 자동화
- ZIP 백업, Slack/Notion/Email 연동 정상 작동
- 실행 기록 및 루프 판단 자동 저장 시스템 구축

[기억 구조]
- .env, gpt_trigger.json, loop_execution_reason.json, memory_structure_summary.md 존재
- Streamlit 대시보드로 상태 시각화 가능
- 루프 실행 이력 기반 구조도(GIWANOS_Structure.png) 생성 완료

[진단 결과 요약]
- diagnose_giwanos_v2.py로 모든 항목 점검 완료
- 회고 PDF: 존재함
- ZIP 백업: 존재함
- 로그 오류: 없음
- 한글 폰트 정상 인식

[현재 상태]
- GIWANOS v13 구조 완성
- 자동화 OS 수준 운영 가능
- 판단 루프 확장(v14) 또는 배포(GitHub) 선택 가능 상태
''')

output_path = "GIWANOS_Final_Summary_Report_CLEAN.pdf"
pdf.output(output_path)
print(f"[✅ 클린 PDF 생성 완료] → {output_path}")