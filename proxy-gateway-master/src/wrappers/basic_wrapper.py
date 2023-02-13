from urllib.parse import urlparse

from bravado.client import SwaggerClient
from bravado.requests_client import RequestsClient


class BasicWrapper:
    def __init__(self, api_url: str, token: str):
        self.client = self._init_api_client(api_url, token)

    def _init_api_client(self, api_url: str, token: str) -> SwaggerClient:
        http_client = RequestsClient()
        http_client.set_api_key(
            urlparse(api_url).netloc, f'Bearer {token}',
            param_name='Authorization', param_in='header'
        )

        client = SwaggerClient.from_url(
            f'{api_url}swagger.json',
            http_client=http_client,
            config={'validate_responses': False,
                    'use_models': False}
        )

        return client

    def __call__(self) -> SwaggerClient:
        return self.client
