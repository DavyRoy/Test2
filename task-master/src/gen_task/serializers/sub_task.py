from rest_framework import serializers
from gen_task.models import SubTask


class SubTaskSerializer(serializers.ModelSerializer):
    task = serializers.UUIDField(source='task.id', allow_null=True)

    def create(self, validated_data):
        task_id = validated_data.pop('task')['id']
        return SubTask.objects.create(task_id=task_id, **validated_data)

    def update(self, instance, validated_data):
        instance.task.id = validated_data.pop('task')['id']
        instance.save()
        return super().update(instance, validated_data)

    class Meta:

        depth = 1
        model = SubTask
        read_only_fields = (
            'id',
            'created_at',
            'updated_at'
        )
        fields = [
            'id',
            'name',
            'task',
            'is_completed',
            'executor',
            'updated_at',
            'created_at',
            'updated_by',
            'created_by'
        ]
