# src/static/http_methods.py
from enum import Enum

class HTTPMethods(Enum):
    """
    HTTP 요청 메서드를 정의하는 열거형.
    각 메서드는 웹 애플리케이션과 서버 간의 통신 방식에 사용.
    """
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    OPTIONS = "OPTIONS"
