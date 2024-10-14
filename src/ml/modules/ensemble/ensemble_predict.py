from src.ml.modules.image.preprocess_image import preprocess_image

def ensemble_predict(models, image_path):
    """앙상블 예측 함수"""
    img = preprocess_image(image_path)
    
    predictions = []
    for animal, model in models:
        results = model(img)  # 이제 모델이 객체이므로 호출 가능
        predictions.append((animal, results.xyxy[0]))  # 동물 레이블과 예측 결과 저장

    return predictions