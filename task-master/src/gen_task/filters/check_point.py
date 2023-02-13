import django_filters as filters

from gen_task.models import Status, Priority, CheckPoint


class CheckPointFilter(filters.FilterSet):
    project = filters.CharFilter(field_name='project', lookup_expr='icontains')
    executor = filters.CharFilter(field_name='executor', lookup_expr='icontains')
    started_at = filters.DateTimeFromToRangeFilter(field_name='started_at')
    planned_ended_at = filters.DateTimeFromToRangeFilter(field_name='planned_ended_at')
    status = filters.ChoiceFilter(choices=Status.choices)
    priority = filters.ChoiceFilter(choices=Priority.choices)
    order_by = filters.OrderingFilter(fields=(
        ('priority', 'priority'),
        ('status', 'status'),
        ('started_at', 'started'),
        ('planned_ended_at', 'planned_ended'),
        ('ended_at', 'ended'),
    ))

    class Meta:
        model = CheckPoint
        fields = ['status', 'priority']
