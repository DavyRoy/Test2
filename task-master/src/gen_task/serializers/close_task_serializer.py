from rest_framework.serializers import CharField, Serializer, ValidationError

from gen_task.models import Task
from gen_task.services import CloseTaskService


class CloseTaskSerializer(Serializer):
    id = CharField(max_length=100)

    def create(self, validated_data):
        task = validated_data.get('task')
        task = CloseTaskService(task).process()
        return task

    def validate(self, data):
        task_id = data.get('id', None)
        if not (task_instance := Task.objects.filter(id=task_id)).exists():
            raise ValidationError('Task to close not found')

        data['task'] = task_instance.first()
        return data
