from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.openapi import TYPE_STRING, TYPE_ARRAY, Items, TYPE_OBJECT, Schema, TYPE_INTEGER, Parameter, IN_QUERY
from drf_yasg.utils import swagger_auto_schema, no_body
from rest_framework.response import Response
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from gen_task.filters import CheckPointFilter
from gen_task.models import CheckPoint
from gen_task.serializers import CheckPointSerializer


class CheckPointViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        mixins.DestroyModelMixin,
                        GenericViewSet):

    serializer_class = CheckPointSerializer
    queryset = CheckPoint.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CheckPointFilter

    @swagger_auto_schema(manual_parameters=[], request_body=Schema(
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
            'created_by': Schema(type=TYPE_STRING, title='created_by'),
        },
        required=['name', 'project', 'description', 'executor', 'priority', 'status', 'started_at', 'planned_ended_at',
                  'created_by']
    ), responses={201: CheckPointSerializer})
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[], request_body=Schema(
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
            'updated_by': Schema(type=TYPE_STRING, title='updated_by'),
        }, required=['updated_by']
    ), responses={200: CheckPointSerializer})
    def partial_update(self, request, pk=None, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[], request_body=no_body, responses={200: CheckPointSerializer})
    @action(detail=False, methods=['get'])
    def stage_list(self, request,):
        queryset = self.get_queryset()
        serializer = CheckPointSerializer(queryset.exclude(stage=None), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
