from src.be.static.utils.blueprint.bp_list_static import Blueprints
from src.be.modules.utils.generator.bp_generator import generate_blueprint

class BlueprintContainer:
    """
    블루프린트를 생성하고 저장하는 컨테이너 클래스.
    """
    def __init__(self):
        self.MAIN = generate_blueprint(Blueprints.MAIN.value)
        self.IMAGE = generate_blueprint(Blueprints.IMAGE.value)
        self.API = generate_blueprint(Blueprints.API.value)

    def get_blueprints(self):
        """
        클래스 속성을 반복하여 블루프린트 목록을 반환하는 메서드.
        """
        return {name: getattr(self, name) for name in self.__dict__ if not name.startswith('__')}

# bp_list 변수에 BlueprintContainer 인스턴스 저장
bp_list = BlueprintContainer()
