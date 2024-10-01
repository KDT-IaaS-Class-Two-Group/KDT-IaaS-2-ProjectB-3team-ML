import torch.nn as nn  # PyTorch의 nn 모듈 임포트

class RGBClassifier(nn.Module):
    ''' 
    RGBClassifier 클래스는 RGB 이미지를 분류하기 위한 간단한 신경망 모델입니다.
    
    이 모델은 10x10 크기의 이미지에서 RGB 클래스(빨강, 초록, 파랑)를 분류하는 데 사용됩니다.
    '''
    
    def __init__(self):
        ''' 
        모델의 초기화 메서드입니다. 
        기본적으로 Fully Connected (FC) 레이어를 정의합니다.
        '''
        super(RGBClassifier, self).__init__()  # 부모 클래스의 초기화 메서드 호출
        self.fc = nn.Linear(3 * 10 * 10, 3)  # 입력 차원: 3 (RGB 채널) x 10 (높이) x 10 (너비), 출력 차원: 3 (클래스 수)

    def forward(self, x):
        ''' 
        모델의 순전파 메서드입니다. 주어진 입력 텐서를 통해 예측값을 계산합니다.
        
        매개변수:
        - x: 입력 텐서 (배치 크기, 채널 수, 높이, 너비)
        
        반환값:
        - fc 레이어를 통과한 출력 텐서
        '''
        x = x.reshape(x.size(0), -1)  # 입력 텐서를 2D 텐서로 변환 (배치 크기, 피처 수)
        return self.fc(x)  # FC 레이어를 통과한 결과 반환
