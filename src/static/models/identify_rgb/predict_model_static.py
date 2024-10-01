# models/identify_rgb/predict_model.py

# 모델 가중치 파일 경로
predict_model_checkpoint_path = 'src/checkpoints/rgb_classifier.pth'

# 라벨 맵
predict_model_label_map = {0: 'R', 1: 'G', 2: 'B'}

# 예측할 이미지 경로 (기본값)
predict_model_default_image_path = 'src/data/test_data/B.png'