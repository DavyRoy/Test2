from drf_yasg.openapi import TYPE_OBJECT, TYPE_STRING, Schema
from drf_yasg.utils import no_body, swagger_auto_schema
from requests import Request
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from gpg.permissions import IsUserApiAuthenticated
from gpg.serializers import (
    ChangePasswordSerializer, SignInSerializer, SignUpSerializer, TokenObtainPairResponseSerializer,
    TokenRefreshResponseSerializer
)
from gpg.services.user_service import user_wrapper
from gpg.utils import get_token_from_request
from gpg.views.swagger_settings import ERROR_RESPONSE, ID_IN_PATH, SUCCESS_RESPONSE
from wrappers.auth_wrapper import AuthWrapper

auth_wrapper = AuthWrapper()


class AuthViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(manual_parameters=[],
                         operation_id='sign_up', request_body=SignUpSerializer,
                         responses={
                             201: Schema(
                                 type=TYPE_OBJECT,
                                 properties={
                                     'username': Schema(type=TYPE_STRING, title='username'),
                                     'email': Schema(type=TYPE_STRING, title='email'),
                                     'first_name': Schema(type=TYPE_STRING, title='first_name'),
                                     'last_name': Schema(type=TYPE_STRING, title='last_name'),
                                 }),
                             status.HTTP_400_BAD_REQUEST: ERROR_RESPONSE
                         })
    @action(detail=False, methods=['post'])
    def sign_up(self, request: Request) -> Response:
        serializer = SignUpSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            data = auth_wrapper.sign_up(data=serializer.data)

            return Response(data=data, status=status.HTTP_200_OK)

        return Response(data={'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=[], operation_id='sign_in',
                         request_body=SignInSerializer,
                         responses={status.HTTP_200_OK: TokenObtainPairResponseSerializer})
    @action(detail=False, methods=['post'])
    def sign_in(self, request: Request) -> Response:
        serializer = SignInSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            data = auth_wrapper.sign_in(data=serializer.data)

            return Response(data=data, status=status.HTTP_200_OK)

        return Response(data={'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=[], operation_id='sign_in_refresh',
                         request_body=Schema(
                             type=TYPE_OBJECT,
                             properties={
                                 'refresh': Schema(type=TYPE_STRING, title='refresh_token')
                             }),
                         responses={status.HTTP_200_OK: TokenRefreshResponseSerializer})
    @action(detail=False, methods=['post'])
    def sign_in_refresh(self, request: Request) -> Response:
        data = auth_wrapper.sign_in_refresh(data=request.data)

        return Response(data=data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=ID_IN_PATH, operation_id='change_password',
                         request_body=ChangePasswordSerializer,
                         responses={
                             status.HTTP_200_OK: SUCCESS_RESPONSE,
                             status.HTTP_400_BAD_REQUEST: ERROR_RESPONSE
                         })
    @action(detail=True, methods=['put'], permission_classes=(IsUserApiAuthenticated,))
    def change_password(self, request, pk) -> Response:

        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            token = get_token_from_request(request)
            data = user_wrapper(token).change_password(id=pk, data=serializer.data)

            return Response(data=data, status=status.HTTP_200_OK)

        return Response(data={'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=[], operation_id='sign_out', request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'refresh_token': Schema(type=TYPE_STRING, title='refresh_token'),
        }), responses={
        status.HTTP_200_OK: SUCCESS_RESPONSE,
        status.HTTP_400_BAD_REQUEST: ERROR_RESPONSE
    })
    @action(detail=False, methods=['post'])
    def sign_out(self, request: Request) -> Response:
        data = auth_wrapper.sign_out(data=request.data)

        return Response(data=data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=ID_IN_PATH,
                         operation_id='sing_out_all', request_body=no_body,
                         responses={
                             status.HTTP_200_OK: SUCCESS_RESPONSE,
                             status.HTTP_400_BAD_REQUEST: ERROR_RESPONSE
                         })
    @action(detail=True, methods=['post'])
    def sign_out_all(self, request: Request, pk: str) -> Response:
        data = auth_wrapper.sign_out_all(id=pk)

        return Response(data=data, status=status.HTTP_200_OK)
