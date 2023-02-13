from gen_task.models import Task, TaskAnalyticData
from gen_task.services.create_system_history_records_service import CreateSystemHistoryRecordsService


class CreateTaskService:

    def __init__(self, kwargs):
        self.kwargs = kwargs

    def create_task(self):
        if (check_point := self.kwargs.pop('check_point', None)) is not None and check_point != '':
            self.kwargs['check_point_id'] = check_point['id']
        if (previous_task := self.kwargs.pop('previous_task', None)) is not None and previous_task != '':
            self.kwargs['previous_task_id'] = previous_task['id']
        if (next_task := self.kwargs.pop('next_task', None)) is not None and next_task != '':
            self.kwargs['next_task_id'] = next_task['id']

        self.kwargs['task_analytic_data'] = TaskAnalyticData.objects.create()
        task = Task.objects.create(**self.kwargs)
        CreateSystemHistoryRecordsService(task, self.kwargs).create_task_notification()
        return task

    def __call__(self):

        return self.create_task()
