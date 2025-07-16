
# ✅ 회고 PDF 백업 ZIP 자동화 스크립트 (.env 미사용, 폴더 생성 보장)
import os
import zipfile
import datetime

def rotate_zip_backups():
    folder = "loop_backups"
    os.makedirs(folder, exist_ok=True)

    pdf = "loop_reflection_with_memory.pdf"
    if not os.path.exists(pdf):
        print("❗ PDF 파일이 존재하지 않음:", pdf)
        return

    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    zipname = f"{folder}/loop_reflection_backup_{now}.zip"
    with zipfile.ZipFile(zipname, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(pdf)

    zips = sorted([f for f in os.listdir(folder) if f.endswith(".zip")])
    while len(zips) > 5:
        oldest = zips.pop(0)
        os.remove(os.path.join(folder, oldest))

    print(f"✅ ZIP 백업 완료: {zipname}")

if __name__ == "__main__":
    rotate_zip_backups()
