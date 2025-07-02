
import os
import shutil
from datetime import datetime
from pathlib import Path

# 경로 설정
source_root = Path("C:/구글지완/ChatGPT_자동화작업")
target_root = source_root / "GPT_정리된자료"
log_path = target_root / "logs"
log_path.mkdir(parents=True, exist_ok=True)
log_file = log_path / "file_sort.log"

# 키워드 기반 분류 기준
routing_rules = {
    "01_문서자료/급여": ["급여", "salary", "pay"],
    "01_문서자료/계약": ["계약", "contract", ".hwp"],
    "01_문서자료/일반업무": ["일반", "보고", "업무"],
    "02_설계자료/시스템": ["설계", "architecture", "system"],
    "02_설계자료/자동화": ["자동화", "script", "automation"],
    "03_데이터/단가": ["단가", ".xlsx", ".csv"],
    "03_데이터/매출": ["매출", "sales", "data"],
    "04_보고서/GPT분석": ["gpt", "분석결과", ".md", "_result"],
    "04_보고서/업무작성": ["보고서", "업무", "작성"]
}
default_folder = "99_분류불가"

sorted_files = []
for folder_name in os.listdir(source_root):
    folder_path = source_root / folder_name
    if folder_path.is_dir() and folder_name != "GPT_정리된자료":
        for dirpath, _, filenames in os.walk(folder_path):
            for filename in filenames:
                full_path = Path(dirpath) / filename
                lowered = filename.lower()

                destination_rel = None
                for dest, keywords in routing_rules.items():
                    if any(k.lower() in lowered for k in keywords):
                        destination_rel = dest
                        break
                if not destination_rel:
                    destination_rel = default_folder

                destination_path = target_root / destination_rel
                destination_path.mkdir(parents=True, exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                new_filename = f"{timestamp}_{filename}"
                shutil.copy2(full_path, destination_path / new_filename)
                sorted_files.append(f"[{timestamp}] {filename} → {destination_rel}/{new_filename}")

# 로그 저장
with open(log_file, "a", encoding="utf-8") as f:
    for line in sorted_files:
        f.write(line + "\n")

print("✅ 파일 정리 완료! 총 정리된 파일 수:", len(sorted_files))
