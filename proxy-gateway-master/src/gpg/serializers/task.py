from rest_framework import serializers

from gpg.serializers import CheckPointSerializer
from gpg.serializers.comment_task import CommentTaskSerializer
from gpg.serializers.sub_task import SubTaskSerializer
from gpg.serializers.task_file import TaskFileSerializer
from gpg.serializers.task_nested_previous_task import TaskNestedPreviousTaskSerializer
from gpg.services import TaskRepresentationService


class TaskSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=2555)
    executor = serializers.CharField(max_length=255)
    check_point = CheckPointSerializer(required=False, allow_null=True)
    reviewers = serializers.ListField(required=False)
    responsible = serializers.ListField(required=False)
    observers = serializers.ListField(required=False)
    members = serializers.ListField(required=False)
    is_selected_reviewer = serializers.BooleanField(required=False)
    is_task_agreement = serializers.BooleanField(required=False)
    priority = serializers.ChoiceField(choices=[0, 1, 2])
    status = serializers.ChoiceField(choices=[0, 1, 2, 3, 4, 5, 6])
    type = serializers.ChoiceField(choices=[0, 1, 2, 3])
    previous_task = TaskNestedPreviousTaskSerializer(required=False, allow_null=True)
    next_task = TaskNestedPreviousTaskSerializer(required=False, allow_null=True)
    project = serializers.CharField(max_length=255)
    progress = serializers.FloatField(read_only=True)
    started_at = serializers.DateTimeField()
    planned_ended_at = serializers.DateTimeField()
    ended_at = serializers.DateTimeField(required=False)
    updated_by = serializers.CharField(max_length=55, required=False)
    created_by = serializers.CharField(max_length=55, required=False)
    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    sub_tasks = SubTaskSerializer(many=True)
    task_files = TaskFileSerializer(many=True)
    task_comments = CommentTaskSerializer(many=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation['checkpoint'] =
        representation = TaskRepresentationService(representation)()

        return representation

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
