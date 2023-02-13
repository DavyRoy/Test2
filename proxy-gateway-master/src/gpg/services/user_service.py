import json

from gpg.services.redis_service import redis_client
from wrappers.user_wrapper import UserApiWrapper

user_wrapper = UserApiWrapper()


class UserService:
    def __init__(self, user_id: str) -> None:
        self.user_id = user_id

    def __call__(self, *args, **kwargs):
        return self.process()

    def process(self) -> dict:
        if (cashed_user := redis_client.get(self.user_id)) is not None:
            return json.loads(cashed_user)

        user = user_wrapper(instance='user', view='read', id=self.user_id)
        redis_client.set(name=self.user_id, value=json.dumps(user, indent=4, sort_keys=True, default=str))
        return user



