from flask import Blueprint, request, jsonify
from src.models.identify_rgb.predict_model import predict_image
from src.static.routes.predict_image_static import predict_route,temp_dir_to_save,allowed_extenstions
from src.scripts.check_extension import allowed_file
from src.scripts.save_file_to_temp import save_file_to_temp
import os

# 블루프린트 객체를 생성하여 'predict' 관련 라우트들을 관리
predict_bp = Blueprint('predict', __name__)

# '/predict' 경로로 POST 요청을 처리하는 예측 엔드포인트를 정의
@predict_bp.route(predict_route, methods=['POST'])
def predict():
    # 요청에서 'file'이라는 이름의 파일을 포함하고 있는지 확인
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    # 'file'이 요청에 포함된 경우 파일 객체를 가져옴
    file = request.files['file']
    
    # 파일이 선택되었고, 해당 파일이 허용된 확장자인지 확인
    if file and allowed_file(file.filename, allowed_extenstions):
        # 저장된 파일을 이용해 이미지 예측을 수행
        try:
            temp_path = save_file_to_temp(file,temp_dir_to_save)
            
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
