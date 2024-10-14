from flask import Blueprint

def generate_blueprint(bp_name):
    """주어진 이름으로 블루프린트를 생성하는 함수"""
    return Blueprint(bp_name, __name__)