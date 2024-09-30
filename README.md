---

# KDT-IaaS-2-ProjectB-3team-ML

## 프로젝트 개요
이 프로젝트는 카메라를 통해 실시간으로 야생 동물 분류 및 행동 예측을 수행하고, 이를 기반으로 위치 기반 주변 알림 시스템을 개발하는 것을 목표로 합니다. 이 시스템은 야생 동물의 행동을 분석하여 사용자에게 실시간 알림을 제공함으로써, 보다 안전하고 효과적인 환경을 조성하는 데 기여할 것입니다.

## 레포지토리 구조
이 레포지토리는 다음과 같은 구조로 되어 있습니다:

```
.
├── README.md                   # 프로젝트 설명서
├── app                         # 애플리케이션 관련 코드
│   ├── __init__.py            # 패키지 초기화
│   ├── checkpoints             # 모델 체크포인트 저장
│   │   └── rgb_classifier.pth  # RGB 분류기 체크포인트
│   ├── data                    # 데이터 관련 파일
│   │   ├── preprocess_data      # 전처리된 데이터 파일
│   │   │   ├── B.pt
│   │   │   ├── G.pt
│   │   │   └── R.pt
│   │   ├── test_data            # 테스트 데이터 파일
│   │   │   ├── B.png
│   │   │   ├── G.png
│   │   │   └── R.png
│   │   └── train_data           # 학습 데이터 파일
│   │       ├── B.png
│   │       ├── G.png
│   │       └── R.png
│   ├── models                   # 모델 관련 코드
│   │   └── identify_rgb
│   │       ├── datasets         # 데이터셋 관련 코드
│   │       │   └── rgb_dataset.py
│   │       ├── networks         # 네트워크 구조
│   │       │   └── rgb_classifer.py
│   │       ├── predict_model.py  # 예측 모델
│   │       ├── test_model.py     # 모델 테스트
│   │       └── train_model.py    # 모델 학습
│   ├── routes                   # 라우트 관련 코드
│   │   └── predict_image.py      # 이미지 예측 라우트
│   ├── scripts                  # 스크립트 파일
│   │   ├── check_extension.py    # 파일 확장자 체크
│   │   ├── generate_data.py      # 데이터 생성 스크립트
│   │   ├── preprocess            # 전처리 관련 스크립트
│   │   │   ├── preprocess_image.py
│   │   │   └── preprocess_image_for_predict.py
│   │   └── preprocess_data.py    # 데이터 전처리 스크립트
│   └── static                   # 정적 파일 및 모듈
│       ├── models
│       │   └── identify_rgb
│       │       ├── predict_model_static.py
│       │       ├── test_model_static.py
│       │       └── train_model_static.py
│       ├── routes
│       │   └── predict_image_static.py
│       └── scripts
│           ├── generatae_data_static.py
│           └── preprocess_data_static.py
├── config.py                   # 설정 파일
├── main.py                     # 애플리케이션 진입점
├── requirements.txt            # 필요 라이브러리 목록
├── temp                        # 임시 파일 저장
└── tests                       # 테스트 코드
    └── test_app.py            # 애플리케이션 테스트
```

## 설치 및 실행 방법
1. 레포지토리를 클론합니다:
   ```bash
   git clone <레포지토리_URL>
   ```
2. 필요한 패키지를 설치합니다:
   ```bash
   pip install -r requirements.txt
   ```
3. 애플리케이션을 실행합니다:
   ```bash
   python main.py
   ```

## 기여
기여를 원하신다면 이슈를 생성하시거나 풀 리퀘스트를 제출해 주시기 바랍니다.

## 라이센스
이 프로젝트는 MIT 라이센스에 따라 라이센스가 부여됩니다.

---
