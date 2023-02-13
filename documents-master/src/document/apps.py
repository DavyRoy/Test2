from django.apps import AppConfig


class DocumentConfig(AppConfig):
    name = 'document'

    def ready(self):
        try:
            import document.signals  # noqa F401
        except ImportError:
            pass