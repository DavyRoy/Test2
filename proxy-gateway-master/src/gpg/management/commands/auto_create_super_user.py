from logging import getLogger

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import IntegrityError

logger = getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            User.objects.create_superuser(username=settings.SUPERUSER_USERNAME,
                                          password=settings.SUPERUSER_PASSWORD)
            logger.info('create admin user complete')
        except IntegrityError:
            logger.info('admin user already created')
