from rest_framework import serializers

from gpg.services import TaskFileRepresentationService


class TaskFileSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255)
    file_id = serializers.CharField(max_length=2555)
    task = serializers.UUIDField()
    updated_by = serializers.CharField(max_length=55, required=False)
    created_by = serializers.CharField(max_length=55, required=False)
    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation = TaskFileRepresentationService(representation)()

        return representation

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
