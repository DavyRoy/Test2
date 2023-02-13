import json
import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from logging import getLogger

from user_api.serializers import UserSerializer
from user_api.services import redis_client


logging.basicConfig(level=logging.INFO)
logger = getLogger(__name__)
User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        try:
            users = User.objects.all()
            for user in users:
                redis_client.set(name=str(user.id), value=json.dumps(UserSerializer(user).data, indent=4, sort_keys=True, default=str))
            logger.info('users cached!')
        except Exception as e:
            logger.info('error while try to cache users\n', e)
            pass
