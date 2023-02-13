from rest_framework import serializers
from gen_task.models import CheckPoint


class TaskNestedCheckPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = CheckPoint
        fields = [
            'id',
            'name',
            'project'
        ]
