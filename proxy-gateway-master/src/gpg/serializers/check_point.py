from rest_framework import serializers


class CheckPointSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255)
    project = serializers.CharField(max_length=255)
    is_stage = serializers.BooleanField(read_only=True)
    stage = serializers.CharField(max_length=255, allow_null=True)

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
