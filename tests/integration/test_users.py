from io_lottery.app import app


def test_can_add_user_on_post() -> None:
    with app.test_client() as c:
        result = c.post("/users")
        assert result.status_code == 501
