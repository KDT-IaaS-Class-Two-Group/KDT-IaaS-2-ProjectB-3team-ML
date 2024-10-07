# from model_loader import load_models
# from image_processor import preprocess_image
# from predictor import ensemble_predict
# from confidence_updater import update_best_confidences
# from best_animal_finder import get_best_animal
# from result_printer import print_results

from modules.model.load_models import load_models
from modules.image.preprocess_image import preprocess_image
from modules.ensemble.ensemble_predict import ensemble_predict
from modules.update.confidence_updater import update_best_confidences
from modules.find_animal import get_best_animal
from modules.print.print_result import print_results

def main(image_path):
    """메인 함수"""
    # 모델 로드
    models = load_models()

    # 앙상블 예측
    predictions = ensemble_predict(models, image_path)

    # 각 동물별로 최고 신뢰도를 저장할 딕셔너리
    best_confidences = {info['animal']: 0.0 for info in model_info}

    # 최고 신뢰도 업데이트
    update_best_confidences(predictions, best_confidences)

    # 전체 중 가장 높은 신뢰도를 가진 동물 찾기
    best_animal, best_overall_confidence = get_best_animal(best_confidences)

    # 결과 출력
    print_results(best_confidences, best_animal)

# 예측하고 싶은 이미지 파일 경로
if __name__ == "__main__":
    image_path = './Dataset/images/gorani_train.jpg'
    main(image_path)
