from logging import getLogger
from os import getenv

from faker import Faker

from projects.backend.core.http_client import HttpClient
from projects.backend.core.http_method_types import HttpMethodTypes
from projects.backend.objects.currency_ids import CurrencyIds
from projects.backend.objects.login_request import LoginRequest
from projects.backend.objects.registration_request import RegistrationRequest
from projects.backend.objects.user_types import UserTypes


class UserConsumer:
    """
    UserConsumer class contains all the user related endpoints
    """

    def __init__(self):
        self.host = getenv("BASE_URI")
        self.logger = getLogger(__name__)

    def register_new_user(self):
        """
        Registers a new user using faker

        Returns:
            The response object
        """
        new_name = Faker().name()
        response = HttpClient().http_request(
            method=HttpMethodTypes.POST,
            url_path=["users"],
            request_body=RegistrationRequest(
                first_name=new_name.split()[0],
                last_name=new_name.split()[1],
                email=f"{new_name.split()[0].lower()}.{new_name.split()[1].lower()}@gmail.com",
                password=getenv("PASSWORD"),
                phone_number="+44-1234567890",
                user_type=UserTypes.USER.value,
                currency_id=CurrencyIds.POUND.value,
            ),
        )
        return response

    def login_with_user(self, user_email: str):
        """
        Logs in with the user defined in params

        Params:
            user_email: the email of the user

        Returns:
            The response object
        """
        response = HttpClient().http_request(
            method=HttpMethodTypes.POST,
            url_path=["users", "sign_in"],
            request_body=LoginRequest(email=user_email, password=getenv("PASSWORD")),
        )
        return response
