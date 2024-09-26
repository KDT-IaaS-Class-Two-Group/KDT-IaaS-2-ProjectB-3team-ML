from PIL import Image
from torchvision import transforms

def preprocess_image_for_predict(image_path):
    img = Image.open(image_path).convert('RGB')
    img = img.resize((10, 10))  # 모델 입력 크기에 맞게 조정
    img_tensor = transforms.ToTensor()(img)  # (C, H, W) 형식으로 변환
    img_tensor = img_tensor.unsqueeze(0)  # 배치 차원 추가 (1, C, H, W)
    return img_tensor
