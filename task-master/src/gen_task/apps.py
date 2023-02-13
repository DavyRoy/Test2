from django.apps import AppConfig


class GenTaskConfig(AppConfig):
    name = 'gen_task'

    def ready(self):
        try:
            import gen_task.signals  # noqa F401
        except ImportError:
            pass
