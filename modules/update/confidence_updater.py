def update_best_confidences(predictions, best_confidences):
    """최고 신뢰도 업데이트 함수"""
    for animal, model_predictions in predictions:
        for *box, conf, cls in model_predictions:
            conf = conf.item()  # tensor에서 값을 가져옵니다
            # 현재 동물의 최고 신뢰도 업데이트
            if conf > best_confidences[animal]:
                best_confidences[animal] = conf