from drf_yasg.openapi import TYPE_ARRAY, TYPE_BOOLEAN, TYPE_INTEGER, TYPE_OBJECT, TYPE_STRING, Items, Schema, TYPE_FILE

TASK_CREATE_REQUEST_BODY = Schema(
    type=TYPE_OBJECT,
    properties={
        'name': Schema(type=TYPE_STRING, title='task_name'),
        'description': Schema(type=TYPE_STRING, title='description'),
        'priority': Schema(type=TYPE_INTEGER, title='priority', description='0 - High, 1 - Medium, 2 - Low'),
        'check_point': Schema(type=TYPE_STRING, title='check_point'),
        'previous_task': Schema(type=TYPE_STRING, title='previous_task'),
        'next_task': Schema(type=TYPE_STRING, title='next_task'),
        'project': Schema(type=TYPE_STRING, title='project'),
        'is_selected_reviewer': Schema(type=TYPE_BOOLEAN, title='is_selected_reviewer'),
        'is_task_agreement': Schema(type=TYPE_BOOLEAN, title='is_task_agreement'),
        'reviewers': Schema(type=TYPE_ARRAY, items=Items(type=TYPE_STRING), title='reviewers'),
        'responsible': Schema(type=TYPE_ARRAY, items=Items(type=TYPE_STRING), title='responsible'),
        'members': Schema(type=TYPE_ARRAY, items=Items(type=TYPE_STRING), title='members'),
        'executor': Schema(type=TYPE_STRING, title='executor'),
        'observers': Schema(type=TYPE_ARRAY, items=Items(type=TYPE_STRING), title='observers'),
        'status': Schema(type=TYPE_INTEGER, title='status',
                         description='0 - Created, 1 - Processing, 2 - On pause, 3 - On review 4 - Returned, 5 - Agreed, 6 - Finished'),
        'type': Schema(type=TYPE_INTEGER, title='type',
                       description='0 - Issue, 1 - Assignment, 2 - Agreement, 3 - SOS'),
        'started_at': Schema(type=TYPE_STRING, title='started_at'),
        'planned_ended_at': Schema(type=TYPE_STRING, title='planned_ended_at'),
        'ended_at': Schema(type=TYPE_STRING, title='ended_at'),
        'sub_tasks': Schema(type=TYPE_ARRAY, items=Items(type=TYPE_STRING), title='sub_tasks'),
    }, required=['name', 'description', 'priority', 'executor', 'status', 'type', 'started_at',
                 'planned_ended_at']
)

TASK_PARTIAL_UPDATE_REQUEST_BODY = Schema(
    type=TYPE_OBJECT,
    properties={
        'name': Schema(type=TYPE_STRING, title='task_name'),
        'description': Schema(type=TYPE_STRING, title='description'),
        'priority': Schema(type=TYPE_INTEGER, title='priority', description='0 - High, 1 - Medium, 2 - Low'),
        'check_point': Schema(type=TYPE_STRING, title='check_point'),
        'previous_task': Schema(type=TYPE_STRING, title='previous_task'),
        'next_task': Schema(type=TYPE_STRING, title='next_task'),
        'project': Schema(type=TYPE_STRING, title='project'),
        'is_selected_reviewer': Schema(type=TYPE_BOOLEAN, title='is_selected_reviewer'),
        'is_task_agreement': Schema(type=TYPE_BOOLEAN, title='is_task_agreement'),
        'reviewers': Schema(type=TYPE_ARRAY, items=Items(type=TYPE_STRING), title='reviewers'),
        'responsible': Schema(type=TYPE_ARRAY, items=Items(type=TYPE_STRING), title='responsible'),
        'executor': Schema(type=TYPE_STRING, title='executor'),
        'observers': Schema(type=TYPE_ARRAY, items=Items(type=TYPE_STRING), title='observers'),
        'status': Schema(type=TYPE_INTEGER, title='status',
                         description='0 - Created, 1 - Processing, 2 - On pause, 3 - On review 4 - Returned, 5 - Agreed, 6 - Finished'),
        'type': Schema(type=TYPE_INTEGER, title='type',
                       description='0 - Issue, 1 - Assignment, 2 - Agreement, 3 - SOS'),
        'started_at': Schema(type=TYPE_STRING, title='started_at'),
        'planned_ended_at': Schema(type=TYPE_STRING, title='planned_ended_at'),
        'ended_at': Schema(type=TYPE_STRING, title='ended_at'),
    }
)

