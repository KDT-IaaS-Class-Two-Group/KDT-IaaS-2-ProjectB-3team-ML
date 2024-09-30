# 확장자를 확인하는 기능
def allowed_file(filename, allowed_extenstions):
    """
    파일 이름이 특정 확장자 중 하나인지 확인합니다.

    :param filename: 검사할 파일 이름
    :param allowed_extenstions: 허용할 확장자
    :return: 확장자가 허용된 파일일 경우 True, 그렇지 않으면 False
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extenstions