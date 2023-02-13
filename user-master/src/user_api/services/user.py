from user_api.models import User


class UserModelService:

    @staticmethod
    def create_user(**kwargs):
        created_user = User.objects.create(**kwargs)
        return created_user

    @staticmethod
    def update_user(task: User, **kwargs):
        updated_user = User.objects.filter(pk=task.pk).update(**kwargs)
        return updated_user