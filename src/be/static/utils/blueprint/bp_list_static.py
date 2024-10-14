from enum import Enum

class Blueprints(Enum):
    """
    애플리케이션에서 사용할 블루프린트를 정의하는 열거형.
    각 블루프린트는 기능 그룹화를 위해 사용
    """
    MAIN = "main"
    IMAGE = "image"
    API = "api"
