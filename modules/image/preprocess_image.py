from PIL import Image

def preprocess_image(image_path):
    """이미지 전처리 함수"""
    img = Image.open(image_path)
    img = img.convert("RGB")  # 색상 모드 변환
    return img
