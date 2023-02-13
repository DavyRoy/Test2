from django.core.management.base import BaseCommand, CommandError

from user_api.services.message_consumer import MessageConsumer


class Command(BaseCommand):

    def handle(self, *args, **options):
        MessageConsumer().start()
