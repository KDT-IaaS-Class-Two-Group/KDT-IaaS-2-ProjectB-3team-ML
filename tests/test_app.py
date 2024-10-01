import unittest
from src import create_app
from flask import current_app
import os
import json

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_app_exists(self):
        with self.app.app_context():
            self.assertIsNotNone(current_app)

    def test_app_is_testing(self):
        self.assertTrue(self.app.testing)

    def test_home_endpoint(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, Flask!', response.data)

    def test_predict_endpoint(self):
        test_image_path = os.path.join('src', 'data', 'train_data', 'R.png')
        
        with open(test_image_path, 'rb') as img:
            response = self.client.post('/predict', data={'file': (img, 'R.png')})
        
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data.decode('utf-8'))
        
        self.assertIn('result', response_data)
        predicted_result = response_data['result']
        
        print(f"\nPredicted result: {predicted_result}")  # 예측 결과 출력
        
        self.assertEqual(predicted_result, 'R')  # 'R'이 예상되는 예측 결과라고 가정, 만약 여러개의 값중 옳은지 고르려면 assertIn을 사용

if __name__ == '__main__':
    unittest.main()