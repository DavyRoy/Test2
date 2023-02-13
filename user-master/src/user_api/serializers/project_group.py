from rest_framework import serializers
from user_api.models import ProjectGroup


class ProjectGroupSerializer(serializers.ModelSerializer):

    class Meta:

        model = ProjectGroup
        read_only_fields = (
            'id',
            'created_at',
            'updated_at'
        )
        fields = [
            'id',
            'name',
            'users',
            'updated_by',
            'updated_at',
            'created_by',
            'created_at'
        ]
