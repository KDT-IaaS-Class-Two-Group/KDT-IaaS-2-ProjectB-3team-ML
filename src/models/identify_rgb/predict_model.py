import torch  # PyTorch 라이브러리 임포트
from app.models.identify_rgb.train_model import RGBClassifier  # RGBClassifier 모델 임포트
from app.scripts.preprocess.preprocess_image_for_predict import preprocess_image_for_predict
from app.static.models.identify_rgb.predict_model_static import predict_model_checkpoint_path,predict_model_default_image_path,predict_model_label_map

def predict_image(image_path):
    # RGBClassifier 모델 초기화
    model = RGBClassifier()
    
    # 학습된 모델의 가중치 불러오기
    model.load_state_dict(torch.load(predict_model_checkpoint_path, weights_only=True))
    
    # 모델을 평가 모드로 설정 (dropout 및 batch normalization 비활성화)
    model.eval()

    # 이미지 전처리 및 배치 차원 추가
    img_tensor = preprocess_image_for_predict(image_path).unsqueeze(0)  # Add batch dimension
    
    with torch.no_grad():  # 기울기 계산을 비활성화하여 메모리 절약
        output = model(img_tensor)  # 모델을 통한 예측
        _, predicted = torch.max(output, 1)  # 가장 높은 확률의 클래스를 선택

    # 라벨 맵 생성
    return predict_model_label_map[predicted.item()]  # 예측된 라벨 반환

if __name__ == "__main__":
    # 예측할 이미지 경로 지정
    result = predict_image(predict_model_default_image_path)
    
    # 예측 결과 출력
    print(f'Predicted: {result}')
