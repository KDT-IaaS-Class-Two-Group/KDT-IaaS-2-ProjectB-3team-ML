import torch
from torch.utils.data import DataLoader
from app.models.identify_rgb.train_model import RGBClassifier, RGBDataset
from app.static.models.identify_rgb.test_model_static import test_model_batch_size,test_model_preprocess_data_dir, test_model_path
def test_model():
    """
    학습된 모델을 테스트하고 정확도를 계산하는 함수입니다.
    
    이 함수는 사전 학습된 모델을 불러와 데이터를 예측하고, 실제 라벨과 비교하여 정확도를 계산합니다.
    
    Args:
        없음.
    
    Returns:
        없음. 
        하지만 정확도를 콘솔에 출력합니다.
    """
    
    # 테스트 데이터셋을 불러오고 DataLoader를 사용하여 배치로 나누고 순서대로 처리
    dataset = RGBDataset(test_model_preprocess_data_dir)  # 데이터셋을 로드
    dataloader = DataLoader(dataset, batch_size=test_model_batch_size, shuffle=False)  # 배치를 4로 나누고 shuffle을 하지 않음 (순차적 처리)

    # 모델을 인스턴스화하고 저장된 가중치를 불러온 후 평가 모드로 설정
    model = RGBClassifier()  # RGBClassifier 모델 인스턴스 생성
    model.load_state_dict(torch.load(test_model_path, weights_only=True))  # 저장된 가중치 불러오기
    model.eval()  # 모델을 평가 모드로 설정 (학습 관련 동작 비활성화)

    correct = 0  # 맞춘 예측값 개수
    total = 0    # 총 데이터 개수

    # 기울기 계산을 하지 않도록 no_grad() 사용
    with torch.no_grad():  # 역전파를 하지 않음
        for data, labels in dataloader:  # 데이터셋에서 배치 단위로 데이터를 가져옴
            outputs = model(data)  # 모델에 데이터를 입력하여 예측값 생성
            _, predicted = torch.max(outputs, 1)  # 가장 높은 확률값을 가진 클래스를 예측값으로 선택
            total += labels.size(0)  # 총 데이터 개수 업데이트
            correct += (predicted == labels).sum().item()  # 맞춘 예측값의 개수 계산

    if total == 0:
        print("No samples to evaluate.")
    else:
        print(f'Accuracy: {100 * correct / total:.2f}%')  # 소수점 두 자리로 포맷팅
    
if __name__ == "__main__":
    test_model()
