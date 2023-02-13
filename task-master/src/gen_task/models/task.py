from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

from .basic_model import BasicModel
from .priority import Priority
from .status import Status
from .type import Type


class TaskQuerySet(models.QuerySet):
    def expired(self, task) -> bool:
        return timezone.now() > task.planned_ended_at

    def get_by_executor(self, user_id: str) -> models.QuerySet:
        return self.filter(executor=user_id)

    def get_executor_unfinished_tasks(self, user_id: str) -> models.QuerySet:
        return self.filter(executor=user_id).exclude(status=Status.finished)

    def get_executor_unfinished_tasks_exclude_self(self, user_id: str, task_id: str = None):
        queryset = self.get_executor_unfinished_tasks(user_id)

        if task_id is not None:
            queryset = queryset.exclude(id=task_id)

        return queryset


class Task(BasicModel):
    description = models.CharField(max_length=2555, verbose_name='Описание')
    check_point = models.ForeignKey('gen_task.CheckPoint', on_delete=models.CASCADE, related_name='tasks', blank=True, null=True, verbose_name='Контрольная точка')
    executor = models.CharField(max_length=255, verbose_name='Исполнитель')
    reviewers = ArrayField(models.CharField(max_length=255, blank=True, null=True), null=True, blank=True, size=20, default=list, verbose_name='Аудиторы')
    observers = ArrayField(models.CharField(max_length=255, blank=True, null=True), null=True, blank=True, size=20, default=list, verbose_name='Наблюдатели')
    responsible = ArrayField(models.CharField(max_length=255, blank=True, null=True), null=True, blank=True, size=20, default=list, verbose_name='Отвественные')
    members = ArrayField(models.CharField(max_length=255, blank=True, null=True), null=True, blank=True, size=20, default=list, verbose_name='Участники')
    priority = models.IntegerField(choices=Priority.choices, verbose_name='Приоритет')
    status = models.IntegerField(choices=Status.choices, verbose_name='Статус')
    type = models.IntegerField(choices=Type.choices, verbose_name='Тип')
    project = models.CharField(max_length=255, null=True, blank=True, verbose_name='Проект')

    previous_task = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Предыдущая Задача', related_name='previous_tasks')
    next_task = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Следующая Задача', related_name='next_tasks')

    is_selected_reviewer = models.BooleanField(default=False, verbose_name='Вернуть на проверку')
    is_task_agreement = models.BooleanField(default=False, verbose_name='Создать задачу на согласование')
    notification_owner = models.BooleanField(default=False, verbose_name='Уведомлять создателя')
    task_analytic_data = models.OneToOneField('gen_task.TaskAnalyticData', on_delete=models.CASCADE,
                                              related_name='task')
    started_at = models.DateTimeField(verbose_name='Дата начала')
    planned_ended_at = models.DateTimeField(verbose_name='Планируемая дата окончания')
    ended_at = models.DateTimeField(blank=True, null=True, verbose_name='Фактическая дата окончания')
    objects = TaskQuerySet.as_manager()

    @property
    def progress(self):
        if self.sub_tasks.exists():
            progress = self.sub_tasks.filter(is_completed=True).count() / self.sub_tasks.count()
            return round(progress, 2) * 100
        return 100 if self.status == Status.finished else 0

    class Meta:
        ordering = ["started_at"]
