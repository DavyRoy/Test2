from gen_task.models import Task, CheckPoint
from gen_task.services.create_system_history_records_service import CreateSystemHistoryRecordsService


class UpdateTaskService:

    def __init__(self, task: Task, kwargs) -> None:
        self.task: Task = task
        self.kwargs = kwargs
        self.task_qs = Task.objects.filter(pk=self.task.pk)

    def process(self):
        if (check_point := self.kwargs.pop('check_point', None)) is not None:
            self.task.check_point = CheckPoint.objects.filter(id=check_point['id']).first()
        if (previous_task := self.kwargs.pop('previous_task', None)) is not None:
            self.task.previous_task = Task.objects.filter(id=previous_task['id']).first()
        if (next_task := self.kwargs.pop('next_task', None)) is not None:
            self.task.next_task = Task.objects.filter(id=next_task['id']).first()
        self.task.save()
        self.task_qs.update(**self.kwargs)

        CreateSystemHistoryRecordsService(self.task, self.kwargs)()
        return self.task_qs.first()

    def __call__(self):

        return self.process()
