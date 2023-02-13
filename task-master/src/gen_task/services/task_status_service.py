from copy import deepcopy
from datetime import timedelta

from django.conf import settings
from django.utils import timezone

from gen_task.models import Task, Status, Priority, Type
from gen_task.services import CreateTaskService
from gen_task.services.create_system_history_records_service import CreateSystemHistoryRecordsService
from gen_task.services.status_change_message_broker import Message


class TaskStatusService:
    def __init__(self, task: Task, status: int, ):
        self.task: Task = task
        self.status: int = status
        self.task_qs = Task.objects.filter(pk=self.task.pk)
        self.statuses = {
            0: 'Created',
            1: 'Processing',
            2: 'On pause',
            3: 'On review',
            4: 'Returned',
            5: 'Agreed',
            6: 'Finished'
        }
        self.status_field = self.statuses[self.status]

    def process(self):
        status_change_data = {
            'id': str(self.task.pk),
            'old_status': self.task.status,
            'new_status': self.status,
            'created_by': self.task.created_by
        }
        self.change_status()
        if self.task.notification_owner:
            Message(settings.STATUS_CHANGE_RABBITMQ_TITLE, status_change_data).send()

        self.task.refresh_from_db()

    def change_status(self):
        if self.status == Status.finished:
            task_fields_for_create = {'name': f'Проверить задачу `{self.task.name}`',
                                      'description': f'Проверить задачу `{self.task.name}`',
                                      'executor': self.task.created_by,
                                      'priority': Priority.high,
                                      'status': Status.created,
                                      'type': Type.agreement,
                                      'started_at': timezone.now(),
                                      'check_point_id': str(
                                          self.task.check_point.id) if self.task.check_point is not None else None,
                                      'planned_ended_at': timezone.now() + timedelta(days=7),
                                      'updated_by': self.task.executor,
                                      'created_by': self.task.executor,
                                      }
            if self.task.check_point is not None:
                task_fields_for_create['check_point_id'] = str(self.task.check_point.id)

            if self.task.is_selected_reviewer:
                CreateTaskService(task_fields_for_create)()

            if len(self.task.reviewers) != 0:
                for reviewer in self.task.reviewers:
                    task_fields_for_create['executor'] = reviewer
                    task_fields_for_create['created_by'] = self.task.executor

                    CreateTaskService(task_fields_for_create)()

        self.task_qs.update(status=self.status, updated_at=timezone.now(), ended_at=timezone.now())
        setattr(self.task.task_analytic_data, self.status_field, timezone.now())
        self.task.task_analytic_data.save()

        CreateSystemHistoryRecordsService(
            task=self.task,
            fields={'status': self.status}
        )()

    def __call__(self):
        self.process()

        return self.task
