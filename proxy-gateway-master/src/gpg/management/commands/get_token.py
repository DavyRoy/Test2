from logging import getLogger
from pprint import pprint

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

logger = getLogger(__name__)
User = get_user_model()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('username', nargs='+', type=str)
        parser.add_argument('password', nargs='+', type=str)

    def handle(self, *app_labels, **options):

        serializer = TokenObtainPairSerializer(data={'username': options['username'][0], 'password': options['password'][0]})
        serializer.is_valid(raise_exception=True)
        tokens = serializer.validated_data
        pprint(tokens)
