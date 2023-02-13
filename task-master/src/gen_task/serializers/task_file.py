from rest_framework import serializers
from gen_task.models import TaskFile


class TaskFilesSerializer(serializers.ModelSerializer):
    task = serializers.UUIDField(source='task.id', allow_null=True)

    def create(self, validated_data):
        if (task := validated_data.pop('task', None)) is not None:
            validated_data['task_id'] = task['id']
        return TaskFile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.task.id = validated_data.pop('task')['id']
        instance.save()
        return super().update(instance, validated_data)

    class Meta:

        depth = 1
        model = TaskFile
        read_only_fields = (
            'id',
            'created_at',
            'updated_at'
        )
        fields = [
            'id',
            'name',
            'file_id',
            'task',
            'updated_by',
            'updated_at',
            'created_by',
            'created_at'
        ]
