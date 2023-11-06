import pytest
from pytest_schema import schema

from projects.backend.consumers.user_consumer import UserConsumer
from projects.backend.schemas.schemas import Schemas


def test_login_with_existing_user():
    """
    Logs in with an existing user and verifies the results
    """
    response = UserConsumer().login_with_user(user_email=pytest.current_user["email"])
    assert response.status_code == 200
    assert schema(Schemas().successful_sign_in) == response.json(), "Schema does not match"


def test_login_with_non_existing_user():
    """
    Logs in with a non-existing user and verifies the results
    """
    response = UserConsumer().login_with_user(user_email="non.existent.user@gmail.com")
    print(response.json())
    assert response.status_code == 422
    assert schema(Schemas().email_not_registered) == response.json(), "Schema does not match"
