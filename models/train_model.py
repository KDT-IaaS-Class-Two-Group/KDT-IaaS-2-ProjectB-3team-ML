import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
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

class RGBClassifier(nn.Module):
    def __init__(self):
        super(RGBClassifier, self).__init__()
        self.fc = nn.Linear(3*10*10, 3)
        
    def forward(self, x):
        x = x.reshape(x.size(0), -1)  # view 대신 reshape 사용
        return self.fc(x)

def train_model():
    dataset = RGBDataset('data/preprocess_data')
    dataloader = DataLoader(dataset, batch_size=4, shuffle=True)

    model = RGBClassifier()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    for epoch in range(10):  # 10 epochs
        for data, labels in dataloader:
            data, labels = data.to(device), labels.to(device)  # 데이터와 라벨을 CUDA로 이동

            outputs = model(data)
            loss = criterion(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    torch.save(model.state_dict(), 'checkpoints/rgb_classifier.pth')

if __name__ == "__main__":
    train_model()
