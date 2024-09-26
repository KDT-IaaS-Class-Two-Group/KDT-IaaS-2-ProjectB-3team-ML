import torch
from torch.utils.data import  Dataset
import os

class RGBDataset(Dataset):
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.files = [f for f in os.listdir(data_dir) if f.endswith('.pt')]
        self.labels = {"R": 0, "G": 1, "B": 2}

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        file = self.files[idx]
        label = self.labels[file[0]]  # 파일 이름의 첫 글자 기반 라벨
        data = torch.load(os.path.join(self.data_dir, file), weights_only=True)  # weights_only=True 추가
        return data, label