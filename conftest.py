"""
To share the fixtures that will be defined all tests in the test suite
"""
from json import load
from os import getenv
from os.path import dirname, join

import pytest
from dotenv import load_dotenv


@pytest.fixture(scope="session", autouse=True)
def load_dot_env():
    """
    Loads the .env file to be used for the test suite
    """
    dotenv_path = join(dirname(__file__), ".env")
    load_dotenv(dotenv_path)


@pytest.fixture(scope="session", autouse=True)
def read_config():
    """
    Loads the config.json file for the test suite
    """
    with open("projects/shared/config.json", "r", encoding="utf-8") as f:
        pytest.testing_config = load(f)


@pytest.fixture(scope="session", autouse=True)
def read_users():
    """
    Loads the current, previously registered user for the test suite
    """
    current_env = [env for env in pytest.testing_config["configs"] if env["uri"] == getenv("BASE_URI")][0]
    pytest.current_user = current_env["users"][0]
