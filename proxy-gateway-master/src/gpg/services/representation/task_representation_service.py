
from gpg.services.user_service import UserService


class TaskRepresentationService:
    def __init__(self, task_representation: dict):
        self.task_representation = task_representation
        self.single_user_fields = ('executor', 'updated_by', 'created_by')
        self.list_user_fields = ('observers', 'members', 'responsible', 'reviewers')
        self.nested_task_field = ('task_comments', 'task_files', 'sub_tasks')

    def __call__(self, *args, **kwargs):
        self.process()
        return self.task_representation

    @staticmethod
    def _get_user(user_id: str) -> dict:
        return UserService(user_id)()

    def reveal_user_by_field(self, field: str) -> None:
        if (user := self.task_representation.get(field, None)) is not None:
            self.task_representation[field] = self._get_user(user)

    def reveal_many_users_by_field(self, field: str) -> None:
        if (users := self.task_representation.get(field, None)) is not None:
            if len(users) != 0:
                self.task_representation[field] = [self._get_user(user) for user in users]

    def reveal_nested_users_by_field(self, field: str) -> None:
        if (nested_task_field_value := self.task_representation.get(field, None)) is not None:
            if len(nested_task_field_value) != 0:
                for obj in nested_task_field_value:
                    if (user := obj.get('created_by', None)) is not None:
                        obj['created_by'] = self._get_user(user)

                    if (user := obj.get('updated_by', None)) is not None:
                        obj['updated_by'] = self._get_user(user)

    def reveal_single_users(self) -> None:
        for field in self.single_user_fields:
            self.reveal_user_by_field(field)

    def reveal_list_users(self):
        for field in self.list_user_fields:
            self.reveal_many_users_by_field(field)

    def reveal_nested_users(self):
        for field in self.nested_task_field:
            self.reveal_nested_users_by_field(field)


    def process(self):
        self.reveal_single_users()
        self.reveal_list_users()
        #self.reveal_nested_users()


