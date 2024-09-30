import unittest
from app import create_app
from flask import current_app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        # 애플리케이션을 생성하고 테스트 모드로 전환합니다.
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()  # 테스트 클라이언트 생성

    def test_app_exists(self):
        # 애플리케이션 인스턴스가 존재하는지 확인합니다.
        with self.app.app_context():
            self.assertIsNotNone(current_app)

    def test_app_is_testing(self):
        # 애플리케이션이 테스트 모드에서 실행되고 있는지 확인합니다.
        self.assertTrue(self.app.testing)

    def test_home_endpoint(self):
        # '/' 엔드포인트가 올바르게 작동하는지 확인합니다.
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, Flask!', response.data)  # 응답에 예상 문자열이 포함되어 있는지 확인합니다.

if __name__ == '__main__':
    unittest.main()
