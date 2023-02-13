from datetime import datetime, timezone
from freezegun import freeze_time
from pytz import UTC

from gen_task.models import Task, CheckPoint, Status
from gen_task.services import CloseTaskService


@freeze_time("2022, 1, 30")
def test_services_close_task(close_task):
    service = CloseTaskService()
    service.process(close_task)
    time_delta = datetime.now(timezone.utc) - close_task.planned_ended_at
    planned_ended_check_point = CheckPoint.objects.get(planned_ended_at=datetime(2022, 3, 2, tzinfo=UTC))
    planned_ended_task = [x.planned_ended_at for x in Task.objects.exclude(id=close_task.id)]
    time_check_point_planned_end = planned_ended_check_point.planned_ended_at - time_delta
    time_task_planned_end = planned_ended_task[0] - time_delta
    assert time_task_planned_end == datetime(2022, 1, 30, tzinfo=UTC)
    assert time_check_point_planned_end == datetime(2022, 2, 10, tzinfo=UTC)


@freeze_time(datetime.now())
def test_close_agreement_task(parent_task_object):
    service = CloseTaskService()
    service.process(parent_task_object)
    agreement_to_close_object = Task.objects.get(name=f'Agreement: {parent_task_object.name}')
    service.process(agreement_to_close_object)
    agreement_to_close_object = Task.objects.get(name=f'Agreement: {parent_task_object.name}')
    parent_task_object = Task.objects.get(id=parent_task_object.id)
    assert parent_task_object.status == Status.finished
    assert agreement_to_close_object.status == Status.finished
    assert parent_task_object.ended_at == datetime.now(timezone.utc)
    assert agreement_to_close_object.ended_at == datetime.now(timezone.utc)


@freeze_time(datetime.now())
def test_append_reviewer(append_reviewer):
    service = CloseTaskService()
    service.process(append_reviewer[0])
    agreement_to_close_object1 = Task.objects.get(name=f'Agreement: {append_reviewer[0].name}')
    service.process(agreement_to_close_object1)
    service.process(append_reviewer[1])
    agreement_to_close_object2 = Task.objects.get(name=f'Agreement: {append_reviewer[1].name}')
    service.process(agreement_to_close_object2)
    assert agreement_to_close_object1.created_by in agreement_to_close_object1.reviewers
    assert agreement_to_close_object2.created_by not in agreement_to_close_object2.reviewers


@freeze_time(datetime.now())
def test_task_return_to_revision(task_return_to_revision):
    service = CloseTaskService()
    service.process(task_return_to_revision)
    parent_task = Task.objects.get(id=task_return_to_revision.previous_task_id)
    assert parent_task.status == Status.returned
