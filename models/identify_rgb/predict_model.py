import torch
from train_model import RGBClassifier
from scripts.preprocess.preprocess_image_for_predict import preprocess_image_for_predict

def predict_image(image_path):
    model = RGBClassifier()
    model.load_state_dict(torch.load('checkpoints/rgb_classifier.pth', weights_only=True))
    model.eval()

    img_tensor = preprocess_image_for_predict(image_path).unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        output = model(img_tensor)
        _, predicted = torch.max(output, 1)

    label_map = {0: 'R', 1: 'G', 2: 'B'}
    return label_map[predicted.item()]

if __name__ == "__main__":
    result = predict_image('data/test_data/B.png')
    print(f'Predicted: {result}')
