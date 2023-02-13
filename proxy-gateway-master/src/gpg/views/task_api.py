from drf_yasg.utils import no_body, swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from gpg.serializers import CheckPointSerializer, TaskSerializer, ProjectSerializer
from wrappers.task_wrapper import TaskApiWrapper
from .swagger_settings import (
    CHECKPOINT_CREATE_REQUEST_BODY, CHECKPOINT_PARAMETERS, CHECKPOINT_PARTIAL_UPDATE_REQUEST_BODY,
    COMMENT_TASK_CREATE_REQUEST_BODY, COMMENT_TASK_PARTIAL_UPDATE_REQUEST_BODY, ERROR_RESPONSE, ID_IN_PATH,
    SUB_TASK_CREATE_REQUEST_BODY, SUB_TASK_PARTIAL_UPDATE_REQUEST_BODY, TASK_CHANGE_STATUS_REQUEST_BODY,
    TASK_CREATE_REQUEST_BODY, TASK_FILES_CREATE_REQUEST_BODY, TASK_FILES_PARTIAL_UPDATE_REQUEST_BODY, TASK_PARAMETERS,
    TASK_PARTIAL_UPDATE_REQUEST_BODY
)
from ..serializers.comment_task import CommentTaskSerializer
from ..serializers.sub_task import SubTaskSerializer
from ..serializers.task_file import TaskFileSerializer
from ..services.s3_service import S3UploadService
from ..utils import reveal_query_params

task_wrapper = TaskApiWrapper()


class TaskViewSet(viewsets.ViewSet):

    @swagger_auto_schema(manual_parameters=TASK_PARAMETERS,
                         operation_id='task_list', request_body=no_body,
                         responses={200: TaskSerializer(many=True)})
    def list(self, request: Request) -> Response:

        query_params = reveal_query_params(request.query_params)
        tasks = task_wrapper(instance='task', view='list', **query_params)
        serializer = TaskSerializer(tasks, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[],
                         operation_id='task_create', request_body=TASK_CREATE_REQUEST_BODY,
                         responses={201: 'ok',
                                    status.HTTP_400_BAD_REQUEST: ERROR_RESPONSE})
    def create(self, request: Request) -> Response:
        sub_tasks = request.data.get('sub_tasks', None)

        task = task_wrapper(instance='task', view='create', data=request.data)
        if sub_tasks is not None:
            if len(sub_tasks) != 0:
                for sub_task in sub_tasks:
                    sub_task['task'] = task['id']
                    sub_task['created_by'] = request.data['created_by']
                    created_sub_task = task_wrapper(instance='sub_task', view='create', data=sub_task)
                    task['sub_tasks'].append(created_sub_task)
        serializer = TaskSerializer(task)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(manual_parameters=ID_IN_PATH,
                         operation_id='task_read', request_body=no_body,
                         responses={200: TaskSerializer})
    def retrieve(self, request: Request, pk: str = None) -> Response:
        task = task_wrapper(instance='task', view='read', id=pk)
        serializer = TaskSerializer(task)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=ID_IN_PATH,
                         operation_id='close_task', request_body=no_body,
                         responses={200: TaskSerializer})
    @action(detail=True, methods=['post'])
    def close_task(self, request: Request, pk: str = None) -> Response:
        task = task_wrapper(instance='task', view='close_task', id=pk)
        serializer = TaskSerializer(task)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[],
                         operation_id='get_all_projects', request_body=no_body,
                         responses={200: ProjectSerializer(many=True)})
    @action(detail=False, methods=['get'])
    def get_all_projects(self, request: Request, pk: str = None) -> Response:
        projects = task_wrapper(instance='task', view='get_all_projects')
        return Response(projects, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=ID_IN_PATH,
                         operation_id='change_status', request_body=TASK_CHANGE_STATUS_REQUEST_BODY,
                         responses={200: TaskSerializer})
    @action(detail=True, methods=['post'])
    def change_status(self, request: Request, pk: str = None) -> Response:
        task = task_wrapper(instance='task', view='change_status', id=pk, data=request.data)
        serializer = TaskSerializer(task)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=ID_IN_PATH,
                         operation_id='task_partial_update', request_body=TASK_PARTIAL_UPDATE_REQUEST_BODY,
                         responses={200: TaskSerializer,
                                    status.HTTP_400_BAD_REQUEST: ERROR_RESPONSE})
    def partial_update(self, request: Request, pk: str = None) -> Response:
        task = task_wrapper(instance='task', view='partial_update', id=pk, data=request.data)
        serializer = TaskSerializer(task)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=ID_IN_PATH,
                         operation_id='task_delete', request_body=no_body,
                         responses={200: TaskSerializer})
    def destroy(self, request: Request, pk: str = None) -> Response:
        task_wrapper(instance='task', view='delete', id=pk)

        return Response(data={}, status=status.HTTP_204_NO_CONTENT)


