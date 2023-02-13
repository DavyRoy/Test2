from drf_yasg.openapi import IN_PATH, IN_QUERY, TYPE_STRING, Parameter

ID_IN_PATH = [Parameter('id', IN_PATH, required=True, type=TYPE_STRING)]

TASK_PARAMETERS = [
        Parameter('ordering', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('executors', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('check_points', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('priority', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('status', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('type', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('planned_ended_at_before', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('planned_ended_at_after', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('started_at_before', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('started_at_after', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('overdue', IN_QUERY, required=False, type=TYPE_STRING,
                  description='actually type boolean `true` or `false`'),
        Parameter('deadline', IN_QUERY, required=False, type=TYPE_STRING,
                  description='actually type boolean `true` or `false`'),
        Parameter('stage', IN_QUERY, required=False, type=TYPE_STRING,
                  description='UUID of checkpoint with `is_stage=True`'),
        Parameter('project', IN_QUERY, required=False, type=TYPE_STRING),

        Parameter('end_date', IN_QUERY, required=False, type=TYPE_STRING),
    ]

CHECKPOINT_PARAMETERS = [
        Parameter('project', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('executors', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('priority', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('status', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('date_range', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('end_date', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('order_by', IN_QUERY, required=False, type=TYPE_STRING),
    ]