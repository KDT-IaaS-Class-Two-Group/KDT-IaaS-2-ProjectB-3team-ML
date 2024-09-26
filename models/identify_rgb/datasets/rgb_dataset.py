import torch  # PyTorch 라이브러리 임포트
from torch.utils.data import Dataset  # PyTorch의 Dataset 클래스 임포트
import os  # 파일 및 디렉토리 작업을 위한 os 모듈 임포트

class RGBDataset(Dataset):
    ''' 
    RGBDataset 클래스는 RGB 이미지를 포함하는 데이터셋을 나타냅니다.
    
    이 데이터셋은 이미지 텐서와 해당하는 레이블(R, G, B)을 포함합니다.
    '''
    
    def __init__(self, data_dir):
        ''' 
        데이터셋 초기화 메서드입니다.
        
        매개변수:
        - data_dir: 이미지 텐서가 저장된 디렉토리의 경로 (str)
        '''
        self.data_dir = data_dir  # 데이터 디렉토리 경로 저장
        # 데이터 디렉토리에서 '.pt' 파일만 선택하여 파일 리스트 생성
        self.files = [f for f in os.listdir(data_dir) if f.endswith('.pt')]
        # RGB 클래스 레이블을 딕셔너리 형태로 정의
        self.labels = {"R": 0, "G": 1, "B": 2}

    def __len__(self):
        ''' 
        데이터셋의 총 샘플 수를 반환하는 메서드입니다.
        
        반환값:
        - 총 샘플 수 (int)
        '''
        return len(self.files)  # 파일 리스트의 길이 반환

    def __getitem__(self, idx):
        ''' 
        주어진 인덱스에 해당하는 샘플과 레이블을 반환하는 메서드입니다.
        
        매개변수:
        - idx: 가져올 샘플의 인덱스 (int)
        
        반환값:
        - data: 입력 데이터 텐서 (torch.Tensor)
        - label: 해당 데이터의 클래스 레이블 (int)
        '''
        file = self.files[idx]  # 주어진 인덱스에 해당하는 파일 이름
        label = self.labels[file[0]]  # 파일 이름의 첫 글자를 기반으로 라벨 지정
        # 파일 경로를 결합하여 텐서를 로드하고, weights_only=True 추가
        data = torch.load(os.path.join(self.data_dir, file), weights_only=True)
        return data, label  # 데이터와 라벨 반환
