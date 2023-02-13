from rest_framework import serializers
from user_api.models import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:

        model = Role
        read_only_fields = (
            'id',
            'created_at',
            'updated_at'
        )
        fields = [
            'id',
            'name',
            'priority',
            'updated_by',
            'updated_at',
            'created_by',
            'created_at'
        ]
