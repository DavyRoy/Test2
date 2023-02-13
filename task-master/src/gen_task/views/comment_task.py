from drf_yasg.openapi import Parameter, IN_QUERY, TYPE_STRING, TYPE_ARRAY, Items, TYPE_OBJECT, Schema, TYPE_INTEGER, \
    TYPE_BOOLEAN
from drf_yasg.utils import swagger_auto_schema

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from gen_task.models import CommentTask
from gen_task.serializers import CommentTaskSerializer


class CommentTaskViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         mixins.DestroyModelMixin,
                         GenericViewSet):

    serializer_class = CommentTaskSerializer
    queryset = CommentTask.objects.all()
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[], request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'text': Schema(type=TYPE_STRING, title='sub_task_name'),
            'task': Schema(type=TYPE_STRING, title='task_id'),
            'created_by': Schema(type=TYPE_STRING, title='created_by'),
        }, required=['text', 'task', 'created_by']
    ), responses={201: CommentTaskSerializer})
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[], request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'name': Schema(type=TYPE_STRING, title='comment_task_name'),
            'text': Schema(type=TYPE_STRING, title='text'),
            'task': Schema(type=TYPE_STRING, title='task_comments'),
            'updated_by': Schema(type=TYPE_STRING, title='updated_by'),
        }, required=['updated_by']
    ), responses={200: CommentTaskSerializer})
    def partial_update(self, request, pk=None, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
