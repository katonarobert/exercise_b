from dataclasses import dataclass


@dataclass
class LoginRequest:
    """
    LoginRequest contains the request body for login endpoint
    """

    email: str
    password: str

    @property
    def repr_json(self):
        """
        Returns the dataclass in a dict format
        """
        return {
            "email": self.email,
            "password": self.password,
        }
