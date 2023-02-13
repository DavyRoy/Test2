import django_filters as filters
from django.utils import timezone
from django.db.models import F
from gen_task.models import Priority, Status, Type, Task


def filter_overdue(queryset, field_name, value):
    if value:

        return queryset.filter(planned_ended_at__lt=timezone.now(), ended_at__isnull=True)

    else:

        return queryset.filter(planned_ended_at__gt=timezone.now(), ended_at__isnull=True)


def filter_tasks_by_stage(queryset, field_name, value):

    return queryset.filter(check_point__stage__id=value)


def order_tasks_by_deadline(queryset, field_name, flag):
    if flag:

        return queryset.annotate(deadline=timezone.now() - F(field_name)).order_by('-deadline')

    return queryset


class TaskFilter(filters.FilterSet):
    check_point_name = filters.CharFilter(field_name='check_point__name', lookup_expr='icontains')
    executor = filters.CharFilter(field_name='executor', lookup_expr='icontains')
    started_at = filters.DateTimeFromToRangeFilter(field_name='started_at')
    planned_ended_at = filters.DateTimeFromToRangeFilter(field_name='planned_ended_at')
    stage = filters.CharFilter(field_name='check_point__stage__id', lookup_expr='icontains')
    deadline = filters.BooleanFilter(field_name='planned_ended_at', method=order_tasks_by_deadline, label='order_by_deadline')
    project = filters.CharFilter(field_name='project', lookup_expr='icontains')
    overdue = filters.BooleanFilter(field_name='planned_ended_at', method=filter_overdue, label='overdue')
    status = filters.ChoiceFilter(choices=Status.choices)
    priority = filters.ChoiceFilter(choices=Priority.choices)
    type = filters.ChoiceFilter(choices=Type.choices)
    order_by = filters.OrderingFilter(fields=(
        ('priority', 'priority'),
        ('status', 'status'),
        ('type', 'type'),
        ('check_point', 'check_point'),
        ('started_at', 'started'),
        ('planned_ended_at', 'planned_ended'),
        ('ended_at', 'ended'),
    ))

    class Meta:
        model = Task
        fields = ['status', 'priority', 'type']
