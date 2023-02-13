from rest_framework import serializers

from gpg.services import CommentTaskRepresentationService


class CommentTaskSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    text = serializers.CharField(max_length=3000)
    task = serializers.UUIDField()
    is_system_comment = serializers.BooleanField(read_only=True)
    updated_by = serializers.CharField(max_length=55, required=False)
    created_by = serializers.CharField(max_length=55, required=False)
    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation = CommentTaskRepresentationService(representation)()

        return representation

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
