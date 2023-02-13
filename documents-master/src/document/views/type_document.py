from drf_yasg.openapi import IN_QUERY, TYPE_STRING, TYPE_OBJECT, TYPE_BOOLEAN, Schema
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from document.models import TypeDocument
from document.serializers import TypeDocumentSerializer


class TypeDocumentViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):

    serializer_class = TypeDocumentSerializer
    queryset = TypeDocument.objects.all()
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[], request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'name': Schema(type=TYPE_STRING, title='name'),
            'activity': Schema(type=TYPE_BOOLEAN, title='activity'),
            'created_by': Schema(type=TYPE_STRING, title='created_by'),
        }, required=['name', 'activity', 'created_by']
    ), responses={201: TypeDocumentSerializer})
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[], requests_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'activity': Schema(type=IN_QUERY, title='activity')
        }
    ))
    @action(detail=True, methods=['post'])
    def active(self, request, pk=None):
        type_document = self.get_object()
        type_document.activity = True
        type_document.save()
        return Response(status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[], request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'name': Schema(type=TYPE_STRING, title='name'),
            'activity': Schema(type=TYPE_BOOLEAN, title='activity'),
            'updated_by': Schema(type=TYPE_STRING, title='updated_by'),
        }, required=['updated_by']
    ), responses={201: TypeDocumentSerializer})
    def partial_update(self, request, pk=None, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
