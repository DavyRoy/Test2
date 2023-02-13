from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from user_api.serializers import TokenObtainPairResponseSerializer, TokenRefreshResponseSerializer, \
    TokenVerifyResponseSerializer


class DecoratedTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(operation_id='sign_in',
                         responses={
                             status.HTTP_200_OK: TokenObtainPairResponseSerializer,
                         }
                         )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenRefreshView(TokenRefreshView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(operation_id='sign_in_refresh',
                         responses={
                             status.HTTP_200_OK: TokenRefreshResponseSerializer,
                         }
                         )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenVerifyView(TokenVerifyView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(operation_id='sign_in_verify',
                         responses={
                             status.HTTP_200_OK: TokenVerifyResponseSerializer,
                             status.HTTP_401_UNAUTHORIZED: Schema(
                                 type=TYPE_OBJECT,
                                 properties={'detail': Schema(type=TYPE_STRING, title='Token is invalid or expired'),
                                             'code': Schema(type=TYPE_STRING, title='token_not_valid')})
                         }
                         )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
