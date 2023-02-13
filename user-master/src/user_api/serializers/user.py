from rest_framework import serializers
from user_api.models import User


class UserSerializer(serializers.ModelSerializer):
    role = serializers.UUIDField(source='role.id', allow_null=True)
    
    class Meta:

        model = User
        read_only_fields = (
            'id',
            'created_at',
            'updated_at'
        )
        fields = [
                  'id',
                  'avatar',
                  'role',
                  'first_name',
                  'last_name',
                  'username',
                  'kpi',
                  'phone',
                  'email',
                  'updated_by',
                  'updated_at',
                  'created_by',
                  'created_at'
        ]
