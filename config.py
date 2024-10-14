import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 예시입니다. 얼마든지 수정 가능.
class Config:
    FE_MAIN_URL = os.getenv('FE_MAIN_URL', 'http://localhost:8080')
    ML_MAIN_URL = os.getenv('ML_MAIN_URL', 'http://localhost:8000')
    EP_API = os.getenv('EP_API', 'api')
    EP_ML = os.getenv('EP_ML', 'ml')
    API_UPLOAD_URL = os.getenv('API_UPLOAD_URL')