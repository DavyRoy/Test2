from rest_framework.serializers import CharField, Serializer, ValidationError, IntegerField

from gen_task.models import Task, Status
from gen_task.services import TaskStatusService


class StatusChangeSerializer(Serializer):
    id = CharField(max_length=100)
    status = IntegerField()
    created_by = CharField(max_length=100)

    def create(self, validated_data):
        task = validated_data.get('task', None)
        status = validated_data.get('status', None)
        if task is not None:
            task.updated_by = validated_data.get('created_by', None)
        status = TaskStatusService(task, status)()
        return status

    def validate(self, data):
        task_id = data.get('id', None)
        task_status_index = data.get('status', None)
        if not (task_instance := Task.objects.filter(id=task_id)).exists():
            raise ValidationError('Task not found')
        if 0 < task_status_index > len(Status.choices):
            raise ValidationError('Status not found')

        data['task'] = task_instance.first()
        return data
