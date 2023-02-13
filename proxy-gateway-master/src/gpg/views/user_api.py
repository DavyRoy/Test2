from drf_yasg.utils import no_body, swagger_auto_schema
from requests import Request
from rest_framework import status, viewsets
from rest_framework.response import Response

from gpg.permissions import IsUserApiAuthenticated
from gpg.serializers import UserSerializer
from gpg.services.user_service import user_wrapper
from gpg.views.swagger_settings import ID_IN_PATH, USER_PARTIAL_UPDATE_REQUEST_BODY


class UserViewSet(viewsets.ViewSet):
    permission_classes = (IsUserApiAuthenticated,)

    @swagger_auto_schema(manual_parameters=[],
                         operation_id='user_list', request_body=no_body,
                         responses={200: UserSerializer(many=True)})
    def list(self, request: Request) -> Response:
        users = user_wrapper(instance='user', view='list')

        return Response(data=users, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=ID_IN_PATH,
                         operation_id='user_read', request_body=no_body,
                         responses={200: UserSerializer})
    def retrieve(self, request: Request, pk: str = None) -> Response:
        user = user_wrapper(instance='user', view='read', id=pk)

        return Response(user, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=ID_IN_PATH,
                         operation_id='user_partial_update', request_body=USER_PARTIAL_UPDATE_REQUEST_BODY,
                         responses={201: UserSerializer})
    def partial_update(self, request: Request, pk: str = None) -> Response:
        user = user_wrapper(instance='user', view='partial_update', id=pk, data=request.data)

        return Response(user, status=status.HTTP_200_OK)


class ProjectGroupViewSet(viewsets.ViewSet):
    permission_classes = (IsUserApiAuthenticated,)

    @swagger_auto_schema(manual_parameters=[],
                         operation_id='project_group_list', request_body=no_body,
                         responses={200: UserSerializer(many=True)})
    def list(self, request: Request) -> Response:
        users = user_wrapper(instance='project_group', view='list')

        return Response(data=users, status=status.HTTP_200_OK)


