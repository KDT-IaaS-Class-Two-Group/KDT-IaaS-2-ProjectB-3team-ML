import torch
import torch.nn as nn
import torch.optim as optim
import os
from torch.utils.data import DataLoader
from app.models.identify_rgb.datasets.rgb_dataset import RGBDataset
from app.models.identify_rgb.networks.rgb_classifer import RGBClassifier
from app.static.models.identify_rgb.train_model_static import train_model_batch_size,train_model_checkpoint_dir,train_model_epochs,train_model_learning_rate,train_model_preprocess_data_dir, train_model_save_name
# 만약 따로 구분 짓지 않겠다면, import * 로 파일안의 모든 것 import 가능.

"""
    RGB 이미지 분류 모델을 학습시키는 함수입니다.
    
    이 함수는 주어진 데이터셋을 사용해 RGB 이미지를 분류하는 모델을 학습시킵니다.
    데이터는 DataLoader로 배치로 나누어 처리되며, CrossEntropyLoss를 사용해 손실을 계산하고 Adam 옵티마이저로 모델을 업데이트합니다.
    학습이 완료되면 모델의 가중치를 'checkpoints/rgb_classifier.pth' 파일에 저장합니다.
    
    Args:
        없음. (이 함수는 고정된 데이터 경로와 설정으로 동작합니다.)

    Returns:
        없음. (학습된 모델의 가중치를 파일로 저장합니다.)
"""

def train_model():
    """
    데이터셋을 로드하고 모델을 학습하는 주요 과정입니다.
    """
    dataset = RGBDataset(train_model_preprocess_data_dir)  # RGBDataset을 이용해 전처리된 데이터셋을 불러옵니다.
    dataloader = DataLoader(dataset, batch_size=train_model_batch_size, shuffle=True)  # 데이터셋을 배치 크기 4로 나누고, 데이터를 무작위로 섞습니다.

    model = RGBClassifier()  # RGBClassifier 모델을 인스턴스화합니다.
    criterion = nn.CrossEntropyLoss()  # 다중 클래스 분류에서 사용하는 손실 함수인 CrossEntropyLoss를 정의합니다.
    optimizer = optim.Adam(model.parameters(), lr=train_model_learning_rate)  # Adam 옵티마이저를 사용해 모델의 가중치를 업데이트합니다.

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # CUDA가 사용 가능하면 GPU, 아니면 CPU를 사용합니다.
    model.to(device)  # 모델을 선택된 장치로 이동시킵니다.

    # 학습 루프 시작
    for epoch in range(train_model_epochs):  # 10 에포크 동안 학습합니다.
        for data, labels in dataloader:  # DataLoader로부터 배치 데이터를 가져옵니다.
            data, labels = data.to(device), labels.to(device)  # 데이터를 CUDA(또는 CPU)로 이동시킵니다.

            outputs = model(data)  # 모델에 입력 데이터를 넣고 출력값을 계산합니다.
            loss = criterion(outputs, labels)  # 모델의 출력과 실제 라벨 간의 손실을 계산합니다.

            optimizer.zero_grad()  # 역전파 전에 옵티마이저의 기울기를 초기화합니다.
            loss.backward()  # 역전파를 통해 손실에 대한 기울기를 계산합니다.
            optimizer.step()  # 옵티마이저가 계산된 기울기를 사용해 모델의 가중치를 업데이트합니다.
            
    if not os.path.exists(train_model_checkpoint_dir):  # 폴더가 존재하지 않으면
        os.makedirs(train_model_checkpoint_dir)  # 폴더를 생성

    # 학습된 모델의 가중치를 파일에 저장
    torch.save(model.state_dict(), os.path.join(train_model_checkpoint_dir, train_model_save_name))  # 학습된 모델 가중치를 파일로 저장

if __name__ == "__main__":
    train_model()
