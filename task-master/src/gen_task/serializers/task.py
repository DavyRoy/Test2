from rest_framework import serializers
# from rest_framework.serializers import ValidationError
# from ..utils import get_half_hour_timedelta
from gen_task.models import Task
from .task_nested_check_point import TaskNestedCheckPointSerializer
from .task_nested_previous_task import TaskNestedPreviousTaskSerializer
from ..services import CreateTaskService, UpdateTaskService


class TaskSerializer(serializers.ModelSerializer):
    check_point = serializers.UUIDField(source='check_point.id', required=False, allow_null=True)
    previous_task = serializers.UUIDField(source='previous_task.id', required=False, allow_null=True)
    next_task = serializers.UUIDField(source='next_task.id', required=False, allow_null=True)

    def create(self, validated_data):
        return CreateTaskService(validated_data)()

    def update(self, instance, validated_data):
        return UpdateTaskService(instance, validated_data)()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.check_point is not None:
            representation["check_point"] = TaskNestedCheckPointSerializer(instance.check_point).data
        if instance.previous_task is not None:
            representation["previous_task"] = TaskNestedPreviousTaskSerializer(instance.previous_task).data
        if instance.next_task is not None:
            representation["next_task"] = TaskNestedPreviousTaskSerializer(instance.next_task).data

        return representation

    # def validate(self, data): # TODO: UNCOMMENT IN GOOD TIME
    #     executor = data.get('executor', None)
    #     started_at = data.get('started_at', None)
    #     planned_ended_at = data.get('planned_ended_at', None)
    #     task_id = self.context.get('pk', None)
    #
    #     if all((executor, started_at, planned_ended_at)):
    #         started_at_timedelta = get_half_hour_timedelta(started_at)
    #         planned_ended_at_timedelta = get_half_hour_timedelta(planned_ended_at)
    #
    #         executor_tasks = Task.objects.get_executor_unfinished_tasks_exclude_self(executor, task_id)
    #         if executor_tasks.filter(started_at__range=started_at_timedelta).exists():
    #             raise ValidationError('The task for this started_at time has already been created')
    #         if executor_tasks.filter(planned_ended_at__range=planned_ended_at_timedelta).exists():
    #             raise ValidationError('The task for this planned_ended_at time has already been created')
    #
    #     return data

    class Meta:
        depth = 1
        model = Task

        fields = (
            'id',
            'name',
            'description',
            'priority',
            'check_point',
            'is_selected_reviewer',
            'is_task_agreement',
            'reviewers',
            'responsible',
            'members',
            'executor',
            'observers',
            'status',
            'type',
            'project',
            'started_at',
            'planned_ended_at',
            'ended_at',
            'previous_task',
            'next_task',
            'progress',
            'updated_by',
            'updated_at',
            'created_by',
            'created_at',
            'task_files',
            'task_comments',
            'sub_tasks'
        )
