from rest_framework import serializers
from gen_task.models import Task


class TaskNestedPreviousTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task

        fields = (
            'id',
            'name',

        )
