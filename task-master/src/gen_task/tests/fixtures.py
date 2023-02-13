import datetime
import pytest
from pytz import UTC

from gen_task.models import Type, Status
from gen_task.tests.fixtures_factory import (
    CheckPointFactory,
    TaskFactory
)

_ = pytest.fixture(autouse=True)(lambda db: None)


@pytest.fixture()
def close_task():
    check_point = CheckPointFactory.create(
        started_at=datetime.datetime(2022, 1, 1, tzinfo=UTC),
        planned_ended_at=datetime.datetime(2022, 1, 30, tzinfo=UTC),
    )
    task = TaskFactory.create(
        started_at=datetime.datetime(2022, 1, 1, tzinfo=UTC),
        planned_ended_at=datetime.datetime(2022, 1, 10, tzinfo=UTC),
        check_point=check_point,
        updated_at=datetime.datetime(2022, 1, 1),
        created_at=datetime.datetime(2022, 1, 1),
        previous_task=None
    )
    TaskFactory.create(
        started_at=datetime.datetime(2022, 1, 20, tzinfo=UTC),
        planned_ended_at=datetime.datetime(2022, 1, 30, tzinfo=UTC),
        check_point=check_point,
        previous_task=None
    )
    CheckPointFactory.create(
        project=check_point.project,
        started_at=datetime.datetime(2022, 2, 1, tzinfo=UTC),
        planned_ended_at=datetime.datetime(2022, 2, 10, tzinfo=UTC),
        updated_at=datetime.datetime(2022, 1, 1),
        created_at=datetime.datetime(2022, 1, 1)
    )
    return task


@pytest.fixture()
def parent_task_object():
    check_point = CheckPointFactory.create(
        started_at=datetime.datetime(2022, 1, 1, tzinfo=UTC),
        planned_ended_at=datetime.datetime(2022, 1, 30, tzinfo=UTC),
        updated_at=datetime.datetime(2022, 1, 1),
        created_at=datetime.datetime(2022, 1, 1),
    )
    task = TaskFactory.create(
        is_task_agreement=True,
        started_at=datetime.datetime(2022, 1, 1, tzinfo=UTC),
        planned_ended_at=datetime.datetime(2022, 1, 10, tzinfo=UTC),
        check_point=check_point,
        updated_at=datetime.datetime(2022, 1, 1),
        created_at=datetime.datetime(2022, 1, 1),
        previous_task=None
    )
    return task


@pytest.fixture()
def append_reviewer():
    check_point = CheckPointFactory.create(
        started_at=datetime.datetime(2022, 1, 1, tzinfo=UTC),
        planned_ended_at=datetime.datetime(2022, 1, 30, tzinfo=UTC),
        updated_at=datetime.datetime(2022, 1, 1),
        created_at=datetime.datetime(2022, 1, 1),
    )
    task = TaskFactory.create(
        is_selected_reviewer=True,
        is_task_agreement=True,
        started_at=datetime.datetime(2022, 1, 1, tzinfo=UTC),
        planned_ended_at=datetime.datetime(2022, 1, 10, tzinfo=UTC),
        check_point=check_point,
        updated_at=datetime.datetime(2022, 1, 1),
        created_at=datetime.datetime(2022, 1, 1),
        previous_task=None
    )
    task2 = TaskFactory.create(
        is_selected_reviewer=False,
        is_task_agreement=True,
        started_at=datetime.datetime(2022, 1, 1, tzinfo=UTC),
        planned_ended_at=datetime.datetime(2022, 1, 10, tzinfo=UTC),
        check_point=check_point,
        updated_at=datetime.datetime(2022, 1, 1),
        created_at=datetime.datetime(2022, 1, 1),
        previous_task=None
    )
    return [task, task2]


@pytest.fixture()
def task_return_to_revision():
    check_point = CheckPointFactory.create(
        started_at=datetime.datetime(2022, 1, 1, tzinfo=UTC),
        planned_ended_at=datetime.datetime(2022, 1, 30, tzinfo=UTC),
        updated_at=datetime.datetime(2022, 1, 1),
        created_at=datetime.datetime(2022, 1, 1),
    )
    task = TaskFactory.create(
        is_selected_reviewer=True,
        is_task_agreement=True,
        status=Status.processing,
        started_at=datetime.datetime(2022, 1, 1, tzinfo=UTC),
        planned_ended_at=datetime.datetime(2022, 1, 10, tzinfo=UTC),
        check_point=check_point,
        updated_at=datetime.datetime(2022, 1, 1),
        created_at=datetime.datetime(2022, 1, 1),
        previous_task=None
    )
    agreement_task = TaskFactory.create(
        name=f"Agreement: {task.name}",
        is_selected_reviewer=False,
        is_task_agreement=False,
        reviewers=task.reviewers,
        status=Status.on_review,
        started_at=datetime.datetime(2022, 1, 1, tzinfo=UTC),
        planned_ended_at=datetime.datetime(2022, 1, 10, tzinfo=UTC),
        type=Type.assignment,
        check_point=task.check_point,
        updated_at=datetime.datetime(2022, 1, 1),
        created_at=datetime.datetime(2022, 1, 1),
        previous_task=task
    )
    return agreement_task
