from celery import shared_task
from logging import getLogger
from django.conf import settings
from django.utils import timezone

from gen_task.models import Task, Status

logger = getLogger(__name__)


@shared_task
def archived_tasks():
    tasks_to_archive = Task.objects.filter(status=Status.finished,
                                           ended_at__lte=timezone.now() - settings.ARCHIVE_TASK_DELAY)
    logger.info(f'tasks for archived {tasks_to_archive.count()}')
    tasks_to_archive.update(status=Status.archived)
