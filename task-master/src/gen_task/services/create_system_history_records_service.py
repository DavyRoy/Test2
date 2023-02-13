from gen_task.models import CommentTask, Task
from babel.dates import format_datetime


class CreateSystemHistoryRecordsService:
    def __init__(self, task: Task = None, fields=None) -> None:
        self.task = task
        self.fields = fields
        self.text: str = ''

        self.validate_fields()

    def __call__(self) -> None:
        self.statuses = {
            0: 'Создана',
            1: 'В работе',
            2: 'На паузе',
            3: 'На проверке',
            4: 'Возвращена',
            5: 'Согласована',
            6: 'Завершена'
        }
        self.priorities = {
            0: 'Высокий',
            1: 'Средний',
            2: 'Низкий',
        }
        self.types = {
            0: 'Задача',
            1: 'Поручение',
            2: 'Согласование',
            3: 'SOS'
        }
        if len(self.fields) != 0:
            self.generate_system_comment_text()
            if self.text:
                self.process()

    def validate_fields(self) -> None:

        self.fields.pop('created_at', None)
        self.fields.pop('created_by', None)
        self.fields.pop('updated_at', None)
        self.fields.pop('updated_by', None)
        self.fields.pop('task_analytic_data', None)

    def get_enum_fields(self, enum_dict, name, value) -> (str, str):
        old_value = enum_dict[getattr(self.task, name)]
        field_value = enum_dict[value]
        return old_value, field_value

    def generate_system_comment_text(self) -> str:

        for field_name, field_value in self.fields.items():

            old_value = getattr(self.task, field_name)

            if old_value != field_value:

                match field_name:
                    case 'status':
                        self.text += f'Поставил статус `{self.statuses[field_value]}`, '

                    case 'type':
                        # old_value, field_value = self.get_enum_fields(self.types, 'type', field_value)
                        self.text += f'Поставил тип `{self.types[field_value]}`, '

                    case 'priority':
                        # old_value, field_value = self.get_enum_fields(self.priorities, 'priority', field_value)
                        self.text += f'Поставил приоритет `{self.priorities[field_value]}`, '

                    case 'started_at' | 'planned_ended_at' | 'ended_at':
                        old_value = format_datetime(old_value, locale='ru_RU')
                        field_value = format_datetime(field_value, locale='ru_RU')
                        self.text += f'Изменил поле `{getattr(Task, field_name).field.verbose_name}` с `{old_value}` на `{field_value}`, '

                    case 'is_selected_reviewer':
                        localize_boolead = lambda field: 'Да' if field else 'Нет'

                        old_value = localize_boolead(old_value)
                        field_value = localize_boolead(field_value)
                        self.text += f'Изменил поле `{getattr(Task, field_name).field.verbose_name}` с `{old_value}` на `{field_value}`, '

                    case 'project':
                        self.text += f'Изменил `{getattr(Task, field_name).field.verbose_name}`, '

                    case 'reviewers' | 'observers' | 'responsible' | 'members' | 'executor':
                        self.text += f'Изменил поле `{getattr(Task, field_name).field.verbose_name}` , '

                    case _:
                        self.text += f'Изменил поле `{getattr(Task, field_name).field.verbose_name}` с `{old_value}` на `{field_value}`, '

        self.text = f'{self.text[:-2]}.' if len(self.text) != 0 else ''

    def create_task_notification(self):
        self.text = 'Создал эту задачу'
        self.process()

    def process(self) -> None:
        CommentTask.objects.create(
            text=self.text,
            task=self.task,
            is_system_comment=True,
            created_by=self.task.updated_by if self.task.updated_by is not None else self.task.created_by
        )
