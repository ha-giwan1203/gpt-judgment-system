
from fpdf import FPDF
from search_memory_with_prompt import search_memory_for_context
import datetime
import os

class ReflectionPDF(FPDF):
    def header(self):
        # ✅ 한글 및 이모지 지원 폰트 설정 (fpdf2 방식)
        self.add_font("NotoSansKR", "", "Nanum_Gothic/NotoSansKR-Regular.ttf")
        self.set_font("NotoSansKR", "", 14)
        self.cell(0, 10, "🧠 GIWANOS 회고 보고서", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("NotoSansKR", "", 10)
        self.cell(0, 10, f"페이지 {self.page_no()}", align="C")

    def chapter_title(self, title):
        self.set_font("NotoSansKR", "", 12)
        self.ln(10)
        self.cell(0, 10, title, ln=True)

    def chapter_body(self, body):
        self.set_font("NotoSansKR", "", 11)
        self.multi_cell(0, 10, body)

    def add_reflection_section(self, title, content):
        self.chapter_title(title)
        self.chapter_body(content)

def generate_reflection_pdf(output_path="loop_reflection_with_memory.pdf"):
    pdf = ReflectionPDF()
    pdf.add_page()

    # 1. 일반 회고
    pdf.add_reflection_section("✅ 일반 회고 요약", "이번 루프에서 발생한 주요 흐름과 실행 결과를 요약합니다...")

    # 2. 기억 검색 포함
    context = search_memory_for_context("이번 회고와 유사한 과거 사례는?")
    pdf.add_reflection_section("🧠 과거 기억 반영", context)

    # 3. 저장
    pdf.output(output_path)
    print(f"✅ 회고 PDF 생성 완료: {output_path}")

if __name__ == "__main__":
    generate_reflection_pdf()
