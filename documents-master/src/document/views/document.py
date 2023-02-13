from drf_yasg.openapi import IN_QUERY, TYPE_STRING, TYPE_OBJECT, TYPE_BOOLEAN, Schema
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from document.models import Document
from document.serializers import DocumentSerializer


class DocumentViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):

    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[], request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'name_document': Schema(type=TYPE_STRING, title='name_document'),
            'type': Schema(type=TYPE_STRING, title='type'),
            'preview_image': Schema(type=TYPE_STRING, title='preview_image'),
            'file': Schema(type=TYPE_STRING, title='file'),
            'is_archive': Schema(type=TYPE_BOOLEAN, title='is_archive'),
            'created_by': Schema(type=TYPE_STRING, title='created_by'),
        }, required=['name_document', 'type', 'preview_image', 'file', 'is_archive', 'created_by']
    ), responses={201: DocumentSerializer})
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[], requests_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'is_archive': Schema(type=IN_QUERY, title='is_archive')
        }
    ))
    @action(detail=True, methods=['post'])
    def archives(self, request, pk=None):
        document = self.get_object()
        document.is_archive = True
        document.save()
        return Response(status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(is_archive=False)
        return queryset

    @swagger_auto_schema(manual_parameters=[], request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'name_document': Schema(type=TYPE_STRING, title='name_document'),
            'type': Schema(type=TYPE_STRING, title='type'),
            'preview_image': Schema(type=TYPE_STRING, title='preview_image'),
            'file': Schema(type=TYPE_STRING, title='file'),
            'is_archive': Schema(type=TYPE_BOOLEAN, title='is_archive'),
            'updated_by': Schema(type=TYPE_STRING, title='updated_by'),
        }, required=['updated_by']
    ), responses={201: DocumentSerializer})
    def partial_update(self, request, pk=None, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
