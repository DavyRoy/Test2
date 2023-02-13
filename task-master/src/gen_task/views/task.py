import uuid

from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.openapi import Parameter, IN_QUERY, TYPE_STRING, TYPE_ARRAY, Items, TYPE_OBJECT, Schema, TYPE_INTEGER, \
    TYPE_BOOLEAN, IN_PATH
from drf_yasg.utils import swagger_auto_schema, no_body
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from gen_task.filters import TaskFilter
from gen_task.models import Task, CheckPoint, Status
from gen_task.serializers import TaskSerializer, CloseTaskSerializer, StatusChangeSerializer, ProjectSerializer


class TaskViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.exclude(status=Status.archived)
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter

    @swagger_auto_schema(manual_parameters=[
        Parameter('check_points', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('executors', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('planned_ended_at_before', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('planned_ended_at_after', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('started_at_before', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('started_at_after', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('overdue', IN_QUERY, required=False, type=TYPE_STRING, description='actually type boolean `true` or `false`'),
        Parameter('stage', IN_QUERY, required=False, type=TYPE_STRING,
                  description='UUID of checkpoint with `is_stage=True`'),

    ])
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(manual_parameters=[], request_body=Schema(
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
                             description='0 - Created, 1 - Processing, 2 - On pause, 3 - On review 4 - Returned, 5 - Finished'),
            'type': Schema(type=TYPE_INTEGER, title='type',
                           description='0 - Issue, 1 - Assignment, 2 - Agreement, 3 - SOS'),
            'started_at': Schema(type=TYPE_STRING, title='started_at'),
            'planned_ended_at': Schema(type=TYPE_STRING, title='planned_ended_at'),
            'ended_at': Schema(type=TYPE_STRING, title='ended_at'),
            'created_by': Schema(type=TYPE_STRING, title='created_by'),
        }, required=['name', 'description', 'priority', 'executor', 'status', 'type', 'started_at',
                     'planned_ended_at', 'created_by']
    ), responses={201: TaskSerializer,
                  400: Schema(type=TYPE_OBJECT, properties={'error': Schema(type=TYPE_STRING, title='some_error')})})
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[], request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'name': Schema(type=TYPE_STRING, title='task_name'),
            'description': Schema(type=TYPE_STRING, title='description'),
            'priority': Schema(type=TYPE_INTEGER, title='priority'),
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
            'status': Schema(type=TYPE_INTEGER, title='status'),
            'type': Schema(type=TYPE_INTEGER, title='type'),
            'started_at': Schema(type=TYPE_STRING, title='started_at'),
            'planned_ended_at': Schema(type=TYPE_STRING, title='planned_ended_at'),
            'ended_at': Schema(type=TYPE_STRING, title='ended_at'),
            'updated_by': Schema(type=TYPE_STRING, title='updated_by'),
        }, required=['updated_by']
    ), responses={200: TaskSerializer,
                  400: Schema(type=TYPE_OBJECT, properties={'error': Schema(type=TYPE_STRING, title='some_error')})})
    def partial_update(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        serializer = TaskSerializer(instance=instance, data=request.data, context={'pk': pk}, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data={'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(request_body=no_body, responses={200: TaskSerializer})
    @action(detail=True, methods=['post'])
    def close_task(self, request, pk=None):
        serializer = CloseTaskSerializer(data={'id': pk})
        if serializer.is_valid():
            serializer.save()
            task = self.get_object()
            serializer = TaskSerializer(task)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data={'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_queryset(self):
        queryset = self.queryset
        check_point = self.request.query_params.get('check_points')
        if check_point is not None:
            check_points = check_point.split(',')
            queryset = queryset.filter(check_point__id__in=check_points)
        executor = self.request.query_params.get('executors')
        if executor is not None:
            executors = executor.split(',')
            queryset = queryset.filter(executor__in=executors)
        return queryset

    @swagger_auto_schema(manual_parameters=[
        Parameter('id', IN_PATH, required=True, type=TYPE_STRING)
    ], request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'status': Schema(type=TYPE_INTEGER, title='status',
                             description='0 - Created, 1 - Processing, 2 - On pause, 3 - On review, 4 - Returned, 5 - Agreed, 6 - Finished')
        }), responses={200: TaskSerializer})
    @action(detail=True, methods=['post'])
    def change_status(self, request, pk=None):
        serializer = StatusChangeSerializer(data={'id': pk, **request.data})
        if serializer.is_valid():
            serializer.save()
            task = self.get_object()
            serializer = TaskSerializer(task)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data={'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(manual_parameters=[],operation_id='v1_task_get_all_projects',  request_body=no_body, responses={200: ProjectSerializer(many=True)})
    @action(detail=False, methods=['get'])
    def get_all_projects(self, request, pk=None):
        qs = self.queryset
        task_projects = qs.values_list('project', flat=True).distinct()
        checkpoint_projects = CheckPoint.objects.values_list('project', flat=True).distinct()
        projects = [{'id': uuid.uuid4(), 'name': project} for project in set(list(task_projects) + list(checkpoint_projects)) if project is not None]
        serializer = ProjectSerializer(data=projects, many=True)

        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)
