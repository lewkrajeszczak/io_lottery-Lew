from factory import Factory
from factory.fuzzy import FuzzyText, FuzzyInteger, FuzzyFloat
from pytest import fixture

from io_lottery.domain import User


class UserFactory(Factory):
    class Meta:
        model = User

    first_name = FuzzyText()
    last_name = FuzzyText()
    email = FuzzyText()
    age = FuzzyInteger(low=0)
    essays_count = FuzzyInteger(low=0)
    rating = FuzzyFloat(low=0)


@fixture
def user() -> User:
    return UserFactory()


def test_can_instantiate_user(user: User) -> None:
    pass


def test_user_has_first_name_as_attribute(user: User) -> None:
    assert user.first_name
