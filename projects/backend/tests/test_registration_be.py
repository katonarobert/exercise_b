from pytest_schema import schema

from projects.backend.consumers.user_consumer import UserConsumer
from projects.backend.schemas.schemas import Schemas


def test_register_new_user():
    """
    Registers a new user and verifies the results
    """
    response = UserConsumer().register_new_user()
    assert response.status_code == 200
    assert schema(Schemas().registration_schema) == response.json(), "Schema does not match"
