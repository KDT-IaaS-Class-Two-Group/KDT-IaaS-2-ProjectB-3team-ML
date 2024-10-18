from PIL import Image
from src.ml.modules.image.preprocess_image import preprocess_image

def ensemble_predict(models, image):
    # image는 PIL.Image 객체여야 합니다
    # 모델에 따라 이미지를 적절히 전처리해야 합니다
    processed_image = preprocess_image(image)

    # 모델에 대한 예측 수행
    predictions = []
    for model in models:
        pred = model.predict(processed_image)
        predictions.append(pred)

    return predictions