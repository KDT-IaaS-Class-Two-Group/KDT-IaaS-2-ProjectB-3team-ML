import torch
from torch.utils.data import DataLoader
from .train_model import RGBClassifier, RGBDataset

def test_model():
    dataset = RGBDataset('data/preprocess_data')
    dataloader = DataLoader(dataset, batch_size=4, shuffle=False)

    model = RGBClassifier()
    model.load_state_dict(torch.load('checkpoints/rgb_classifier.pth'))
    model.eval()

    correct = 0
    total = 0

    with torch.no_grad():
        for data, labels in dataloader:
            outputs = model(data)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f'Accuracy: {100 * correct / total}%')

if __name__ == "__main__":
    test_model()
