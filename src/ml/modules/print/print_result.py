def print_results(best_confidences, best_animal):
    """결과 출력 함수"""
    for animal, confidence in best_confidences.items():
        if animal == best_animal and confidence > 0.5:  # 신뢰도 기준
            print(f"이 이미지는 {animal}입니다 (신뢰도: {confidence:.2f}): Y")
        else:
            print(f"이 이미지는 {animal}가 아닙니다 (신뢰도: {confidence:.2f}): N")
