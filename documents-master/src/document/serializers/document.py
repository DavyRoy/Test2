from rest_framework import serializers
from document.models import Document
from document.services import GeneratorPreviewJpeg


class DocumentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        file = validated_data.get('file', None)
        validated_data['preview_image'] = GeneratorPreviewJpeg(file.file)()
        return super().create(validated_data)

    class Meta:
        model = Document
        read_only_fields = (
            'id',
            'preview_image',
            'updated_at',
            'created_at'
        )
        fields = [
            'id',
            'name_document',
            'type',
            'file',
            'preview_image',
            'is_archive',
            'created_by',
            'updated_by',
            'updated_at',
            'created_at'
        ]
