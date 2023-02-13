import datetime
from django.db.models import F
from django.utils import timezone

from gen_task.models import Task, CheckPoint, Type, Status, Priority
from gen_task.services.create_task_service import CreateTaskService


class CloseTaskService:

    def __init__(self, task: Task) -> None:
        self.task: Task = task
        self.task_qs = Task.objects.filter(pk=self.task.pk)
        self.expiration_delta = timezone.now() - self.task.planned_ended_at

    def _create_agreement_task(self):
        task = CreateTaskService.create_task(
            name=f"Agreement: {self.task.name}",
            description='Agreement',
            status=Status.on_review,
            executor=self.task.executor,
            observers=self.task.observers,
            check_point=self.task.check_point,
            reviewers=self.task.reviewers,
            priority=Priority.high,
            started_at=timezone.now(),
            planned_ended_at=timezone.now()+datetime.timedelta(days=2),
            type=Type.agreement,
            previous_task=self.task,
            created_by=self.task.created_by)

        return task

    def overdue_tasks(self):
        if self.task.check_point is not None:
            linked_check_points = CheckPoint.objects.filter(
                project=self.task.check_point.project,
                planned_ended_at__gt=timezone.now()
            ).exclude(id=self.task.check_point.id)
            linked_check_points.update(
                planned_ended_at=F('planned_ended_at') + self.expiration_delta,
                started_at=F('started_at') + self.expiration_delta
            )
            local_check_point_tasks = self.task.check_point.tasks.exclude(
                id=self.task.id
            ).exclude(
                ended_at__isnull=False
            )
            linked_tasks = Task.objects.filter(
                id__in=linked_check_points.values_list('tasks', flat=True),
                ended_at__isnull=True) | local_check_point_tasks
            linked_tasks.update(
                planned_ended_at=F('planned_ended_at') + self.expiration_delta,
                started_at=F('started_at') + self.expiration_delta
            )
            self.task_qs.exclude(is_task_agreement=True).update(
                ended_at=timezone.now(),
                status=Status.finished
            )
        else:
            self.task_qs.exclude(is_task_agreement=True).update(
                ended_at=timezone.now(),
                status=Status.finished
            )

    def task_not_overdue(self):
        task_not_agreement = self.task_qs.exclude(is_task_agreement=True)
        task_not_agreement.update(
            ended_at=timezone.now(),
            status=Status.finished
        )

    def task_agreement(self):
        if self.task.is_selected_reviewer and self.task.created_by not in self.task.reviewers:
            self.task.reviewers.append(self.task.created_by)
        self._create_agreement_task()
        self.task_qs.exclude(is_task_agreement=False).update(
            is_task_agreement=False,
            status=Status.on_review
        )

    def agreement_previous_task_update(self):
        if self.task.type == Type.agreement:
            if self.task.previous_task is not None:
                previous_task_qs = Task.objects.filter(pk=self.task.previous_task.pk)
                if self.task.status == Status.returned:
                    previous_task_qs.update(
                        status=Status.returned,
                        is_task_agreement=True,
                    )
                else:
                    previous_task_qs.update(
                        ended_at=timezone.now(),
                        status=Status.finished
                    )
            self.task_qs.update(
                ended_at=timezone.now(),
                status=Status.finished
            )

    def process(self):
        if Task.objects.expired(self.task):
            self.overdue_tasks()
        else:
            self.task_not_overdue()

        if self.task.is_task_agreement:
            self.task_agreement()

        self.agreement_previous_task_update()

        return self.task

    def __call__(self):
        return self.process()