class CheckPointViewSet(viewsets.ViewSet):
    serializer_class = CheckPointSerializer

    @swagger_auto_schema(manual_parameters=CHECKPOINT_PARAMETERS,
                         operation_id='check_point_list', request_body=no_body,
                         responses={200: CheckPointSerializer(many=True)})
    def list(self, request: Request) -> Response:
        query_params = {key: value[0] for key, value in request.query_params.items()}

        check_points = task_wrapper(instance='check_point', view='list', **query_params)
        serializer = CheckPointSerializer(check_points, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[],
                         operation_id='check_point_create', request_body=CHECKPOINT_CREATE_REQUEST_BODY,
                         responses={201: CheckPointSerializer})
    def create(self, request: Request) -> Response:

        check_point = task_wrapper(instance='check_point', view='create', data=request.data)
        serializer = CheckPointSerializer(check_point)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(manual_parameters=ID_IN_PATH,
                         operation_id='check_point_read', request_body=no_body,
                         responses={200: CheckPointSerializer})
    def retrieve(self, request: Request, pk: str = None) -> Response:
        check_point = task_wrapper(instance='check_point', view='read', id=pk)
        serializer = CheckPointSerializer(check_point)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=ID_IN_PATH,
                         operation_id='check_point_partial_update', request_body=CHECKPOINT_PARTIAL_UPDATE_REQUEST_BODY,
                         responses={201: CheckPointSerializer})
    def partial_update(self, request: Request, pk: str = None) -> Response:
        check_point = task_wrapper(instance='check_point', view='partial_update', id=pk, data=request.data)

        serializer = CheckPointSerializer(check_point)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=ID_IN_PATH,
                         operation_id='check_point_delete', request_body=no_body,
                         responses={200: CheckPointSerializer})
    def destroy(self, request: Request, pk: str = None) -> Response:
        task_wrapper(instance='check_point', view='delete', id=pk)

        return Response(data={}, status=status.HTTP_204_NO_CONTENT)


class CommentTaskViewSet(viewsets.ViewSet):
    #serializer_class = CommentTaskSerializer

    @swagger_auto_schema(manual_parameters=[],
                         operation_id='comment_task_list', request_body=no_body,
                         responses={200: CommentTaskSerializer(many=True)})
    def list(self, request: Request) -> Response:
        task_comments = task_wrapper(instance='comment_task', view='list')

        serializer = CommentTaskSerializer(task_comments, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[],
                         operation_id='comment_task_create', request_body=COMMENT_TASK_CREATE_REQUEST_BODY,
                         responses={201: CommentTaskSerializer})
    def create(self, request: Request) -> Response:

        comment_task = task_wrapper(instance='comment_task', view='create', data=request.data)
        serializer = CommentTaskSerializer(comment_task)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(manual_parameters=ID_IN_PATH,
                         operation_id='comment_task_read', request_body=no_body,
                         responses={200: CommentTaskSerializer})
    def retrieve(self, request: Request, pk: str = None) -> Response:
        comment_task = task_wrapper(instance='comment_task', view='read', id=pk)

        serializer = CommentTaskSerializer(comment_task)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[],
                         operation_id='comment_task_partial_update',
                         request_body=COMMENT_TASK_PARTIAL_UPDATE_REQUEST_BODY,
                         responses={200: CommentTaskSerializer})
    def partial_update(self, request: Request, pk: str = None) -> Response:
        comment_task = task_wrapper(instance='comment_task', view='partial_update', id=pk, data=request.data)

        serializer = CommentTaskSerializer(comment_task)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=ID_IN_PATH,
                         operation_id='comment_task_delete', request_body=no_body,
                         responses={200: CommentTaskSerializer})
    def destroy(self, request: Request, pk: str = None) -> Response:
        task_wrapper(instance='comment_task', view='delete', id=pk)

        return Response(data={}, status=status.HTTP_204_NO_CONTENT)


