from flask import Flask, jsonify, request
from src.ml.ensembler import predict_animal_from_image  # 예측 함수 가져오기
from flask_cors import CORS
from src.be.modules.routes.register_routes import register_routes
from src.be.modules.utils.blueprint.bp_list import bp_list
import logging
import os

def create_app():
    """
    Flask 애플리케이션 인스턴스를 생성하고 설정하는 함수입니다.

    1. Flask 애플리케이션 인스턴스를 생성합니다.
    2. CORS(Cross-Origin Resource Sharing)를 활성화하여 외부 요청을 허용합니다.
    3. 이미지 업로드와 관련된 라우트를 설정합니다.

    Returns:
        app: 설정된 Flask 애플리케이션 인스턴스
    """
    
    app = Flask(__name__)
    
    # 업로드 폴더 경로를 리터럴로 지정
    UPLOAD_FOLDER = './upload/'
    
    # 업로드 폴더가 존재하지 않으면 생성
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

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

        try:
            # 파일을 업로드 폴더에 저장
            image_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(image_path)

            # 예측 수행
            result = predict_animal_from_image(image_path)

                # result 딕셔너리에서 문자열 추출 (예: '이 이미지는 고라니입니다 (신뢰도: 0.87)')
            result_str = list(result.values())[0]  

            return jsonify({"message": result_str})
        except Exception as e:
            logging.error(f"업로드 중 오류 발생: {e}")
            return jsonify({"message": "Upload failed due to an error."}), 500

        finally:
            # 만약 예외가 발생하더라도 이미지 삭제
            if os.path.exists(image_path):
                os.remove(image_path)

    return app
