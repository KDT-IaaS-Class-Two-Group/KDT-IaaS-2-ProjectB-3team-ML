def ensemble_predict(models, image_path):
    """앙상블 예측 함수"""
    img = preprocess_image(image_path)
    predictions = [(animal, predict_model(model, img)) for animal, model in models]
    return predictions