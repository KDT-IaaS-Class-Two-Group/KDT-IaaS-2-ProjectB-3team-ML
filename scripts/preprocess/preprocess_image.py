import numpy as np  # NumPy 라이브러리 임포트
from PIL import Image  # PIL 라이브러리의 Image 모듈 임포트
import torch  # PyTorch 라이브러리 임포트

def preprocess_image(image_path):
    ''' 
    주어진 이미지 파일 경로를 읽고, 전처리하여 PyTorch 텐서로 변환하는 함수입니다.
    
    매개변수:
    - image_path: 전처리할 이미지의 파일 경로 (str)
    
    반환값:
    - img_tensor: (C, H, W) 형태의 PyTorch 텐서 (float32) 
      - C: 채널 수 (RGB)
      - H: 이미지 높이
      - W: 이미지 너비
    '''
    
    # 이미지 파일 열기
    img = Image.open(image_path)
    
    # 이미지를 NumPy 배열로 변환하고 0-1 범위로 정규화
    img_array = np.array(img) / 255.0  # Normalize to 0-1
    
    # NumPy 배열을 PyTorch 텐서로 변환하고 채널 차원 순서를 변경
    img_tensor = torch.tensor(img_array, dtype=torch.float32).permute(2, 0, 1)  # (H, W, C) -> (C, H, W)
    
    return img_tensor  # 전처리된 이미지 텐서 반환
