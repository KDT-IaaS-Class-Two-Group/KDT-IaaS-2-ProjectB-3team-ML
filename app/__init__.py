# app/__init__.py
from .models import *
from .scripts import *
from .static import *
from flask import Flask
from flask_cors import CORS

def create_app():

    # Flask 앱 인스턴스 생성
    app = Flask(__name__)

    # Flask 앱의 설정값을 .env 파일이나 config.py에서 불러오기
    app.config.from_object('config.Config')

    # 필요한 플러그인 초기화 (예: CORS)
    CORS(app)

    @app.route('/')
    def home() :
        return "hello Python"


    return app
