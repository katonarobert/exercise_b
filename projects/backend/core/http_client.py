from json import dumps
from logging import getLogger
from os import getenv
from urllib.parse import urlencode

from requests import Response, request

from projects.backend.core.enhanced_json_encoder import EnhancedJSONEncoder
from projects.backend.core.http_method_types import HttpMethodTypes


class HttpClient(object):
    """
    Http client to access REST API.
    """

    def __init__(self):
        self.host = getenv("BASE_URI")
        self.logger = getLogger(__name__)

    def _build_url(self, url_path: list[str], query_params: dict) -> str:
        """
        Builds the final URL to be passed to requests

        Params:
            url_path: the path as list of strings
            query_params: A dictionary of all the query parameters

        Returns:
            The built string
        """
        url = ""
        count = 0
        while count < len(url_path):
            url += f"/{url_path[count]}"
            count += 1

        if query_params:
            url_values = urlencode(sorted(query_params.items()), True)
            url = f"{url}?{url_values}"

        return url

    def http_request(
        self,
        url_path: list[str],
        method: HttpMethodTypes,
        request_body: str or dict or object = None,
        query_params: dict = None,
        request_headers: dict = None,
        timeout: float = None,
    ) -> Response:
        """
        Does the actual API call

        Params:
            url_path: the path as list of strings
            method: the request method
            request_body: HTTP request body
            query_params: HTTP query parameters
            request_headers: HTTP headers.
            timeout: HTTP request timeout.

        Returns:
            The Response object
        """
        if request_headers is None:
            request_headers = {}
        if request_body is None:
            data = None
        else:
            if "Content-Type" in request_headers and request_headers["Content-Type"] != "application/json":
                data = request_body.encode("utf-8")
            else:
                request_headers.setdefault("Content-Type", "application/json")
                data = dumps(request_body, cls=EnhancedJSONEncoder).encode("utf-8")
        url = f"{self.host}{self._build_url(url_path, query_params)}"
        headers = request_headers

        self.logger.debug(f"{method} Request: {url}")
        if data:
            self.logger.debug(f"PAYLOAD: {data}")
        self.logger.debug(f"HEADERS: {headers}")

        response = request(method=method.value, url=url, headers=headers, data=data, timeout=timeout)

        self.logger.debug(f"{method} Response: {response.status_code} {response.text}")

        return response
