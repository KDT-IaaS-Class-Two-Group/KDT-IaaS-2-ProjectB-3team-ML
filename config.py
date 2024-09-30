import os
from dotenv import load_dotenv

load_dotenv()
# 예시입니다. 얼마든지 수정 가능.
class Config:
    
    HOST = os.getenv("HOST","0.0.0.0")
    PORT = os.getenv("PORT",8000)
    
    
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    MODEL_PATH = os.getenv('MODEL_PATH')
    DEBUG = os.getenv('FLASK_DEBUG', False)
