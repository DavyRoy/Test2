from django.conf import settings

from . import BasicWrapper

class NotificationApiWrapper:
    def __init__(self):
        self.client = BasicWrapper(settings.NOTIFICATION_API_URL, settings.NOTIFICATION_API_TOKEN)()

    def send_message(self, data: dict):
        return self.client.v1.send_message(data=data).result()
