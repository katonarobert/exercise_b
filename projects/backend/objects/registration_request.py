from dataclasses import dataclass

from projects.backend.objects.currency_ids import CurrencyIds
from projects.backend.objects.user_types import UserTypes


@dataclass
class RegistrationRequest:
    """
    RegistrationRequest contains the request body for registration endpoint
    """

    first_name: str
    last_name: str
    email: str
    password: str
    phone_number: str
    user_type: UserTypes
    currency_id: CurrencyIds
    utm_campaign: str = ""
    utm_source: str = ""
    utm_medium: str = ""
    utm_content: str = ""
    utm_term: str = ""

    @property
    def repr_json(self):
        """
        Returns the dataclass as dict
        """
        return {
            "user": {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "email": self.email,
                "password": self.password,
                "phone_number": self.phone_number,
                "user_type": self.user_type,
                "currency_id": self.currency_id,
                "utm_campaign": self.utm_campaign,
                "utm_source": self.utm_source,
                "utm_medium": self.utm_medium,
                "utm_content": self.utm_content,
                "utm_term": self.utm_term,
            }
        }
