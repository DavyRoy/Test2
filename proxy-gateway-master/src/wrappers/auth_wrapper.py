from django.conf import settings
from rest_framework.response import Response

from wrappers import BasicWrapper


class AuthWrapper:
    def __init__(self, user_api_token=settings.USER_API_TOKEN):
        self.client = BasicWrapper(settings.USER_API_URL, user_api_token)()

    def sign_up(self, data: dict) -> dict:
        return self.client.auth.sign_up(data=data).result()

    def sign_in(self, data: dict) -> dict:
        return self.client.auth.sign_in(data=data).result()

    def sign_in_refresh(self, data: dict) -> dict:
        return self.client.auth.sign_in_refresh(data=data).result()

    def sign_in_verify(self, data: dict) -> Response:
        return self.client.auth.sign_in_verify(data=data).response()

    def sign_out(self, data: dict) -> dict:
        return self.client.auth.sign_out(data=data).result()

    def sign_out_all(self, id: str) -> dict:
        return self.client.auth.sign_out_all(id=id).result()

    def change_password(self, id: str, data: dict) -> dict:
        return self.client.auth.change_password(data=data, id=id).result()
