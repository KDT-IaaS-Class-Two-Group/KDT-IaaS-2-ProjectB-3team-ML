# KDT-IaaS-2-ProjectB-3team-ML
카메라를 통해서  실시간으로 야생 동물 분류 및 행동 예측을 통해 위치 기반 주변 알림 시스템 ML

### < 레포지토리 구조 > 
.
├── README.md
├── app
│   ├── __init__.py
│   ├── checkpoints
│   │   └── rgb_classifier.pth
│   ├── data
│   │   ├── preprocess_data
│   │   │   ├── B.pt
│   │   │   ├── G.pt
│   │   │   └── R.pt
│   │   ├── test_data
│   │   │   ├── B.png
│   │   │   ├── G.png
│   │   │   └── R.png
│   │   └── train_data
│   │       ├── B.png
│   │       ├── G.png
│   │       └── R.png
│   ├── models
│   │   └── identify_rgb
│   │       ├── datasets
│   │       │   └── rgb_dataset.py
│   │       ├── networks
│   │       │   └── rgb_classifer.py
│   │       ├── predict_model.py
│   │       ├── test_model.py
│   │       └── train_model.py
│   ├── scripts
│   │   ├── generate_data.py
│   │   ├── preprocess
│   │   │   ├── preprocess_image.py
│   │   │   └── preprocess_image_for_predict.py
│   │   └── preprocess_data.py
│   └── static
│       ├── models
│       │   └── identify_rgb
│       │       ├── predict_model_static.py
│       │       ├── test_model_static.py
│       │       └── train_model_static.py
│       └── scripts
│           ├── generatae_data_static.py
│           └── preprocess_data_static.py
└── requirements.txt

16 directories, 27 files