import os  # 운영 체제와의 상호작용을 위한 os 모듈 임포트
import torch  # PyTorch 라이브러리 임포트
from app.scripts.preprocess.preprocess_image import preprocess_image  # 이미지 전처리 함수 임포트
from app.static.scripts.preprocess_data_static import preprocess_input_dir,preprocess_input_ext,preprocess_output_dir,preprocess_output_ext

def preprocess_and_save_data(input_dir=preprocess_input_dir, output_dir=preprocess_output_dir):
    # 출력 디렉토리가 존재하지 않으면 생성
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 입력 디렉토리의 파일 리스트를 반복
    for filename in os.listdir(input_dir):
        # 파일이 .png 확장자로 끝나는지 확인
        if filename.endswith(preprocess_input_ext):
            # 이미지 파일 경로 생성 및 전처리
            img_tensor = preprocess_image(os.path.join(input_dir, filename))
            
            # 전처리된 텐서를 .pt 파일로 저장
            torch.save(img_tensor, os.path.join(output_dir, filename.replace(preprocess_input_ext,preprocess_output_ext)))

if __name__ == "__main__":
    # 입력 디렉토리와 출력 디렉토리 지정 후 함수 호출
    preprocess_and_save_data()
