from flask import Flask, Response, request, jsonify

from io_lottery.controllers import AddUserController, AddUserRequest, GetUserController
from io_lottery.repositories import UserRepository

app = Flask(__name__)


@app.post("/users")
def add_user() -> Response:
    repository = UserRepository()
    controller = AddUserController(repository=repository)
    controller.add(request=AddUserRequest(json=request.json))
    return jsonify(request.json)


@app.get("/users/<id>")
def get_user(id: int) -> Response:
    controller = GetUserController()
    try:
        controller.get(id)
    except NotImplementedError:
        pass
    return Response(status=501)
