from django.core.management.base import BaseCommand

from datetime import timedelta

from django.utils import timezone

from gen_task.models import Task, CheckPoint, CommentTask, TaskFile, SubTask
from gen_task.tests.fixtures_factory import CheckPointFactory, TaskFactory, CommentTaskFactory, TaskFileFactory, SubTaskFactory


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):

        for _ in range(3):
            check_point = CheckPointFactory.create(
                stage=None,
                started_at=timezone.now() + timedelta(days=-60),
                planned_ended_at=timezone.now() + timedelta(days=-30)
            )
            task = TaskFactory.create(
                check_point=check_point,
                previous_task=None,
                started_at=timezone.now() + timedelta(days=-60),
                planned_ended_at=timezone.now() + timedelta(days=-30)
            )
            TaskFactory.create(
                check_point=check_point,
                previous_task=task,
                started_at=timezone.now(),
                planned_ended_at=timezone.now() + timedelta(days=30)
            )
            CommentTaskFactory.create(
                task=task
            )
            TaskFileFactory.create(
                task=task
            )
            SubTaskFactory.create(
                task=task
            )

        print(f"Number of CheckPoint: {CheckPoint.objects.all().count()}\n"
              f"Number of Task: {Task.objects.all().count()}\n"
              f"Number of SubTask: {SubTask.objects.all().count()}\n"
              f"Number of CommentTask: {CommentTask.objects.all().count()}\n"
              f"Number of TaskFile: {TaskFile.objects.all().count()}")
