import torch

def load_models(model_info):
    """모델 로드 함수"""
    models = []
    for info in model_info:
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=info['path'], force_reload=True)
        models.append((info['animal'], model))  # 동물 레이블과 모델 객체를 함께 저장
    return models
