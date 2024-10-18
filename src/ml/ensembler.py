import os
from PIL import Image
from src.ml.static.modules.model.load_models import model_info
from src.ml.modules.model.load_models import load_models
from src.ml.modules.ensemble.ensemble_predict import ensemble_predict
import logging

# 모델 로드
models = load_models(model_info)

# 신뢰도 기준을 외부에서 설정할 수 있도록
CONFIDENCE_THRESHOLD = 0.5

def predict_animal_from_image(image_path):
    try:
        # 이미지 경로로부터 이미지를 읽어서 PIL 이미지로 변환
        image = Image.open(image_path).convert('RGB')

        # 앙상블 예측
        predictions = ensemble_predict(models, image)

        # 각 동물별로 최고 신뢰도를 저장할 딕셔너리
        best_confidences = {info['animal']: 0.0 for info in model_info}

        # 예측 결과를 출력하고 각 동물별 최고 신뢰도를 업데이트합니다.
        for animal, model_predictions in predictions:
            for *box, conf, cls in model_predictions:
                conf = conf.item()  # tensor에서 값을 가져옵니다

                # 현재 동물의 최고 신뢰도 업데이트
                if conf > best_confidences[animal]:
                    best_confidences[animal] = conf

        # 전체 중 가장 높은 신뢰도를 가진 동물 찾기
        best_animal = max(best_confidences, key=best_confidences.get)

        # 결과 출력 및 반환
        result = {}
        for info in model_info:
            animal = info['animal']
            if animal == best_animal and best_confidences[animal] > CONFIDENCE_THRESHOLD:  # 신뢰도 기준
                result['Y'] = f"이 이미지는 {animal}입니다 (신뢰도: {best_confidences[animal]:.2f})"
            else:
                result[animal] = f"이 이미지는 {animal}가 아닙니다 (신뢰도: {best_confidences[animal]:.2f})"

        return result

    except Exception as e:
        logging.error(f"예측 중 오류 발생: {e}")
        return {"message": "Prediction failed due to an error."}

    finally:
        # 예외가 발생하더라도 이미지 파일 삭제
        if os.path.exists(image_path):
            os.remove(image_path)
