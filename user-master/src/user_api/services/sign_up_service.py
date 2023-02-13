import json

from user_api.models import User, Role
from user_api.serializers import UserSerializer
from user_api.services import redis_client


class SignUpService:
    def __init__(self, validated_data: dict):
        self.validated_data = validated_data

    def __call__(self, *args, **kwargs):
        user = self.create_user()
        return user

    def create_user(self):
        default_role = Role.objects.get(is_default=True)

        user = User.objects.create(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )
        user.role.add(default_role)
        user.set_password(self.validated_data['password'])
        user.save()
        redis_client.set(name=str(user.id), value=json.dumps(UserSerializer(user).data, indent=4, sort_keys=True, default=str))

        return user
