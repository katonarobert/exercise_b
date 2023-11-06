from dataclasses import dataclass
from enum import Enum


@dataclass
class HttpMethodTypes(Enum):
    """
    HttpMethodTypes contains all the method types of a http call
    """

    POST = "post"
    GET = "get"
    PUT = "put"
    PATCH = "patch"
