from factory import DictFactory
from factory.fuzzy import FuzzyInteger, FuzzyText, FuzzyFloat

from io_lottery.app import app

class UserPayloadFactory(DictFactory):
    name = FuzzyText()
    last_name = FuzzyText()
    email = FuzzyText()
    age = FuzzyInteger(low=0)
    essays_count: object = FuzzyInteger(low=0)
    rating = FuzzyFloat(low=0)

def test_can_add_user_on_post() -> None:
    payload = UserPayloadFactory()
    with app.test_client() as c:
        result = c.post("/users", json=payload)
        assert result.status_code == 200
