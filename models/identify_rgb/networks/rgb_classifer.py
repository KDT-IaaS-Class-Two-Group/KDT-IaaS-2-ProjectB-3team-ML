import torch.nn as nn

class RGBClassifier(nn.Module):
    def __init__(self):
        super(RGBClassifier, self).__init__()
        self.fc = nn.Linear(3*10*10, 3)

    def forward(self, x):
        x = x.reshape(x.size(0), -1)  # view 대신 reshape 사용
        return self.fc(x)
