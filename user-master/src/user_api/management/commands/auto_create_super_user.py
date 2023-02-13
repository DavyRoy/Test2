from django.conf import settings
from django.contrib.auth import get_user_model
from user_api.models import Role
from django.core.management.base import BaseCommand
import logging
from django.db import IntegrityError

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:

            user = User.objects.create_superuser(username=settings.SUPERUSER_USERNAME,
                                                 password=settings.SUPERUSER_PASSWORD)
            default_role = Role.objects.get_or_create(name='default role', is_default=True, created_by=user)
            user.role.set(default_role)
            user.save()
            logger.info('create admin user complete')
        except IntegrityError:
            logger.info('admin user already created')
