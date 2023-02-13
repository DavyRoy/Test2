from drf_yasg.openapi import Parameter, IN_QUERY, TYPE_STRING, TYPE_ARRAY, Items, TYPE_OBJECT, Schema, TYPE_INTEGER, \
    TYPE_BOOLEAN
from drf_yasg.utils import swagger_auto_schema

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from gen_task.models import SubTask
from gen_task.serializers import SubTaskSerializer


class SubTaskViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     GenericViewSet):

    serializer_class = SubTaskSerializer
    queryset = SubTask.objects.all()
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[], request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'name': Schema(type=TYPE_STRING, title='sub_task_name'),
            'task': Schema(type=TYPE_STRING, title='sub_tasks'),
            'is_completed': Schema(type=TYPE_BOOLEAN, title='is_completed'),
            'created_by': Schema(type=TYPE_STRING, title='created_by'),
            'executor': Schema(type=TYPE_STRING, title='sub_task_executor'),
        }, required=['name', 'task', 'is_completed', 'created_by']
    ), responses={201: SubTaskSerializer})
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[], request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'name': Schema(type=TYPE_STRING, title='sub_task_name'),
            'task': Schema(type=TYPE_STRING, title='sub_tasks'),
            'is_completed': Schema(type=TYPE_BOOLEAN, title='is_completed'),
            'updated_by': Schema(type=TYPE_STRING, title='updated_by'),
        }, required=['updated_by']
    ), responses={200: SubTaskSerializer})
    def partial_update(self, request, pk=None, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
