# Flask 앱에 블루 프린트들을 등록하는 함수
register_routes = lambda app, *blueprints: [app.register_blueprint(bp) for bp in blueprints]