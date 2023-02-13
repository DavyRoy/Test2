from rest_framework import serializers
from gen_task.models import CommentTask


class CommentTaskSerializer(serializers.ModelSerializer):
    task = serializers.UUIDField(source='task.id', allow_null=True)

    def create(self, validated_data):
        task_id = validated_data.pop('task')['id']
        return CommentTask.objects.create(task_id=task_id, **validated_data)

    def update(self, instance, validated_data):
        instance.task.id = validated_data.pop('task')['id']
        instance.save()
        return super().update(instance, validated_data)

    class Meta:

        depth = 1
        model = CommentTask
        read_only_fields = (
            'id',
            'created_at',
            'updated_at'
        )
        fields = [
            'id',
            'text',
            'task',
            'updated_by',
            'updated_at',
            'created_by',
            'created_at'
        ]