from flask import Flask, Response

app = Flask(__name__)


@app.post("/users")
def add_user() -> Response:
    return Response(status=501)
