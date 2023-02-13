import uuid
import factory
from django.utils import timezone
from factory import Faker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from gen_task.models import CheckPoint, Task, SubTask, CommentTask, TaskFile, Status, Type, Priority, BasicModel


class BasicModelFactory(DjangoModelFactory):
    id = Faker('uuid4')
    name = Faker('name')
    updated_by = Faker('uuid4')
    updated_at = Faker('date_time')
    created_by = Faker('uuid4')
    created_at = timezone.now()

    class Meta:
        model = BasicModel


class CheckPointFactory(BasicModelFactory):
    project = Faker('word')
    stage = factory.SubFactory('gen_task.tests.fixtures_factory.CheckPointFactory')
    is_stage = False
    description = Faker('text')
    executor = Faker('uuid4')
    observers = factory.List(str(uuid.uuid4()) for _ in range(3))
    priority = FuzzyChoice(Priority)
    status = FuzzyChoice(Status)
    started_at = Faker('date_time')
    planned_ended_at = Faker('date_time')
    ended_at = None

    class Meta:
        model = CheckPoint


class TaskFactory(BasicModelFactory):
    description = Faker('text')
    check_point = factory.SubFactory(CheckPointFactory)
    executor = Faker('uuid4')
    reviewers = factory.List(str(uuid.uuid4()) for _ in range(3))
    observers = factory.List(str(uuid.uuid4()) for _ in range(3))
    responsible = factory.List(str(uuid.uuid4()) for _ in range(3))
    priority = FuzzyChoice(Priority)
    status = FuzzyChoice(Status)
    type = FuzzyChoice(Type)
    previous_task = factory.SubFactory('gen_task.tests.fixtures_factory.TaskFactory')
    is_selected_reviewer = False
    is_task_agreement = False
    started_at = Faker('date_time')
    planned_ended_at = Faker('date_time')
    ended_at = None

    class Meta:
        model = Task


class SubTaskFactory(BasicModelFactory):
    task = factory.SubFactory(TaskFactory)
    is_completed = False

    class Meta:
        model = SubTask


class CommentTaskFactory(BasicModelFactory):
    text = Faker('text')
    task = factory.SubFactory(TaskFactory)

    class Meta:
        model = CommentTask


class TaskFileFactory(BasicModelFactory):
    file_id = Faker('uuid4')
    task = factory.SubFactory(TaskFactory)

    class Meta:
        model = TaskFile
