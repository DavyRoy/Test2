from rest_framework import serializers
from gen_task.models import CheckPoint


class CheckPointSerializer(serializers.ModelSerializer):
    stage = serializers.UUIDField(source='stage.id', required=False, allow_null=True)

    class Meta:

        depth = 1
        model = CheckPoint
        read_only_fields = (
            'id',
            'created_at',
            'updated_at'
        )
        fields = [
            'id',
            'name',
            'description',
            'project',
            'stage',
            'is_stage',
            'priority',
            'executor',
            'observers',
            'status',
            'started_at',
            'planned_ended_at',
            'ended_at',
            'updated_by',
            'updated_at',
            'created_by',
            'created_at',
            'tasks',
            'stages'
        ]
