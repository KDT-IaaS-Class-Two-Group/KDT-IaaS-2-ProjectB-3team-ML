def predict_model(model, img):
    """단일 모델에 대한 예측 수행"""
    return model(img).xyxy[0]