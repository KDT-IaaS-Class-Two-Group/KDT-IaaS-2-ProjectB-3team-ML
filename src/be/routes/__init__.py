from flask import jsonify, request
from src.be.modules.utils.blueprint.bp_list import bp_list
from src.be.modules.utils.path.path_joiner import path_joiner
from src.be.modules.utils.env.env_loader import env_loader
from src.be.static.env.env_list_static import EnvList
from src.be.static.utils.symbols.forward_slash_static import forward_slash
from src.be.static.routes.__init__static import env_values_for_join
from src.be.static.http.http_methods_static import HTTPMethods
from src.ml.ensembler import predict_animal_from_image  # 예측 함수 가져오기

# # 환경 변수를 통해 URL 경로 설정
# url_path = path_joiner(forward_slash, *[env_loader(value) for value in env_values_for_join])  # 환경 변수에 따라 경로 설정
# print(url_path) 


@bp_list.API.route("/api/upload", methods=[HTTPMethods.POST.value])
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
    result = predict_animal_from_image(image_binary)

    # 결과 확인 및 반환
    if 'Y' in result:
        return jsonify({"message": result['Y']})  # Y 키의 값을 반환
    else:
        return jsonify({"message": "Prediction failed"}), 500  # 예측 실패 시 오류 반환
