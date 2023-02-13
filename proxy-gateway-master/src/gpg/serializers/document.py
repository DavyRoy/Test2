from rest_framework import serializers


class DocumentSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name_document = serializers.CharField(max_length=255)
    type = serializers.UUIDField()
    preview_image = serializers.ImageField(read_only=True)
    file = serializers.FileField(read_only=True)
    is_archive = serializers.BooleanField(required=False)
    updated_by = serializers.CharField(max_length=55, required=False)
    created_by = serializers.CharField(max_length=55, required=False)
    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
