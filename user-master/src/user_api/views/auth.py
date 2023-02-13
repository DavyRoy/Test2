from django.db import transaction
from drf_yasg.openapi import TYPE_OBJECT, Schema, TYPE_STRING, IN_PATH, Parameter
from drf_yasg.utils import swagger_auto_schema, no_body
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.tokens import RefreshToken

from user_api.models import User
from user_api.serializers import SignUpSerializer, ChangePasswordSerializer, UserSerializer


class AuthViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    @transaction.atomic
    @swagger_auto_schema(manual_parameters=[],
                         operation_id='sign_up', request_body=Schema(
            type=TYPE_OBJECT,
            properties={
                'username': Schema(type=TYPE_STRING, title='username'),
                'password': Schema(type=TYPE_STRING, title='password'),
                'password2': Schema(type=TYPE_STRING, title='repeated password'),
                'email': Schema(type=TYPE_STRING, title='email'),
                'first_name': Schema(type=TYPE_STRING, title='first_name'),
                'last_name': Schema(type=TYPE_STRING, title='last_name'),
            },
            required=['username', 'password', 'password2', 'email', 'first_name', 'last_name']
        ),
                         responses={
                             201: Schema(
                                 type=TYPE_OBJECT,
                                 properties={
                                     'username': Schema(type=TYPE_STRING, title='username'),
                                     'email': Schema(type=TYPE_STRING, title='email'),
                                     'first_name': Schema(type=TYPE_STRING, title='first_name'),
                                     'last_name': Schema(type=TYPE_STRING, title='last_name'),
                                 }),
                             400: Schema(type=TYPE_OBJECT,
                                         properties={'error': Schema(type=TYPE_STRING, title='some_error')})
                         }
                         )
    @action(detail=False, methods=['post'])
    def sign_up(self, request):
        serializer = SignUpSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data={'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(manual_parameters=[], operation_id='change_password', request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'old_password': Schema(type=TYPE_STRING, title='old_password'),
            'password': Schema(type=TYPE_STRING, title='password'),
            'password2': Schema(type=TYPE_STRING, title='password2'),
        }), responses={
        200: Schema(type=TYPE_OBJECT, properties={'success': Schema(type=TYPE_STRING, title='success')}),
        400: Schema(type=TYPE_OBJECT, properties={'error': Schema(type=TYPE_STRING, title='some_error')})
    })
    @action(detail=True, methods=['put'], permission_classes=(IsAuthenticated,))
    def change_password(self, request, pk):
        serializer = ChangePasswordSerializer(instance=request.user, data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(data={'success': True}, status=status.HTTP_200_OK)

        return Response(data={'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=[], operation_id='sign_out', request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'refresh_token': Schema(type=TYPE_STRING, title='refresh_token'),
        }), responses={
        200: Schema(type=TYPE_OBJECT, properties={'success': Schema(type=TYPE_STRING, title='success')}),
        400: Schema(type=TYPE_OBJECT, properties={'error': Schema(type=TYPE_STRING, title='some_error')})
    })
    @action(detail=False, methods=['post'])
    def sign_out(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(data={'success': True}, status=status.HTTP_200_OK)

        except Exception as e:

            return Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=[
        Parameter('id', IN_PATH, required=True, type=TYPE_STRING)],
        operation_id='sign_out_all', request_body=no_body, responses={
            200: Schema(type=TYPE_OBJECT, properties={'success': Schema(type=TYPE_STRING, title='success')}),
            400: Schema(type=TYPE_OBJECT, properties={'error': Schema(type=TYPE_STRING, title='some_error')})
        })
    @action(detail=True, methods=['post'])
    def sign_out_all(self, request, pk=None):
        user = self.get_object()
        try:
            tokens = OutstandingToken.objects.filter(user_id=user.id)
            for token in tokens:
                t, _ = BlacklistedToken.objects.get_or_create(token=token)

            return Response(data={'success': True}, status=status.HTTP_200_OK)

        except Exception as e:

            return Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
