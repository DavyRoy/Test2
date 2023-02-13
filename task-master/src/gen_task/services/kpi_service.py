from django.conf import settings
from django.utils import timezone

from gen_task.models import Task
from gen_task.services.kpi_message_broker import Message


class KPIService:
    def __init__(self, user_id: str) -> None:
        self.user_id: str = user_id
        self.active_user_tasks = self._get_active_user_tasks()

    def _get_active_user_tasks(self):

        return Task.objects.get_by_executor(user_id=self.user_id).filter(started_at__gt=timezone.now() - settings.KPI_RANGE_DATE,
                                                                         started_at__lt=timezone.now())

    def _calculate(self) -> float:
        self.finished_tasks_count: int = self.active_user_tasks.exclude(ended_at=None).count()
        self.active_tasks_count: int = self.active_user_tasks.count() - self.finished_tasks_count
        kpi = round(self.finished_tasks_count / self.active_user_tasks.count(), 2)
        kpi_data = {
            'user_id': self.user_id,
            'kpi': kpi
        }
        Message(settings.KPI_RABBITMQ_TITLE, kpi_data).send()

        return kpi

    def __call__(self) -> float:
        kpi = self._calculate()

        return kpi
