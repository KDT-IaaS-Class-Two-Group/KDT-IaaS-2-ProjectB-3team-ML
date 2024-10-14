from enum import Enum

class EnvList(Enum):
    """
    환경 변수 이름을 정의하는 열거형.
    애플리케이션에서 필요한 환경 변수를 관리하기 위해 사용.
    """
    FE_MAIN_URL = "FE_MAIN_URL"
    ML_MAIN_URL = "ML_MAIN_URL"
    EP_API = "EP_API"
    EP_ML = "EP_ML"
