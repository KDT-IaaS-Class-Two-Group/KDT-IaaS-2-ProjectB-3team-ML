from PIL import Image  # PIL 라이브러리의 Image 모듈 임포트
from torchvision import transforms  # torchvision의 transforms 모듈 임포트

def preprocess_image_for_predict(image_path):
    ''' 
    주어진 이미지 파일 경로를 읽고, 전처리하여 모델 예측을 위한 PyTorch 텐서로 변환하는 함수입니다.
    
    매개변수:
    - image_path: 전처리할 이미지의 파일 경로 (str)
    
    반환값:
    - img_tensor: (1, C, H, W) 형태의 PyTorch 텐서 (float32) 
      - 1: 배치 크기 (1)
      - C: 채널 수 (RGB)
      - H: 이미지 높이
      - W: 이미지 너비
    '''
    
    # 이미지 파일 열기 및 RGB로 변환
    img = Image.open(image_path).convert('RGB')
    
    # 모델 입력 크기에 맞게 이미지 크기 조정
    img = img.resize((10, 10))  # 모델 입력 크기에 맞게 조정
    
    # 이미지를 텐서로 변환하고 (C, H, W) 형태로 변환
    img_tensor = transforms.ToTensor()(img)  # (C, H, W) 형식으로 변환
    
    # 배치 차원 추가 (1, C, H, W)
    img_tensor = img_tensor.unsqueeze(0)  # 배치 차원 추가 (1, C, H, W)
    
    return img_tensor  # 전처리된 이미지 텐서 반환
