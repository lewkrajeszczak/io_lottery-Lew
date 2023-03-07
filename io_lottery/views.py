from flask.views import MethodView


class UserView(MethodView):
    def post(self) -> None:
        raise NotImplementedError