TASK_CHANGE_STATUS_REQUEST_BODY = Schema(
    type=TYPE_OBJECT,
    properties={
        'status': Schema(type=TYPE_INTEGER, title='status',
                         description='0 - Created, 1 - Processing, 2 - On pause, 3 - On review 4 - Returned, 5 - Agreed, 6 - Finished'),
    }, required=['status']
)


CHECKPOINT_CREATE_REQUEST_BODY = Schema(
    type=TYPE_OBJECT,
    properties={
        'name': Schema(type=TYPE_STRING, title='check_point_name'),
        'project': Schema(type=TYPE_STRING, title='project'),
        'description': Schema(type=TYPE_STRING, title='description'),
        'executor': Schema(type=TYPE_STRING, title='executor'),
        'observers': Schema(type=TYPE_ARRAY, items=Items(type=TYPE_STRING), title='observers'),
        'priority': Schema(type=TYPE_INTEGER, title='priority', description='0 - High, 1 - Medium, 2 - Low'),
        'status': Schema(type=TYPE_INTEGER, title='status',
                         description='0 - Created, 1 - Processing, 2 - On pause, 3 - On review 4 - Returned, 5 - Finished'),
        'started_at': Schema(type=TYPE_STRING, title='started_at'),
        'planned_ended_at': Schema(type=TYPE_STRING, title='planned_ended_at'),
        'ended_at': Schema(type=TYPE_STRING, title='ended_at'),
    }, required=['name', 'project', 'description', 'executor', 'priority', 'status', 'started_at',
                 'planned_ended_at']
)

CHECKPOINT_PARTIAL_UPDATE_REQUEST_BODY = Schema(
    type=TYPE_OBJECT,
    properties={
        'name': Schema(type=TYPE_STRING, title='check_point_name'),
        'project': Schema(type=TYPE_STRING, title='project'),
        'description': Schema(type=TYPE_STRING, title='description'),
        'executor': Schema(type=TYPE_STRING, title='executor'),
        'observers': Schema(type=TYPE_ARRAY, items=Items(type=TYPE_STRING), title='observers'),
        'priority': Schema(type=TYPE_INTEGER, title='priority', description='0 - High, 1 - Medium, 2 - Low'),
        'status': Schema(type=TYPE_INTEGER, title='status',
                         description='0 - Created, 1 - Processing, 2 - On pause, 3 - On review 4 - Returned, 5 - Finished'),
        'started_at': Schema(type=TYPE_STRING, title='started_at'),
        'planned_ended_at': Schema(type=TYPE_STRING, title='planned_ended_at'),
        'ended_at': Schema(type=TYPE_STRING, title='ended_at'),
    }
)

COMMENT_TASK_CREATE_REQUEST_BODY = Schema(
    type=TYPE_OBJECT,
    properties={
        'text': Schema(type=TYPE_STRING, title='text'),
        'task': Schema(type=TYPE_STRING, title='task_comments'),
    }, required=['text', 'task']
)

COMMENT_TASK_PARTIAL_UPDATE_REQUEST_BODY = Schema(
    type=TYPE_OBJECT,
    properties={
        'text': Schema(type=TYPE_STRING, title='text'),
        'task': Schema(type=TYPE_STRING, title='task_comments')
    }
)

SUB_TASK_CREATE_REQUEST_BODY = Schema(
    type=TYPE_OBJECT,
    properties={
        'name': Schema(type=TYPE_STRING, title='sub_task_name'),
        'task': Schema(type=TYPE_STRING, title='sub_tasks'),
        'is_completed': Schema(type=TYPE_BOOLEAN, title='is_completed'),
    }, required=['name', 'task', 'is_completed']
)

SUB_TASK_PARTIAL_UPDATE_REQUEST_BODY = Schema(
    type=TYPE_OBJECT,
    properties={
        'name': Schema(type=TYPE_STRING, title='sub_task_name'),
        'task': Schema(type=TYPE_STRING, title='sub_tasks'),
        'is_completed': Schema(type=TYPE_BOOLEAN, title='is_completed'),

    }
)

TASK_FILES_CREATE_REQUEST_BODY = Schema(
    type=TYPE_OBJECT,
    properties={
        'name': Schema(type=TYPE_STRING, title='task_file_name'),
        'file': Schema(type=TYPE_FILE, title='file'),
        'task': Schema(type=TYPE_STRING, title='task_files'),
    }, required=['name', 'file_id', 'task']
)

TASK_FILES_PARTIAL_UPDATE_REQUEST_BODY = Schema(
    type=TYPE_OBJECT,
    properties={
        'name': Schema(type=TYPE_STRING, title='task_file_name'),
        'file_id': Schema(type=TYPE_STRING, title='file_id'),
        'task': Schema(type=TYPE_STRING, title='task_files'),
    }
)
