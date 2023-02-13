from drf_yasg.openapi import IN_PATH, TYPE_STRING, Parameter, TYPE_OBJECT, Schema, Items, TYPE_ARRAY, TYPE_INTEGER, \
    TYPE_BOOLEAN
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from user_api.models import User
from user_api.serializers import UserSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[Parameter('id', IN_PATH, required=True, type=TYPE_STRING)],
                         operation_id='user_partial_update', request_body=Schema(
            type=TYPE_OBJECT,
            properties={
                'role': Schema(type=TYPE_STRING, title='role'),
                'first_name': Schema(type=TYPE_STRING, title='first_name'),
                'last_name': Schema(type=TYPE_STRING, title='last_name'),
                'username': Schema(type=TYPE_STRING, title='username'),
                'email': Schema(type=TYPE_STRING, title='email'),
                'phone': Schema(type=TYPE_STRING, title='phone'),

            },

        ),
                         responses={200: UserSerializer})
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


