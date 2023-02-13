from rest_framework import serializers

from gen_task.models import TaskAnalyticData


class TaskAnalyticDataSerializer(serializers.ModelSerializer):

    class Meta:
        Model = TaskAnalyticData

        read_only_fields = (
            'id',
            'created',
            'processing',
            'on_pause',
            'on_review',
            'returned',
            'finished'
        )
        fields = [
            'id',
            'created',
            'processing',
            'on_pause',
            'on_review',
            'returned',
            'finished',
            'agreed'
        ]

