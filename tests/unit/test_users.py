from flask import Response

from io_lottery.app import add_user


def test_returns_501() -> None:
    actual = add_user()
    expected = Response(status=501)
    assert actual.status_code == expected.status_code