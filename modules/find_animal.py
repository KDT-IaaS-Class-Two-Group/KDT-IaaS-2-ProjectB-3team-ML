def get_best_animal(best_confidences):
    """최고 신뢰도를 가진 동물 찾기"""
    return max(best_confidences, key=best_confidences.get), best_confidences[max(best_confidences, key=best_confidences.get)]
