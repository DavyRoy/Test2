from gpg.services.user_service import UserService


class CheckPointRepresentationService:
    def __init__(self, check_point_representation: dict):
        self.check_point_representation = check_point_representation
        self.single_user_fields = ('executor', 'updated_by', 'created_by')
        self.list_user_fields = ('observers', )

    def __call__(self, *args, **kwargs):
        self.process()
        return self.check_point_representation

    @staticmethod
    def _get_user(user_id: str) -> dict:
        return UserService(user_id)()

    def reveal_user_by_field(self, field: str) -> None:
        if (user := self.check_point_representation.get(field, None)) is not None:
            self.check_point_representation[field] = self._get_user(user)

    def reveal_many_users_by_field(self, field: str) -> None:
        if (users := self.check_point_representation.get(field, None)) is not None:
            if len(users) != 0:
                self.check_point_representation[field] = [self._get_user(user) for user in users]

    def reveal_single_users(self) -> None:
        for field in self.single_user_fields:
            self.reveal_user_by_field(field)

    def reveal_list_users(self):
        for field in self.list_user_fields:
            self.reveal_many_users_by_field(field)

    def process(self):
        self.reveal_single_users()
        self.reveal_list_users()
