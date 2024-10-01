#models/identify_rgb/train_model.py
# 저장할 디렉토리 이름
train_model_checkpoint_dir = 'src/checkpoints'
# 데이터셋 할당 디렉토리 이름
train_model_preprocess_data_dir = 'src/data/preprocess_data'
train_model_batch_size = 4
train_model_learning_rate = 0.001
# 학습 횟수
train_model_epochs = 10  
# 저장할 모델 이름
train_model_save_name = 'rgb_classifier.pth'