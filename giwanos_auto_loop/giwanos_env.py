
import os
from dotenv import load_dotenv

def load_giwanos_env(verbose=False):
    dotenv_path = ".env"
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
        if verbose:
            print("✅ .env 환경변수 로드 완료")
    else:
        if verbose:
            print("⚠️ .env 파일이 존재하지 않습니다.")
