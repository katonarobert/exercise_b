import random
from json import load
from os import getenv

from dotenv import load_dotenv
from locust import HttpUser, between, task


class Login(HttpUser):
    """
    Login performance tests
    """

    config: object
    users: list[object]
    wait_time = between(1, 5)

    def on_start(self):
        dotenv_path = ".env"
        print("dotenv_path", dotenv_path)
        load_dotenv(dotenv_path)
        with open("projects/shared/config.json", "r", encoding="utf-8") as f:
            self.config = load(f)
        current_env = [env for env in self.config["configs"] if env["uri"] == self.host][0]
        self.users = current_env["users"]

    @task
    def login_with_users(self):
        """
        Logs in with a random user specified in config.json
        """

        response = self.client.post(
            url="/users/sign_in",
            json={"email": random.choice(self.users)["email"], "password": getenv("PASSWORD")},
        )
        print("Response status code:", response.status_code)
        print("Response text:", response.text)
