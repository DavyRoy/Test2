from gpg.services.user_service import UserService


class CommentTaskRepresentationService:
    def __init__(self, comment_task_representation: dict):
        self.comment_task_representation = comment_task_representation
        self.single_user_fields = ('updated_by', 'created_by')

    def __call__(self, *args, **kwargs):
        self.process()
        return self.comment_task_representation

    @staticmethod
    def _get_user(user_id: str) -> dict:
        return UserService(user_id)()

    def reveal_user_by_field(self, field: str) -> None:
        if (user := self.comment_task_representation.get(field, None)) is not None:
            self.comment_task_representation[field] = self._get_user(user)

    def reveal_single_users(self) -> None:
        for field in self.single_user_fields:
            self.reveal_user_by_field(field)

    def process(self):
        self.reveal_single_users()
