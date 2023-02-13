from django.conf import settings

from wrappers import BasicWrapper


class DocumentApiWrapper:
    def __init__(self):
        self.client = BasicWrapper(settings.DOCUMENT_API_URL, settings.DOCUMENT_API_TOKEN)()

    def __call__(self, instance: str, view:str, *args, **kwargs):
        """
        :param instance: task_api instance example task or check_point
        :param view: task_api view, example list or create or update or close_task
        :param args:
        :param kwargs: filtering or sorting option, example status=2 or id='qefaegfaeg'
        :return: result dict from task_api
        """

        request_view = getattr(self.client.v1, f'v1_{instance}_{view}')

        return request_view(*args, **kwargs).result()