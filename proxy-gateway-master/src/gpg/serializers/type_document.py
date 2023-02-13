from rest_framework import serializers


class TypeDocumentSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255)
    activity = serializers.BooleanField(required=False)
    updated_by = serializers.CharField(max_length=55, required=False)
    created_by = serializers.CharField(max_length=55, required=False)
    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
