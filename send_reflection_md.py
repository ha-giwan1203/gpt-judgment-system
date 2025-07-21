import sys
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except AttributeError:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace', line_buffering=True)


import os
import glob
from datetime import datetime
from upload_notion_safe import upload_to_notion

ROOT = "C:/giwanos"
REFLECTION_DIR = os.path.join(ROOT, "reflections")

print("📄 회고 md 전송기 시작")

# 가장 최신 md 파일 찾기
md_files = glob.glob(os.path.join(REFLECTION_DIR, "*.md"))
if not md_files:
    print("❌ 회고 md 파일 없음")
    exit()

# 최신 파일 기준 정렬
latest_md = max(md_files, key=os.path.getmtime)
print(f"✅ 최신 회고 md 파일 발견: {latest_md}")

# 페이지 제목에 날짜 포함
filename = os.path.basename(latest_md)
date_part = filename.replace("loop_reflection_log_", "").replace(".md", "")
try:
    formatted_date = datetime.strptime(date_part, "%Y%m%d_%H%M%S").strftime("%Y-%m-%d %H:%M")
except:
    formatted_date = "미지정"

page_title = f"GIWANOS 회고 요약 ({formatted_date})"
upload_to_notion(latest_md, page_title=page_title)

print("✅ 회고 md 전송 완료")
