from drf_yasg.openapi import IN_PATH, IN_QUERY, TYPE_BOOLEAN, TYPE_OBJECT, TYPE_STRING, Parameter, Schema
from drf_yasg.utils import no_body, swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from gpg.serializers import DocumentSerializer, TypeDocumentSerializer
from wrappers.document_wrapper import DocumentApiWrapper

document_wrapper = DocumentApiWrapper()


class DocumentViewSet(viewsets.ViewSet):
    serializer_class = DocumentSerializer

    @swagger_auto_schema(manual_parameters=[
        Parameter('name_document', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('type', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('preview_image', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('file', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('is_archive', IN_QUERY, required=False, type=TYPE_STRING),
    ], request_body=no_body, responses={200: DocumentSerializer(many=True)})
    @action(detail=False, methods=['get'])
    def document_list(self, request=None):
        document = document_wrapper(instance='document', view='list')
        return Response(data=document, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[], request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'name_document': Schema(type=TYPE_STRING, title='name_document'),
            'type': Schema(type=TYPE_STRING, title='type'),
            'preview_image': Schema(type=TYPE_STRING, title='preview_image'),
            'file': Schema(type=TYPE_STRING, title='file'),
            'is_archive': Schema(type=TYPE_BOOLEAN, title='is_archive'),
        }, required=['name_document', 'type', 'preview_image', 'file', 'is_archive']
    ), responses={201: DocumentSerializer})
    @action(detail=False, methods=['post'])
    def document_create(self, request):
        request.data['created_by'] = '0000' # TODO: REWORK AFTER CREATE AUTH
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            document = document_wrapper(instance='document', view='create', data=serializer.data)
            return Response(document, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=[
        Parameter('id', IN_PATH, required=True, type=TYPE_STRING),
    ], request_body=no_body, responses={200: DocumentSerializer})
    @action(detail=True, methods=['get'])
    def document_read(self, request, pk=None):
        document = DocumentSerializer(instance='document', view='read', id=pk)
        return Response(document, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[
        Parameter('id', IN_PATH, required=True, type=TYPE_STRING),
    ], request_body=no_body, responses={200: DocumentSerializer})
    @action(detail=True, methods=['post'])
    def archives(self, request, pk=None):
        document = document_wrapper(instance='document', view='archives', id=pk)
        return Response(document, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[
        Parameter('id', IN_PATH, required=True, type=TYPE_STRING),
    ], request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'name_document': Schema(type=TYPE_STRING, title='name_document'),
            'type': Schema(type=TYPE_STRING, title='type'),
            'preview_image': Schema(type=TYPE_STRING, title='preview_image'),
            'file': Schema(type=TYPE_STRING, title='file'),
            'is_archive': Schema(type=TYPE_BOOLEAN, title='is_archive'),
        }, required=['name_document', 'type', 'preview_image', 'file', 'is_archive']
    ), responses={201: DocumentSerializer})
    @action(detail=True, methods=['put'])
    def document_update(self, request, pk=None):  # TODO: NOT TESTED
        request.data['updated_by'] = '0000' # TODO: REWORK AFTER CREATE AUTH
        document = document_wrapper(instance='document', view='update', id=pk, data=request.data)
        return Response(document, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[
        Parameter('id', IN_PATH, required=True, type=TYPE_STRING),
    ], request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'name_document': Schema(type=TYPE_STRING, title='name_document'),
            'type': Schema(type=TYPE_STRING, title='type'),
            'preview_image': Schema(type=TYPE_STRING, title='preview_image'),
            'file': Schema(type=TYPE_STRING, title='file'),
            'is_archive': Schema(type=TYPE_BOOLEAN, title='is_archive'),
        }, required=['name_document', 'type', 'preview_image', 'file', 'is_archive']
    ), responses={201: DocumentSerializer})
    @action(detail=True, methods=['patch'])
    def document_partial_update(self, request, pk=None):
        request.data['updated_by'] = '0000' # TODO: REWORK AFTER CREATE AUTH
        document = document_wrapper(instance='document', view='partial_update', id=pk, data=request.data)
        return Response(document, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[
        Parameter('id', IN_PATH, required=True, type=TYPE_STRING),
    ], request_body=no_body, responses={200: DocumentSerializer})
    @action(detail=True, methods=['delete'])
    def document_delete(self, request, pk=None):
        document_wrapper(instance='document', view='delete', id=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TypeDocumentViewSet(viewsets.ViewSet):
    serializer_class = TypeDocumentSerializer

    @swagger_auto_schema(manual_parameters=[
        Parameter('name', IN_QUERY, required=False, type=TYPE_STRING),
        Parameter('activity', IN_QUERY, required=False, type=TYPE_STRING),
    ], request_body=no_body, responses={200: TypeDocumentSerializer(many=True)})
    @action(detail=False, methods=['get'])
    def type_document_list(self, request=None):
        type_document = document_wrapper(instance='type_document', view='list')
        return Response(data=type_document, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[], request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'name': Schema(type=TYPE_STRING, title='name'),
            'activity': Schema(type=TYPE_BOOLEAN, title='activity'),
        }, required=['name', 'activity']
    ), responses={201: TypeDocumentSerializer})
    @action(detail=False, methods=['post'])
    def type_document_create(self, request):
        request.data['created_by'] = '0000'  # TODO: REWORK AFTER CREATE AUTH
        serializer = TypeDocumentSerializer(data=request.data)
        if serializer.is_valid():
            type_document = document_wrapper(instance='type_document', view='create', data=serializer.data)
            return Response(type_document, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=[
        Parameter('id', IN_PATH, required=True, type=TYPE_STRING),
    ], request_body=no_body, responses={200: TypeDocumentSerializer})
    @action(detail=True, methods=['get'])
    def type_document_read(self, request, pk=None):
        type_document = TypeDocumentSerializer(instance='type_document', view='read', id=pk)
        return Response(type_document, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[
        Parameter('id', IN_PATH, required=True, type=TYPE_STRING),
    ], request_body=no_body, responses={200: TypeDocumentSerializer})
    @action(detail=True, methods=['post'])
    def active(self, request, pk=None):
        type_document = document_wrapper(instance='type_document', view='active', id=pk)
        return Response(type_document, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[
        Parameter('id', IN_PATH, required=True, type=TYPE_STRING),
    ], request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'name': Schema(type=TYPE_STRING, title='name'),
            'activity': Schema(type=TYPE_BOOLEAN, title='activity'),
        }, required=['name', 'activity']
    ), responses={201: TypeDocumentSerializer})
    @action(detail=True, methods=['put'])
    def type_document_update(self, request, pk=None):  # TODO: NOT TESTED
        request.data['updated_by'] = '0000'  # TODO: REWORK AFTER CREATE AUTH
        type_document = document_wrapper(instance='type_document', view='update', id=pk, data=request.data)
        return Response(type_document, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[
        Parameter('id', IN_PATH, required=True, type=TYPE_STRING),
    ], request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'name': Schema(type=TYPE_STRING, title='name'),
            'activity': Schema(type=TYPE_BOOLEAN, title='activity'),
        }, required=['name',  'activity']
    ), responses={201: TypeDocumentSerializer})
    @action(detail=True, methods=['patch'])
    def type_document_partial_update(self, request, pk=None):
        request.data['updated_by'] = '0000'  # TODO: REWORK AFTER CREATE AUTH
        type_document = document_wrapper(instance='type_document', view='partial_update', id=pk, data=request.data)
        return Response(type_document, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[
        Parameter('id', IN_PATH, required=True, type=TYPE_STRING),
    ], request_body=no_body, responses={200: TypeDocumentSerializer})
    @action(detail=True, methods=['delete'])
    def type_document_delete(self, request, pk=None):
        document_wrapper(instance='type_document', view='delete', id=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)