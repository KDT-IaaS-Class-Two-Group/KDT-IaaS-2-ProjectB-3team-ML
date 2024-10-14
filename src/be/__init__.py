from flask import Flask, jsonify, request
from src.ml.ensembler import predict_animal_from_image  # 예측 함수 가져오기
from flask_cors import CORS
from src.be.modules.routes.register_routes import register_routes
from src.be.modules.utils.blueprint.bp_list import bp_list

def create_app():
    """
    Flask 애플리케이션 인스턴스를 생성하고 설정하는 함수입니다.

    1. Flask 애플리케이션 인스턴스를 생성합니다.
    2. 설정 객체(config.Config)에서 설정을 로드합니다.
    3. CORS(Cross-Origin Resource Sharing)를 활성화하여 외부 요청을 허용합니다.
    4. 등록된 블루프린트를 사용하여 라우트를 설정합니다.

    Returns:
        app: 설정된 Flask 애플리케이션 인스턴스
    """
    
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    CORS(app)

    @app.post("/api/upload")
    def upload_image():
        # 파일이 요청에 포함되어 있는지 확인
        if 'file' not in request.files:
            return jsonify({"message": "No file part in the request"}), 400

        file = request.files['file']
        
        # 파일 이름이 비어 있는지 확인
        if file.filename == '':
            return jsonify({"message": "No selected file"}), 400

        # 파일을 이진 데이터로 읽기
        image_binary = file.read()

        # 예측 수행
        result = predict_animal_from_image(image_binary)  # 바이너리 데이터 전달

        # 결과 확인 및 반환
        if 'Y' in result:
            return jsonify({"message": result['Y']})  # Y 키의 값을 반환
        else:
            return jsonify({"message": "Prediction failed"}), 500  # 예측 실패 시 오류 반환

    return app

