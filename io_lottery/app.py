from flask import Flask, Response, request

app = Flask(__name__)


@app.post("/users")
def add_user() -> Response:
    print(request.json)
    return request.json
