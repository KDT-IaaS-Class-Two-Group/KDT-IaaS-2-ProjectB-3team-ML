from flask import Blueprint, request, jsonify
from app.models.identify_rgb.predict_model import predict_image
from app.static.routes.predict_image_static import PREDICT_ROUTE, ALLOWED_EXTENSIONS
from app.scripts.check_extension import allowed_file
import os

# 블루프린트 객체를 생성하여 'predict' 관련 라우트들을 관리
predict_bp = Blueprint('predict', __name__)

# '/predict' 경로로 POST 요청을 처리하는 예측 엔드포인트를 정의
@predict_bp.route(PREDICT_ROUTE, methods=['POST'])
def predict():
    # 요청에서 'file'이라는 이름의 파일을 포함하고 있는지 확인
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    # 'file'이 요청에 포함된 경우 파일 객체를 가져옴
    file = request.files['file']
    
    # 파일이 선택되지 않았는지 확인 (파일명이 빈 문자열인 경우)
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # 파일이 선택되었고, 해당 파일이 허용된 확장자인지 확인
    if file and allowed_file(file.filename, ALLOWED_EXTENSIONS):
        # 임시로 파일을 저장할 'temp' 디렉터리 경로를 생성
        temp_dir = os.path.join(os.getcwd(), 'temp')
        
        # 'temp' 디렉터리가 존재하지 않는 경우 새로 생성
        os.makedirs(temp_dir, exist_ok=True)
        
        # 업로드된 파일을 임시 디렉터리에 저장
        temp_path = os.path.join(temp_dir, file.filename)
        file.save(temp_path)
        
        # 저장된 파일을 이용해 이미지 예측을 수행
        try:
            result = predict_image(temp_path)
            
            # 예측이 완료된 후 임시 파일 삭제
            os.remove(temp_path)
            
            # 예측 결과를 JSON 형태로 반환
            return jsonify({'result': result})
        except Exception as e:
            # 예측 중 오류가 발생한 경우에도 임시 파일 삭제
            os.remove(temp_path)
            
            # 오류 메시지를 JSON 형태로 반환
            return jsonify({'error': str(e)}), 500
    
    # 허용되지 않은 파일 유형인 경우 오류 메시지 반환
    return jsonify({'error': 'File type not allowed'}), 400
