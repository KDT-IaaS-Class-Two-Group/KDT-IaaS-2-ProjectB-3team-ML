import numpy as np  # NumPy 라이브러리 임포트
from PIL import Image  # PIL 라이브러리의 Image 모듈 임포트
import os  # 운영 체제와의 상호작용을 위한 os 모듈 임포트

def generate_rgb_images(save_dir, size=(10, 10)):
    # RGB 색상 정의
    colors = {
        "R": [255, 0, 0],  # 빨간색
        "G": [0, 255, 0],  # 초록색
        "B": [0, 0, 255]   # 파란색
    }
    
    # 저장할 디렉토리가 없으면 생성
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # 색상별로 이미지 생성
    for color_name, rgb in colors.items():
        # 지정한 크기와 RGB 값으로 배열 생성
        img_array = np.full((size[0], size[1], 3), rgb, dtype=np.uint8)
        
        # NumPy 배열을 이미지로 변환
        img = Image.fromarray(img_array)
        
        # 이미지 저장
        img.save(os.path.join(save_dir, f"{color_name}.png"))

if __name__ == "__main__":
    # RGB 이미지를 저장할 디렉토리 지정
    generate_rgb_images('data/test_data')  # 'data/test_data' 디렉토리에 이미지 생성
