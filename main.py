from app import create_app

# Flask 애플리케이션 생성
app = create_app()

if __name__ == "__main__":
    # 애플리케이션 실행 (개발 환경에서 디버그 모드를 켤 수 있음)
    app.run(host=app.config["HOST"], port=app.config["PORT"], debug=True)
