from flask import Flask, Response, request, jsonify

from io_lottery.controllers import AddUserController, AddUserRequest

app = Flask(__name__)


@app.post("/users")
def add_user() -> Response:
    controller = AddUserController()
    controller.add(request=AddUserRequest(json=request.json))
    return jsonify(request.json)