class SubTaskViewSet(viewsets.ViewSet):
   #serializer_class = SubTaskSerializer

    @swagger_auto_schema(manual_parameters=[],
                         operation_id='sub_task_list', request_body=no_body,
                         responses={200: SubTaskSerializer(many=True)})
    def list(self, request: Request) -> Response:
        sub_tasks = task_wrapper(instance='sub_task', view='list')

        serializer = SubTaskSerializer(sub_tasks, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[],
                         operation_id='sub_task_create', request_body=SUB_TASK_CREATE_REQUEST_BODY,
                         responses={201: SubTaskSerializer})
    def create(self, request: Request) -> Response:

        sub_task = task_wrapper(instance='sub_task', view='create', data=request.data)
        serializer = SubTaskSerializer(sub_task)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(manual_parameters=ID_IN_PATH,
                         operation_id='sub_task_read', request_body=no_body,
                         responses={200: SubTaskSerializer})
    def retrieve(self, request: Request, pk: str = None) -> Response:
        sub_task = task_wrapper(instance='sub_task', view='read', id=pk)

        serializer = SubTaskSerializer(sub_task)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[],
                         operation_id='sub_task_partial_update',
                         request_body=SUB_TASK_PARTIAL_UPDATE_REQUEST_BODY,
                         responses={201: SubTaskSerializer})
    def partial_update(self, request: Request, pk: str = None) -> Response:
        sub_task = task_wrapper(instance='sub_task', view='partial_update', id=pk, data=request.data)

        serializer = SubTaskSerializer(sub_task)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=ID_IN_PATH,
                         operation_id='sub_task_delete', request_body=no_body,
                         responses={200: SubTaskSerializer})
    def destroy(self, request: Request, pk: str = None) -> Response:
        task_wrapper(instance='sub_task', view='delete', id=pk)

        return Response(data={}, status=status.HTTP_204_NO_CONTENT)


class TaskFileViewSet(viewsets.ViewSet):
    serializer_class = TaskFileSerializer

    @swagger_auto_schema(manual_parameters=[],
                         operation_id='task_file_list', request_body=no_body,
                         responses={200: TaskFileSerializer(many=True)})
    def list(self, request: Request) -> Response:
        task_files = task_wrapper(instance='task_files', view='list')

        serializer = TaskFileSerializer(task_files, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[],
                         operation_id='task_file_create', request_body=TASK_FILES_CREATE_REQUEST_BODY,
                         responses={201: TaskFileSerializer})
    def create(self, request: Request) -> Response:
        file = request.FILES
        s3_url = S3UploadService(file)()
        data = {
            'task': request.data.get('task'),
            'created_by': request.data.get('created_by'),
            'file_id': s3_url,
            'name': file['file'].name
        }
        task_file = task_wrapper(instance='task_files', view='create', data=data)

        serializer = TaskFileSerializer(task_file)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(manual_parameters=ID_IN_PATH,
                         operation_id='task_file_read', request_body=no_body,
                         responses={200: TaskFileSerializer})
    def retrieve(self, request: Request, pk: str = None) -> Response:
        task_file = task_wrapper(instance='task_files', view='read', id=pk)

        serializer = TaskFileSerializer(task_file)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[],
                         operation_id='task_file_partial_update', request_body=TASK_FILES_PARTIAL_UPDATE_REQUEST_BODY,
                         responses={201: TaskFileSerializer})
    def partial_update(self, request: Request, pk: str = None) -> Response:
        task_file = task_wrapper(instance='task_files', view='partial_update', id=pk, data=request.data)

        serializer = TaskFileSerializer(task_file)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=ID_IN_PATH,
                         operation_id='task_file_delete', request_body=no_body,
                         responses={200: TaskFileSerializer})
    def destroy(self, request: Request, pk: str = None) -> Response:
        task_wrapper(instance='task_files', view='delete', id=pk)

        return Response(data={}, status=status.HTTP_204_NO_CONTENT)
