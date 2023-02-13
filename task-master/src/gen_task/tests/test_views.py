from datetime import datetime, timezone
from django.urls import reverse
from freezegun import freeze_time
from pytz import UTC

from gen_task.models import Task, CheckPoint, Status


@freeze_time("2022, 1, 30")
def test_views_close_task(close_task, admin_client):
    response = admin_client.post(reverse('gen_task:task-close-task', kwargs={'pk': str(close_task.id)}))
    time_delta = datetime.now(timezone.utc) - close_task.planned_ended_at
    planned_ended_check_point = CheckPoint.objects.get(planned_ended_at=datetime(2022, 3, 2, tzinfo=UTC))
    planned_ended_task = [x.planned_ended_at for x in Task.objects.exclude(id=close_task.id)]
    time_check_point_planned_end = planned_ended_check_point.planned_ended_at - time_delta
    time_task_planned_end = planned_ended_task[0] - time_delta
    assert response.status_code == 200
    assert time_task_planned_end == datetime(2022, 1, 30, tzinfo=UTC)
    assert time_check_point_planned_end == datetime(2022, 2, 10, tzinfo=UTC)


@freeze_time(datetime.now())
def test_close_agreement_task(parent_task_object, admin_client):
    response = admin_client.post(reverse('gen_task:task-close-task', kwargs={'pk': str(parent_task_object.id)}))
    agreement_to_close_object = Task.objects.get(name=f'Agreement: {parent_task_object.name}')
    admin_client.post(reverse('gen_task:task-close-task', kwargs={'pk': str(agreement_to_close_object.id)}))
    agreement_to_close_object = Task.objects.get(name=f'Agreement: {parent_task_object.name}')
    parent_task_object = Task.objects.get(id=parent_task_object.id)
    assert parent_task_object.status == Status.finished
    assert agreement_to_close_object.status == Status.finished
    assert parent_task_object.ended_at == datetime.now(timezone.utc)
    assert agreement_to_close_object.ended_at == datetime.now(timezone.utc)


@freeze_time(datetime.now())
def test_append_reviewer(append_reviewer, admin_client):
    admin_client.post(reverse('gen_task:task-close-task', kwargs={'pk': str(append_reviewer[0].id)}))
    agreement_to_close_object1 = Task.objects.get(name=f'Agreement: {append_reviewer[0].name}')
    admin_client.post(reverse('gen_task:task-close-task', kwargs={'pk': str(agreement_to_close_object1.id)}))

    admin_client.post(reverse('gen_task:task-close-task', kwargs={'pk': str(append_reviewer[1].id)}))
    agreement_to_close_object2 = Task.objects.get(name=f'Agreement: {append_reviewer[1].name}')
    admin_client.post(reverse('gen_task:task-close-task', kwargs={'pk': str(agreement_to_close_object2.id)}))
    assert agreement_to_close_object1.created_by in agreement_to_close_object1.reviewers
    assert agreement_to_close_object2.created_by not in agreement_to_close_object2.reviewers


@freeze_time(datetime.now())
def test_task_return_to_revision(task_return_to_revision, admin_client):
    response = admin_client.post(reverse('gen_task:task-close-task', kwargs={'pk': str(task_return_to_revision.id)}))
    parent_task = Task.objects.get(id=task_return_to_revision.previous_task_id)
    assert response.status_code == 200
    assert parent_task.status == Status.returned
