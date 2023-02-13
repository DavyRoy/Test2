from rest_framework import serializers

from gpg.services import SubTaskRepresentationService


class SubTaskSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255)
    task = serializers.UUIDField()
    is_completed = serializers.BooleanField()
    updated_by = serializers.CharField(max_length=55, required=False)
    created_by = serializers.CharField(max_length=55, required=False)
    executor = serializers.CharField(max_length=55, required=False, allow_null=True)
    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation = SubTaskRepresentationService(representation)()

        return representation

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
