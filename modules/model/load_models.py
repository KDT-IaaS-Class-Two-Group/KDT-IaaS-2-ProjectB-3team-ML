import torch

# 모델 경로와 동물 레이블 매핑
model_info = [
    {'animal': '고라니', 'path': './animals/gorani/best.pt'},
    {'animal': '족제비', 'path': './animals/jokjebi/best.pt'},
    {'animal': '너구리', 'path': './animals/neoguri/best.pt'},
    {'animal': '반달가슴곰', 'path': './animals/bandalgaseumgom/best.pt'},
    {'animal': '청설모', 'path': './animals/cheongseolmo/best.pt'},
    {'animal': '다람쥐', 'path': './animals/daramjwi/best.pt'},
    {'animal': '중대백로', 'path': './animals/joongdaebaekro/best.pt'},
    {'animal': '멧토끼', 'path': './animals/maettokki/best.pt'},
    {'animal': '멧돼지', 'path': './animals/maetdaeji/best.pt'},
    {'animal': '노루', 'path': './animals/noru/best.pt'},
    {'animal': '왜가리', 'path': './animals/waegari/best.pt'},
]

def load_models():
    """모델 로드 함수"""
    models = []
    for info in model_info:
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=info['path'], force_reload=True)
        models.append((info['animal'], model))  # 동물 레이블과 모델 객체를 함께 저장
    return models
