from django.apps import AppConfig


class UserApiConfig(AppConfig):
    name = 'user_api'

    def ready(self):
        try:
            import user_api.signals  # noqa F401
        except ImportError:
            pass