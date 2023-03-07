import pytest
from flask.views import MethodView

from io_lottery.views import UserView


@pytest.fixture
def user_view() -> UserView:
    return UserView()


def test_user_view_is_subclass_for_method_view(user_view: UserView) -> None:
    assert isinstance(user_view, MethodView)


def test_user_view_has_post_method(user_view: UserView) -> None:
    with pytest.raises(NotImplementedError):
        user_view.post()
