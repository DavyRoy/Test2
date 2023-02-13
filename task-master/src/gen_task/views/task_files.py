from drf_yasg.openapi import Parameter, IN_QUERY, TYPE_STRING, TYPE_ARRAY, Items, TYPE_OBJECT, Schema, TYPE_INTEGER, \
    TYPE_BOOLEAN
from drf_yasg.utils import swagger_auto_schema

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from gen_task.models import TaskFile
from gen_task.serializers import TaskFilesSerializer


class TaskFilesViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       mixins.DestroyModelMixin,
                       GenericViewSet):

    serializer_class = TaskFilesSerializer
    queryset = TaskFile.objects.all()
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[], request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'name': Schema(type=TYPE_STRING, title='task_file_name'),
            'file_id': Schema(type=TYPE_STRING, title='file_id'),
            'task': Schema(type=TYPE_STRING, title='task_files'),
            'created_by': Schema(type=TYPE_STRING, title='created_by'),
        }, required=['name', 'file_id', 'task', 'created_by']
    ), responses={201: TaskFilesSerializer})
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[], request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'name': Schema(type=TYPE_STRING, title='task_file_name'),
            'file_id': Schema(type=TYPE_STRING, title='file_id'),
            'task': Schema(type=TYPE_STRING, title='task_files'),
            'updated_by': Schema(type=TYPE_STRING, title='updated_by'),
        }, required=['updated_by']
    ), responses={200: TaskFilesSerializer})
    def partial_update(self, request, pk=None, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
