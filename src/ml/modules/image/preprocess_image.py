from PIL import Image
import numpy as np

def preprocess_image(image):
    # 이미지 전처리 예시
    # 필요에 따라 크기 조정, 정규화 등의 작업 수행
    image = image.resize((416, 416))  # 모델에 맞는 크기로 조정
    image_array = np.array(image) / 255.0  # 0-1로 정규화
    return image_array