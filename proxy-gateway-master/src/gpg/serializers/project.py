from rest_framework import serializers


class ProjectSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()

    class Meta:
        fields = [
            'id',
            'name',
        ]
