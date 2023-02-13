from rest_framework import serializers
from document.models import TypeDocument


class TypeDocumentSerializer(serializers.ModelSerializer):
    class Meta:

        model = TypeDocument
        read_only_fields = (
            'id',
            'updated_at',
            'created_at'
        )
        fields = [
            'id',
            'name',
            'activity',
            'created_by',
            'updated_by',
            'updated_at',
            'created_at'
        ]
