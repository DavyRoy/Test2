from django.conf import settings
from rest_framework.response import Response

from wrappers import BasicWrapper


class UserApiWrapper:
    def __init__(self, user_api_token=settings.USER_API_TOKEN):
        self.client = BasicWrapper(settings.USER_API_URL, user_api_token)()

    def __call__(self, instance: str, view: str, *args, **kwargs):
        """
        :param instance: task_api instance example task or check_point
        :param view: task_api view, example list or create or update or close_task
        :param args:
        :param kwargs: filtering or sorting option, example status=2 or id='Defacing'
        :return: result dict from task_api
        """

        client = getattr(self.client, instance)

        request_view = getattr(client, f'{instance}_{view}')
        response = request_view(*args, **kwargs).result()

        return response

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
