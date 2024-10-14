import os
from dotenv import load_dotenv

def env_loader(envName):
    """
    환경 변수를 로드하는 함수.
    기본 .env 파일을 로드한 후, ENV_MODE에 따라 적절한 .env 파일을 선택하여 로드.
    주어진 환경 변수 이름에 해당하는 값을 반환.
    """
    load_dotenv()
    env_mode = os.getenv("ENV_MODE")
    env_file = ".env.development" if env_mode == "development" else ".env.production"
    load_dotenv(env_file)
    return os.getenv(envName)
